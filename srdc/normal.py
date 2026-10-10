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
from utils.exceptions import InvalidGame, InvalidCategory, InvalidPlatform, UnsupportedGame, InvalidPosNumber


# NormalRun
# This handles the logic of querying the SRDC
# API for a normal run submission. This is
# used by !run only.
class NormalRun:
	def __init__(self, api, game_map, platform_map, plat_category_map, category_map, board_slugs, md_aliases, wr, utils):
		self.api = api
		self.game_map = game_map
		self.platform_map = platform_map
		self.plat_cat_map = plat_category_map
		self.category_map = category_map
		self.board_slugs = board_slugs
		self.md_aliases = md_aliases
		self.wr = wr
		self.utils = utils

	def process_normal_run(self, game: str, platform: str, board: str, player: str, flags: dict):
		"""
		This method will confirm that the game, platform and category
		can be found in the config data, then creates an internal key
		for use within the lookup.

		Returns a SpeedRun object or None.
		"""
		no_game = True
		is_unsupported = False
		supported_platforms = []
		category_list = self.category_map.copy()
		game_int_name = None
		game_name = None
		ordering_mode = None
		slug = None
		for key_name, data in self.game_map.items():
			if game == key_name or game in data.get("aliases", []):
				no_game = False
				game_int_name = key_name
				game_name = data["name"]
				supported_platforms = data.get("platforms", [])
				is_unsupported = data.get("unsupported", False)
				ordering_mode = data.get("ordering", "cf")
				break

		# Do some initial validation checks before continuing.
		if no_game:
			raise InvalidGame(f"Unknown game: '{game}'.")
		if is_unsupported:
			raise UnsupportedGame(f"Game code '{game}' is currently unsupported in the bot due to technical limitations. This will be resolved in the future.")
		if platform not in self.platform_map:
			raise InvalidPlatform(f"Unknown platform: '{platform}'.")
		if platform not in supported_platforms:
			raise UnsupportedGame(f"The platform '{platform}' cannot be used for this game, please try one of the allowed platforms: {', '.join(supported_platforms)}")

		# Produce an internal key and get the slug URL.
		internal_key = f"{game_int_name}_{platform}"
		for slug_url, aliases in self.board_slugs.items():
			if internal_key in aliases:
				slug = slug_url
				break

		# Capture the category data for the game, if any specific ones exist.
		board_cfg = self.utils.resolve_leaderboard_config(slug, internal_key)
		if board_cfg:
			category_list.update(board_cfg.get("categories", {}))

		# Check if the board name is in the category list.
		not_board = True
		category_name = None
		int_category_id = None
		int_name = None
		for board_name, data in category_list.items():
			if board in data["aliases"]:
				not_board = False
				category_name = board_name
				int_category_id = data.get("board_id", None)
				int_name = data["internal_name"]
				break

		# If not found, then raise an error
		if not_board:
			raise InvalidCategory(f"Unknown category/board: '{board}'.")

		# Process additional metadata and then get the Game ID/Category list from SRDC.
		cat_clean_name, int_key = self.utils.process_additional_md(flags["additional_metadata"], self.md_aliases, category_name, internal_key)
		game_id, game_cats = self.api.get_game_code(slug)

		# Check that there is a category matching the one we asked for.
		# This can change depending on what order mode is set.
		category_id = None
		match ordering_mode:
			case "cf":
				for cat_id, cat_name in game_cats.items():
					# Prefer matching on cat_id first. This is more likely to
					# match over names which may change.
					if cat_id == int_category_id:
						category_id = cat_id
						break
					# If cat_id failed (highly unlikely), use cat_name as fallback.
					if cat_name == category_name:
						category_id = cat_id
						break
			case "pf":
				# Use the internal key to get the pieces.
				codes = internal_key.split("_")
				pm = self.plat_cat_map[codes[0]]
				wanted_category = None
				for cat_name, aliases in pm.items():
					if codes[1] not in aliases:
						continue
					if flags["emulator"]:
						if "emu" in cat_name.lower() or cat_name == "emulator":
							wanted_category = cat_name
							break
					else:
						if "emu" not in cat_name.lower():
							wanted_category = cat_name
							break

				# Now do the same category loop we normally do
				# but using the wanted_category because we are in
				# pf mode. We still prefer cat_id matching first before
				# using the name though.
				for cat_id, cat_name in game_cats.items():
					if cat_id == int_category_id:
						category_id = cat_id
						break
					if cat_name == wanted_category:
						category_id = cat_id
						break

		# If no category exists with the given name, raise ValueError and quit.
		if not category_id:
			raise InvalidCategory("The category name obtained from the category key could not be mapped to a valid speedrun.com category for this game.")

		# Capture variables from the category configuration.
		cat_cfg = self.utils.resolve_category_config(board_cfg, int_key, int_name)
		var_filters = None
		if cat_cfg and cat_cfg.get("variables", None):
			var_filters = self.utils.generate_var_filters(board_cfg["variables"], flags)

		# Depending on whether the world_record flag is set, lookup the
		# relevant run, then return it.
		if flags["world_record"]:
			run = self.wr.lookup_world_record_run(game_id, category_id, var_filters)
		elif flags["place_num"] > 0:
			run = self.utils.find_run_at_position(game_id, category_id, flags["place_num"], var_filters)
		else:
			run = self.lookup_run(game_id, category_id, var_filters, player)

		return run, cat_clean_name, game_name

	def lookup_run(self, game_id: str, category_id: str, var_filters: list, player: str) -> SpeedRun | None:
		"""
		Look up the fastest verified run for a player in a specific game/category.
		Uses SRDC variable filters and client-side filtering to ensure only the run the
		user requested is returned (this is due to the way SRDC returns runs from the API)

		Please be aware that the returned run object from this method may not necessarily
		be a PB run. In most cases, it will be, but keep that in mind.
		"""
		# Resolve user ID, then search for runs.
		# If nothing there, just return None.
		user_id = self.api.get_srdc_user(player)
		runs = self.api.search_runs(game_id, category_id, user_id, var_filters)
		if not runs:
			return None

		# After returning runs, you may receive more than you asked for: this
		# is a limitation of SRDC. Thus, to just have "one run", we need to do
		# some filtering here.
		if var_filters is not None:
			runs = self.utils.filter_all_runs(runs, var_filters)
		if not runs:
			return None

		# Sort the runs by the most recently verified run (newest at the top)
		runs.sort(key=lambda rx: rx["submitted"], reverse=True)
		best_run = runs[0]

		# Find the placement of the run in the leaderboard.
		# In some very rare instances, such as when two runs are submitted
		# at the same time, place lookup may return None. If that occurs,
		# then perform a second lookup using the next run in the list.
		place = self.utils.lookup_run_place(game_id, category_id, best_run["id"], var_filters if var_filters is not None else None)
		if place is None:
			best_run = runs[1]
			if best_run is not None:
				place = self.utils.lookup_run_place(game_id, category_id, best_run["id"], var_filters if var_filters is not None else None)

		# Extract all run details and the leaderboard placement, then return the run object.
		sr = self.utils.extract_run(best_run, player)
		sr.place = place
		return sr
