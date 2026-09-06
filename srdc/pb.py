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
from model import SpeedRun
import datetime
import config
from typing import Dict
import srcomapi.datatypes as dt


# PersonalBest
# This handles the logic of querying the SRDC
# API for a Personal Best from a single user.
# This is used by !pb only.
class PersonalBest:
	def __init__(self, srdc_api, game_map, platform_map, category_map, ce_board_aliases, ce_category_map, utils):
		self.api = srdc_api
		self.game_map = game_map
		self.platform_map = platform_map
		self.category_map = category_map
		self.ce_board_aliases = ce_board_aliases
		self.ce_category_map = ce_category_map
		self.utils = utils
		self.game_code_cache = {}

	# ---------------------------------------------------------
	# PB FETCH
	# ---------------------------------------------------------
	def search_pbs(self, player: str, game_id: str):
		"""Fetch PBs for a player/game combination."""
		return self.api.get(f"users/{player}/personal-bests?game={game_id}&embed=variables")

	# ---------------------------------------------------------
	# PB EXTRACTION
	# ---------------------------------------------------------
	@staticmethod
	def extract_pb(entry, player_name) -> SpeedRun:
		"""Convert a PB entry into a structured dataclass."""
		run = entry["run"]
		seconds = run["times"]["primary_t"]
		time = str(datetime.timedelta(seconds=seconds))
		return SpeedRun(
			player=player_name,
			game=str(run["game"]),
			category=str(run["category"]),
			time=time,
			raw=run,
			emulator=run["system"]["emulated"],
			place=entry["place"],
			link=run["weblink"],
			id=run["id"]
		)

	# ---------------------------------------------------------
	# PB FILTERING
	# ---------------------------------------------------------
	def find_pbs(self, player: str, pbs: list, category_id: str, variable_filter=None, flags: dict=None):
		"""
		Find PBs matching a category and optional variable filter.
		variable_filter = ("variable_id", "expected_value")
		"""
		results = []
		for entry in pbs:
			# Check for a category match: if none, continue.
			run = entry["run"]
			if str(run["category"]) != category_id:
				continue

			# Optional variable match (CE, multiruns)
			if variable_filter is not None:
				# If the variable_filter data includes a "variables" key, use data from there
				variable_data = variable_filter.get("variables", None)
				if variable_data is not None:
					# The variable_data might include multiple variable dictionaries.
					# To identify the one we need, capture the name value and map it
					# to the flags' dictionary. Flags are derived from the users' input.
					slice_names = {x["name"] for x in variable_data if "name" in x}
					active_slice = None
					if flags is not None:
						for name in slice_names:
							if flags.get(name, False):
								active_slice = name
								break

					# Check for a slice or continue on if there was nothing.
					if active_slice is not None:
						variable_data = [x for x in variable_data if x["name"] == active_slice]

					# Now parse just the variable that we need.
					all_match = True
					for x in variable_data:
						var_id = x.get("var_id").split("-")[1]
						expected = x.get("value_id", None)
						if run["values"].get(var_id) == expected:
							break
						all_match = False

					if not all_match:
						continue
				else:
					# Check if the value ID is the one we wanted.
					var_id, expected = variable_filter
					if run["values"].get(var_id) != expected:
						continue

			# Append the PB result to the list.
			results.append(self.extract_pb(entry, player))

		return results

	# ---------------------------------------------------------
	# PB LOOKUP
	# ---------------------------------------------------------
	def lookup_pb(self, game_key: str, internal_key: str, cat_key: str, player: str, extras: list, flags: dict | None) -> SpeedRun | None:
		"""
		Look up the most recent Personal Best for a player in a specific game/category.
		Uses SRDC variable filters and client-side filtering to ensure only the run the
		user requested is returned.
		"""
		# Obtain the slug URL for the game key.
		# If one doesn't exist, it might be a CE.
		slug = config.BOARD_GAME_SLUG.get(internal_key, None)
		if slug is None:
			for key, val in config.CE_GAME_MAP.items():
				if val["id"] == game_key:
					slug = val["id"]
					break

		# Throw an error here if slug is still None
		if slug is None:
			raise ValueError("An error has occurred with an internal function: the slug URL couldn't be found for this combination of inputs.")

		# Pull game object and category information if needed
		game_obj = self.utils.get_game_code(slug)
		category_meta = self.category_map.get(cat_key, None)
		ce_category_meta = self.ce_board_aliases.get(internal_key.split("_")[0], None)

		# Find the actual category object inside the game
		# This may be a normal run board or a CE board, so
		# check for either one.
		category_obj = None
		for cat in game_obj.categories:
			if cat.name == category_meta or (ce_category_meta is not None and cat.name == ce_category_meta.upper()):
				category_obj = cat
				break

		# Raise ValueError if the category object does not exist for this game.
		if not category_obj:
			raise ValueError("Category not found in game")

		# Fetch PBs for this player based on this game ID.
		# Also, load unified leaderboard config for this game (if present)
		pbs = self.search_pbs(player, game_obj.id)
		variables = self.utils.resolve_leaderboard_config(game_key, internal_key)
		variables_2 = None
		if variables is not None:
			variables_2 = variables.get(cat_key, None)

		# Filter the PB list to try and find the PB the user asked for.
		# If no PB found, return None.
		result = self.find_pbs(player, pbs, category_obj.id, variables if variables_2 is None else variables_2, flags)
		if not result:
			return None

		# Return this PB run.
		return result[0]
