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
	"dbb": "Disney's Brother Bear"
}

# Map abbreviations passed by users to human-readable names.
# This is just for main boards: for CE's and Multiruns, use
# the ce.py and multi.py files under the configs folder.
CATEGORY_MAP = {
	"Any": ["any"],
	"100%": ["100", "hundo"],
	"Glitchless": ["gless", "glitchless"],
	"No Major Skips": ["nms", "nomajorskips"],
	"Any% No EDS": ["noeds", "anynoeds"],
	"All Wizard Cards": ["awc", "allwizardcards"],
	"Warpless": ["warpless"]
}

# Board slug mapping. This is used to map the values produced by
# concatenating platform and game in the code. The ordering of the
# keys is to ensure they are grouped by platform commonalities for
# easier reading.
BOARD_GAME_SLUG = {
	"hp1_ps1": "hp1ps1",
	"hp2_ps1": "hp2ps1",
	"hp1_pc": "hp1pc",
	"hp2_pc": "hp2pc",
	"hp3_pc": "hp3pc",
	"hp4_pc": "hp4",
	"hp5_pc": "hp5",
	"hp6_pc": "hp6",
	"hp7.1_pc": "hp7p1",
	"hp7.2_pc": "hp7p2",
	"hp1_ps2": "hp1_6th_gen",
	"hp2_ps2": "hp2ps2",
	"hp3_ps2": "hp3_6th_gen",
	"hp4_ps2": "hp4",
	"hp5_ps2": "hp5",
	"hp6_ps2": "hp6",
	"hp1_xbox": "hp1_6th_gen",
	"hp2_xbox": "hp2_6th_gen",
	"hp3_xbox": "hp3_6th_gen",
	"hp4_xbox": "hp4",
	"hp5_xbox": "hp5",
	"hp6_xbox": "hp6",
	"hp7.1_xbox": "hp7p1",
	"hp7.2_xbox": "hp7p2",
	"hp1_gcn": "hp1_6th_gen",
	"hp2_gcn": "hp2_6th_gen",
	"hp3_gcn": "hp3_6th_gen",
	"hp4_gcn": "hp4",
	"hp1_gba": "hp1gba",
	"hp2_gba": "hp2gba",
	"hp3_gba": "hp3gba",
	"hp4_gba": "hp4gba",
	"hp5_gba": "hp5gbads",
	"hp1_gbc": "hp1gbc",
	"hp2_gbc": "hp2gbc",
	"hp4_ds": "hp4gba",
	"hp5_ds": "hp5gbads",
	"hp6_ds": "hp6ds",
	"hp7.1_ds": "hp7p1ds",
	"hp7.2_ds": "hp7p2ds"
}
