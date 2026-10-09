#
# Multi Run Configs
#
# This file contains all the constants used for
# handling Multi Runs.
#

# Game mapping.
# The key name should be the series that has a multirun board.
# The value of each key is a dictionary which contains two
# keys: a human-readable name and the Slug URL ID.
GAME_MAP = {
	"hp": {"name": "Harry Potter Multiruns", "aliases": ["hpmultirun", "hpmultiruns"], "id": "hpmulti"},
	"rac": {"name": "Multiple Ratchet & Clank Games", "aliases": ["racmultirun", "racmultiruns"], "id": "racmulti"}
}

# Sub-category mapping.
# This refers to the second board under the top level board.
SUB_CATEGORY_MAP = {
	"Any%": {"aliases": ["any", "any%"], "internal_name": "any"},
	"100%": {"aliases": ["100", "hundo", "100%"], "internal_name": "100"},
	"All Wizard Cards": {"aliases": ["awc", "allwizardcards"], "internal_name": "awc"},
	"No Major Skips": {"aliases": ["nms", "nomajorskips"], "internal_name": "nms"}
}

# Board aliases. The key name must be the alias name to display:
# the value of each key is a list of string aliases to be checked.
BOARD_ALIASES = {}

# Category aliases
# Like board aliases, this is used to map user input
# to the name that is used internally to reference
# a specific sub-board for a category extension.
CATEGORY_ALIASES = {
	"hpmulti": {
		"pctri": {
			"any": ["any", "any%"],
			"100": ["100", "hundo", "100%"],
			"awc": ["awc", "wizardcards", "allwizardcards"]
		},
		"7pcduo": {
			"any": ["any", "any%"],
			"100": ["100", "hundo", "100%"],
		},
		"pcocto": {
			"any": ["any", "any%"],
			"100": ["100", "hundo", "100%"]
		},
		"ps1duo": {
			"any": ["any", "any%"],
			"100": ["100", "hundo", "100%"],
			"nms": ["nms", "nomajorskips"]
		},
		"6thgentri": {
			"any": ["any", "any%"],
			"100": ["100", "hundo", "100%"]
		},
		"gbcduo": {
			"any": ["any", "any%"],
			"100": ["100", "hundo", "100%"]
		},
		"gbapenta": {
			"any": ["any", "any%"],
			"100": ["100", "hundo", "100%"]
		},
		"hhocto": {
			"any": ["any", "any%"],
			"100": ["100", "hundo", "100%"]
		},
		"fs": {
			"any": ["any", "any%"],
			"100": ["100", "hundo", "100%"]
		}
	}
}
