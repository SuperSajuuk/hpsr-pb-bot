#
# Custom Content Configs
#
# This file contains all the constants used for
# handling Custom Content categories.
#

# Game mapping.
# Key names must be abbreviations that would be called in !run cc
# commands. The value of key is a dictionary which contains two
# keys: a human-readable name and the Slug URL ID.
GAME_MAP = {
	"hp": {"name": "Harry Potter Custom Content", "id": "hpcc"}
}

# Category aliases
# Like board aliases, this is used to map user input
# to the name that is used internally to reference
# a specific sub-board for custom content.
CATEGORY_ALIASES = {
	"hpcc": {
		"fm": {
			"any": ["any", "any%"],
			"100": ["100", "hundo", "100%"],
			"gless": ["gl", "gless", "glitchless"]
		},
		"rs": {
			"any": ["any", "any%"],
			"gless": ["gl", "gless", "glitchless"]
		},
		"1tc": {
			"any": ["any", "any%"],
			"gless": ["gl", "gless", "glitchless"],
			"awc": ["awc", "wizardcards", "allwizardcards"]
		},
		"bingo": {
			"single": ["single"],
			"triple": ["triple"],
			"blackout": ["bo", "bout", "blackout"]
		},
		"2tc": {
			"gless": ["gl", "gless", "glitchless"],
			"awc": ["awc", "wizardcards", "allwizardcards"],
			"wl": ["wl", "wless", "warpless"]
		}
	}
}
