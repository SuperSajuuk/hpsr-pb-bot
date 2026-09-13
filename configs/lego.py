#
# LEGO Main Board Configs
#
# This file contains all the constants used for
# handling LEGO Games' main boards.
#

# Sub-board token matches
# This is just a list of strings to see if the token
# for extract_flags is a match to something here.
FLAG_TOKEN_MATCHES = ["solo", "co-op", "coop", "nocut5", "n0cut5", "standard", "unrestricted", "restricted"]

# Game mapping.
# Key names must be abbreviations that would be called in !run lego
# commands. The value of key is a dictionary which contains two
# keys: a human-readable name and the Slug URL ID.
GAME_MAP = {
	"hp14": {"name": "LEGO Harry Potter Years 1-4", "slug": "lhp1_4"},
	"hp57": {"name": "LEGO Harry Potter Years 5-7", "slug": "lhp5_7"}
}

# Board aliases. Useful if you want multiple
# user input choices to display the appropriate label.
BOARD_ALIASES = {
	"hp14": {
		"Any%": ["any"],
		"No Levels Early": ["nle", "noearly", "noearlylevels", "nolevelsearly"],
		"Free Play": ["fp", "freeplay"],
		"Replay Story": ["rs", "replay", "replaystory"],
		"All Crests": ["ac", "allcrests"],
		"100%": ["100", "hundo"]
	},
	"hp57": {
		"Any%": ["any"],
		"No Levels Early": ["nle", "noearly", "noearlylevels", "nolevelsearly"],
		"Free Play": ["fp", "freeplay"],
		"Replay Story": ["rs", "replay", "replaystory"],
		"All Crests": ["ac", "allcrests"],
		"100%": ["100", "hundo"]
	}
}

# Board token aliases.
# This is used to map user input to the name that
# is used internally to reference a specific
# top-level board for a category extension.
BOARD_TOKEN_ALIASES = {
	"lhp1_4": {
		"nle": ["noearly", "noearlylevels", "nolevelsearly"],
		"fp": ["freeplay"],
		"replay": ["rs", "replaystory"],
		"ac": ["allcrests"],
		"100": ["hundo"]
	},
	"lhp5_7": {
		"nle": ["noearly", "noearlylevels", "nolevelsearly"],
		"freeplay": ["fp"],
		"replay": ["rs", "replaystory"],
		"ac": ["allcrests"],
		"100": ["hundo"]
	},
}

# Category aliases
# Like board aliases, this is used to map user input
# to the name that is used internally to reference
# a specific sub-board.
CATEGORY_ALIASES = {
	"hp14": {
		"any": {"solo": "solo", "coop": "coop", "co-op": "coop"},
		"nle": {"solo": "solo", "coop": "coop", "co-op": "coop"},
		"freeplay": {"solo": "solo", "coop": "coop", "co-op": "coop"},
		"replay": {"solo": "solo", "coop": "coop", "co-op": "coop"},
		"allcrests": {"solo": "solo", "coop": "coop", "co-op": "coop"},
		"100": {"solo": "solo", "coop": "coop", "co-op": "coop"}
	},
	"hp57": {
		"any": {"solo": "solo", "coop": "coop", "co-op": "coop"},
		"nle": {"solo": "solo", "coop": "coop", "co-op": "coop"},
		"freeplay": {"solo": "solo", "coop": "coop", "co-op": "coop"},
		"replay": {"solo": "solo", "coop": "coop", "co-op": "coop"},
		"allcrests": {"solo": "solo", "coop": "coop", "co-op": "coop"},
		"100": {"solo": "solo", "coop": "coop", "co-op": "coop"}
	}
}

# Sub-category aliases
# Similar to board aliases, but allows better printing of
# the primary sub-category.
SUB_CATEGORY_ALIASES = {
	"hp14": {
		"Solo": ["solo"],
		"Co-Op": ["coop", "co-op"],
		"N0CUT5": ["nocut5", "n0cut5"],
		"Standard": ["standard"]
	},
	"hp57": {
		"Solo": ["solo"],
		"Co-Op": ["coop", "co-op"],
		"N0CUT5": ["nocut5", "n0cut5"],
		"Standard": ["standard"],
		"Unrestricted": ["unrestricted"],
		"Restricted": ["restricted"]
	}
}