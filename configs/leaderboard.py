#
# Leaderboard Config Importer
#
# This config file contains just one constant: LEADERBOARD_CONFIG
# It is used to handle a lot of the leaderboard requirements around
# variable IDs, value IDs and other filtering.
#
# Due to the size of all these dictionaries, leaderboard config data
# is stored in loose files under the leaderboards sub-folder. The code
# below is designed to import all leaderboard data and store them in a
# dynamically populated LEADERBOARD_CONFIG constant.
#
import importlib
import pkgutil
import configs.leaderboards as leaderboards

# Import leaderboard config from the source files.
LEADERBOARD_CONFIG = {}
for _, module_name, _ in pkgutil.iter_modules(leaderboards.__path__):
	module = importlib.import_module(f"{leaderboards.__name__}.{module_name}")
	data = getattr(module, "LEADERBOARD_DATA", None)
	if not data:
		continue

	# Check if there is a root key. If there is, add the config data
	# to that: otherwise, just add all data directly into the config.
	root_key = getattr(module, "ROOT_KEY", None)
	if root_key is not None:
		# Don't add this entry if it's already there.
		if root_key in LEADERBOARD_CONFIG:
			raise RuntimeError(f"Duplicate leaderboard key detected: {root_key}")
		LEADERBOARD_CONFIG[root_key] = data
		continue

	# No root key, just do a check for dupes and add onto the dict.
	for key in data:
		if key in LEADERBOARD_CONFIG:
			raise RuntimeError(f"Duplicate leaderboard key detected: {key}")
	LEADERBOARD_CONFIG.update(data)

# Build a set of all aliases representing category extensions.
# This is needed to support extract_flags for token matching.
CE_TOKEN_LOOKUP = set()
for cfg in LEADERBOARD_CONFIG.values():
	sub_cats = cfg.get("sub_categories", None)
	if not sub_cats:
		continue
	for aliases in sub_cats.values():
		if not isinstance(aliases, list):
			continue
		CE_TOKEN_LOOKUP.update(aliases)
