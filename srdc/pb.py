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
	def __init__(self, srdc_api, game_map: dict, platform_map: dict, category_map: dict):
		self.api = srdc_api
		self.game_map = game_map
		self.platform_map = platform_map
		self.category_map = category_map
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
	def find_pbs(self, player: str, pbs: list, category_id: str, variable_filter=None):
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
				var_id, expected = variable_filter
				if run["values"].get(var_id) != expected:
					continue

			# Append the PB result to the list.
			results.append(self.extract_pb(entry, player))

		return results

	# ---------------------------------------------------------
	# HIGH-LEVEL PB LOOKUP
	# ---------------------------------------------------------
	def lookup_pb(self, game_key: str, cat_key: str, player: str, platform: str = None) -> list[SpeedRun] | dict[str, SpeedRun] | None:
		"""
		High-level PB lookup:
		- Resolve game
		- Resolve category
		- Fetch PBs
		- Filter PBs
		- Return SpeedRun objects
		Supports multiruns (Any% + 100%) automatically.
		"""
		game_obj = self.get_game_code(game_key)
		category_meta = self.category_map[cat_key]

		# Find the actual category object inside the game
		category_obj = None
		for cat in game_obj.categories:
			if str(cat) == category_meta["name"]:
				category_obj = cat
				break

		# Raise ValueError if the category object does not exist for this game.
		if not category_obj:
			raise ValueError("Category not found in game")

		# Fetch PBs for this player based on this game ID.
		# Also, load unified leaderboard config for this game (if present)
		pbs = self.search_pbs(player, game_obj.id)
		cfg = config.LEADERBOARD_CONFIG.get(game_key, None)

		# Optional platform filtering (console/emulator)
		if platform is not None and cfg is not None:
			plat_cfg = cfg["platform"]
			plat_var_id = plat_cfg["var_id"]
			plat_value = plat_cfg["values"][platform]
			pbs = [pb for pb in pbs if pb["run"]["values"].get(plat_var_id) == plat_value]
			if not pbs:
				return None

		# Some categories might include multi-run metadata.
		# If that is the case, search for a PB in those.
		if "variables" in category_meta:
			var_id = list(category_meta["variables"].keys())[0]
			var_values = category_meta["variables"][var_id]
			results = {}

			# Any%
			any_pbs = self.find_pbs(player, pbs, category_obj.id, (var_id, var_values["any"]))
			if any_pbs:
				# Build variable set for leaderboard lookup
				best_any = any_pbs[0]
				variables_any = {}
				if cfg is not None:
					cat_cfg = cfg["categories"][cat_key]
					cat_var_id = cat_cfg["var_id"]
					if cat_var_id in best_any.raw["values"]:
						variables_any[cat_var_id] = best_any.raw["values"][cat_var_id]

					# Always include platform variable if present
					plat_cfg = cfg["platform"]
					plat_var_id = plat_cfg["var_id"]
					if plat_var_id in best_any.raw["values"]:
						variables_any[plat_var_id] = best_any.raw["values"][plat_var_id]
				else:
					# Fallback: use only the category variable
					if var_id in best_any.raw["values"]:
						variables_any[var_id] = best_any.raw["values"][var_id]

				place_any = self._lookup_run_place(game_obj.id, category_obj.id, best_any.id, variables_any)
				best_any.place = place_any
				results["any"] = best_any

			# 100%
			hundo_pbs = self.find_pbs(player, pbs, category_obj.id, (var_id, var_values["100"]))
			if hundo_pbs:
				# Build variable set for leaderboard lookup
				best_hundo = hundo_pbs[0]
				variables_hundo = {}
				if cfg is not None:
					cat_cfg = cfg["categories"][cat_key]
					cat_var_id = cat_cfg["var_id"]
					if cat_var_id in best_hundo.raw["values"]:
						variables_hundo[cat_var_id] = best_hundo.raw["values"][cat_var_id]

					# Always include platform variable if present
					plat_cfg = cfg["platform"]
					plat_var_id = plat_cfg["var_id"]
					if plat_var_id in best_hundo.raw["values"]:
						variables_hundo[plat_var_id] = best_hundo.raw["values"][plat_var_id]
				else:
					# Fallback: use only the category variable
					if var_id in best_hundo.raw["values"]:
						variables_hundo[var_id] = best_hundo.raw["values"][var_id]

				place_hundo = self._lookup_run_place(game_obj.id, category_obj.id, best_hundo.id, variables_hundo)
				best_hundo.place = place_hundo
				results["100"] = best_hundo

			# Return all SpeedRun objects that have been found.
			return results

		# Optional variable filtering (for CE categories)
		# Written using an in-line expression for tidiness.
		# If no PB found, return None.
		variable_filter = ("2lg3d4on", category_meta["cecode"]) if "cecode" in category_meta else None
		result = self.find_pbs(player, pbs, category_obj.id, variable_filter)
		if not result:
			return None

		# Build variable set for leaderboard lookup for single PB
		best_pb = result[0]
		variables = {}
		if cfg is not None:
			cat_cfg = cfg["categories"][cat_key]
			cat_var_id = cat_cfg["var_id"]
			if cat_var_id in best_pb.raw["values"]:
				variables[cat_var_id] = best_pb.raw["values"][cat_var_id]

			# Always include platform variable if present
			plat_cfg = cfg["platform"]
			plat_var_id = plat_cfg["var_id"]
			if plat_var_id in best_pb.raw["values"]:
				variables[plat_var_id] = best_pb.raw["values"][plat_var_id]
		else:
			# Fallback: only include category variable
			if variable_filter:
				var_id, var_val = variable_filter
				if var_id in best_pb.raw["values"]:
					variables[var_id] = best_pb.raw["values"][var_id]

		# Find the place number and return this PB run.
		place = self._lookup_run_place(game_obj.id, category_obj.id, best_pb.id, variables)
		best_pb.place = place
		return result
