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
import srcomapi.datatypes as dt


# MultiRun
# This handles the logic of querying the SRDC
# API for a Multirun submission.
# This is used by !run only.
class MultiRun:
	def __init__(self, api, game_map, platform_map, category_map, category_aliases, board_aliases, token_aliases, lb_config, utils):
		self.api = api
		self.game_map = game_map
		self.platform_map = platform_map
		self.category_map = category_map
		self.category_aliases = category_aliases
		self.board_aliases = board_aliases
		self.token_aliases = token_aliases
		self.lb_config = lb_config
		self.utils = utils

	# Resolve the Game Slug for a Multirun
	# Using just the game code provided, check our
	# local config for that code. If it's not there,
	# query SRDC and ensure it does have the category
	# extension tag.
	def resolve_multirun_game_slug(self, base_game: str) -> dt.Game | str:
		"""
		Resolve the Game Slug for a Multirun

		If possible, rely on local config data before querying SRDC.
		If we don't have a config key for this, query SRDC and ensure
		the game does have the Multi Run game type assigned.

		Raises ValueError if no such game is found.
		"""
		# Check if the base game key is already in the game map.
		# Use it first before querying SRDC.
		if base_game in self.game_map:
			return self.game_map[base_game]

		# Couldn't find it in our hard-coded list, so
		# query SRDC for the specific game that is needed.
		search = self.api.get(f"games?abbreviation={base_game}&embed=tags")
		if not search:
			raise ValueError(f"No Multi-run game found for base game: {base_game}")

		# Parse the game object for the relevant tag.
		# This is hard-coded because multi-run is
		# always the same and doesn't change.
		game = search[0]
		is_multi_run = False
		for tag in game["gametypes"]:
			if tag == "rj1dy1o8":
				is_multi_run = True
				break

		# Error here, because the required tag cannot be found.
		if not is_multi_run:
			raise ValueError(f"No Multi-run game found for base game: {base_game}")

		# Return the game object for this multi-run board.
		return game

	def process_multi_run(self, base_game: str, mr_board: str, mr_category_board: str, player: str) -> (SpeedRun | None, str | None):
		"""
		Using the provided variables, determine if the multi-run board
		is configured and whether there is a valid mr_board value.

		If all above board, pass the data over to lookup_ce_run,
		alongside the player and internal_key and find the run.

		Returns a SpeedRun object or None.
		"""
		# Parse the base_game to see if we have a supported multi-run
		# board in the code. If not, there is an error.
		mr_key = self.game_map.get(base_game)
		if not mr_key:
			return None

		# Parse the mr_key (which contains the game name) to see
		# if it exists. If not, there is an error.
		alias_table = self.category_aliases.get(mr_key["id"])
		if not alias_table:
			return None

		# Check if the top board is defined in the alias list.
		# If it isn't, the user might have provided an alternative
		# name, which needs to be checked
		if mr_board not in alias_table:
			mr_board = self.token_aliases[mr_key["id"]].get(mr_board, None)
			if mr_board is None:
				return None

		# Use the board_token (the top-level board) to find
		# actual internal token name (this is needed to ensure
		# random user input always maps to the correct internal
		# value).
		#
		# If this returns None, then whatever token they provided
		# does not exist in the alias table.
		board_token = alias_table[mr_board].get(mr_category_board, None)
		if board_token is None:
			return None

		# Build the internal key and lookup the multi-run.
		internal_key = f"{mr_board}_{board_token}"
		run = self.lookup_multi_run(base_game, internal_key, player)

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

	def lookup_multi_run(self, base_game: str, mr_category: str, player: str) -> SpeedRun | None:
		"""
		Resolve and fetch a Multirun Board run using the same SRDC logic as normal runs,
		but with multirun-specific variables.
		"""
		# Find the required Slug URL for this category extension board,
		# then resolve the slug to find the game object.
		mr_slug = self.resolve_multirun_game_slug(base_game)
		slug_id = mr_slug.get("id", None)
		game_id, game_cats = self.utils.get_game_code(slug_id)

		# Find the leaderboard config for this category.
		cfg = self.lb_config.get(slug_id)
		if cfg is None:
			raise ValueError(f"No leaderboard config found for Multirun game slug: {slug_id}")

		# Category metadata is necessary for Multiruns: if nothing is found, or the
		# Multirun category cannot be found in the configuration, return an error.
		if mr_category not in cfg:
			raise ValueError(f"Unknown Multirun category key: {mr_category}")

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
			raise ValueError("Multirun category not found in Multirun game")

		# Resolve the user ID, capture the category vars and then search for runs.
		user_id = self.utils.get_user_id(player)
		mr_cat_vars = category_meta.get("variables", [])
		runs = self.utils.search_runs(game_id, category_id, user_id, mr_cat_vars)
		if not runs:
			return None

		# Sort the runs by the most recently verified run (newest at the top).
		runs.sort(key=lambda rx: rx["submitted"], reverse=True)

		# Unlike category extensions, multi-runs tends to have very few sub-boards
		# However, as they're still a form of category extension, we do need to ensure
		# all returned runs are filtered to get the correct run that the user asked for.
		required_variables = {var["var_id"]: var["value_id"] for var in mr_cat_vars}
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

		# The only run that we have is the one that the user asked form.
		# Lookup the placement and extract run data, using the same helper as normal runs
		best_run = filtered_runs[0]
		place = self.utils.lookup_run_place(game_id, category_id, best_run["id"], required_variables)
		sr = self.utils.extract_run(best_run, player)
		sr.place = place
		return sr
