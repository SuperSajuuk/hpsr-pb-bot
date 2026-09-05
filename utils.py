#
# Utilities
#
# Generic utility functions are stored here, then used
# around other classes and objects by basic variable passing.
#
# This allows them to be easily maintained and avoids the
# methods being duplicated several times.
import srcomapi.datatypes as dt
import datetime
from model import SpeedRun


class Utilities:
	def __init__(self, api):
		self.api = api
		self.game_code_cache = {}

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
		result = self.api.search(dt.Game, {"abbreviation": game_key})
		if not result:
			raise ValueError(f"Game not found on SRDC: {game_id}")

		# Cache the result and return it.
		game_obj = result[0]
		self.game_code_cache[game_key] = game_obj
		return game_obj

	def get_user_id(self, username: str) -> str:
		"""Resolve a Speedrun.com username to a user ID."""
		result = self.api.search(dt.User, {"name": username})
		if not result:
			raise ValueError(f"User not found on SRDC: {username}")
		return result[0].id

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

	def lookup_run_place(self, game_id, category_id, run_id, variables: dict | None):
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

	@staticmethod
	def find_run_placement(leaderboard, run_id: str) -> int | None:
		"""Return the leaderboard placement for a given run ID."""
		for entry in leaderboard["runs"]:
			if entry["run"]["id"] == run_id:
				return entry["place"]
		return None

	@staticmethod
	def extract_run(run_obj, player_name) -> SpeedRun:
		"""
		Convert a srcomapi Run object into a SpeedRun dataclass.
		"""
		# Before creating the object, parse the time, which is given in seconds.
		# This may come up in some runs which are measured with millisecond precision.
		# To avoid looking silly in some places, millisecond precision will only be
		# given if the API returns it.
		seconds = run_obj["times"]["primary_t"]
		td = datetime.timedelta(seconds=seconds)
		total_ms = int(td.total_seconds() * 1000)
		hours, remainder = divmod(total_ms, 3600_000)
		minutes, remainder = divmod(remainder, 60_000)
		secs, ms = divmod(remainder, 1000)

		# Decide whether to show milliseconds
		# If this is an integer, time will be HH:MM:SS.
		# If it's a float, then it'll be HH:MM:SS.mmm
		time = f"{hours}:{minutes:02d}:{secs:02d}" if seconds.is_integer() else f"{hours}:{minutes:02d}:{secs:02d}.{ms:03d}"

		# Create a SpeedRun model and return it.
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
