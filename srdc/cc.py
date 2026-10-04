#
# Custom Content Run
#
# This code processes a Custom Content Run object. A CC run is
# defined as a run belonging to a defined Custom Content board:
# such boards have the "Modification" tag on them. Should a
# user provide a game which we do not have a hard-coded value for,
# the system will look up SRDC and then fail if no board exists.
from utils.model import SpeedRun
from utils.exceptions import InvalidGame, InvalidCategory, InvalidPlatform, MissingInternalData
import srcomapi.datatypes as dt


# CustomContent
# This handles the logic of querying the SRDC
# API for a category extension run submission.
# This is used by !run only.
class CustomContent:
	def __init__(self, api, game_map, category_map, category_aliases, board_aliases, md_aliases, lb_config, utils):
		self.api = api
		self.game_map = game_map
		self.category_map = category_map
		self.category_aliases = category_aliases
		self.board_aliases = board_aliases
		self.md_aliases = md_aliases
		self.lb_config = lb_config
		self.utils = utils

	def process_custom_content(self, base_game: str, cc_top_board: str, cc_category_board: str, player: str, flags: dict) -> (SpeedRun | None, str | None):
		"""
		Using the provided variables, determine if the category
		extension is configured and whether there is a valid
		category_board value.

		If all above board, pass the data over to lookup_ce_run,
		alongside the player and internal_key and find the run.

		Returns a SpeedRun object or None.
		"""
		# Parse the base_game value to see if this is defined internally.
		# If not, look up SRDC and raise InvalidGame if nothing is found.
		cc_key = self.game_map.get(base_game)
		if not cc_key:
			lk = self.api.get_ce_mr_game(base_game, "lyn97m9o", "custom content")
			if not lk:
				raise InvalidGame(f"Unknown CE game series: '{base_game}'. Check for typos or whether this is a supported series for CE lookups.")
			cc_key = {"name": lk["names"]["international"], "id": lk["abbreviation"]}

		# Check for a table of aliases referring to the categories.
		# Even if the game object is returned by SRDC, an alias table
		# is still required internally, as it's used to map user input
		# to a hard-coded internal name.
		alias_table = self.category_aliases.get(cc_key["id"])
		if not alias_table:
			raise MissingInternalData(f"No alias table exists for ID '{cc_key['id']}, which prevents category matching. Please report this as a bug on the GitHub repository.")

		# Check if the top board is defined in the alias list.
		# Currently, this does not support alternative aliases from
		# user input, as CC boards usually contain smaller amounts
		# of data.
		if cc_top_board not in alias_table:
			raise InvalidCategory("The top-board category name provided could not be found in the alias table. Please check your input, and try again.")

		# Use the board_token (the top-level board) to find the
		# actual internal token name (this is needed to ensure
		# random user input always maps to the correct internal
		# value).
		board_token = None
		for name, aliases in alias_table.get(cc_top_board, {}).items():
			if cc_category_board in aliases:
				board_token = name
				break

		# After the loop above, if this is still None, then whatever
		# token they provided does not exist in the alias table.
		if board_token is None:
			raise InvalidCategory("No board token could be found for this category. This could be an issue with your input, or no alias data exists to create a mapping.")

		# Produce a clean name based on the alias value. This allows one
		# "output" name against lots of aliases for tidiness of the
		# board aliases.
		board_alias_name = None
		for name, aliases in self.category_map.items():
			if cc_category_board in aliases:
				board_alias_name = name
				break

		# Generate the internal key, process additional metadata and
		# then look up the custom category run.
		internal_key = f"{cc_top_board}_{board_token}"
		board_alias_name, int_key = self.utils.process_additional_md(flags["additional_metadata"], self.md_aliases, board_alias_name, internal_key, cat_name_extend=False)
		run = self.lookup_cc_run(cc_key["id"], int_key, player, flags)

		# Create the category name output string
		# Currently, this is crafted from the additional metadata, but
		# that isn't very ideal, in future I'll move this to a better
		# system.
		alias_name = ""
		for val in flags["additional_metadata"].values():
			for name, data in self.md_aliases.items():
				if val in data["aliases"]:
					alias_name += f"{name} "
					break

		return run, board_alias_name, alias_name.strip()

	def lookup_cc_run(self, slug_id: str, cc_category: str, player: str, flags: dict = None) -> SpeedRun | None:
		"""
		Resolve and fetch a Custom Content run using the same SRDC logic as normal runs,
		but with CC-specific variables.

		Returns a SpeedRun object or None if nothing was found.
		"""
		# Resolve the Slug ID for its SRDC ID and all categories,
		# then capture the leaderboard data.
		game_id, game_cats = self.api.get_game_code(slug_id)
		cfg = self.lb_config.get(slug_id)
		if cfg is None:
			raise MissingInternalData(f"No leaderboard config found for Custom Content game slug: {slug_id}")

		# Category metadata is necessary for Custom Content boards: if nothing is found,
		# or the CC category cannot be found in the configuration, return an error.
		if cc_category not in cfg:
			raise MissingInternalData(f"Unknown Custom Content category key: {cc_category}")

		# Using the CE Category config, search the SRDC Game categories
		# list to find the matching board name.
		category_meta = cfg[cc_category]
		category_id = None
		for cat_id, cat_name in game_cats.items():
			if cat_name.strip() == category_meta["board"]:
				category_id = cat_id
				break

		# If category_id is still None, then the category does not exist.
		if not category_id:
			raise InvalidCategory("Custom Content category not found in CC game.")

		# Resolve the user ID and capture the category vars. If the
		# metadata parameter is not None, set a slice to capture the
		# specific piece of metadata that was asked for.
		user_id = self.api.get_user_id(player)
		cc_cat_vars = self.utils.generate_var_filters(category_meta, flags)

		# Search for runs, if none found then return.
		runs = self.api.search_runs(game_id, category_id, user_id, cc_cat_vars)
		if not runs:
			return None

		# Custom Content boards are unlikely to return very many sub-boards, due
		# to them involving modded content, which tend to contain a limited number
		# of boards. Still though, the list of runs must be filtered to get the
		# correct run that the user asked for.
		filtered_runs = self.utils.filter_all_runs(runs, cc_cat_vars)
		if not filtered_runs:
			return None

		# Sort the runs by the most recently verified run (newest at the top).
		# As this is likely to be a very short list, the expected run would be
		# the most recently submitted. Select it, then find its placement on the
		# leaderboard. Return the SpeedRun object for this run using the helpers.
		filtered_runs.sort(key=lambda rx: rx["submitted"], reverse=True)
		best_run = filtered_runs[0]
		place = self.utils.lookup_run_place(game_id, category_id, best_run["id"], cc_cat_vars)
		sr = self.utils.extract_run(best_run, player)
		sr.place = place
		return sr
