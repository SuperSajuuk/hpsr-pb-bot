# Category Extension Run
#
# This code processes a Category Extension Run object. A CE run is
# defined as a run belonging to a defined Category Extension board:
# such boards have the "Category Extension" tag on them. Should a
# user provide a game which we do not have a hard-coded value for,
# the system will look up SRDC and then fail if no board exists.
from model import SpeedRun
import datetime
import config
from typing import Any, Dict


# CategoryExtension
# This handles the logic of querying the SRDC
# API for a category extension run submission.
# This is used by !run only.
class CategoryExtension:
	def __init__(self, api, game_map, platform_map, board_aliases, category_map, utils):
		self.api = api
		self.game_map = game_map
		self.board_aliases = board_aliases
		self.platform_map = platform_map
		self.category_map = category_map
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

	# Resolve the Game Slug for a CE
	# Using just the game code provided, check our
	# local config for that code. If it's not there,
	# query SRDC and ensure it does have the category
	# extension tag.
	def resolve_ce_game_slug(self, base_game: str) -> str:
		"""
		Resolve the Game Slug for a Category Extension

		If possible, rely on local config data before querying SRDC.
		If we don't have a config key for this, query SRDC and ensure
		the game does have the Category Extension game type assigned.

		Raises ValueError if no such game is found.
		"""
		# Check if the base game key is already in the game map.
		# Use it first before querying SRDC.
		if base_game in self.game_map:
			return self.game_map[base_game]

		# Couldn't find it in our hard-coded list, so
		# query SRDC for the specific game that is needed. We also have to
		# query the
		search = self.api.get(f"games?abbreviation={base_game}&embed=tags")
		if search is None:
			# If not found by the abbreviation, try searching on the name.
			# If still not found, raise ValueError.
			search = self.api.get(f"games?name={base_game}&embed=tags")
			if search is None:
				raise ValueError(f"No Category Extension game found for base game: {base_game}")

		# Parse the game object for the relevant tag.
		# This is hard-coded because category extension is
		# always the same and doesn't change.
		game = search[0]
		is_ce = False
		for tag in game["gametypes"]:
			if tag == "53no817x":
				is_ce = True
				break

		# Error here, because the required tag cannot be found.
		if not is_ce:
			raise ValueError(f"No Category Extension game found for base game: {base_game}")

		# Return the game object for this category extension board.
		return game

	def lookup_ce_run(self, base_game: str,	ce_category: str, player: str, flags: dict) -> SpeedRun | None:
		"""
		Resolve and fetch a Category Extensions run using the same SRDC logic as normal runs,
		but with CE-specific variables.
		"""
		# Find the required Slug URL for this category extension board,
		# then resolve the slug to find the game object.
		ce_slug = self.resolve_ce_game_slug(base_game)
		slug_id = ce_slug.get("id", None)
		game_obj = self.utils.get_game_code(slug_id)
		if game_obj is None:
			raise ValueError(f"Could not find the game `{base_game}`. Check for typos and try again.")

		# Find the leaderboard config for this category.
		slug_id = ce_slug.get("id")
		cfg = config.LEADERBOARD_CONFIG.get(slug_id)
		if cfg is None:
			raise ValueError(f"No leaderboard config found for CE game slug: {slug_id}")

		# Category metadata is necessary for CEs: if nothing is found, or the
		# CE category cannot be found in the configuration, return an error.
		ce_categories_cfg = cfg.get("categories", {})
		if ce_category not in ce_categories_cfg:
			raise ValueError(f"Unknown CE category key: {ce_category}")

		# Using the CE Category config, search the SRDC Game categories
		# list to find the matching board name.
		category_meta = ce_categories_cfg[ce_category]
		category_obj = None
		for cat in game_obj.categories:
			if cat.name == category_meta["board"]:
				category_obj = cat
				break

		# If category_obj is still None, then the category does not exist.
		if not category_obj:
			raise ValueError("CE category not found in CE game")

		# Resolve the user ID, capture the category vars and then search for runs.
		user_id = self.utils.get_user_id(player)
		ce_cat_vars = category_meta.get("variables", [])
		runs = self.search_runs(game_obj.id, category_obj.id, user_id, ce_cat_vars)
		if not runs:
			return None

		# Sort the runs by the most recently verified run (newest at the top).
		runs.sort(key=lambda rx: rx["submitted"], reverse=True)

		# Because CE's contain a lot of sub-boards, the ce_cat_vars will return a lot
		# of additional runs. The list of runs must be filtered to get the correct
		# run that the user asked for.
		required_variables = {var["var_id"].split("-")[-1]: var["value_id"] for var in ce_cat_vars}
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
