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
	def __init__(self, api, game_map, platform_map, levels_map, category_map, board_slugs, ik_mapping, utils):
		self.api = api
		self.game_map = game_map
		self.platform_map = platform_map
		self.levels_map = levels_map
		self.category_map = category_map
		self.board_slugs = board_slugs
		self.ik_mapping = ik_mapping
		self.utils = utils

	def search_il_wrs(self, game_id: str):
		"""
		Queries SRDC to find the top 1 run of every IL board for
		the provided game ID. Will return an empty list or
		all matching runs.
		"""
		base_q = f"games/{game_id}/records?top=1&scope=levels&embed=players"
		all_runs = []
		offset = 0
		while True:
			# Start at 20, then increase the offset per loop.
			# If the batch returns nothing, break the loop.
			q = f"{base_q}&max=20&offset={offset}"
			batch = self.api.get(q)
			if not batch:
				break

			# Append the runs, then increase the offset and continue.
			all_runs.extend(batch)
			offset += 20

		# Return the full list.
		return all_runs

	def process_il(self, game: str, platform: str, level: str, category: str, player: str, is_wr: bool):
		"""
		This method will capture all the requirements of finding an IL, which is
		then passed over to lookup_il to find it.

		Returns a SpeedRun object or None.
		"""
		# Normalise the internal key, in case game/platform
		# is for a different platform. If this key isn't in
		# the alias list, we just use it as is.
		internal_key = f"{game}_{platform}"
		for ik, aliases in self.ik_mapping.items():
			if internal_key in aliases:
				internal_key = ik
				break

		# Check if this internal key is in the aliases map.
		level_aliases = self.levels_map.get(internal_key)
		if not level_aliases:
			raise ValueError("This combination of game and platform does not map to any configuration. Perhaps this game isn't supported in config yet, or it doesn't have any ILs supported.")

		# Check if the category alias is in the alias table.
		ind_level_id = None
		ind_level_name = None
		for level_name, data in level_aliases.items():
			if level in data["aliases"]:
				ind_level_id = data["level_id"]
				ind_level_name = level_name
				break

		# If none, then this IL does not exist.
		if not ind_level_name:
			raise ValueError(f"No individual level was found internally for level name `{ind_level_name}`. Check your spelling and try again.")

		# Check that the category actually exists for this IL.
		# Obtain the relevant category name from the category map.
		cat_name = None
		for category_name, aliases in self.category_map.items():
			if category in aliases:
				cat_name = category_name
				break

		# If nothing found, just raise an error.
		if not cat_name:
			raise ValueError("The category you have requested could not be found for this IL. Check your spelling and try again. If this persists, it might be a bug.")

		# If the flag "world_record" has been set, lookup only the WR on these parameters.
		# Otherwise, look up the users' specific IL submission.
		if is_wr:
			run = self.lookup_il_world_record(internal_key, ind_level_id, cat_name)
		else:
			run = self.lookup_il(internal_key, ind_level_id, cat_name, player)

		# Set the clean name and return the run that was found.
		cat_clean_name = f"{ind_level_name} {cat_name}"
		return run, cat_clean_name

	def lookup_il(self, internal_key: str, level_id: str, category_meta: str, player: str) -> SpeedRun | None:
		"""
		Look up the fastest verified run for a player in an individual level submission.
		As ILs are much simpler in SRDC due to lesser options, the code similarly
		does minimal processing and relies on the data provided by SRDC.
		"""
		# Parse the internal_key and cat_key to obtain the game and category.
		slug = self.board_slugs[internal_key]
		game_id, game_cats = self.utils.get_game_code(slug, redis_key="levels", type_filter="per-level")

		# Check that there is a category matching the one we asked for.
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
		user_id = self.utils.get_user_id(player)
		q = f"runs?game={game_id}&level={level_id}&category={category_id}&user={user_id}&status=verified&embed=players"
		runs = self.utils.search_runs(game_id, category_id, user_id, base_query=q)
		if not runs:
			return None

		# Sort the runs by the most recently verified run (newest at the top)
		# The run at the top of the index will then be used to get its placement
		# in the leaderboard. To avoid duplication, leaderboard placement is
		# parsed by a helper function.
		runs.sort(key=lambda rx: rx["submitted"], reverse=True)
		best_run = runs[0]

		# Extract all run details and the leaderboard placement, then return the run object.
		lb_q = f"leaderboards/{game_id}/level/{level_id}/{category_id}?embed=players"
		place = self.utils.lookup_run_place(game_id, category_id, best_run["id"], variables=None, alt_url=lb_q)
		sr = self.utils.extract_run(best_run, player)
		sr.place = place
		return sr

	def lookup_il_world_record(self, internal_key, level_id, category_meta) -> SpeedRun | None:
		"""
		Queries SRDC to find the current world record submission
		for an IL.
		"""
		# Parse the internal_key and cat_key to obtain the game and category.
		slug = self.board_slugs[internal_key]
		game_id, game_cats = self.utils.get_game_code(slug, redis_key="levels", type_filter="per-level")

		# Check that there is a category matching the one we asked for.
		category_id = None
		for cat_id, cat_name in game_cats.items():
			if cat_name == category_meta:
				category_id = cat_id
				break

		# If no category exists with the given name, raise ValueError and quit.
		if not category_id:
			raise ValueError("Category not found in game")

		# Query SRDC for all world records under these parameters.
		runs = self.search_il_wrs(game_id)
		if not runs:
			raise ValueError("No IL world records could be found for these conditions.")

		# This returns a large list of runs. We need to filter it down to
		# just the one that the user asked for. If the new list is completely
		# empty, then raise a ValueError
		run = [r for r in runs if r["level"] == level_id and r["category"] == category_id]
		if not run:
			raise ValueError("No IL world records could be found for these conditions.")

		# This doesn't need to be sorted, nor do we need to find run placement, as the
		# parameters ensure only one run will be returned, which will be the world record.
		# Just return this run from the data given.
		# (Yes, I know the parameters below are extremely cursed: scromapi parses this
		# very bizarrely for some reason lol)
		sr = self.utils.extract_run(run[0]["runs"][0]["run"], run[0]["players"]["data"][0]["names"]["international"])
		return sr
