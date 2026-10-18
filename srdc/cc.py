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
	def __init__(self, api, game_map, md_aliases, lb_config, utils):
		self.api = api
		self.game_map = game_map
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
				raise InvalidGame(f"Unknown custom content game series: '{base_game}'. Check for typos or whether this is a supported series for CE lookups.")
			cc_key = {"name": lk["names"]["international"], "id": lk["abbreviation"]}

		# Pull in game id and game cats from cache/SRDC, alongside
		# the leaderboard data. Custom Content boards will often contain
		# leaderboard data, so require it -- even if it's very limited.
		slug_id = cc_key["id"]
		game_id, game_cats = self.api.get_game_code(slug_id)
		cfg = self.lb_config.get(slug_id)
		if cfg is None:
			raise MissingInternalData(f"No leaderboard config found for custom content game slug: {slug_id}")

		# Check if the ce_top_board is in the defined category list.
		tb_int_name = None
		cc_top_board_name = None
		cc_top_board_id = None
		for board_name, data in cfg["categories"].items():
			if cc_top_board in data["aliases"]:
				tb_int_name = data["internal_name"]
				cc_top_board_id = data["board_id"]
				cc_top_board_name = board_name
				break

		# Build the internal key and check if it can be found in the key list.
		internal_key = f"{base_game}_{tb_int_name}"
		if internal_key not in cfg:
			raise MissingInternalData(f"Internal key '{internal_key}' cannot be found.")

		# Check for a table of aliases referring to the categories.
		# Even if the game object is returned by SRDC, an alias table
		# is still required internally, as it's used to map user input
		# to a hard-coded internal name.
		alias_table = cfg.get("sub_categories", None)
		if not alias_table:
			raise MissingInternalData(f"No alias table exists for ID '{cc_key['id']}, which prevents category matching. Please report this as a bug on the GitHub repository.")

		# Use the board_token (the top-level board) to find the
		# actual internal token name (this is needed to ensure
		# random user input always maps to the correct internal
		# value).
		board_token = None
		category_id = None
		cat_alias_name = None
		for name, data in alias_table.items():
			if cc_category_board in data["aliases"]:
				cat_alias_name = name
				board_token = data["internal_name"]
				break

		# After the loop above, if this is still None, then whatever
		# token they provided does not exist in the alias table.
		if board_token is None:
			raise InvalidCategory("No board token could be found for this category. This could be an issue with your input, or no alias data exists to create a mapping.")

		# Generate the variable filters and set the category ID.
		# Am not convinced we need to overwrite the ce_board flag
		# with the board token, but it is fine for now.
		var_filters = self.utils.generate_var_filters(cfg[internal_key]["variables"], flags)
		for cat_id, cat_name in game_cats.items():
			if cat_name == cc_top_board_name or cat_id == cc_top_board_id:
				category_id = cat_id
				break

		# If category_id is still None, then the category does not exist.
		if not category_id:
			raise InvalidCategory("CE category not found in category extension game.")

		# Check if place_num was set.
		if flags["place_num"] > 0:
			run = self.utils.find_run_at_position(game_id, category_id, flags["place_num"], var_filters)
		else:
			run = self.lookup_cc_run(game_id, category_id, player, var_filters)

		# Return the run object and the alias_name produced.
		cat_alias_name, _ = self.utils.process_additional_md(flags["additional_metadata"], self.md_aliases, cat_alias_name)
		return run, cc_top_board_name, cat_alias_name

	def lookup_cc_run(self, game_id: str, category_id: str, player: str, var_filters: list) -> SpeedRun | None:
		"""
		Resolve and fetch a Custom Content run using the same SRDC logic as normal runs,
		but with CC-specific variables.

		Returns a SpeedRun object or None if nothing was found.
		"""
		# Resolve the user ID and then search for runs.
		user_id = self.api.get_srdc_user(player)
		runs = self.api.search_runs(game_id, category_id, user_id, var_filters)
		if not runs:
			return None

		# Custom Content boards are unlikely to return very many sub-boards, due
		# to them involving modded content, which tend to contain a limited number
		# of boards. Still though, the list of runs must be filtered to get the
		# correct run that the user asked for.
		filtered_runs = self.utils.filter_all_runs(runs, var_filters)
		if not filtered_runs:
			return None

		# Sort the runs by the most recently verified run (newest at the top).
		# As this is likely to be a very short list, the expected run would be
		# the most recently submitted. However, just in case, use the helper to
		# find it.
		filtered_runs.sort(key=lambda rx: rx["submitted"], reverse=True)
		best_run, place = self.utils.get_run_and_place(game_id, category_id, filtered_runs, var_filters)
		if best_run is None:
			return None

		# Extract the run object and return it.
		sr = self.utils.extract_run(best_run, player)
		sr.place = place
		return sr
