#
# Normal Run
#
# This code processes a Normal Run object. A normal run is
# defined as something belong to a primary board: ie it isn't
# part of a category extension or a multi-run. These kind of runs
# are the most common lookups we'll do in the code, as it's covering
# the main boards. CE's are to be handled in ce.py and multiruns will
# be in multi.py
from utils.model import SpeedRun
from configs.generic import COMMAND_USAGE_DOC


# NormalRun
# This handles the logic of querying the SRDC
# API for a normal run submission. This is
# used by !run only.
class NormalRun:
	def __init__(self, api, game_map, platform_map, category_map, board_slugs, utils):
		self.api = api
		self.game_map = game_map
		self.platform_map = platform_map
		self.category_map = category_map
		self.board_slugs = board_slugs
		self.utils = utils

	def process_normal_run(self, game: str, platform: str, board: str, player: str, flags: dict):
		"""
		This method will confirm that the game, platform and category
		can be found in the config data, then creates an internal key
		for use within the lookup.

		Returns a SpeedRun object or None.
		"""
		if game not in self.game_map:
			raise ValueError(f"Unknown game: '{game}'. Refer to the docs for the supported games: {COMMAND_USAGE_DOC}")
		if platform not in self.platform_map:
			raise ValueError(f"Unknown platform: '{platform}'. Refer to the docs for the supported platforms: {COMMAND_USAGE_DOC}")

		# Check if the board name is in the category list.
		not_board = True
		category_name = None
		for board_name, aliases in self.category_map.items():
			if board in aliases:
				not_board = False
				category_name = board_name
				break

		# If not found, then raise an error
		if not_board:
			raise ValueError(f"Unknown category/board: '{board}'.  Refer to the docs for the supported categories: {COMMAND_USAGE_DOC}")

		# If there are additional metadata flags, then append it to
		# category name for output. There would usually only be
		# a single key here, hence the hard coding for just key_1.
		if flags.get("additional_metadata", {}):
			category_name += f" {flags['additional_metadata'].get('key_1').capitalize()}"

		# Create an internal key, look up the run, and return the result.
		internal_key = f"{game}_{platform}"
		run = self.lookup_run(internal_key, board, player, flags)
		return run, category_name

	def lookup_run(self, internal_key: str, cat_key: str, player: str, flags: dict | None) -> SpeedRun | None:
		"""
		Look up the fastest verified run for a player in a specific game/category.
		Uses SRDC variable filters and client-side filtering to ensure only the run the
		user requested is returned (this is due to the way SRDC returns runs from the API)
		"""
		# Parse the internal_key and cat_key to obtain the game and category.
		slug = self.board_slugs[internal_key]
		game_id, game_cats = self.utils.get_game_code(slug)

		# Obtain the relevant category name from the category map.
		category_meta = None
		for category_name, aliases in self.category_map.items():
			if cat_key in aliases:
				category_meta = category_name
				break

		if not category_meta:
			return None

		# Check that there is a category matching the one we asked for.
		category_id = None
		for cat_id, cat_name in game_cats.items():
			if cat_name == category_meta:
				category_id = cat_id
				break

		# If no category exists with the given name, raise ValueError and quit.
		if not category_id:
			raise ValueError("Category not found in game")

		# # Done the checks, but need to do a small additive to cat_key.
		# # If additional metadata exists, append key as suffix.
		# print(cat_key)
		# if flags["additional_metadata"]:
		# 	for key, val in flags["additional_metadata"].items():
		# 		cat_key += f"_{val}"

		# Resolve user ID, then check for variables in case we have one.
		user_id = self.utils.get_user_id(player)
		cfg = self.utils.resolve_leaderboard_config(slug, internal_key, cat_key)
		cfg_2 = None
		if cfg is not None:
			cfg_2 = cfg.get(cat_key, None)

		# Check if either cfg or cfg_2 contains a variables key.
		# If so, capture all variables and build a var_filters list
		# for use in the query.
		var_filters = None
		active_slice = None
		if (cfg and "variables" in cfg) or (cfg_2 and "variables" in cfg_2):
			# All the variable data is stored in the "variables" key.
			# Use that to capture all the relevant info we need.
			# Some keys might contain names to define what they are.
			variable_data = cfg.get("variables", None)
			if variable_data is None:
				variable_data = cfg_2.get("variables", [])

			# Check the user provided flags against the slice names.
			slice_names = {x["name"] for x in variable_data if "name" in x}
			if flags:
				# Flags that match slice names AND are True.
				# If any are found, select it as the active slice.
				true_flags = {name for name in slice_names if flags.get(name) is True}
				if true_flags:
					active_slice = next(iter(true_flags))
				else:
					# Perhaps check in the additional metadata in case there's something there.
					additional_flags = {name for key, name in flags["additional_metadata"].items()}
					if additional_flags:
						active_slice = next(iter(additional_flags))
					else:
						active_slice = next((name for name in slice_names if name not in flags), None)

			# This might still be None: in which case, just pick the first slice.
			if active_slice is None:
				active_slice = next(iter(slice_names), None)

			# Build var_filters
			var_filters = []
			for x in variable_data:
				if "name" not in x:
					var_filters.append({x["var_id"]: x["value_id"]})
					continue
				if x.get("name") == active_slice:
					var_filters.append({x["var_id"]: x["value_id"]})
					continue

		# With the provided data, search SRDC for runs.
		# If nothing there, just return None.
		runs = self.utils.search_runs(game_id, category_id, user_id, var_filters)
		if not runs:
			return None

		# After returning runs, you may receive more than you asked for: this
		# is a limitation of SRDC. Thus, to just have "one run", we need to do
		# some filtering here.
		if active_slice is not None:
			filtered_runs = []
			for r in runs:
				# Check if this run matches the chosen slice
				for x in var_filters:
					for key, val in x.items():
						if r["values"].get(key) == val:
							filtered_runs.append(r)
							break
			runs = filtered_runs

		# If nothing remains after filtering, return None
		if not runs:
			return None

		# Sort the runs by the most recently verified run (newest at the top)
		# The run at the top of the index will then be used to get its placement
		# in the leaderboard. To avoid duplication, leaderboard placement is
		# parsed by a helper function.
		runs.sort(key=lambda rx: rx["submitted"], reverse=True)
		best_run = runs[0]

		# Extract all run details and the leaderboard placement, then return the run object.
		place = self.utils.lookup_run_place(game_id, category_id, best_run["id"], var_filters[0] if var_filters is not None else None)
		sr = self.utils.extract_run(best_run, player)
		sr.place = place
		return sr
