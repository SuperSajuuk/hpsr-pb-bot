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

		# Check if we've defined the platform in this request.
		platform_var_id = None
		desired_value = None
		if platform is not None:
			# Get the platform ID from the first value of the allow list.
			# Then, filter it to see if runs are provided.
			allowlist = config.CATEGORY_VARIABLE_ALLOWLIST.get(game_key, {})
			platform_var_id = allowlist.get("platform")
			if platform_var_id:
				desired_value = config.PLATFORM_VALUES[game_key][platform]
				runs = [r for r in runs if r["values"].get(platform_var_id) == desired_value]

				# If filtering removed all runs, return None
				if not runs:
					return None

		# In some games, there might be a multi-run: check for those first.
		if "variables" in category_meta:
			var_id = list(category_meta["variables"].keys())[0]
			var_values = category_meta["variables"][var_id]
			results = {}

			# Any%
			any_runs = [
				r for r in runs
				if r["values"].get(var_id) == var_values["any"] and (platform_var_id is None or r["values"].get(platform_var_id) == desired_value)
			]
			if any_runs:
				# Sort the Any% runs by verification date, and find its place in the list
				any_runs.sort(key=lambda r: r["status"]["verify-date"], reverse=True)
				best_any = any_runs[0]
				variables_any = best_any["values"]
				place_any = self._lookup_run_place(game_obj.id, category_obj.id, best_any["id"], variables_any)

				# Extract the run details and store it in the dictionary.
				sr_any = self.extract_run(best_any, player)
				sr_any.place = place_any
				results["any"] = sr_any

			# 100%
			hundo_runs = [
				r for r in runs
				if r["values"].get(var_id) == var_values["100"] and (platform_var_id is None or r["values"].get(platform_var_id) == desired_value)
			]
			if hundo_runs:
				# Sort the 100% runs by verification date, and find its place in the list.
				hundo_runs.sort(key=lambda r: r["status"]["verify-date"], reverse=True)
				best_hundo = hundo_runs[0]
				variables_hundo = best_hundo["values"]
				place_hundo = self._lookup_run_place(game_obj.id, category_obj.id, best_hundo["id"], variables_hundo)

				# Extract the run details and store it in the dictionary.
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

		# Check for variables and set them up.
		variables = {}
		allowlist = config.CATEGORY_VARIABLE_ALLOWLIST.get(game_key, {})
		category_var_id = allowlist.get("category")
		if category_var_id and category_var_id in best_run["values"]:
			variables[category_var_id] = best_run["values"][category_var_id]

		# Include platform variable ONLY if user requested platform
		if platform is not None:
			platform_var_id = allowlist.get("platform")
			if platform_var_id and platform_var_id in best_run["values"]:
				variables[platform_var_id] = best_run["values"][platform_var_id]

		# all_vars = best_run["values"]
		# allowlist = config.CATEGORY_VARIABLE_ALLOWLIST.get(game_key, None)
		# variables = {vid: all_vars[vid] for vid in allowlist if vid in all_vars} if allowlist is not None else all_vars
		# place = self._lookup_run_place(game_obj.id, category_obj.id, best_run["id"], variables)

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
	def lookup_pb(self, game_key: str, cat_key: str, player: str) -> list[SpeedRun] | dict[str, SpeedRun] | None:
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
		pbs = self.search_pbs(player, game_obj.id)

		# Some categories might include multi-run metadata.
		# If that is the case, search for a PB in those.
		if "variables" in category_meta:
			var_id = list(category_meta["variables"].keys())[0]
			var_values = category_meta["variables"][var_id]
			results = {}

			# Any%
			any_pbs = self.find_pbs(player, pbs, category_obj.id, (var_id, var_values["any"]))
			if any_pbs:
				results["any"] = any_pbs[0]

			# 100%
			hundo_pbs = self.find_pbs(player, pbs, category_obj.id, (var_id, var_values["100"]))
			if hundo_pbs:
				results["100"] = hundo_pbs[0]

			# Return all SpeedRun objects that have been found.
			return results

		# Optional variable filtering (for CE categories)
		# Written using an in-line expression for tidiness.
		variable_filter = ("2lg3d4on", category_meta["cecode"]) if "cecode" in category_meta else None
		return self.find_pbs(player, pbs, category_obj.id, variable_filter)
