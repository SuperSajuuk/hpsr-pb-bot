#
# LEGO Games Main Board Run
#
# This code processes a LEGO Games Main Board run object.
#
# This is simply an extension of the normal run class, but instead
# its built to handle the very flexible requirements of certain LEGO
# main boards like Batman, Harry Potter and so on. The reason for that
# is due to the required number of parameters used on such boards: these
# include things like NOCUT5, Solo/Co-Op, Restricted/Unrestricted and so
# on.
from model import SpeedRun
import datetime
import configs.generic as config
from typing import Dict


# LEGONormalRun
# This handles the logic of querying the SRDC
# API for a LEGO Games run submission. This is
# used by !run only.
class LEGONormalRun:
	def __init__(self, api, game_map, category_map, utils):
		self.api = api
		self.game_map = game_map
		self.category_map = category_map
		self.utils = utils

	# ---------------------------------------------------------
	# LOOKUP RUN
	# ---------------------------------------------------------
	def lookup_lego_run(self, game: str, internal_key: str, slug: str, cat_key: str, player: str) -> SpeedRun | None:
		"""
		Look up the fastest verified run for a player in a specific game/category.
		Uses SRDC variable filters and client-side filtering to ensure only the run the
		user requested is returned (this is due to the way SRDC returns runs from the API)
		"""
		# Get the game object from the slug.
		game_obj = self.utils.get_game_code(slug)
		if not game_obj:
			raise ValueError("Invalid game object, make sure the slug URL is defined correctly in the configuration files.")

		# Obtain the relevant category name from the category map.
		category_meta = None
		for category_name, aliases in self.category_map[game].items():
			if cat_key in aliases:
				category_meta = category_name
				break

		# Return if category_meta is still None (no match would have been found)
		if not category_meta:
			return None

		# Check that there is a category matching the one we asked for.
		category_obj = None
		for cat in game_obj.categories:
			if cat.name == category_meta:
				category_obj = cat
				break

		# If no category exists with the given name, raise ValueError and quit.
		if not category_obj:
			raise ValueError("Category not found in game")

		# Resolve user ID and pull in all variables for the game.
		user_id = self.utils.get_user_id(player)
		cfg = self.utils.resolve_leaderboard_config(game, internal_key, cat_key)
		if cfg is None:
			raise ValueError(f"Missing leaderboard configuration data for key: '{internal_key}'.")

		# With the provided data, search SRDC for runs.
		# If nothing there, just return None.
		var_filters = cfg.get("variables", None)
		runs = self.utils.search_runs(game_obj.id, category_obj.id, user_id, var_filters)
		if not runs:
			return None

		# LEGO runs contain a significant number of variables, which require
		# the returned list of runs to be filtered. This ensures only the
		# run the user asked for is returned by the system.
		required_variables = {var["var_id"]: var["value_id"] for var in var_filters}
		filtered_runs = []
		for r in runs:
			ok = True
			for var_id, value_id in required_variables.items():
				if r["values"].get(var_id) != value_id:
					ok = False
					break
			if ok:
				filtered_runs.append(r)

		# If no runs were found, return None
		if not filtered_runs:
			return None

		# Sort the runs by the most recently verified run (newest at the top)
		# The run at the top of the index will then be used to get its placement
		# in the leaderboard. To avoid duplication, leaderboard placement is
		# parsed by a helper function.
		filtered_runs.sort(key=lambda rx: rx["submitted"], reverse=True)
		best_run = filtered_runs[0]

		# Extract all run details and the leaderboard placement, then return the run object.
		place = self.utils.lookup_run_place(game_obj.id, category_obj.id, best_run["id"], required_variables)
		sr = self.utils.extract_run(best_run, player)
		sr.place = place
		return sr
