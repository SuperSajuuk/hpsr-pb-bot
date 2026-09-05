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
import config
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
		cfg = config.LEADERBOARD_CONFIG.get(slug, None)
		want_emulator = bool(flags and flags.get("emulator", False))
		var_filters = None
		if cfg and "platform" in cfg:
			# Capture the variable ID and values depending on the platform.
			platform_cfg = cfg["platform"]
			var_id = platform_cfg["var_id"]
			values = platform_cfg["values"]
			console_val = values["console"]
			emulator_val = values["emulator"]

			# Build initial var_filters based on flags. Then, query SRDC to capture
			# runs with the initial filter, and do client-side processing to check
			# for console/emulator splits.
			var_filters = {var_id: emulator_val} if want_emulator else {var_id: console_val}
			runs = self.search_runs(game_obj.id, category_obj.id, user_id, var_filters)
			if want_emulator:
				# Keep only emulator runs
				runs = [r for r in runs if r["values"].get(var_id) == emulator_val]
			else:
				# Prefer console runs: keep only console runs if any exist
				console_runs = [r for r in runs if r["values"].get(var_id) == console_val]
				if console_runs:
					runs = console_runs
				else:
					# Fallback: try emulator runs
					runs = self.search_runs(game_obj.id, category_obj.id, user_id, {var_id: emulator_val})
					runs = [r for r in runs if r["values"].get(var_id) == emulator_val]
		else:
			# No platform variable configured: fall back to unfiltered search
			runs = self.search_runs(game_obj.id, category_obj.id, user_id)

		# If nothing is returned by this, just return None.
		if not runs:
			return None

		# Sort the runs by the most recently verified run (newest at the top)
		# The run at the top of the index will then be used to get its placement
		# in the leaderboard. To avoid duplication, leaderboard placement is
		# parsed by a helper function.
		runs.sort(key=lambda r: r["status"]["verify-date"], reverse=True)
		best_run = runs[0]

		# Extract all run details and the leaderboard placement, then return the run object.
		place = self.utils.lookup_run_place(game_obj.id, category_obj.id, best_run["id"], var_filters)
		sr = self.utils.extract_run(best_run, player)
		sr.place = place
		return sr
