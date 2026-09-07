#
# Normal Run Configs
#
# This file contains all the constants used for
# handling Normal runs (ie main boards: not CE's
# or multi-runs)
#

# Game mapping. This is used to define all known games that exist in the bot.
GAME_MAP = {
	# Harry Potter
	"hp1": "Harry Potter and the Philosopher's Stone",
	"hp2": "Harry Potter and the Chamber of Secrets",
	"hp3": "Harry Potter and the Prisoner of Azkaban",
	"hp4": "Harry Potter and the Goblet of Fire",
	"hp5": "Harry Potter and the Order of the Phoenix",
	"hp6": "Harry Potter and the Half Blood Prince",
	"hp7.1": "Harry Potter and the Deathly Hallows Part 1",
	"hp7.2": "Harry Potter and the Deathly Hallows Part 2",

	# Selection of other games. Extend appropriately.
	"dbb": "Disney's Brother Bear",

	# Generic game maps (these may be removed in the future)
	"ce": "Category Extensions",
	"multi": "Multiruns"
}

# Map abbreviations passed by users to human-readable names.
# CATEGORY_MAP is for main boards, CE_CATEGORY_MAP is for the
# defined Category Extensions board, and MULTIRUN_CATEGORY_MAP
# is for the defined Multi Run board.
CATEGORY_MAP = {
	"any": "Any%",
	"100": "100%",
	"glitchless": "Glitchless",
	"gless": "Glitchless",
	"nms": "No Major Skips",
	"noeds": "Any% No EDS",
	"awc": "All Wizard Cards",
	"warpless": "Warpless"
}