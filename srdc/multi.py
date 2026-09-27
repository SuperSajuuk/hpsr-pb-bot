#
# Multirun Boards
#
# This code processes a Multirun Board Run object. A Multirun board is
# basically a category extension board, but the type of categories are
# specifically about running more than one game. Such boards usually have
# the "Multi-game" tag on them. Should a user provide a game which we
# do not have a hard-coded value for, the system will look up SRDC and
# then fail if no board exists.
from utils.model import SpeedRun
from utils.exceptions import InvalidGame, InvalidCategory, InvalidPlatform, MissingInternalData
import srcomapi.datatypes as dt


# MultiRun
# This handles the logic of querying the SRDC
# API for a Multirun submission.
# This is used by !run only.
class MultiRun:
	def __init__(self, api, game_map, category_map, category_aliases, board_aliases, token_aliases, lb_config, utils):
		self.api = api
		self.game_map = game_map
		self.category_map = category_map
		self.category_aliases = category_aliases
		self.board_aliases = board_aliases
		self.token_aliases = token_aliases
		self.lb_config = lb_config
		self.utils = utils

	def process_multi_run(self, base_game: str, mr_board: str, mr_category_board: str, player: str, flags: dict) -> (SpeedRun | None, str | None):
		"""
		Using the provided variables, determine if the multi-run board
		is configured and whether there is a valid mr_board value.

		If all above board, pass the data over to lookup_ce_run,
		alongside the player and internal_key and find the run.

		Returns a SpeedRun object or None.
		"""
		# Parse the base_game value to see if this is defined internally.
		# If not, look up SRDC and raise InvalidGame if nothing is found.
		mr_key = self.game_map.get(base_game)
		if not mr_key:
			lk = self.api.get_ce_mr_game(base_game, "rj1dy1o8", "Multi-run")
			if not lk:
				raise InvalidGame(f"Unknown Multirun game series: '{base_game}'. Check for typos or whether this is a supported series for multirun lookups.")
			mr_key = {"name": lk["names"]["international"], "id": lk["abbreviation"]}

		# Check for a table of aliases referring to the categories.
		# Even if the game object is returned by SRDC, an alias table
		# is still required internally, as it's used to map user input
		# to a hard-coded internal name.
		alias_table = self.category_aliases.get(mr_key["id"])
		if not alias_table:
			raise MissingInternalData(f"No alias table exists for ID '{mr_key['id']}, which prevents category matching. Please report this as a bug on the GitHub repository.")

		# Check if the top board is defined in the alias list.
		# If it isn't, the user might have provided an alternative
		# name, which needs to be checked
		if mr_board not in alias_table:
			mr_board = self.token_aliases[mr_key["id"]].get(mr_board, None)
			if mr_board is None:
				raise InvalidCategory("The top-board category name provided could not be found in the alias table. Please check your input, and try again.")

		# Use the board_token (the top-level board) to find
		# actual internal token name (this is needed to ensure
		# random user input always maps to the correct internal
		# value).
		#
		# If this returns None, then whatever token they provided
		# does not exist in the alias table.
		board_token = alias_table[mr_board].get(mr_category_board, None)
		if board_token is None:
			raise InvalidCategory("No board token could be found for this category. This could be an issue with your input, or no alias data exists to create a mapping.")

		# Build the internal key and lookup the multi-run.
		internal_key = f"{mr_board}_{board_token}"
		run = self.lookup_multi_run(mr_key["id"], internal_key, player, flags)

		# Produce a clean name based on the alias value. This allows one
		# "output" name against lots of aliases for tidiness of the
		# board aliases.
		alias_name = None
		cat_clean_name = None
		for name, aliases in self.board_aliases.items():
			if mr_board in aliases:
				alias_name = name
				break
		for name, aliases in self.category_map.items():
			if mr_category_board in aliases:
				cat_clean_name = name
				break

		# Return the run object and the alias_name produced.
		return run, cat_clean_name, alias_name

	def lookup_multi_run(self, slug_id: str, mr_category: str, player: str, flags: dict) -> SpeedRun | None:
		"""
		Resolve and fetch a Multirun Board run using the same SRDC logic as normal runs,
		but with multirun-specific variables.
		"""
		# Resolve the Slug ID for its SRDC ID and all categories,
		# then capture the leaderboard data.
		game_id, game_cats = self.api.get_game_code(slug_id)
		cfg = self.lb_config.get(slug_id)
		if cfg is None:
			raise MissingInternalData(f"No leaderboard config found for Multirun game slug: {slug_id}")

		# Category metadata is necessary for Multiruns: if nothing is found, or the
		# Multirun category cannot be found in the configuration, return an error.
		if mr_category not in cfg:
			raise MissingInternalData(f"Unknown Multirun category key: {mr_category}")

		# Using the CE Category config, search the SRDC Game categories
		# list to find the matching board name.
		category_meta = cfg[mr_category]
		category_id = None
		for cat_id, cat_name in game_cats.items():
			if cat_name == category_meta["board"]:
				category_id = cat_id
				break

		# If category_obj is still None, then the category does not exist.
		if not category_id:
			raise InvalidCategory("Multirun category not found in Multirun game")

		# Resolve the user ID, capture the category vars and then search for runs.
		user_id = self.api.get_user_id(player)
		mr_cat_vars = self.utils.generate_var_filters(category_meta, flags)
		runs = self.api.search_runs(game_id, category_id, user_id, mr_cat_vars)
		if not runs:
			return None

		# Unlike CE's, multiruns tend to have fewer sub-categories, however the
		# returned list will contain a lot of additional runs. The list of runs
		# must be filtered to get the correct run that the user asked for.
		filtered_runs = self.utils.filter_all_runs(runs, mr_cat_vars)
		if not filtered_runs:
			return None

		# Sort the runs by the most recently verified run (newest at the top).
		# As this is likely to be a very short list, the expected run would be
		# the most recently submitted. Select it, then find its placement on the
		# leaderboard. Return the SpeedRun object for this run using the helpers.
		filtered_runs.sort(key=lambda rx: rx["submitted"], reverse=True)
		best_run = filtered_runs[0]
		place = self.utils.lookup_run_place(game_id, category_id, best_run["id"], mr_cat_vars)
		sr = self.utils.extract_run(best_run, player)
		sr.place = place
		return sr
