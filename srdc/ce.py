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
	def __init__(self, api, game_map, category_map, category_aliases, board_aliases, token_aliases, md_aliases, lb_config, utils):
		self.api = api
		self.game_map = game_map
		self.category_map = category_map
		self.category_aliases = category_aliases
		self.board_aliases = board_aliases
		self.token_aliases = token_aliases
		self.md_aliases = md_aliases
		self.lb_config = lb_config
		self.utils = utils

	# Resolve the Game Slug for a CE
	# Using just the game code provided, check our
	# local config for that code. If it's not there,
	# query SRDC and ensure it does have the category
	# extension tag.
	def resolve_ce_game_slug(self, base_game: str) -> dt.Game | str:
		"""
		Resolve the Game Slug for a Category Extension

		If possible, rely on local config data before querying SRDC.
		If we don't have a config key for this, query SRDC and ensure
		the game does have the Category Extension game type assigned.

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
			raise ValueError(f"No Category Extension game found for base game: {base_game}")

		# Parse the game object for the relevant tag.
		# This is hard-coded because category extension is
		# always the same and doesn't change.
		game = search[0]
		is_ce = False
		for tag in game["gametypes"]:
			if tag == "53no817x":
				is_ce = True
				break

		# Error here, because the required tag cannot be found.
		if not is_ce:
			raise ValueError(f"No Category Extension game found for base game: {base_game}")

		# Return the game object for this category extension board.
		return game

	def process_category_extension(self, base_game: str, ce_top_board: str, ce_category_board: str, player: str, flags: dict) -> (SpeedRun | None, str | None):
		"""
		Using the provided variables, determine if the category
		extension is configured and whether there is a valid
		category_board value.

		If all above board, pass the data over to lookup_ce_run,
		alongside the player and internal_key and find the run.

		Returns a SpeedRun object or None.
		"""
		# Parse the base_game to see if we have a supported CE
		# board in the code. If not, there is an error.
		ce_key = self.game_map.get(base_game)
		if not ce_key:
			raise InvalidGame(f"Unknown CE game series: '{ce_key}'. Check for typos or whether this is a supported series for CE lookups.")

		# Parse the ce_key (which contains the game name) to see
		# if it exists. If not, there is an error.
		alias_table = self.category_aliases.get(ce_key["id"])
		if not alias_table:
			raise MissingInternalData(f"No alias table exists for ID '{ce_key['id']}, which prevents category matching. Please report this as a bug on the GitHub repository.")

		# Check if the top board is defined in the alias list.
		# If it isn't, the user might have provided an alternative
		# name, which needs to be checked.
		if ce_top_board not in alias_table:
			ce_top_board = self.token_aliases[ce_key["id"]].get(ce_top_board, None)
			if ce_top_board is None:
				raise InvalidCategory("The top-board category name provided could not be found in the alias table. Please check your input, and try again.")

		# Use the board_token (the top-level board) to find the
		# actual internal token name (this is needed to ensure
		# random user input always maps to the correct internal
		# value).
		board_token = None
		for name, aliases in alias_table.get(ce_top_board, {}).items():
			if ce_category_board in aliases:
				board_token = name
				break

		# After the loop above, if this is still None, then whatever
		# token they provided does not exist in the alias table.
		if board_token is None:
			raise InvalidCategory("No board token could be found for this category. This could be an issue with your input, or no alias data exists to create a mapping.")

		# Build the internal key and lookup the CE.
		internal_key = f"{ce_top_board}_{board_token}"
		run = self.lookup_ce_run(base_game, internal_key, player)

		# Produce a clean name based on the alias value. This allows one
		# "output" name against lots of aliases for tidiness of the
		# board aliases.
		alias_name = None
		cat_alias_name = None
		for name, aliases in self.board_aliases.items():
			if ce_top_board in aliases:
				alias_name = name
				break
		for name, aliases in self.category_map.items():
			if ce_category_board in aliases:
				cat_alias_name = name
				break

		# Return the run object and the alias_name produced.
		return run, cat_alias_name, alias_name

	def lookup_ce_run(self, base_game: str,	ce_category: str, player: str) -> SpeedRun | None:
		"""
		Resolve and fetch a Category Extensions run using the same SRDC logic as normal runs,
		but with CE-specific variables.

		Returns a SpeedRun object or None if nothing was found.
		"""
		# Find the required Slug URL for this category extension board,
		# then resolve the slug to find the game object.
		ce_slug = self.resolve_ce_game_slug(base_game)
		slug_id = ce_slug.get("id", None)
		game_id, game_cats = self.utils.get_game_code(slug_id)

		# Find the leaderboard config for this category.
		cfg = self.lb_config.get(slug_id)
		if cfg is None:
			raise MissingInternalData(f"No leaderboard config found for CE game slug: {slug_id}")

		# Category metadata is necessary for CEs: if nothing is found, or the
		# CE category cannot be found in the configuration, return an error.
		if ce_category not in cfg:
			raise MissingInternalData(f"Unknown CE category key: {ce_category}")

		# Using the CE Category config, search the SRDC Game categories
		# list to find the matching board name.
		category_meta = cfg[ce_category]
		category_id = None
		for cat_id, cat_name in game_cats.items():
			if cat_name == category_meta["board"]:
				category_id = cat_id
				break

		# If category_id is still None, then the category does not exist.
		if not category_id:
			raise InvalidCategory("CE category not found in CE game")

		# Resolve the user ID and capture the category vars. Then,
		# search for runs, if none found then return.
		user_id = self.utils.get_user_id(player)
		ce_cat_vars = category_meta.get("variables", [])
		runs = self.utils.search_runs(game_id, category_id, user_id, ce_cat_vars)
		if not runs:
			return None

		# Because CE's contain a lot of sub-boards, the returned list will contain
		# a lot of additional runs. The list of runs must be filtered to get
		# the correct run that the user asked for.
		required_variables = [{var["var_id"]: var["value_id"] for var in ce_cat_vars}]
		filtered_runs = self.utils.filter_all_runs(runs, required_variables)

		# If no runs were found, return None
		if not filtered_runs:
			return None

		# Sort the runs by the most recently verified run (newest at the top).
		# As this is likely to be a very short list, the expected run would be
		# the most recently submitted. Select it, then find its placement on the
		# leaderboard. Return the SpeedRun object for this run using the helpers.
		filtered_runs.sort(key=lambda rx: rx["submitted"], reverse=True)
		best_run = filtered_runs[0]
		place = self.utils.lookup_run_place(game_id, category_id, best_run["id"], required_variables)
		sr = self.utils.extract_run(best_run, player)
		sr.place = place
		return sr
