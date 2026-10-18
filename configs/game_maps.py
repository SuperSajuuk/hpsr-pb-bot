#
# Game Mapping Config Importer
#
# This config file contains the various constants used to create the
# game maps for each aspect of the program.
#
# As these configuration keys expand over time and more functionality is
# moved from catch-all config files to relevant locations, this helps
# ensure that all config data can be stored in a more structured manner.
#
# The game map keys are defined on their overall mapping: a specific key
# is used
#
import importlib
import pkgutil
import configs.games as games

# Import game map config from the source files.
NM_GAME_MAP = {}
CC_GAME_MAP = {}
CE_GAME_MAP = {}
MR_GAME_MAP = {}
LEGO_GAME_MAP = {}
for _, module_name, _ in pkgutil.iter_modules(games.__path__):
	# Import the module and check for the GAME_MAP_DATA.
	# This must always be defined, so if its missing, skip it.
	module = importlib.import_module(f"{games.__name__}.{module_name}")
	data = getattr(module, "GAME_MAP_DATA", None)
	if not data:
		continue

	# Capture the GAME_CONFIG key to see which dictionary it should be
	# added to. There's an expectation of this always existing, but if
	# not, skip it.
	root_key = getattr(module, "GAME_CONFIG", None)
	if root_key is None:
		continue

	# Set the target to whatever value exists for root_key.
	# We do a de-duplication later and then add to the relevant
	# config.
	match root_key:
		case "ce":
			target = CE_GAME_MAP
		case "mr":
			target = MR_GAME_MAP
		case "cc":
			target = CC_GAME_MAP
		case "lego":
			target = LEGO_GAME_MAP
		case "nm":
			target = NM_GAME_MAP
		case _:
			continue

	# Check for a duplicate and raise a RuntimeError if found.
	for key in data:
		if key in target:
			raise RuntimeError(f"Duplicate game key detected in {root_key}: {key}")

	# Append the contents of the GAME_MAP_DATA to the relevant
	# target dictionary.
	target.update(data)
