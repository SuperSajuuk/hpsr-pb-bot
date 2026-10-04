#
# World Records
#
# This code processes run objects connected to World Record lookup.
# A lot of this is similarly to standard boards, except that the goal
# is only to return a world record. All code here is self-contained within
# here, but modified from standard boards.
from utils.model import SpeedRun
from utils.exceptions import InvalidGame, InvalidCategory, InvalidPlatform, UnsupportedGame


# WorldRecords
# This handles the logic of querying the SRDC
# API for world records. Currently, this only
# handles WR's in !run, but the !il lookup will
# move here once I know what bits to include.
class WorldRecords:
	def __init__(self, srdc_api, api, game_map, platform_map, plat_category_map, category_map, board_slugs, md_aliases, utils):
		self.srdc = srdc_api
		self.api = api
		self.game_map = game_map
		self.platform_map = platform_map
		self.plat_cat_map = plat_category_map
		self.category_map = category_map
		self.board_slugs = board_slugs
		self.md_aliases = md_aliases
		self.utils = utils

	def lookup_wr_run(self, game_id: str, category_id: str, variables: list = None):
		"""
		Calls the SRDC API to find the specific world record run.

		Returns either an empty list (with no runs) or a list containing
		just the requested run.
		"""
		base_q = f"leaderboards/{game_id}/category/{category_id}?embed=players&top=1"
		if variables:
			for var in variables:
				for var_id, var_value in var.items():
					base_q += f"&var-{var_id}={var_value}"

		return self.srdc.get(base_q)

	def lookup_world_record_run(self, slug: str, game_id: str, category_id: str, internal_key: str, int_name: str, flags: dict | None) -> SpeedRun | None:
		"""
		Look up the current world record in a specific game/category.
		Uses SRDC variable filters and client-side filtering to ensure only the run the
		user requested is returned (this is due to the way SRDC returns runs from the API).

		Unlike lookup_run(), this method doesn't accept player data, and uses the run object
		returned by SRDC to fill out the required run data.
		"""
		# Capture any variables if needed.
		cfg = self.utils.resolve_leaderboard_config(slug, internal_key, int_name)
		cfg_2 = None
		if cfg is not None:
			cfg_2 = cfg.get(int_name, None)

		# Check if either cfg or cfg_2 contains a variables key.
		# If so, capture all variables and build a var_filters list
		# for use in the query.
		var_filters = None
		if (cfg and "variables" in cfg) or (cfg_2 and "variables" in cfg_2):
			var_filters = self.utils.generate_var_filters(cfg, flags, cfg_2)

		# With the provided data, search SRDC for runs.
		# If nothing there, just return None.
		run = self.lookup_wr_run(game_id, category_id, var_filters)
		if not run:
			return None

		# This doesn't need to be sorted, nor do we need to find run placement, as the
		# parameters ensure only one run will be returned, which will be the world record.
		# Just return this run from the data given.
		sr = self.utils.extract_run(run["runs"][0]["run"], run["players"]["data"][0]["names"]["international"])
		return sr
