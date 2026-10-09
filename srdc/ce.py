#
# Category Extension Run
#
# This code processes a Category Extension Run object. A CE run is
# defined as a run belonging to a defined Category Extension board:
# such boards have the "Category Extension" tag on them. Should a
# user provide a game which we do not have a hard-coded value for,
# the system will look up SRDC and then fail if no board exists.
from utils.model import SpeedRun
from utils.exceptions import InvalidGame, InvalidCategory, InvalidPlatform, MissingInternalData
import srcomapi.datatypes as dt


# CategoryExtension
# This handles the logic of querying the SRDC
# API for a category extension run submission.
# This is used by !run only.
class CategoryExtension:
	def __init__(self, api, game_map, category_aliases, board_aliases, md_aliases, lb_config, utils):
		self.api = api
		self.game_map = game_map
		self.category_aliases = category_aliases
		self.board_aliases = board_aliases
		self.md_aliases = md_aliases
		self.lb_config = lb_config
		self.utils = utils

	def process_category_extension(self, base_game: str, ce_top_board: str, ce_category_board: str, player: str, flags: dict) -> (SpeedRun | None, str | None):
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
		ce_key = self.game_map.get(base_game)
		if not ce_key:
			lk = self.api.get_ce_mr_game(base_game, "53no817x", "category extension")
			if not lk:
				raise InvalidGame(f"Unknown CE game series: '{base_game}'. Check for typos or whether this is a supported series for CE lookups.")
			ce_key = {"name": lk["names"]["international"], "id": lk["abbreviation"]}

		# Pull in game id and game cats from cache/SRDC, alongside
		# the leaderboard data. Unlike normal runs, CE's require leaderboard
		# data, so if there isn't anything, we have to abandon.
		slug_id = ce_key["id"]
		game_id, game_cats = self.api.get_game_code(slug_id)
		cfg = self.lb_config.get(slug_id)
		if cfg is None:
			raise MissingInternalData(f"No leaderboard config found for CE game slug: {slug_id}")

		# Check if the ce_top_board is in the defined category list.
		tb_int_name = None
		ce_top_board_name = None
		for board_name, data in cfg["categories"].items():
			if ce_top_board in data["aliases"]:
				tb_int_name = data["internal_name"]
				ce_top_board_name = board_name
				break

		# Build the internal key and check if it can be found in the key list.
		internal_key = f"{base_game}_{tb_int_name}"
		if internal_key not in cfg:
			raise MissingInternalData(f"Internal key '{internal_key}' cannot be found.")

		# Check for a table of aliases referring to the categories. Also,
		# do a check for tb_int_name being in the alias_table.
		# Even if the game object is returned by SRDC, an alias table
		# is still required internally, as it's used to map user input
		# to a hard-coded internal name.
		alias_table = self.category_aliases.get(slug_id)
		if not alias_table:
			raise MissingInternalData(f"No alias table exists for ID '{slug_id}, which prevents category matching. Please report this as a bug on the GitHub repository.")
		if tb_int_name not in alias_table:
			raise InvalidCategory("The top-board category name provided could not be found in the alias table. Please check your input, and try again.")

		# Use the board_token (the top-level board) to find the
		# actual internal token name (this is needed to ensure
		# random user input always maps to the correct internal
		# value).
		board_token = None
		for name, aliases in alias_table.get(tb_int_name, {}).items():
			if ce_category_board in aliases:
				board_token = name
				break

		# After the loop above, if this is still None, then whatever
		# token they provided does not exist in the alias table.
		if board_token is None:
			raise InvalidCategory("No board token could be found for this category. This could be an issue with your input, or no alias data exists to create a mapping.")

		# Look for the CE run.
		# To avoid issues, ce_board is overwritten with the value of
		# board_token above.
		flags["ce_board"] = board_token
		run = self.lookup_ce_run(game_id, game_cats, cfg[internal_key], player, flags)

		# Produce a clean name based on the alias value. This allows one
		# "output" name against lots of aliases for tidiness of the
		# board aliases.
		cat_alias_name = None
		for name, aliases in cfg["sub_categories"].items():
			if ce_category_board in aliases:
				cat_alias_name = name
				break

		# Return the run object and the alias_name produced.
		cat_alias_name, _ = self.utils.process_additional_md(flags["additional_metadata"], self.md_aliases, cat_alias_name)
		return run, cat_alias_name, ce_top_board_name

	def lookup_ce_run(self, game_id: str, game_cats: dict, cat_data: dict, player: str, flags: dict = None) -> SpeedRun | None:
		"""
		Resolve and fetch a Category Extensions run using the same SRDC logic as normal runs,
		but with CE-specific variables.

		Returns a SpeedRun object or None if nothing was found.
		"""
		# Using the CE Category config, search the SRDC Game categories
		# list to find the matching board name.
		category_id = None
		for cat_id, cat_name in game_cats.items():
			if cat_name == cat_data["board"]:
				category_id = cat_id
				break

		# If category_id is still None, then the category does not exist.
		if not category_id:
			raise InvalidCategory("CE category not found in category extension game")

		# Resolve the user ID, capture the category vars and then search for runs.
		user_id = self.api.get_srdc_user(player)
		ce_cat_vars = self.utils.generate_var_filters(cat_data["variables"], flags)
		runs = self.api.search_runs(game_id, category_id, user_id, ce_cat_vars)
		if not runs:
			return None

		# Because CE's contain a lot of sub-boards, the returned list will contain
		# a lot of additional runs. The list of runs must be filtered to get the
		# correct run that the user asked for.
		filtered_runs = self.utils.filter_all_runs(runs, ce_cat_vars)
		if not filtered_runs:
			return None

		# Sort the runs by the most recently verified run (newest at the top).
		# As this is likely to be a very short list, the expected run would be
		# the most recently submitted. Select it, then find its placement on the
		# leaderboard. Return the SpeedRun object for this run using the helpers.
		filtered_runs.sort(key=lambda rx: rx["submitted"], reverse=True)
		best_run = filtered_runs[0]
		place = self.utils.lookup_run_place(game_id, category_id, best_run["id"], ce_cat_vars)
		sr = self.utils.extract_run(best_run, player)
		sr.place = place
		return sr
