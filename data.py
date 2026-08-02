# Data Class
#
# This combines various pieces of app.py into a more reusable class
# A class is far simpler to understand and avoids repetition of the code
# while placing it in a defined structure.
from dataclasses import dataclass
import datetime
import config
from typing import Dict
import srcomapi
import srcomapi.datatypes as dt


# Create a SpeedRun model.
# We use this to represent a run, whether it's a PB or not.
# Note that a PB has a place, but searching a run may not
# yield that data.
@dataclass
class SpeedRun:
	player: str
	game: str
	category: str
	time: str
	emulator: bool
	place: int | None
	link: str


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
	def __init__(self, game_map: dict, category_map: dict):
		# Instantiate the Speedrun.com API
		# We'll cache all game codes in-memory to avoid
		# hammering SRDC with requests.
		self.api = srcomapi.SpeedrunCom()
		self.api.debug = 1
		self.game_map = game_map
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
			return self.game_code_cache[game_key]

		# Query SRDC. If nothing found, return a ValueError
		game_name = self.game_map[game_key]
		result = self.api.search(dt.Game, {"name": game_name})
		if not result:
			raise ValueError(f"Game not found on SRDC: {game_name}")

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
			emulator=run_obj["system"]["emulated"],
			place=None,  # run search does not include leaderboard place
			link=run_obj["weblink"]
		)

	# ---------------------------------------------------------
	# LOOKUP RUN
	# ---------------------------------------------------------
	def lookup_run(self, game_key: str, cat_key: str, player: str, platform: str = None) -> Speedrun | dict[str, SpeedRun] | None:
		"""
		Look up the fastest verified run for a player in a specific game/category.
		While looking through PBs works well enough, it's a lot more efficient to
		just look for the most recent verified run, which is almost always PB.

		It also supports multi-runs automatically, if variables are provided for it.
		"""
		# Resolve game + category
		game_obj = self.get_game_code(game_key)
		category_meta = self.category_map[cat_key]

		# Find category object
		category_obj = None
		for cat in game_obj.categories:
			if str(cat) == category_meta["name"]:
				category_obj = cat
				break

		# Raise ValueError if no category was found for the game.
		if not category_obj:
			raise ValueError("Category not found in game")

		# Resolve user ID, then search for their runs in the game category.
		# Return "None" if there was nothing found.
		user_id = self.get_user_id(player)
		runs = self.search_runs(game_obj.id, category_obj.id, user_id)
		if not runs:
			return None

		# Load unified leaderboard config for this game (if present)
		cfg = config.LEADERBOARD_CONFIG.get(game_key, None)

		# Optional platform filtering (console/emulator)
		if platform is not None:
			if cfg is not None:
				# Unified config path (preferred)
				plat_cfg = cfg["platform"]
				plat_var_id = plat_cfg["var_id"]
				plat_value = plat_cfg["values"][platform]
				runs = [r for r in runs if r["values"].get(plat_var_id) == plat_value]
				if not runs:
					return None
			else:
				# Fallback path for games without unified config:
				# No platform filtering is possible, so we simply do nothing.
				# This ensures games without config still work normally.
				pass

		# In some games, there might be a multi-run: check for those first.
		if "variables" in category_meta:
			var_id = list(category_meta["variables"].keys())[0]
			var_values = category_meta["variables"][var_id]
			results = {}

			# Any%
			any_runs = [
				r for r in runs
				if r["values"].get(var_id) == var_values["any"] and (platform is None or (
						cfg is not None and
						r["values"].get(cfg["platform"]["var_id"]) == cfg["platform"]["values"][platform]
				))
			]
			if any_runs:
				# Sort the Any% runs by verification date, and find its place in the list
				any_runs.sort(key=lambda r: r["status"]["verify-date"], reverse=True)
				best_any = any_runs[0]

				# Build variable set for leaderboard lookup
				variables_any = {}
				if cfg is not None:
					cat_cfg = cfg["categories"][cat_key]
					cat_var_id = cat_cfg["var_id"]
					if cat_var_id in best_any["values"]:
						variables_any[cat_var_id] = best_any["values"][cat_var_id]
					if platform is not None:
						plat_cfg = cfg["platform"]
						plat_var_id = plat_cfg["var_id"]
						if plat_var_id in best_any["values"]:
							variables_any[plat_var_id] = best_any["values"][plat_var_id]
				else:
					# Fallback: use only the category variable
					if var_id in best_any["values"]:
						variables_any[var_id] = best_any["values"][var_id]

				# Extract the run details and store it in the dictionary.
				place_any = self._lookup_run_place(game_obj.id, category_obj.id, best_any["id"], variables_any)
				sr_any = self.extract_run(best_any, player)
				sr_any.place = place_any
				results["any"] = sr_any

			# 100%
			hundo_runs = [
				r for r in runs
				if r["values"].get(var_id) == var_values["100"] and (platform is None or (
						cfg is not None and
						r["values"].get(cfg["platform"]["var_id"]) == cfg["platform"]["values"][platform]
				))
			]
			if hundo_runs:
				# Sort the 100% runs by verification date, and find its place in the list.
				hundo_runs.sort(key=lambda r: r["status"]["verify-date"], reverse=True)
				best_hundo = hundo_runs[0]

				# Build variable set for leaderboard lookup
				variables_hundo = {}
				if cfg is not None:
					cat_cfg = cfg["categories"][cat_key]
					cat_var_id = cat_cfg["var_id"]
					if cat_var_id in best_hundo["values"]:
						variables_hundo[cat_var_id] = best_hundo["values"][cat_var_id]
					if platform is not None:
						plat_cfg = cfg["platform"]
						plat_var_id = plat_cfg["var_id"]
						if plat_var_id in best_hundo["values"]:
							variables_hundo[plat_var_id] = best_hundo["values"][plat_var_id]
				else:
					# Fallback: use only the category variable
					if var_id in best_hundo["values"]:
						variables_hundo[var_id] = best_hundo["values"][var_id]

				# Extract the run details and store it in the dictionary.
				place_hundo = self._lookup_run_place(game_obj.id, category_obj.id, best_hundo["id"], variables_hundo)
				sr_hundo = self.extract_run(best_hundo, player)
				sr_hundo.place = place_hundo
				results["100"] = sr_hundo

			return results

		# Sort the runs by the most recently verified run (newest at the top)
		# The run at the top of the index will then be used to get its placement
		# in the leaderboard. To avoid duplication, leaderboard placement is
		# parsed by a helper function.
		runs.sort(key=lambda r: r["status"]["verify-date"], reverse=True)
		best_run = runs[0]

		# Build variable set for leaderboard lookup
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
			# Fallback: only include category variable
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
			emulator=run["system"]["emulated"],
			place=place,
			link=link,
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
			pbs = [pb for pb in pbs if pb.values().get(plat_var_id) == plat_value]
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
					if cat_var_id in best_any.values():
						variables_any[cat_var_id] = best_any.values()[cat_var_id]

					# Always include platform variable if present
					plat_cfg = cfg["platform"]
					plat_var_id = plat_cfg["var_id"]
					if plat_var_id in best_any.values:
						variables_any[plat_var_id] = best_any.values()[plat_var_id]
				else:
					# Fallback: use only the category variable
					if var_id in best_any.values():
						variables_any[var_id] = best_any.values()[var_id]

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
					if cat_var_id in best_hundo.values():
						variables_hundo[cat_var_id] = best_hundo.values()[cat_var_id]

					# Always include platform variable if present
					plat_cfg = cfg["platform"]
					plat_var_id = plat_cfg["var_id"]
					if plat_var_id in best_hundo.values():
						variables_hundo[plat_var_id] = best_hundo.values()[plat_var_id]
				else:
					# Fallback: use only the category variable
					if var_id in best_hundo.values():
						variables_hundo[var_id] = best_hundo.values()[var_id]

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
			if cat_var_id in best_pb.values():
				variables[cat_var_id] = best_pb.values()[cat_var_id]

			# Always include platform variable if present
			plat_cfg = cfg["platform"]
			plat_var_id = plat_cfg["var_id"]
			if plat_var_id in best_pb.values():
				variables[plat_var_id] = best_pb.values()[plat_var_id]
		else:
			# Fallback: only include category variable
			if variable_filter:
				var_id, var_val = variable_filter
				if var_id in best_pb.values():
					variables[var_id] = best_pb.values()[var_id]

		# Find the place number and return this PB run.
		place = self._lookup_run_place(game_obj.id, category_obj.id, best_pb.id, variables)
		best_pb.place = place
		return result
