#
# Multirun Boards
#
# This code processes a Multirun Board Run object. A Multirun board is
# basically a category extension board, but the type of categories are
# specifically about running more than one game. Such boards usually have
# the "Multi-game" tag on them. Should a user provide a game which we
# do not have a hard-coded value for, the system will look up SRDC and
# then fail if no board exists.
from model import SpeedRun
import srcomapi.datatypes as dt
import datetime
import config
from typing import Any, Dict


# MultiRun
# This handles the logic of querying the SRDC
# API for a Multirun submission.
# This is used by !run only.
class MultiRun:
	def __init__(self, api, game_map, platform_map, category_map, lb_config, utils):
		self.api = api
		self.game_map = game_map
		self.platform_map = platform_map
		self.category_map = category_map
		self.lb_config = lb_config
		self.utils = utils

	def search_runs(self, game_id: str, category_id: str, user_id: str, var_filters: Dict[str, str] | None = None) -> list[Dict[str, Any]]:
		"""
		Search SRDC for runs matching game/category/user. Also includes variable filters, if any are given.

		Due to some quirks, this can return a lot of irrelevant runs we are not looking for. Consequently,
		this will be paginated to bring back all the matching runs, which can then be filtered appropriately.
		"""
		# Build a base query, which we can then paginate against.
		base_q = f"runs?game={game_id}&category={category_id}&user={user_id}&status=verified&embed=variables,players"
		if var_filters is not None:
			for var in var_filters:
				for var_id, value_id in var.items():
					base_q += f"&var-{var_id}={value_id}"

		# Paginate the results until all are found.
		all_runs: list[Dict[str, Any]] = []
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

	# Resolve the Game Slug for a Multirun
	# Using just the game code provided, check our
	# local config for that code. If it's not there,
	# query SRDC and ensure it does have the category
	# extension tag.
	def resolve_multirun_game_slug(self, base_game: str) -> dt.Game | str:
		"""
		Resolve the Game Slug for a Multirun

		If possible, rely on local config data before querying SRDC.
		If we don't have a config key for this, query SRDC and ensure
		the game does have the Multi Run game type assigned.

		Raises ValueError if no such game is found.
		"""
		# Check if the base game key is already in the game map.
		# Use it first before querying SRDC.
		if base_game in self.game_map:
			return self.game_map[base_game]

		# Couldn't find it in our hard-coded list, so
		# query SRDC for the specific game that is needed.
		search = self.api.get(f"games?abbreviation={base_game}&embed=tags")
		if not search:
			raise ValueError(f"No Multi-run game found for base game: {base_game}")

		# Parse the game object for the relevant tag.
		# This is hard-coded because multi-run is
		# always the same and doesn't change.
		game = search[0]
		is_multi_run = False
		for tag in game["gametypes"]:
			if tag == "rj1dy1o8":
				is_multi_run = True
				break

		# Error here, because the required tag cannot be found.
		if not is_multi_run:
			raise ValueError(f"No Multi-run game found for base game: {base_game}")

		# Return the game object for this multi-run board.
		return game

	def lookup_multi_run(self, base_game: str, mr_category: str, player: str, flags: dict) -> SpeedRun | None:
		"""
		Resolve and fetch a Multirun Board run using the same SRDC logic as normal runs,
		but with multirun-specific variables.
		"""
		# Find the required Slug URL for this category extension board,
		# then resolve the slug to find the game object.
		mr_slug = self.resolve_multirun_game_slug(base_game)
		slug_id = mr_slug.get("id", None)
		game_obj = self.utils.get_game_code(slug_id)
		if game_obj is None:
			raise ValueError(f"Could not find the game `{base_game}`. Check for typos and try again.")

		# Find the leaderboard config for this category.
		slug_id = mr_slug.get("id")
		cfg = self.lb_config.get(slug_id)
		if cfg is None:
			raise ValueError(f"No leaderboard config found for Multirun game slug: {slug_id}")

		# Category metadata is necessary for Multiruns: if nothing is found, or the
		# Multirun category cannot be found in the configuration, return an error.
		mr_categories_cfg = cfg.get("categories", {})
		if mr_category not in mr_categories_cfg:
			raise ValueError(f"Unknown Multirun category key: {mr_category}")

		# Using the CE Category config, search the SRDC Game categories
		# list to find the matching board name.
		category_meta = mr_categories_cfg[mr_category]
		category_obj = None
		for cat in game_obj.categories:
			if cat.name == category_meta["board"]:
				category_obj = cat
				break

		# If category_obj is still None, then the category does not exist.
		if not category_obj:
			raise ValueError("Multirun category not found in Multirun game")

		# Resolve the user ID, capture the category vars and then search for runs.
		user_id = self.utils.get_user_id(player)
		mr_cat_vars = category_meta.get("variables", [])
		runs = self.search_runs(game_obj.id, category_obj.id, user_id, mr_cat_vars)
		if not runs:
			return None

		# Sort the runs by the most recently verified run (newest at the top).
		runs.sort(key=lambda rx: rx["submitted"], reverse=True)

		# Unlike category extensions, multi-runs tends to have very few sub-boards
		# However, as they're still a form of category extension, we do need to ensure
		# all returned runs are filtered to get the correct run that the user asked for.
		required_variables = {var["var_id"].split("-")[-1]: var["value_id"] for var in mr_cat_vars}
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

		# The only run that we have is the one that the user asked form.
		# Lookup the placement and extract run data, using the same helper as normal runs
		best_run = filtered_runs[0]
		place = self.utils.lookup_run_place(game_obj.id, category_obj.id, best_run["id"], required_variables)
		sr = self.utils.extract_run(best_run, player)
		sr.place = place
		return sr
