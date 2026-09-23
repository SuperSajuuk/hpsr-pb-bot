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
from utils.exceptions import InvalidGame, InvalidCategory, InvalidPlatform, UnsupportedGame
from configs.generic import COMMAND_USAGE_DOC


# NormalRun
# This handles the logic of querying the SRDC
# API for a normal run submission. This is
# used by !run only.
class NormalRun:
	def __init__(self, api, game_map, platform_map, plat_category_map, category_map, board_slugs, md_aliases, utils):
		self.api = api
		self.game_map = game_map
		self.platform_map = platform_map
		self.plat_cat_map = plat_category_map
		self.category_map = category_map
		self.board_slugs = board_slugs
		self.md_aliases = md_aliases
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
		game_int_name = None
		game_name = None
		ordering_mode = None
		for key_name, data in self.game_map.items():
			if game == key_name or game in data.get("aliases", []):
				no_game = False
				game_int_name = key_name
				game_name = data["name"]
				is_unsupported = data.get("unsupported", False)
				ordering_mode = data.get("ordering", "cf")
				break

		if no_game:
			raise InvalidGame(f"Unknown game: '{game}'.")
		if is_unsupported:
			raise UnsupportedGame(f"Game code '{game}' is currently unsupported in the bot due to technical limitations. This will be resolved in the future.")
		if platform not in self.platform_map:
			raise InvalidPlatform(f"Unknown platform: '{platform}'.")

		# Check if the board name is in the category list.
		not_board = True
		category_name = None
		int_name = None
		for board_name, data in self.category_map.items():
			if board in data["aliases"]:
				not_board = False
				category_name = board_name
				int_name = data["internal_name"]
				break

		# If not found, then raise an error
		if not_board:
			raise InvalidCategory(f"Unknown category/board: '{board}'.")

		# If there are additional metadata flags, then append it to
		# category name for output. There would usually only be
		# a single key here, hence the hard coding for just key_1.
		internal_key = f"{game_int_name}_{platform}"
		if flags.get("additional_metadata", {}):
			key_val = flags['additional_metadata'].get('key_1')
			if key_val is not None:
				found_alias = False
				for human_name, data in self.md_aliases.items():
					if key_val in data["aliases"]:
						found_alias = True
						category_name += f" {human_name}"
						internal_key += f"_{data['int_key']}"
						break
				if not found_alias:
					category_name += f" {flags['additional_metadata'].get('key_1').capitalize()}"

		# Look up the run, and return the result.
		run = self.lookup_run(internal_key, board, ordering_mode, int_name, player, flags)
		return run, category_name, game_name

	def lookup_run(self, internal_key: str, cat_key: str, order_mode: str, int_name: str, player: str, flags: dict | None) -> SpeedRun | None:
		"""
		Look up the fastest verified run for a player in a specific game/category.
		Uses SRDC variable filters and client-side filtering to ensure only the run the
		user requested is returned (this is due to the way SRDC returns runs from the API)

		Please be aware that the returned run object from this method may not necessarily
		be a PB run. In most cases, it will be, but keep that in mind.
		"""
		# Parse the internal_key and cat_key to obtain the game and category.
		slug = None
		for slug_url, aliases in self.board_slugs.items():
			if internal_key in aliases:
				slug = slug_url
				break

		# Get the Game ID and its top category list. Then,
		# obtain the relevant category name from the category map.
		game_id, game_cats = self.utils.get_game_code(slug)
		category_meta = None
		for category_name, data in self.category_map.items():
			if cat_key in data["aliases"]:
				category_meta = category_name
				break

		# Didn't find anything, so returning.
		if not category_meta:
			raise InvalidCategory("The category key provided could not be found in the alias list. Please check your input, and try again.")

		# Check that there is a category matching the one we asked for.
		category_id = None
		match order_mode:
			case "cf":
				for cat_id, cat_name in game_cats.items():
					if cat_name == category_meta:
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
					if flags.get("emulator", False):
						if "emu" in cat_name.lower() or cat_name == "emulator":
							wanted_category = cat_name
							break
					else:
						if "emu" not in cat_name.lower():
							wanted_category = cat_name
							break

				# Now do the same category loop we normally do
				# but using the wanted_category because we are in
				# pf mode.
				for cat_id, cat_name in game_cats.items():
					if cat_name == wanted_category:
						category_id = cat_id
						break

		# If no category exists with the given name, raise ValueError and quit.
		if not category_id:
			raise InvalidCategory("The category name obtained from the category key could not be mapped to a valid speedrun.com category for this game.")

		# Resolve user ID, then check for variables in case we have one.
		user_id = self.utils.get_user_id(player)
		cfg = self.utils.resolve_leaderboard_config(slug, internal_key, int_name)
		cfg_2 = None
		if cfg is not None:
			cfg_2 = cfg.get(int_name, None)

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
				if x.get("name") == active_slice or active_slice in x.get("aliases", []):
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
			runs = self.utils.filter_all_runs(runs, var_filters)

		# If nothing remains after filtering, return None
		if not runs:
			return None

		# Sort the runs by the most recently verified run (newest at the top)
		runs.sort(key=lambda rx: rx["submitted"], reverse=True)

		# In some cases, the run order above will not be the run we needed. Do
		# some additional filtering, then capture the top run. This only filters
		# if there was no active slice (as its just a repeat of the above behaviour)
		#
		# The run at the top of the index will then be used to get its placement
		# in the leaderboard. To avoid duplication, leaderboard placement is
		# parsed by a helper function.
		best_run = runs[0]
		filtered_runs = []
		if active_slice is None and var_filters is not None:
			# If the filtered runs are empty, there were no runs matching conditions.
			filtered_runs = self.utils.filter_all_runs(runs, var_filters)
			filtered_runs.sort(key=lambda rx: rx["submitted"], reverse=True)
			if len(filtered_runs) == 0:
				return None

			best_run = filtered_runs[0]

		# Find the placement of the run in the leaderboard.
		# For some bizarre reason, this might return None in really rare circumstances.
		# If that happens, do it again but with the next item on the list (perhaps the
		# returned object was for an obsolete run?)
		place = self.utils.lookup_run_place(game_id, category_id, best_run["id"], var_filters if var_filters is not None else None)
		if place is None:
			best_run = filtered_runs[1] if len(filtered_runs) > 1 else runs[1]
			if best_run is not None:
				place = self.utils.lookup_run_place(game_id, category_id, best_run["id"], var_filters if var_filters is not None else None)

		# Extract all run details and the leaderboard placement, then return the run object.
		sr = self.utils.extract_run(best_run, player)
		sr.place = place
		return sr
