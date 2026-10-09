#
# Personal Bests
#
# This code processes a Personal Best object. A Personal Best is
# a speedrun assigned to a specific user which is their "best" submission.
#
# In many respects, this is the same as looking up a normal run through
# the /run/ route. However, as there can be many hundreds of PBs returned
# by the endpoint on SRDC, this is often slower because it has to be
# heavily filtered. In normal cases, it is better to look up runs directly
# using the /run/ route.
from utils.model import SpeedRun
from utils.exceptions import InvalidCategory, MissingInternalData
import datetime


# PersonalBest
# This handles the logic of querying the SRDC
# API for a Personal Best from a single user.
# This is used by !pb only.
class PersonalBest:
	def __init__(self, api, utils):
		self.api = api
		self.utils = utils

	def find_pbs(self, player: str, pbs: list, category_id: str, var_filters=None):
		"""
		Takes a list of PB run objects returned by speedrun.com and
		only returns the PBs that meet conditions.

		If there are matches, the results list will contain SpeedRun objects.
		If no PB matches, the list will be empty.
		"""
		results = []
		for entry in pbs:
			# Check for a category match: if none, continue.
			run = entry["run"]
			if run["category"] != category_id:
				continue

			# If any variable filters are provided, use them to check for
			# additional filtering.
			all_match = True
			if var_filters is not None:
				for x in var_filters:
					for key, val in x.items():
						if run["values"].get(key) != val:
							all_match = False
							break
					if not all_match:
						break

			# Append the PB result to the list if all variables matched.
			if all_match:
				results.append(self.utils.extract_run(run, player, entry["place"]))

		return results

	def lookup_pb(self, slug: str, cat_cfg: dict, category_name: str, player: str, flags: dict | None) -> SpeedRun | None:
		"""
		Look up the most recent Personal Best for a player in a specific game/category.
		Any var filters stored for the specific game in the leaderboard config are used
		to perform client-side filtering, ensuring only the requested PB is returned.
		"""
		# Slug should not be None, because it would have been determined from
		# before this function was invoked.
		if slug is None:
			raise MissingInternalData("An error has occurred with an internal function: the slug URL couldn't be found for this combination of inputs.")

		# Pull game object, then find the category on SRDC.
		game_id, game_cats = self.api.get_game_code(slug)
		category_id = None
		for cat_id, cat_name in game_cats.items():
			if cat_name == category_name:
				category_id = cat_id
				break

		# Raise ValueError if the category object does not exist for this game.
		if not category_id:
			raise InvalidCategory("The category name obtained from the category key could not be mapped to a valid speedrun.com category for this game.")

		# Fetch PBs for this player based on this game ID.
		pbs = self.api.search_pbs(player, game_id)

		# Pull in all relevant config data, build var filters
		# then filter all PBs to find the requested one.
		var_filters = None
		if cat_cfg and cat_cfg.get("variables", None):
			var_filters = self.utils.generate_var_filters(cat_cfg["variables"], flags)

		# Find the PB from the list and then return None if nothing found.
		result = self.find_pbs(player, pbs, category_id, var_filters)
		if not result:
			return None

		# Return this PB run.
		return result[0]
