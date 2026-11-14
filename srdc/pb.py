#
# Personal Bests
#
# This code processes a Personal Best object. A Personal Best is
# a speedrun assigned to a specific user which is their "best" submission.
#
# In many respects, this is the same as looking up a normal run through
# the /run/ route. However, as there can be many hundreds of PBs returned
# by the endpoint on SRDC, this is often slower because it has to be
# heavily filtered. In normal cases, it is better to look up runs directly
# using the /run/ route.
from utils.model import SpeedRun
from utils.exceptions import InvalidCategory, MissingInternalData
import datetime


# PersonalBest
# This handles the logic of querying the SRDC
# API for a Personal Best from a single user.
# This is used by !pb only.
class PersonalBest:
	def __init__(self, api, category_map, platform_map, md_aliases, utils):
		self.api = api
		self.category_map = category_map
		self.platform_map = platform_map
		self.md_aliases = md_aliases
		self.utils = utils

	@staticmethod
	def process_game_arg(game_list: dict, game: str, platform: str = None):
		"""
		Using the provided game_list dictionary and the game string,
		check if this game can be found in the list.

		Returns the game name and its Slug URL or None if nothing was
		found.
		"""
		game_name = None
		slug = None
		ordering_mode = None
		int_key = f"{game}_{platform}"
		for key_name, data in game_list.items():
			# Check for a match via standard methods, or in the shortcuts' dictionary.
			matched = (game == key_name or game in data.get("aliases", []))
			shortcuts = None
			if not matched:
				shortcuts = data.get("shortcuts", {}).get(game)
			if matched or shortcuts:
				game_name = data["name"]
				slug = data.get("slugs", data.get("id"))
				ordering_mode = data.get("ordering", "cf")

		# Process the slug variable if it is a dictionary
		if isinstance(slug, dict):
			for slug_url, aliases in slug.items():
				if int_key in aliases:
					slug = slug_url
					break

		return game_name, slug, int_key, ordering_mode

	@staticmethod
	def filter_pbs_by_vars(pbs: list, var_filters: list = None):
		"""
		Takes a list of PBs returned by the search_pbs method and
		filters it, so only the specific PB the user asked for
		is included.

		Returns a new list of filtered runs.
		"""
		filtered_pbs = []
		for pb in pbs:
			r = pb["run"]
			all_match = True
			if var_filters is not None:
				for x in var_filters:
					for key, val in x.items():
						if r["values"].get(key) != val:
							all_match = False
							break
					if not all_match:
						break
			if all_match:
				filtered_pbs.append(pb)
		return filtered_pbs

	@staticmethod
	def filter_pbs_by_category(pbs, category_id):
		return [pb for pb in pbs if pb["run"]["category"] == category_id]

	def generate_args(self, slug: str, game_cats: dict, ordering_mode: str | None, platform: str, int_key: str, board: str, flags: dict, sub_cat_board: str = None):
		"""
		Using some values provided by the user, generate the var_filters
		and category ID that are needed to filter the PB list in the route
		handler.
		"""
		# Obtain the relevant leaderboard config block
		board_cfg = self.utils.resolve_leaderboard_config(slug, int_key)
		category_list = self.category_map.copy()
		all_metadata = self.md_aliases.copy()
		if board_cfg:
			category_list.update(board_cfg.get("categories", {}))
			all_metadata.update(board_cfg.get("metadata", {}))

		# Identify the specific category from the list based on aliases.
		# The values set here are used to obtain the category ID. Unlike
		# /run/, the /pb/ endpoint uses category names only for display
		# reasons, as the filter must be on an ID.
		top_board_name = None
		int_name = None
		int_category_id = None
		var_filters = None
		for board_name, data in category_list.items():
			if board in data["aliases"]:
				top_board_name = board_name
				int_name = data["internal_name"]
				int_category_id = data.get("board_id")
				break

		# In some cases, we might have sub categories. This small section will
		# handle those instances.
		category_name = top_board_name
		if board_cfg.get("sub_categories") is not None:
			for name, data in board_cfg["sub_categories"].items():
				if sub_cat_board in data["aliases"]:
					category_name = name
					break

		# Process additional metadata to obtain the relevant variables, if required.
		# We'll also obtain the true Category ID at this point, needed for filtering.
		cat_clean_name, int_key, rmd, wanted_cat = self.utils.process_additional_md(flags["additional_metadata"], all_metadata, category_name, int_key)
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
					if cat_name == top_board_name:
						category_id = cat_id
						break
			case "pf":
				# Take the list of platform categories defined,
				# then see if it can be found in the aliases.
				if wanted_cat is None:
					# category wasn't found in the metadata, so derive
					# from the platform_categories key. Note that this
					# checks for any matching categories and then determines
					# the right one later.
					pcs = board_cfg.get("platform_categories", {})
					matching_categories = [name for name, aliases in pcs.items() if platform in aliases]
					if len(matching_categories) == 1:
						wanted_cat = matching_categories[0]
					elif len(matching_categories) > 1:
						# More than one category name is defined.
						# Check if one is emulator or not and pick it if matched.
						for cat_name in matching_categories:
							cat_name_lower = cat_name.lower()
							is_emu_cat = (cat_name_lower == "emu" or cat_name_lower.endswith(" emu"))
							if flags["emulator"] and is_emu_cat:
								wanted_cat = cat_name
								break
							if not flags["emulator"] and not is_emu_cat:
								wanted_cat = cat_name
								break

				# Now do the same category loop we normally do
				# but using the wanted_category because we are in
				# pf mode. We still prefer cat_id matching first before
				# using the name though.
				for cat_id, cat_name in game_cats.items():
					if cat_id == int_category_id:
						category_id = cat_id
						break
					if cat_name == wanted_cat:
						category_id = cat_id
						break

		# Generate var filters here, for later filtering purposes.
		cat_cfg = self.utils.resolve_category_config(board_cfg, int_key, int_name)
		if cat_cfg and cat_cfg.get("variables"):
			var_cfg = board_cfg.get(board)
			if var_cfg is None:
				var_cfg = board_cfg.get(int_key)
			var_filters = self.utils.generate_var_filters(var_cfg.get("variables", {}), flags, platform, board_cfg.get("platform_mapping"), rmd, wanted_cat)

		# Return the three things we need
		return var_filters, category_id, top_board_name, cat_clean_name
