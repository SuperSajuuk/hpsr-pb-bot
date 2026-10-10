#
# LEGO Games Main Board Run
#
# This code processes a LEGO Games Main Board run object.
#
# This is simply an extension of the normal run class, but instead
# its built to handle the very flexible requirements of certain LEGO
# main boards like Batman, Harry Potter and so on. The reason for that
# is due to the required number of parameters used on such boards: these
# include things like NOCUT5, Solo/Co-Op, Restricted/Unrestricted and so
# on.
from utils.model import SpeedRun
from utils.exceptions import InvalidGame, InvalidCategory, InvalidPlatform, MissingInternalData


# LEGONormalRun
# This handles the logic of querying the SRDC
# API for a LEGO Games run submission. This is
# used by !run only.
class LEGONormalRun:
	def __init__(self, api, game_map, category_aliases, sub_category_aliases, md_aliases, lb_config, utils):
		self.api = api
		self.game_map = game_map
		self.category_aliases = category_aliases
		self.sub_category_aliases = sub_category_aliases
		self.md_aliases = md_aliases
		self.lb_config = lb_config
		self.utils = utils

	def process_lego_main_board(self, game: str, board_name: str, lego_md: dict, player: str, flags: dict):
		# Check if the game provided is in the game map.
		lego_key = self.game_map.get(game)
		if not lego_key:
			raise InvalidGame(f"Unknown LEGO game series: '{game}'. Check for typos or whether this is a supported series for Complex LEGO lookups.")

		# Pull in game id and game cats from SRDC, alongside the
		# leaderboard data.
		slug_id = lego_key["slug"]
		game_id, game_cats = self.api.get_game_code(slug_id)
		cfg = self.lb_config.get(game)
		if cfg is None:
			raise MissingInternalData(f"No leaderboard config found for LEGO game slug: {slug_id}")

		# Check if the board_name is in the defined category list.
		tb_int_name = None
		top_board_name = None
		category_id = None
		for name, data in cfg["categories"].items():
			if board_name in data["aliases"]:
				tb_int_name = data["internal_name"]
				top_board_name = name
				break

		# Check for a table of aliases referring to the categories. Also,
		# do a check for tb_int_name being in the alias_table.
		# Even if the game object is returned by SRDC, an alias table
		# is still required internally, as it's used to map user input
		# to a hard-coded internal name.
		alias_table = self.category_aliases.get(game)
		if not alias_table:
			raise MissingInternalData(f"No alias table exists for ID '{slug_id}, which prevents category matching. Please report this as a bug on the GitHub repository.")
		if tb_int_name not in alias_table:
			raise InvalidCategory("The top-board category name provided could not be found in the alias table. Please check your input, and try again.")

		# Use the board_token (the top-level board) to find
		# actual internal token name (this is needed to ensure
		# random user input always maps to the correct internal
		# value).
		#
		# If this returns None, then whatever token they provided
		# does not exist in the alias table.
		sub_category_board = lego_md.get("main_sub_category", None)
		board_token = alias_table[board_name].get(sub_category_board, None)
		if not board_token:
			raise InvalidCategory("No board token could be found for this category. This could be an issue with your input, or no alias data exists to create a mapping.")

		# Check if N0CUT5 mode was asked for.
		is_nocut5_mode = lego_md.get("nocut_mode", None)
		ik_nocut_mode = ""
		scn_nocut_mode = ""
		if is_nocut5_mode is not None:
			ik_nocut_mode = "_nocut" if is_nocut5_mode else "_standard"
			scn_nocut_mode = " N0CUT5" if is_nocut5_mode else " Standard"

		# Do some additional lookups.
		internal_key = f"{board_name}_{sub_category_board}{ik_nocut_mode}"
		var_filters = self.utils.generate_var_filters(cfg[internal_key]["variables"], flags)
		for cat_id, cat_name in game_cats.items():
			if cat_name == top_board_name:
				category_id = cat_id
				break

		# If no category exists with the given name, raise ValueError and quit.
		if not category_id:
			raise InvalidCategory("The category name provided cannot be found on the SRDC game board.")

		# Find the run (check if place_num is set)
		if flags["place_num"] > 0:
			run = self.utils.find_run_at_position(game_id, category_id, flags["place_num"], var_filters)
		else:
			run = self.lookup_lego_run(game_id, category_id, player, var_filters)

		# Unlike other boards, cat_clean_name can be derived from user flags
		sub_cat_name = None
		for name, aliases in self.sub_category_aliases[game].items():
			if sub_category_board in aliases:
				sub_cat_name = name
				break

		# Process the additional metadata, create the cat name output
		# and return the data.
		sub_cat_name, _ = self.utils.process_additional_md(flags["additional_metadata"], self.md_aliases, sub_cat_name)
		new_sub_cat_name = f"{sub_cat_name}{scn_nocut_mode}"
		return run, new_sub_cat_name, top_board_name

	def lookup_lego_run(self, game_id: str, category_id: str, player: str, var_filters: list) -> SpeedRun | None:
		"""
		Look up the fastest verified run for a player in a specific game/category.
		Uses SRDC variable filters and client-side filtering to ensure only the run the
		user requested is returned (this is due to the way SRDC returns runs from the API)
		"""
		# Resolve user ID and pull in all variables for the game.
		user_id = self.api.get_srdc_user(player)
		runs = self.api.search_runs(game_id, category_id, user_id, var_filters)
		if not runs:
			return None

		# LEGO runs contain a significant number of variables, which require
		# the returned list of runs to be filtered. This ensures only the
		# run the user asked for is returned by the system.
		filtered_runs = self.utils.filter_all_runs(runs, var_filters)
		if not filtered_runs:
			return None

		# Sort the runs by the most recently verified run (newest at the top)
		# The run at the top of the index will then be used to get its placement
		# in the leaderboard. To avoid duplication, leaderboard placement is
		# parsed by a helper function.
		filtered_runs.sort(key=lambda rx: rx["submitted"], reverse=True)
		best_run = filtered_runs[0]

		# Extract all run details and the leaderboard placement, then return the run object.
		place = self.utils.lookup_run_place(game_id, category_id, best_run["id"], var_filters)
		sr = self.utils.extract_run(best_run, player)
		sr.place = place
		return sr
