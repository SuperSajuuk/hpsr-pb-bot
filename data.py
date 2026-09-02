# Data Class
#
# This combines various pieces of app.py into a more reusable class
# A class is far simpler to understand and avoids repetition of the code
# while placing it in a defined structure.
from model import SpeedRun
import datetime
import config
from typing import Dict
import srcomapi
import srcomapi.datatypes as dt


# SRDCRuns
# This handles the logic of querying the SRDC
# API and then returning results.
#
# Currently just supports PBs, but will add
# support for just finding a run. One negative
# to only searching PBs is the amount of filtering
# needed, whereas just finding the latest run on a board
# is quicker and more efficient.
class SRDCRuns:
	def __init__(self, game_map: dict, platform_map: dict, category_map: dict):
		# Instantiate the Speedrun.com API
		# We'll cache all game codes in-memory to avoid
		# hammering SRDC with requests.
		self.api = srcomapi.SpeedrunCom()
		self.api.debug = 1
		self.game_map = game_map
		self.platform_map = platform_map
		self.category_map = category_map
		self.game_code_cache = {}

	# ---------------------------------------------------------
	# GAME LOOKUP (Lazy Cached)
	# ---------------------------------------------------------
	def get_game_code(self, game_key: str):
		"""
		Return the srcomapi Game object for a given game code.
		Returns a game object that is then cached. If the game
		is already cached, return that automatically and do not
		query SRDC.
		"""
		if game_key in self.game_code_cache:
			return self.game_code_cache[slug]

		# Query SRDC. If nothing found, return a ValueError
		result = self.api.search(dt.Game, {"id": slug})
		if not result:
			raise ValueError(f"Game not found on SRDC: {game_id}")

		# Cache the result and return it.
		game_obj = result[0]
		self.game_code_cache[game_key] = game_obj
		return game_obj

	# ---------------------------------------------------------
	# USER ID LOOKUP
	# ---------------------------------------------------------
	def get_user_id(self, username: str) -> str:
		"""Resolve a Speedrun.com username to a user ID."""
		result = self.api.search(dt.User, {"name": username})
		if not result:
			raise ValueError(f"User not found on SRDC: {username}")
		return result[0].id

	# ---------------------------------------------------------
	# LEADERBOARD LOOKUP
	# ---------------------------------------------------------
	def get_leaderboard(self, game_id: str, category_id: str, max_runs: int | None = None, variables: dict | None = None):
		"""
		Fetch leaderboard for a game/category.
		If max_runs is provided, only that many runs are returned.
		"""
		url = f"leaderboards/{game_id}/category/{category_id}?embed=players"
		if max_runs is not None:
			url += f"&max={max_runs}"
		if variables:
			for var_id, var_value in variables.items():
				url += f"&var-{var_id}={var_value}"

		return self.api.get(url)

	# ---------------------------------------------------------
	# LEADERBOARD RUN PLACEMENT
	# ---------------------------------------------------------
	def _lookup_run_place(self, game_id, category_id, run_id, variables: dict | None):
		"""
		Looks up the leaderboard for a game and returns the
		place number representing the provided run.
		"""
		# Try partial leaderboard first
		lb_partial = self.get_leaderboard(game_id, category_id, max_runs=100, variables=variables)
		place = self.find_run_placement(lb_partial, run_id)

		# If place is None here, the run wasn't in the top 100.
		# Return all runs and then find it.
		if place is None:
			lb_full = self.get_leaderboard(game_id, category_id, max_runs=None, variables=variables)
			place = self.find_run_placement(lb_full, run_id)

		return place

	# ---------------------------------------------------------
	# FIND RUN PLACEMENT
	# ---------------------------------------------------------
	@staticmethod
	def find_run_placement(leaderboard, run_id: str) -> int | None:
		"""Return the leaderboard placement for a given run ID."""
		for entry in leaderboard["runs"]:
			if entry["run"]["id"] == run_id:
				return entry["place"]
		return None

	# ---------------------------------------------------------
	# RUN FETCH
	# ---------------------------------------------------------
	def search_runs(self, game_id: str, category_id: str, user_id: str):
		"""
		Search SRDC for runs matching game/category/user.
		"""
		return self.api.get(f"runs?game={game_id}&category={category_id}&user={user_id}&status=verified&embed=variables,players")

	# ---------------------------------------------------------
	# RUN EXTRACTION
	# ---------------------------------------------------------
	@staticmethod
	def extract_run(run_obj, player_name) -> SpeedRun:
		"""
		Convert a srcomapi Run object into a SpeedRun dataclass.
		"""
		seconds = run_obj["times"]["primary_t"]
		time = str(datetime.timedelta(seconds=seconds))
		return SpeedRun(
			player=player_name,
			game=str(run_obj["game"]),
			category=str(run_obj["category"]),
			time=time,
			raw=None,
			emulator=run_obj["system"]["emulated"],
			place=None,  # run search does not include leaderboard place
			link=run_obj["weblink"],
			id=None
		)

	# ---------------------------------------------------------
	# LOOKUP CATEGORY EXTENSION RUN
	# ---------------------------------------------------------
	def lookup_ce_run(self, base_game, platform, ce_type, ce_category, player):
		"""
		Resolve and fetch a Category Extensions run.
		Currently, this only supports the HPCE board, but this will be expanded
		in the future to include other CE boards, if they exist.
		"""

		# The CE type needs to be mapped first: do that or return ValueError
		# if no match exists.
		match ce_type:
			case "standard":
				game_map = CE_GAME_MAP
			case "insane":
				game_map = CE_GAME_MAP_INSANE
			case "multiruns":
				game_map = CE_GAME_MAP_MULTIRUNS
			case "single_year":
				game_map = CE_GAME_MAP_SINGLE_YEAR
			case _:
				raise ValueError(f"Unknown CE type: {ce_type}")

		# The lookup key needs to be built: designed for the game_map search.
		lookup_key = None
		match ce_type:
			case "standard" | "insane":
				lookup_key = f"{base_game}_{platform}"
			case "multiruns":
				lookup_key = f"multiruns_{platform}"
			case "single_year":
				lookup_key = base_game

		# Raise ValueError if:
		# - lookup_key is not in the game map.
		# - ce_type is not in the category extension mapping.
		# - ce_category is not found in the ce_cat_map.
		ce_board = game_map[lookup_key]
		ce_cat_map = CATEGORY_EXT_MAP[ce_type]
		if lookup_key not in game_map:
			raise ValueError(f"CE board not found for key: {lookup_key}")
		if ce_type not in CATEGORY_EXT_MAP:
			raise ValueError(f"Unknown CE type in category map: {ce_type}")
		if ce_category not in ce_cat_map:
			raise ValueError(f"Unknown CE category: {ce_category}")

		# Build the h= parameter
		cat_info = ce_cat_map[ce_category]
		h_param = None
		match ce_type:
			case "standard":
				h_param = f"{ce_board}-{cat_info['h_suffix']}"
			case "insane":
				# dynamic suffix: "{game}-{platform}"
				h_param = f"Insane-{base_game}-{platform}"
			case "multiruns":
				h_param = f"Multiruns-{cat_info['h_suffix']}"
			case "single_year":
				h_param = f"Single_Year-{base_game}-{cat_info['h_suffix']}"

		# Build the x= parameter (variables)
		var_ids = {}
		match ce_type:
			# Standard CE boards: one variable
			case "standard":
				var_ids.update(cat_info["var_ids"])
			# Insane%: one variable, dynamic value_id
			case "insane":
				var_id = next(iter(cat_info["var_ids"].keys()))
				value_id = self.ce_insane_value_id(base_game, platform)
				var_ids[var_id] = value_id
			# Multiruns: one variable
			case "multiruns":
				var_ids.update(cat_info["var_ids"])
			# Single Year: two variables (game selector + category selector)
			case "single_year":
				# var1: game selector
				var1 = "xd1vl0rd-2lgr1v7n"
				value1 = self.ce_single_year_game_value(base_game)

				# var2: category selector (any or 100)
				var2 = "wl30dmyl"
				value2 = cat_info["var_ids"][var2]

				var_ids[var1] = value1
				var_ids[var2] = value2

		# Now fetch a leaderboard entry and only return the entry that matches.
		lb = self.get_leaderboard(game_id="hpce", category_id=h_param, variables=var_ids)
		for r in lb:
			if r.player.lower() == player.lower():
				return r
		return None

	# ---------------------------------------------------------
	# LOOKUP MULTI-RUN
	# ---------------------------------------------------------
	def lookup_multirun(self, cat_key: str, player: str) -> Speedrun | None:
		"""
		Look up the fastest verified run for a player in a multi-run category.
		This replaces previously written logic where individual runs were stitched together.
		While that worked, it made no sense because there's a multi-run board that contains
		the time needed.
		"""
		# Resolve game object (hpmulti)
		slug = config.MULTIRUN_SLUG
		category_meta = self.category_map[cat_key]
		game_obj = self.get_game_code(slug)

		# Find category object
		category_obj = None
		for cat in game_obj.categories:
			if str(cat) == category_meta["name"]:
				category_obj = cat
				break

		if not category_obj:
			raise ValueError("Category not found in multi-run board")

		# Resolve user ID
		user_id = self.get_user_id(player)

		# Search runs
		runs = self.search_runs(game_obj.id, category_obj.id, user_id)
		if not runs:
			return None

		# Sort by verification date
		runs.sort(key=lambda r: r["status"]["verify-date"], reverse=True)
		best_run = runs[0]

		# Build variable set
		variables = {}
		var_id = list(category_meta["variables"].keys())[0]
		var_value = category_meta["variables"][var_id][category_meta["default"]]
		variables[var_id] = var_value

		# Placement
		place = self._lookup_run_place(game_obj.id, category_obj.id, best_run["id"], variables)

		sr = self.extract_run(best_run, player)
		sr.place = place
		return sr

	# ---------------------------------------------------------
	# LOOKUP RUN
	# ---------------------------------------------------------
	def lookup_run(self, internal_key: str, cat_key: str, player: str) -> Speedrun | dict[str, SpeedRun] | None:
		"""
		Look up the fastest verified run for a player in a specific game/category.
		While looking through PBs works well enough, it's a lot more efficient to
		just look for the most recent verified run, which is almost always PB.

		It also supports multi-runs automatically, if variables are provided for it.
		"""
		# Resolve game object
		slug = config.BOARD_GAME_SLUG[internal_key]
		game_obj = self.get_game_code(SLUG)
		category_meta = self.category_map[cat_key]

		# Find category object
		category_obj = None
		for cat in game_obj.categories:
			if str(cat) == category_meta["name"]:
				category_obj = cat
				break

		# If there is no category object, raise an error because it doesn't exist.
		if not category_obj:
			raise ValueError("Category not found in game")

		# Resolve user ID and then search the runs to find something.
		user_id = self.get_user_id(player)
		runs = self.search_runs(game_obj.id, category_obj.id, user_id)
		if not runs:
			return None

		# Sort the runs by the most recently verified run (newest at the top)
		# The run at the top of the index will then be used to get its placement
		# in the leaderboard. To avoid duplication, leaderboard placement is
		# parsed by a helper function.
		cfg = config.LEADERBOARD_CONFIG.get(internal_key, None)
		runs.sort(key=lambda r: r["status"]["verify-date"], reverse=True)
		best_run = runs[0]

		# Build variable set
		variables = {}
		if cfg is not None:
			# Always include category variable if present
			cat_cfg = cfg["categories"][cat_key]
			cat_var_id = cat_cfg["var_id"]
			if cat_var_id in best_run["values"]:
				variables[cat_var_id] = best_run["values"][cat_var_id]

			# Always include platform variable if present — even if user didn't specify platform
			plat_cfg = cfg["platform"]
			plat_var_id = plat_cfg["var_id"]
			if plat_var_id in best_run["values"]:
				variables[plat_var_id] = best_run["values"][plat_var_id]
		else:
			# Only include the category variable as a fallback.
			var_id = list(category_meta["variables"].keys())[0]
			if var_id in best_run["values"]:
				variables[var_id] = best_run["values"][var_id]

		# Extract the run, store the place and return it.
		place = self._lookup_run_place(game_obj.id, category_obj.id, best_run["id"], variables)
		sr = self.extract_run(best_run, player)
		sr.place = place
		return sr

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
		place = entry["place"]
		seconds = run["times"]["primary_t"]
		time = str(datetime.timedelta(seconds=seconds))
		link = run["weblink"]
		return SpeedRun(
			player=player_name,
			game=str(run["game"]),
			category=str(run["category"]),
			time=time,
			raw=run,
			emulator=run["system"]["emulated"],
			place=place,
			link=link,
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
