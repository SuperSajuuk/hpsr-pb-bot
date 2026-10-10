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

	def find_run_at_position(self, game_id: str, category_id: str, position: int, var_filters: list) -> SpeedRun | None:
		"""
		Look for the fastest verified run at a defined position, based on game_id, category_id
		and variables, if defined.

		Player will be derived from the data provided by SRDC, rather than being provided by the
		end user.

		Returns a SpeedRun object or None, if no run was found.
		"""
		# Check the value of the position number given.
		# -1 means no number, or an invalid number, was provided.
		# Anything greater than 200 raises an error currently.
		if position == -1:
			raise InvalidPosNumber("No position number has been provided. A whole number between 1-200 inclusive is required.")
		if position > 200:
			raise InvalidPosNumber("You can only use the --position flag on leaderboards up to a maximum of run 200 at this time.")

		# Look for a run that matches requirements.
		# Unlike normal runs, this only uses leaderboard lookup, as it's the only
		# route that includes place numbers. The max number of runs returned is
		# constrained by the position argument for simplicity.
		runs = self.api.get_leaderboard(game_id, category_id, position, var_filters)
		if not runs:
			return None

		# Rather than handing to a specific utility function here, instead
		# just loop all runs until it finds the one with the given
		# position.
		run = None
		for entry in runs["runs"]:
			if entry["place"] == position:
				run = entry
				break

		# Didn't find it (which would be strange...)
		if run is None:
			return None

		# Extract run details from the object.
		player = self.api.get_srdc_user(run["run"]["players"][0]["id"], arg_type="user_id")
		sr = self.extract_run(run["run"], player)
		sr.place = run["place"]
		return sr

	def resolve_leaderboard_config(self, game_key: str, internal_key: str) -> dict | None:
		"""
		Resolves the relevant leaderboard config block, based on game_key
		or internal_key.

		Returns a dictionary of the data, or None if nothing was found.
		"""
		game_cfg = self.lb_config.get(game_key)
		return game_cfg if game_cfg else self.lb_config.get(internal_key)

	@staticmethod
	def resolve_category_config(data: dict, int_key: str = None, cat_key: str = None):
		"""
		Resolve the correct category block from the leaderboard config.

		Returns either the dictionary containing the relevant data, or None.
		"""
		if int_key in data:
			return data[int_key]
		if cat_key in data:
			return data[cat_key]
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
	def process_additional_md(metadata: dict, aliases: dict, cat_name: str, int_key: str = None, cat_name_extend: bool = True):
		"""
		Processes the additional_metadata key of flags to extend the category name
		or the internal key, depending on use case.

		Returns the category name and internal key with the modifications. If no
		modifications were made, then the original values are just returned as is.
		"""
		# If there isn't any metadata, just return.
		if not metadata:
			return cat_name, int_key

		# Process all metadata values
		for key_val in metadata.values():
			found_alias = False
			for human_name, data in aliases.items():
				if key_val in data["aliases"]:
					found_alias = True
					if cat_name_extend:
						cat_name += f" {human_name}"

					# If internal key was provided, and it exists in the
					# data dictionary, extend it.
					if int_key is not None and data.get("int_key", None) is not None:
						int_key += f"_{data['int_key']}"
					break

			# No alias found: do nothing and just continue to the next one.
			if not found_alias:
				continue

		# Return the modified category name and internal key, if any.
		return cat_name, int_key

	@staticmethod
	def generate_var_filters(var_list, flags):
		# Pull in all flags (where flag item is True or its in additional metadata).
		var_filters = []
		selected_tokens = set()
		if flags:
			selected_tokens.update(name for name, val in flags.items() if val is True)
			selected_tokens.update(
				flags.get("additional_metadata", {}).values()
			)
			selected_tokens.update(
				v for v in (flags["ce_board"], flags["cc_board"], flags["mr_board"]) if v is not None
			)

		# Build the var filters based on the tokens list.
		for x in var_list:
			if "name" not in x:
				var_filters.append({x["var_id"]: x["value_id"]})
				continue
			if x["name"] in selected_tokens:
				var_filters.append({x["var_id"]: x["value_id"]})
				continue

		# If the list of selected tokens is empty, fall back
		# to defaults.
		if not selected_tokens:
			for x in var_list:
				if x.get("default", False):
					var_filters.append({x["var_id"]: x["value_id"]})

		# Return the list of var filters generated by the users' query.
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
