#
# Normal Run
#
# This code processes a Normal Run object. A normal run is
# defined as something belong to a primary board: ie it isn't
# part of a category extension or a multi-run. These kind of runs
# are the most common lookups we'll do in the code, as its covering
# the main boards. CE's are to be handled in ce.py and multiruns will
# be in multi.py
from model import SpeedRun
import datetime
import configs.generic as config
from typing import Dict


# NormalRun
# This handles the logic of querying the SRDC
# API for a normal run submission. This is
# used by !run only.
class NormalRun:
	def __init__(self, api, game_map, platform_map, category_map, utils):
		self.api = api
		self.game_map = game_map
		self.platform_map = platform_map
		self.category_map = category_map
		self.utils = utils

	# ---------------------------------------------------------
	# RUN FETCH
	# ---------------------------------------------------------
	def search_runs(self, game_id, category_id, user_id, variables=None):
		"""
		Search SRDC for runs matching game/category/user.
		Also includes variables, if any are given.
		"""
		q = f"runs?game={game_id}&category={category_id}&user={user_id}&status=verified&embed=variables,players"
		if variables is not None:
			for var_id, value_id in variables.items():
				q += f"&var-{var_id}={value_id}"
		return self.api.get(q)

	# ---------------------------------------------------------
	# LOOKUP RUN
	# ---------------------------------------------------------
	def lookup_run(self, internal_key: str, cat_key: str, player: str, flags: dict | None) -> SpeedRun | None:
		"""
		Look up the fastest verified run for a player in a specific game/category.
		Uses SRDC variable filters and client-side filtering to ensure only the run the
		user requested is returned (this is due to the way SRDC returns runs from the API)
		"""
		# Parse the internal_key and cat_key to obtain the game and category.
		slug = config.BOARD_GAME_SLUG[internal_key]
		game_obj = self.utils.get_game_code(slug)
		category_meta = self.category_map[cat_key]

		# Check that there is a category matching the one we asked for.
		category_obj = None
		for cat in game_obj.categories:
			if cat.name == category_meta:
				category_obj = cat
				break

		# If no category exists with the given name, raise ValueError and quit.
		if not category_obj:
			raise ValueError("Category not found in game")

		# Resolve user ID, then check for variables in case we have one.
		user_id = self.utils.get_user_id(player)
		cfg = self.utils.resolve_leaderboard_config(slug, internal_key, cat_key)
		cfg_2 = None
		if cfg is not None:
			cfg_2 = cfg.get(cat_key, None)

		# Check if either cfg or cfg_2 contains a variables key.
		# If so, capture all variables and build a var_filters list
		# for use in the query.
		var_filters = None
		variable_data = None
		active_slice = None
		if (cfg and "variables" in cfg) or (cfg_2 and "variables" in cfg_2):
			# All the variable data is stored in the "variables" key.
			# Use that to capture all the relevant info we need.
			# Some keys might contain names to define what they are.
			variable_data = cfg.get("variables", None)
			if variable_data is None:
				variable_data = cfg_2.get("variables", [])

			# Check the user provided flags against the slice names.
			slice_names = {x["name"] for x in variable_data if "name" in x}
			if flags:
				# Flags that match slice names AND are True.
				# If any are found, select it as the active slice.
				true_flags = {name for name in slice_names if flags.get(name) is True}
				if true_flags:
					active_slice = next(iter(true_flags))
				else:
					active_slice = next((name for name in slice_names if name not in flags), None)

			# This might still be None: in which case, just pick the first slice.
			if active_slice is None:
				active_slice = next(iter(slice_names), None)

			# Build var_filters
			var_filters = {}
			for x in variable_data:
				if "name" not in x:
					var_id = x["var_id"].split("-")[1]
					var_filters[var_id] = x["value_id"]
			for x in variable_data:
				if x.get("name") == active_slice:
					var_id = x["var_id"].split("-")[1]
					var_filters[var_id] = x["value_id"]

		# With the provided data, search SRDC for runs.
		# If nothing there, just return None.
		runs = self.search_runs(game_obj.id, category_obj.id, user_id, var_filters)
		if not runs:
			return None

		# After returning runs, you may receive more than you asked for: this
		# is a limitation of SRDC. Thus, to just have "one run", we need to do
		# some filtering here.
		# Client-side filtering based on selected slice
		if active_slice is not None:
			filtered_runs = []
			for r in runs:
				# Check if this run matches the chosen slice
				for x in variable_data:
					if x.get("name") == active_slice:
						var_id = x["var_id"].split("-")[1]
						if r["values"].get(var_id) == x["value_id"]:
							filtered_runs.append(r)
							break
			runs = filtered_runs

		# If nothing remains after filtering, return None
		if not runs:
			return None

		# Sort the runs by the most recently verified run (newest at the top)
		# The run at the top of the index will then be used to get its placement
		# in the leaderboard. To avoid duplication, leaderboard placement is
		# parsed by a helper function.
		runs.sort(key=lambda rx: rx["submitted"], reverse=True)
		best_run = runs[0]

		# Extract all run details and the leaderboard placement, then return the run object.
		place = self.utils.lookup_run_place(game_obj.id, category_obj.id, best_run["id"], var_filters)
		sr = self.utils.extract_run(best_run, player)
		sr.place = place
		return sr
