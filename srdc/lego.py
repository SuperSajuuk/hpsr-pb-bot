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


# LEGONormalRun
# This handles the logic of querying the SRDC
# API for a LEGO Games run submission. This is
# used by !run only.
class LEGONormalRun:
	def __init__(self, api, game_map, category_map, category_aliases, sub_category_aliases, token_aliases, utils):
		self.api = api
		self.game_map = game_map
		self.category_map = category_map
		self.category_aliases = category_aliases
		self.sub_category_aliases = sub_category_aliases
		self.token_aliases = token_aliases
		self.utils = utils

	def process_lego_main_board(self, game: str, board_name: str, flags: dict, player: str):
		# Check if the game provided is in the game map.
		lego_key = self.game_map.get(game)
		if not lego_key:
			return None

		# Check if there is an alias table for this game.
		alias_table = self.category_aliases.get(game, {})
		if not alias_table:
			return None

		# Check if the top board is defined in the alias list.
		# If it isn't, the user might have provided an alternative
		# name, which needs to be checked
		if board_name not in alias_table:
			token_aliases = self.token_aliases.get(lego_key["slug"], None)
			if token_aliases is None:
				return None
			for name, aliases in token_aliases.items():
				if board_name in aliases:
					board_name = name
					break

			# Still not found, so just exit.
			if board_name is None:
				return None

		# Use the board_token (the top-level board) to find
		# actual internal token name (this is needed to ensure
		# random user input always maps to the correct internal
		# value).
		#
		# If this returns None, then whatever token they provided
		# does not exist in the alias table.
		sub_category_board = flags.get("main_sub_category", None)
		board_token = alias_table[board_name].get(sub_category_board, None)
		if not board_token:
			return None

		# Build an internal key based on the values of flags.
		is_nocut5_mode = flags.get("nocut_mode", None)
		is_restricted = flags.get("restricted_mode", None)
		ik_nocut_mode = ""
		ik_restricted_mode = ""
		scn_nocut_mode = ""
		scn_restricted_mode = ""
		if is_nocut5_mode is not None:
			ik_nocut_mode = "_nocut" if is_nocut5_mode else "_standard"
			scn_nocut_mode = " N0CUT5" if is_nocut5_mode else " Standard"
		if is_restricted is not None:
			ik_restricted_mode = "_restricted" if is_restricted else "_unrestricted"
			scn_restricted_mode = " Restricted" if is_restricted else " Unrestricted"

		internal_key = f"{board_name}_{sub_category_board}{ik_nocut_mode}{ik_restricted_mode}"
		run = self.lookup_lego_run(game, internal_key, lego_key["slug"], board_name, player)

		# Produce a clean category name based on the alias value. This
		# allows one "output" name against lots of aliases for tidiness
		# of the board aliases.
		alias_name = None
		for name, aliases in self.category_map[game].items():
			if board_name in aliases:
				alias_name = name
				break

		# Unlike other boards, cat_clean_name can be derived from user flags
		sub_cat_name = None
		for name, aliases in self.sub_category_aliases[game].items():
			if sub_category_board in aliases:
				sub_cat_name = name
				break

		# Produce the necessary alias name for the attempted category
		# solely based on various flags.
		new_sub_cat_name = f"{sub_cat_name}{scn_nocut_mode}{scn_restricted_mode}"
		return run, new_sub_cat_name, alias_name

	def lookup_lego_run(self, game: str, internal_key: str, slug: str, cat_key: str, player: str) -> SpeedRun | None:
		"""
		Look up the fastest verified run for a player in a specific game/category.
		Uses SRDC variable filters and client-side filtering to ensure only the run the
		user requested is returned (this is due to the way SRDC returns runs from the API)
		"""
		# Get the game object from the slug.
		# Obtain the relevant category name from the category map.
		game_id, game_cats = self.utils.get_game_code(slug)
		category_meta = None
		for category_name, aliases in self.category_map[game].items():
			if cat_key in aliases:
				category_meta = category_name
				break

		# Return if category_meta is still None (no match would have been found)
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

		# Resolve user ID and pull in all variables for the game.
		user_id = self.utils.get_user_id(player)
		cfg = self.utils.resolve_leaderboard_config(game, internal_key, cat_key)
		if cfg is None:
			raise ValueError(f"Missing leaderboard configuration data for key: '{internal_key}'.")

		# With the provided data, search SRDC for runs.
		# If nothing there, just return None.
		var_filters = cfg.get("variables", None)
		runs = self.utils.search_runs(game_id, category_id, user_id, var_filters)
		if not runs:
			return None

		# LEGO runs contain a significant number of variables, which require
		# the returned list of runs to be filtered. This ensures only the
		# run the user asked for is returned by the system.
		required_variables = {var["var_id"]: var["value_id"] for var in var_filters}
		filtered_runs = []
		for r in runs:
			ok = True
			for var_id, value_id in required_variables.items():
				if r["values"].get(var_id) != value_id:
					ok = False
					break
			if ok:
				filtered_runs.append(r)

		# If no runs were found, return None
		if not filtered_runs:
			return None

		# Sort the runs by the most recently verified run (newest at the top)
		# The run at the top of the index will then be used to get its placement
		# in the leaderboard. To avoid duplication, leaderboard placement is
		# parsed by a helper function.
		filtered_runs.sort(key=lambda rx: rx["submitted"], reverse=True)
		best_run = filtered_runs[0]

		# Extract all run details and the leaderboard placement, then return the run object.
		place = self.utils.lookup_run_place(game_id, category_id, best_run["id"], required_variables)
		sr = self.utils.extract_run(best_run, player)
		sr.place = place
		return sr
