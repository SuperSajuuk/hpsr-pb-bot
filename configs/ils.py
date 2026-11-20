#
# IL Config Importer
#
# This config file contains the various constants used to create the
# IL board maps.
#
# As these configuration keys expand over time and more functionality is
# moved from catch-all config files to relevant locations, this helps
# ensure that all config data can be stored in a more structured manner.
#
# The game map keys are defined on their overall mapping: a specific key
# is used.
#
import importlib
import pkgutil
import configs.il_cfg as ind_lvl

# Import the relevant config from the source files.
NM_LEVELS_MAP = {}
MISC_LEVELS_MAP = {}
for _, module_name, _ in pkgutil.iter_modules(ind_lvl.__path__):
	# Import the module and check for the IL_MAPPING.
	# This must always be defined, so if its missing, skip it.
	module = importlib.import_module(f"{ind_lvl.__name__}.{module_name}")
	data = getattr(module, "IL_MAPPING", None)
	if not data:
		continue

	# Capture the IL_CATEGORY key to see which dictionary it should be
	# added to. There's an expectation of this always existing, but if
	# not, skip it.
	root_key = getattr(module, "IL_CATEGORY", None)
	if root_key is None:
		continue

	# Set the target to whatever value exists for root_key.
	# We do a de-duplication later and then add to the relevant
	# config.
	match root_key:
		case "nm":
			target = NM_LEVELS_MAP
		case "misc":
			target = MISC_LEVELS_MAP
		case _:
			continue

	# Check for a duplicate and raise a RuntimeError if found.
	for key in data:
		if key in target:
			raise RuntimeError(f"Duplicate game key detected in {root_key}: {key}")

	# Append the contents of the IL_MAPPING to the relevant
	# target dictionary.
	target.update(data)
