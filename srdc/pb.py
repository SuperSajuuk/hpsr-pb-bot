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
import datetime


# PersonalBest
# This handles the logic of querying the SRDC
# API for a Personal Best from a single user.
# This is used by !pb only.
class PersonalBest:
	def __init__(self, api, game_map, category_map, board_aliases, board_slugs, utils):
		self.api = api
		self.nm_game_map, self.ce_game_map, self.mr_game_map = game_map
		self.nm_category_map, self.ce_category_map, self.mr_category_map = category_map
		self.ce_board_aliases, self.mr_board_aliases = board_aliases
		self.nm_board_slugs = board_slugs
		self.utils = utils

	# Return just the config dicts that match the mode of the PB
	# This prevents us pointlessly checking "all" the categories
	# and assumes the data we have returned is the one we need.
	def get_config_dicts(self, game_mode: str):
		ba = {}
		slugs = {}
		match game_mode:
			case "ce":
				gm = self.ce_game_map
				cm = self.ce_category_map
				ba = self.ce_board_aliases
			case "mr":
				gm = self.mr_game_map
				cm = self.mr_category_map
				ba = self.mr_board_aliases
			case _:
				gm = self.nm_game_map
				cm = self.nm_category_map
				slugs = self.nm_board_slugs

		return gm, cm, ba, slugs

	# ---------------------------------------------------------
	# PB FETCH
	# ---------------------------------------------------------
	def search_pbs(self, player: str, game_id: str):
		"""Fetch PBs for a player/game combination."""
		return self.api.get(f"users/{player}/personal-bests?game={game_id}&embed=variables")

	# ---------------------------------------------------------
	# PB FILTERING
	# ---------------------------------------------------------
	def find_pbs(self, player: str, pbs: list, category_id: str, var_filters=None):
		"""
		Takes a list of PB run objects returned by speedrun.com and
		only returns the PBs that meet conditions.

		If there are matches, the results list will contain SpeedRun objects.
		If no PB matches, the list will be empty.
		"""
		results = []
		for entry in pbs:
			# Check for a category match: if none, continue.
			run = entry["run"]
			if run["category"] != category_id:
				continue

			# If any variable filters are provided, use them to check for
			# additional filtering.
			all_match = True
			if var_filters is not None:
				for x in var_filters:
					for key, val in x.items():
						if run["values"].get(key) != val:
							all_match = False
							break
					if not all_match:
						break

			# Append the PB result to the list if all variables matched.
			if all_match:
				results.append(self.utils.extract_run(run, player, entry["place"]))

		return results

	# ---------------------------------------------------------
	# PB LOOKUP
	# ---------------------------------------------------------
	def lookup_pb(self, pb_mode: str, game_key: str, internal_key: str, cat_key: str, player: str, flags: dict | None) -> SpeedRun | None:
		"""
		Look up the most recent Personal Best for a player in a specific game/category.
		Any var filters stored for the specific game in the leaderboard config are used
		to perform client-side filtering, ensuring only the requested PB is returned.
		"""
		# Pull in all category data based on the PB Mode.
		game_map, category_map, board_aliases, board_slugs = self.get_config_dicts(pb_mode)

		# Get the slug URL
		slug = None
		for slug_url, aliases in board_slugs.items():
			if internal_key in aliases:
				slug = slug_url
				break

		# Throw an error here if slug is still None
		if slug is None:
			raise ValueError("An error has occurred with an internal function: the slug URL couldn't be found for this combination of inputs.")

		# Pull game object and category information if needed
		game_id, game_cats = self.utils.get_game_code(slug)
		category_meta = None
		ce_category_meta = None
		for board_name, data in category_map.items():
			if cat_key in data["aliases"]:
				category_meta = board_name
				break
		if board_aliases is not None:
			ce_cat_key = internal_key.split("_")[0]
			for key, val in board_aliases.items():
				if ce_cat_key in val:
					ce_category_meta = key
					break

		# Find the actual category object inside the game
		# This may be a normal run board or a CE board, so
		# check for either one.
		category_id = None
		for cat_id, cat_name in game_cats.items():
			if cat_name == category_meta or (ce_category_meta is not None and cat_name == ce_category_meta):
				category_id = cat_id
				break

		# Raise ValueError if the category object does not exist for this game.
		if not category_id:
			raise ValueError("Category not found in game")

		# Fetch PBs for this player based on this game ID.
		pbs = self.search_pbs(player, game_id)

		# Pull in all relevant config data, build var filters
		# then filter all PBs to find the requested one.
		cfg = self.utils.resolve_leaderboard_config(game_key, internal_key)
		variables = None if cfg is None else cfg.get(cat_key, None)
		var_filters = self.utils.generate_var_filters(variables, flags)
		result = self.find_pbs(player, pbs, category_id, var_filters)
		if not result:
			return None

		# Return this PB run.
		return result[0]
