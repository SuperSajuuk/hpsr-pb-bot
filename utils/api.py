#
# API
#
# This contains all the methods that interact with the speedrun.com
# API.
#
# This includes methods which may or may not always interact with it
# due to a caching layer.
#
import srcomapi.datatypes as dt


class API:
	def __init__(self, api, cache):
		self.api = api
		self.cache = cache

	def search_pbs(self, player: str, game_id: str):
		"""
		Fetch PBs for a player/game combination.
		"""
		return self.api.get(f"users/{player}/personal-bests?game={game_id}&embed=variables")

	def get_ce_mr_game(self, game_name: str, tag_id: str, type_name: str):
		"""
		Resolve the game object for a CE or Multi-run board.

		This is similar to self.get_game_code, except it has a logic check for
		a specific tag being present in the gametypes list of a returned game
		object. If that isn't present, the lookup fails with a ValueError, as this
		should only be called for games representing category extensions or multi-run
		boards.

		Raises ValueError if no such game is found.
		"""
		# Query SRDC or raise ValueError if nothing was found.
		search = self.api.get(f"games?abbreviation={game_name}&embed=tags")
		if not search:
			return None

		# Parse the game object for the relevant tag.
		# This is hard-coded because the game type
		# ID is fixed and doesn't change.
		game = search[0]
		if tag_id not in game["gametypes"]:
			raise ValueError(f"Game '{game['names']['international']}' is not defined as a {type_name} board.")

		# Return the game object for this board.
		return game

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

	def get_srdc_user(self, arg: str, arg_type: str = "username") -> str:
		"""
		Returns the user object based on the provided username.
		Checks Redis first before querying SRDC.
		"""
		key = self.cache.get_key(f"run-finder:users:{arg}")
		if key is not None:
			return key

		# Not found in Redis, query SRDC instead
		result = None
		match arg_type:
			case "username":
				result = self.api.search(dt.User, {"name": arg})
			case "user_id":
				result = self.api.get(f"users/{arg}")

		# Nothing found, raise an error?
		if not result:
			raise ValueError(f"User not found on SRDC: {arg}")

		# Cache the users' ID, so we don't have to query SRDC again
		val = result[0].id if arg_type == "username" else result["names"]["international"]
		self.cache.create_key(f"run-finder:users:{arg}", val)
		return val

	def get_leaderboard(self, game_id: str, category_id: str, max_runs: int = None, variables: list = None, alt_url: str = None):
		"""
		Fetch leaderboard for a game/category.
		URL is extended based on max_runs or variables being included.
		"""
		# Set the URL.
		url = f"leaderboards/{game_id}/category/{category_id}?embed=variables" if alt_url is None else alt_url

		# Append max_runs and var-value pairs if required.
		if max_runs is not None:
			url += f"&max={max_runs}"
		if variables:
			for var in variables:
				for var_id, var_value in var.items():
					url += f"&var-{var_id}={var_value}"

		return self.api.get(url)

	def search_runs(self, game_id, category_id, user_id, var_filters: list = None, base_query=None):
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
		base_q = f"runs?game={game_id}&category={category_id}&user={user_id}&status=verified&embed=variables" if base_query is None else base_query
		if var_filters:
			for var in var_filters:
				for key, val in var.items():
					base_q += f"&var-{key}={val}"

		# Paginate the results until all are found.
		all_runs = []
		offset = 0
		while True:
			# Start at 50, then increase the offset per loop.
			# If the batch returns nothing, break the loop.
			q = f"{base_q}&max=50&offset={offset}"
			batch = self.api.get(q)
			if not batch:
				break

			# Append the runs, then increase the offset and continue.
			all_runs.extend(batch)
			offset += 50

		# Return the full list.
		return all_runs
