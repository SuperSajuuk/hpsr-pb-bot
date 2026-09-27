#
# Utilities
#
# Generic utility functions are stored here, then used
# around other classes and objects by basic variable passing.
#
# This allows them to be easily maintained and avoids the
# methods being duplicated several times.
import datetime
from utils.model import SpeedRun


class Utilities:
	def __init__(self, api, lb_config, platform_map):
		self.api = api
		self.lb_config = lb_config
		self.platform_map = platform_map

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

	def lookup_run_place(self, game_id, category_id, run_id, variables: list | None, alt_url: str = None):
		"""
		Looks up the leaderboard for a game and returns the
		place number representing the provided run.
		"""
		# Try partial leaderboard first
		lb_partial = self.api.get_leaderboard(game_id, category_id, max_runs=100, variables=variables, alt_url=alt_url)
		place = self.find_run_placement(lb_partial, run_id)

		# If place is None here, the run wasn't in the top 100.
		# Return all runs and then find it.
		if place is None:
			lb_full = self.api.get_leaderboard(game_id, category_id, max_runs=None, variables=variables, alt_url=alt_url)
			place = self.find_run_placement(lb_full, run_id)

		return place

	def resolve_platform_id(self, platform_id):
		"""
		Resolves the platform_id obtained from extract_run to
		get the platform details that the platform code references.

		Returns None if platform_id already equals None: this will
		use the old behaviour of simply uppercasing the users' input.
		"""
		if platform_id is None:
			return None
		for key, data in self.platform_map.items():
			if data["id"] == platform_id:
				return data
		return None

	@staticmethod
	def find_run_placement(leaderboard, run_id: str) -> int | None:
		"""Return the leaderboard placement for a given run ID."""
		for entry in leaderboard["runs"]:
			if entry["run"]["id"] == run_id:
				return entry["place"]
		return None

	@staticmethod
	def filter_all_runs(runs: list, var_filters: list):
		"""
		Takes a list of run objects returned by the search_runs method
		and filters out the runs so only the ones the user asked for
		are included.

		Returns a new list of filtered runs.
		"""
		filtered_runs = []
		for r in runs:
			all_match = True
			for x in var_filters:
				for key, val in x.items():
					if r["values"].get(key) != val:
						all_match = False
						break
				if not all_match:
					break
			if all_match:
				filtered_runs.append(r)
		return filtered_runs

	@staticmethod
	def generate_var_filters(cfg, flags, cfg_2=None):
		# All the variable data is stored in the "variables" key.
		# Use that to capture all the relevant info we need.
		# Some keys might contain names to define what they are.
		active_slice = None
		variable_data = cfg.get("variables", None)
		if variable_data is None:
			variable_data = cfg_2.get("variables", []) if isinstance(cfg_2, dict) else []

		# Check the user provided flags against the slice names.
		slice_names = {x["name"] for x in variable_data if "name" in x}
		if flags:
			# Flags that match slice names AND are True.
			# If any are found, select it as the active slice.
			true_flags = {name for name in slice_names if flags.get(name) is True}
			if true_flags:
				active_slice = next(iter(true_flags))
			else:
				# Perhaps check in the additional metadata in case there's something there.
				additional_flags = {name for key, name in flags["additional_metadata"].items()}
				if additional_flags:
					active_slice = next(iter(additional_flags))
				else:
					active_slice = next((name for name in slice_names if name not in flags), None)

		# This might still be None: in which case, just pick the first slice.
		if active_slice is None:
			active_slice = next(iter(slice_names), None)

		# Build the relevant variable filters and then return the new list.
		var_filters = []
		for x in variable_data:
			if "name" not in x:
				var_filters.append({x["var_id"]: x["value_id"]})
				continue
			if x.get("name") == active_slice or active_slice in x.get("aliases", []):
				var_filters.append({x["var_id"]: x["value_id"]})
				continue

		return var_filters

	@staticmethod
	def extract_run(run, player_name, place_num=None) -> SpeedRun:
		"""
		Convert a srcomapi Run object into a SpeedRun dataclass.
		"""
		# Before creating the object, parse the time, which is given in seconds.
		# This may come up in some runs which are measured with millisecond precision.
		# To avoid looking silly in some places, millisecond precision will only be
		# given if the API returns it.
		seconds = run["times"]["primary_t"]
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
			game=str(run["game"]),
			category=str(run["category"]),
			time=time_str,
			platform=run["system"]["platform"],
			emulator=run["system"]["emulated"],
			place=place_num,
			link=run["weblink"]
		)
