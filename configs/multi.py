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
	"hp": {"name": "Harry Potter Multiruns", "id": "hpmulti"},
	"rac": {"name": "Multiple Ratchet & Clank Games", "id": "racmulti"}
}

# Sub-category mapping.
# This refers to the second board under the top level board.
SUB_CATEGORY_MAP = {
	"any": "Any%",
	"100": "100%",
	"hundo": "100%",
	"awc": "All Wizard Cards",
	"nms": "No Major Skips"
}

# Board aliases. Useful if you want multiple
# user input choices to display the appropriate label.
BOARD_ALIASES = {
	"pctri": "PC Trifecta",
	"pctrifecta": "PC Trifecta",
	"7pcduo": "7PC Duofecta",
	"7pcduofecta": "7PC Duofecta",
	"ps1duo": "PS1 Duofecta",
	"ps1duofecta": "PS1 Duofecta",
	"pcocto": "PC Octofecta",
	"pcoctofecta": "PC Octofecta",
	"6thgentri": "6th Gen Trifecta",
	"6thgentrifecta": "6th Gen Trifecta",
	"gcntri": "6th Gen Trifecta",
	"gcntrifecta": "6th Gen Trifecta",
	"xboxtri": "6th Gen Trifecta",
	"xboxtrifecta": "6th Gen Trifecta",
	"ps2tri": "6th Gen Trifecta",
	"ps2trifecta": "6th Gen Trifecta"
}

# Board token aliases.
# This is used to map user input to the name that
# is used internally to reference a specific
# top-level board for a multi-run.
BOARD_TOKEN_ALIASES = {
	"hpmulti": {
		"pctrifecta": "pctri",
		"7pcduofecta": "7pcduo",
		"pcoctofecta": "pcocto",
		"ps1duofecta": "ps1duo",
		"6thgentrifecta": "6thgentri",
		"gcntri": "6thgentri",
		"gcntrifecta": "6thgentri",
		"xboxtri": "6thgentri",
		"xboxtrifecta": "6thgentri",
		"ps2tri": "6thgentri",
		"ps2trifecta": "6thgentri",
		"gbcduofecta": "gbcduo",
		"gbapentafecta": "gbapenta",
		"hhoctofecta": "hhocto",
		"handheldoctofecta": "hhocto",
		"fullseries": "fs"
	}
}

# Category aliases
# Like board aliases, this is used to map user input
# to the name that is used internally to reference
# a specific sub-board for a category extension.
CATEGORY_ALIASES = {
	"hpmulti": {
		"pctri": {"any": "any", "100": "100", "hundo": "100", "awc": "awc", "allwizardcards": "awc"},
		"7pcduo": {"any": "any", "100": "100", "hundo": "100"},
		"pcocto": {"any": "any", "100": "100", "hundo": "100"},
		"ps1duo": {"any": "any", "100": "100", "hundo": "100", "nms": "nms", "nomajorskips": "nms"},
		"6thgentri": {"any": "any", "100": "100", "hundo": "100"},
		"gbcduo": {"any": "any", "100": "100", "hundo": "100"},
		"gbapenta": {"any": "any", "100": "100", "hundo": "100"},
		"hhocto": {"any": "any", "100": "100", "hundo": "100"},
		"fs": {"any": "any", "100": "100", "hundo": "100"}
	}
}