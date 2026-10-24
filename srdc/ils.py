#
# Individual Levels
#
# This code processes Individual Runs. These are basically
# an extension of main boards (normal.py), but focused on
# individual levels. As a consequence, some parts will be
# the same as normal.py, but will poll IL boards instead.
from utils.model import SpeedRun


# IndividualLevel
# This handles the logic of querying the SRDC
# API for an individual level submission. This is
# used by !run only.
class IndividualLevel:
	def __init__(self, srdc_api, api, game_map, levels_map, category_map, ik_mapping, utils):
		self.srdc = srdc_api
		self.api = api
		self.game_map = game_map
		self.levels_map = levels_map
		self.category_map = category_map
		self.ik_mapping = ik_mapping
		self.utils = utils

	def search_il_wrs(self, game_id: str):
		"""
		Queries SRDC to find the top 1 run of every IL board for
		the provided game ID. Will return an empty list or
		all matching runs.

		Unlike other routes, this one has to embed player metadata
		since the invocation command is trying to find the person who
		has the world record and doesn't know who it is until SRDC
		returns it.

		This is the only place where &embed=players should exist.
		"""
		base_q = f"games/{game_id}/records?top=1&scope=levels&embed=players"
		all_runs = []
		offset = 0
		while True:
			# Start at 50, then increase the offset per loop.
			# If the batch returns nothing, break the loop.
			q = f"{base_q}&max=50&offset={offset}"
			batch = self.srdc.get(q)
			if not batch:
				break

			# Append the runs, then increase the offset and continue.
			all_runs.extend(batch)
			offset += 50

		# Return the full list.
		return all_runs

	def process_il(self, game, platform, level, category, player, is_wr):
		"""
		This method will capture all the requirements of finding an IL, which is
		then passed over to lookup_il to find it.

		Returns a SpeedRun object or None.
		"""
		# Normalise the internal key, in case game/platform
		# is for a different platform. If this key isn't in
		# the alias list, we just use it as is.
		internal_key = f"{game}_{platform}"
		il_internal_key = None
		for ik, aliases in self.ik_mapping.items():
			if internal_key in aliases:
				il_internal_key = ik
				break

		# Find the relevant game entry: this is necessary to capture
		# the relevant board slug for later.
		board_slugs = None
		game_name = None
		for key_name, data in self.game_map.items():
			if game == key_name or game in data.get("aliases", []):
				game_name = data["name"]
				board_slugs = data["slugs"]
				break

		# Check if this internal key is in the aliases map.
		level_aliases = self.levels_map.get(il_internal_key or internal_key)
		if not level_aliases:
			raise ValueError("This combination of game and platform does not map to any configuration. Perhaps this game isn't supported in config yet, or it doesn't have any ILs supported.")

		# Check if the category alias is in the alias table.
		variables = None
		ind_level_id = None
		ind_level_name = None
		for level_name, data in level_aliases.items():
			if level in data["aliases"]:
				ind_level_id = data["level_id"]
				ind_level_name = level_name
				variables = data.get("variables", [])
				break

		# If none, then this IL does not exist.
		if not ind_level_name:
			raise ValueError(f"No individual level was found internally for level name `{ind_level_name}`. Check your spelling and try again.")

		# Check that the category actually exists for this IL.
		# Obtain the relevant category name from the category map.
		cat_name = None
		for category_name, data in self.category_map.items():
			if category in data["aliases"]:
				cat_name = category_name
				break

		# If nothing found, just raise an error.
		if not cat_name:
			raise ValueError("The category you have requested could not be found for this IL. Check your spelling and try again. If this persists, it might be a bug.")

		# Obtain the slug URL based on the internal key variable.
		slug = None
		for slug_url, aliases in board_slugs.items():
			if internal_key in aliases:
				slug = slug_url
				break

		# If the flag "world_record" has been set, lookup only the WR on these parameters.
		# Otherwise, look up the users' specific IL submission.
		var_filters = self.utils.generate_var_filters(variables, None)
		if is_wr:
			run = self.lookup_il_world_record(slug, ind_level_id, cat_name)
		else:
			run = self.lookup_il(slug, ind_level_id, cat_name, player, var_filters)

		# Set the clean name and return the run that was found.
		cat_clean_name = f"{ind_level_name} {cat_name}"
		return run, cat_clean_name, game_name

	def lookup_il(self, slug, level_id, category_meta, player, variables=None) -> SpeedRun | None:
		"""
		Look up the fastest verified run for a player in an individual level submission.
		As ILs are much simpler in SRDC due to lesser options, the code similarly
		does minimal processing and relies on the data provided by SRDC.
		"""
		# Return the game code and then parse the category name for ID.
		game_id, game_cats = self.api.get_game_code(slug, redis_key="levels", type_filter="per-level")
		category_id = None
		for cat_id, cat_name in game_cats.items():
			if cat_name == category_meta:
				category_id = cat_id
				break

		# If no category exists with the given name, raise ValueError and quit.
		if not category_id:
			raise ValueError("Category not found in game")

		# Resolve user ID and then find that specific level run.
		# If nothing there, just return None.
		user_id = self.api.get_srdc_user(player)
		q = f"runs?game={game_id}&level={level_id}&category={category_id}&user={user_id}&status=verified&embed=variables"
		runs = self.api.search_runs(game_id, category_id, user_id, var_filters=variables, base_query=q)
		if not runs:
			return None

		# A small portion of ILs may have variables assigned to them. If that
		# is the case, filter all run objects and return the requested one.
		if variables:
			runs = self.utils.filter_all_runs(runs, variables)

		# Sort the runs by the most recently verified run (newest at the top).
		# Then, find that run on the leaderboard to get placement.
		runs.sort(key=lambda rx: rx["submitted"], reverse=True)
		lb_q = f"leaderboards/{game_id}/level/{level_id}/{category_id}?embed=variables"
		best_run, place = self.utils.get_run_and_place(game_id, category_id, runs, variables, alt_url=lb_q)
		if best_run is None:
			return None

		# Extract run details and return it.
		return self.utils.extract_run(best_run, player, place)

	def lookup_il_world_record(self, slug, level_id, category_name) -> SpeedRun | None:
		"""
		Queries SRDC to find the current world record submission
		for an IL.
		"""
		# Return the game code and then parse the category name for ID.
		game_id, game_cats = self.api.get_game_code(slug, redis_key="levels", type_filter="per-level")
		category_id = None
		for cat_id, cat_name in game_cats.items():
			if cat_name == category_name:
				category_id = cat_id
				break

		# If no category exists with the given name, raise ValueError and quit.
		if not category_id:
			raise ValueError("Category not found in game")

		# Query SRDC for all world records under these parameters.
		runs = self.search_il_wrs(game_id)
		if not runs:
			raise ValueError("No IL world records could be found for these conditions.")

		# The run list will contain one run for every category covered by the
		# main game board. We should only return the run which equates to the
		# specific level and category combination requested by the user. If no run
		# is found, raise a ValueError.
		run = next((r for r in runs if r["level"] == level_id and r["category"] == category_id), None)
		if run is None:
			raise ValueError("No IL world records could be found for these conditions.")

		# This doesn't need to be sorted, nor do we need to find run placement, as the
		# parameters ensure only one run will be returned, which will be the world record.
		# Just return this run from the data given.
		return self.utils.extract_run(run["runs"][0]["run"], run["players"]["data"][0]["names"]["international"])
