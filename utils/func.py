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
from utils.model import SpeedRun


class Utilities:
	def __init__(self, api, cache, lb_config):
		self.api = api
		self.cache = cache
		self.lb_config = lb_config
		self.game_code_cache = {}

	def get_game_code(self, game_key: str, redis_key: str = "categories", type_filter: str = "per-game"):
		"""
		Returns details about the game needing to be searched for.

		If the Game ID exists in Redis, then the ID and the categories
		stored there will be returned. If nothing was found, then SRDC
		will be queried for a result. That result will be cached in Redis
		to remove the requirement to query further.

		The parameters redis_key and type_filter are optional values which
		determine if the system should look for IL categories or the main
		board categories. If these are not provided, the code will just assume
		you're looking for the main boards.
		"""
		# Check to see if the game exists in Redis
		key = self.cache.get_key(f"run-finder:game:{game_key}")
		if key is not None:
			# Check if the categories data exists. If it doesn't, then it may have been
			# evicted automatically, so we would have to re-query SRDC anyway.
			cats = self.cache.get_hash_data(f"run-finder:game:{game_key}:{redis_key}")
			if cats:
				return key, cats

		# Not found in Redis. Therefore, we need to look it up in SRDC.
		result = self.api.search(dt.Game, {"abbreviation": game_key})
		if not result:
			raise ValueError(f"Could not find the game `{game_key}`. Check for typos, and try again. If you are confident there are no typos, this might be a bug.")

		# Store the game ID and category list in Redis and return those values.
		game_obj = result[0]
		cats = {x.id: x.name for x in game_obj.categories if x.type == type_filter}
		self.cache.create_key(f"run-finder:game:{game_key}", game_obj.id)
		self.cache.create_multiple_in_hash(f"run-finder:game:{game_key}:{redis_key}", cats)
		self.cache.key_expiry(f"run-finder:game:{game_key}:{redis_key}", 604800)
		return game_obj.id, cats

	def get_user_id(self, username: str) -> str:
		"""
		Returns the user ID for the identified user.
		Checks Redis first before querying SRDC.
		"""
		key = self.cache.get_key(f"run-finder:users:{username}")
		if key is not None:
			return key

		# Not found in Redis, query SRDC instead
		result = self.api.search(dt.User, {"name": username})
		if not result:
			raise ValueError(f"User not found on SRDC: {username}")

		# Cache the users' ID, so we don't have to query SRDC again
		self.cache.create_key(f"run-finder:users:{username}", result[0].id)
		return result[0].id

	def get_leaderboard(self, game_id: str, category_id: str, max_runs: int | None = None, variables: dict | None = None, alt_url: str = None):
		"""
		Fetch leaderboard for a game/category.
		If max_runs is provided, only that many runs are returned.
		"""
		url = f"leaderboards/{game_id}/category/{category_id}?embed=players" if alt_url is None else alt_url
		if max_runs is not None:
			url += f"&max={max_runs}"
		if variables:
			for var_id, var_value in variables.items():
				url += f"&var-{var_id}={var_value}"

		return self.api.get(url)

	def resolve_leaderboard_config(self, game_key: str, internal_key: str, cat_key: str = None):
		"""
		Resolve the correct leaderboard config block, depending on whether
		the config exists under the game_key or the internal_key. This will
		either return the relevant config dictionary, or None.
		"""
		# Check to see if there is a config key under the game_key
		game_cfg = self.lb_config.get(game_key)
		if game_cfg:
			if internal_key in game_cfg:
				return game_cfg[internal_key]
			if cat_key in game_cfg:
				return game_cfg[cat_key]

		# Didn't find it under game_key, so perhaps look under the internal key
		internal_cfg = self.lb_config.get(internal_key)
		if internal_cfg:
			return internal_cfg

		# Found nothing, so return None.
		return None

	def lookup_run_place(self, game_id, category_id, run_id, variables: dict | None, alt_url: str = None):
		"""
		Looks up the leaderboard for a game and returns the
		place number representing the provided run.
		"""
		# Try partial leaderboard first
		lb_partial = self.get_leaderboard(game_id, category_id, max_runs=100, variables=variables, alt_url=alt_url)
		place = self.find_run_placement(lb_partial, run_id)

		# If place is None here, the run wasn't in the top 100.
		# Return all runs and then find it.
		if place is None:
			lb_full = self.get_leaderboard(game_id, category_id, max_runs=None, variables=variables, alt_url=alt_url)
			place = self.find_run_placement(lb_full, run_id)

		return place

	@staticmethod
	def find_run_placement(leaderboard, run_id: str) -> int | None:
		"""Return the leaderboard placement for a given run ID."""
		for entry in leaderboard["runs"]:
			if entry["run"]["id"] == run_id:
				return entry["place"]
		return None

	def search_runs(self, game_id, category_id, user_id, var_filters=None, base_query=None):
		"""
		Builds a base query from the provided game_id, category_id and user_id
		to find runs on a specific leaderboard of SRDC.

		This also supports appending variables - in key/value pairs of var_id
		and value_id - to perform server-side filtering, which reduces how
		many rows are returned. Pagination is also used if the result set has
		more than 20 records.

		Returns a list, which may be empty or contain a list of Run objects.
		"""
		# Build a base query, which we can then paginate against.
		base_q = f"runs?game={game_id}&category={category_id}&user={user_id}&status=verified&embed=variables,players" if base_query is None else base_query
		if var_filters:
			if isinstance(var_filters, list):
				for var in var_filters:
					for key, val in var.items():
						base_q += f"&var-{key}={val}"
			else:
				for key, val in var_filters.items():
					base_q += f"&var-{key}={val}"

		# Paginate the results until all are found.
		all_runs = []
		offset = 0
		while True:
			# Start at 20, then increase the offset per loop.
			# If the batch returns nothing, break the loop.
			q = f"{base_q}&max=20&offset={offset}"
			batch = self.api.get(q)
			if not batch:
				break

			# Append the runs, then increase the offset and continue.
			all_runs.extend(batch)
			offset += 20

		# Return the full list.
		return all_runs

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
		total_ms = round(seconds * 1000)
		days, remainder = divmod(total_ms, 86_400_000)
		hours, remainder = divmod(remainder, 3_600_000)
		minutes, remainder = divmod(remainder, 60_000)
		secs, ms = divmod(remainder, 1000)

		# Return a time string that is dependent on the highest level of data.
		if days:
			time_str = f"{days}d {hours:02d}:{minutes:02d}:{secs:02d}"
		elif hours:
			time_str = f"{hours}:{minutes:02d}:{secs:02d}"
		else:
			time_str = f"{minutes}:{secs:02d}"

		# If there is milliseconds and the original time is a float, append it.
		if ms and not seconds.is_integer():
			time_str += f".{ms:03d}"

		# Create a SpeedRun model and return it.
		return SpeedRun(
			player=player_name,
			game=str(run_obj["game"]),
			category=str(run_obj["category"]),
			time=time_str,
			raw=None,
			platform=run_obj["system"]["platform"],
			emulator=run_obj["system"]["emulated"],
			place=None,  # run search does not include leaderboard place
			link=run_obj["weblink"],
			id=None
		)
