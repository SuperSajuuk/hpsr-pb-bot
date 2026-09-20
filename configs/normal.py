#
# Normal Run Configs
#
# This file contains all the constants used for
# handling Normal runs (ie main boards: not CE's
# or multi-runs)
#

# Game mapping.
# This is used for main boards that have no separate
# handler.
GAME_MAP = {
	# Harry Potter
	"hp1": {"name": "Harry Potter and the Philosopher's Stone"},
	"hp2": {"name": "Harry Potter and the Chamber of Secrets"},
	"hp3": {"name": "Harry Potter and the Prisoner of Azkaban"},
	"hp4": {"name": "Harry Potter and the Goblet of Fire"},
	"hp5": {"name": "Harry Potter and the Order of the Phoenix"},
	"hp6": {"name": "Harry Potter and the Half Blood Prince"},
	"hp7.1": {"name": "Harry Potter and the Deathly Hallows Part 1", "aliases": ["hp71", "hp7p1"]},
	"hp7.2": {"name": "Harry Potter and the Deathly Hallows Part 2", "aliases": ["hp72", "hp7p2"]},
	"qwc": {"name": "Harry Potter: Quidditch World Cup", "aliases": ["hpqwc"]},
	"legacy": {"name": "Hogwarts Legacy", "aliases": ["hl", "hogwartslegacy"]},

	# Selection of other games. Extend appropriately.
	"dbb": {"name": "Disney's Brother Bear", "aliases": ["disneysbrotherbear", "brotherbear"]},
	"r3": {"name": "Rayman 3: Hoodlum Havoc", "aliases": ["rayman3"], "unsupported": True}
}

# Map abbreviations passed by users to human-readable names.
# This is just for main boards: for CE's and Multiruns, use
# the ce.py and multi.py files under the configs folder.
CATEGORY_MAP = {
	"Any%": ["any", "any%"],
	"100%": ["100", "hundo", "100%"],
	"Glitchless": ["gless", "glitchless"],
	"No Major Skips": ["nms", "nomajorskips", "any%nms", "any%nomajorskips"],
	"No Major Glitches": ["nmg", "nomajorglitches", "any%nmg", "any%nomajorglitches"],
	"Any% No EDS": ["noeds", "anynoeds", "any%noeds"],
	"All Wizard Cards": ["awc", "wizardcards", "allwizardcards"],
	"All Requirements": ["allreq", "allreqs", "requirements", "allrequirements"],
	"All Crests": ["ac", "crests", "allcrests"],
	"Warpless": ["wl", "warpless"],
	"Boostless": ["bl", "boostless"],
	"All Shields": ["as", "shields", "allshields"],
	"Beat Hogwarts Cup": ["bhc", "hogwarts", "hogwartscup", "beathogwarts", "beathogwartscup"],
	"Beat World Cup": ["bwc", "world", "worldcup", "beatworld", "beatworldscup"],
	"Beat the Tutorial": ["btt", "tutorial", "beattutorial", "beatthetutorial"],
	"NG+": ["ng", "ngplus", "newgameplus", "ng+"],
	"Kill Ranrok": ["ranrok", "killranrok"],
	"All Quests": ["aq", "quests", "allquests"],
	"Glitched": ["glitched"],
	"All Teensies": ["at", "allteensies"],
	"No Teensies": ["not", "noteensies"]
}

# Board slug mapping. This is used to map the values produced by
# concatenating platform and game in the code.
#
# There should be one key for each board slug: its value should be
# a list of all internal keys that represent it.
BOARD_GAME_SLUG = {
	"hp1ps1": ["hp1_ps1"],
	"hp2ps1": ["hp2_ps1"],
	"hp1pc": ["hp1_pc"],
	"hp2pc": ["hp2_pc"],
	"hp3pc": ["hp3_pc"],
	"hp4": ["hp4_pc", "hp4_ps2", "hp4_xbox", "hp4_gcn"],
	"hp5": ["hp5_pc", "hp5_ps2", "hp5_ps3", "hp5_xbox", "hp5_x360", "hp5_wii"],
	"hp6": ["hp6_pc", "hp6_ps2", "hp6_ps3", "hp6_xbox", "hp6_x360", "hp6_wii"],
	"hp7p1": ["hp7.1_ps3", "hp7.1_xbox", "hp7.1_pc", "hp7.1_wii"],
	"hp7p2": ["hp7.2_ps3", "hp7.2_xbox", "hp7.2_pc", "hp7.2_wii"],
	"hp1_6th_gen": ["hp1_ps2", "hp1_xbox",	"hp1_gcn"],
	"hp2ps2": ["hp2_ps2"],
	"hp3_6th_gen": ["hp3_ps2", "hp3_xbox", "hp3_gcn"],
	"hp2_6th_gen": ["hp2_xbox", "hp2_gcn"],
	"hp1gba": ["hp1_gba"],
	"hp2gba": ["hp2_gba"],
	"hp3gba": ["hp3_gba"],
	"hp4gba": ["hp4_gba", "hp4_ds"],
	"hp5gbads": ["hp5_gba", "hp5_ds"],
	"hp1gbc": ["hp1_gbc"],
	"hp2gbc": ["hp2_gbc"],
	"hp6ds": ["hp6_ds"],
	"hp7p1ds": ["hp7.1_ds"],
	"hp7p2ds": ["hp7.2_ds"],
	"hpquidditch": ["qwc_pc", "qwc_ps2", "qwc_gcn",	"qwc_xbox"],
	"quidditch_gba": ["qwc_gba"],
	"disneys_brother_bear": ["dbb_pc"],
	"hpcc": ["hp2_cc"],
	"legacy": ["legacy_pc", "legacy_ps4", "legacy_ps5"],
	"r3": ["r3_gcn", "r3_ps3", "r3_x360", "r3_ps2", "r3_pc"]
}

# Additional metadata aliases
# Converts the value of the key_1 key in the additional
# metadata to a human-readable value. Very small list for
# a rare number of instances
METADATA_ALIASES = {
	"Story": ["story"],
	"Hard": ["hard"],
	"1 Player": ["1p", "1player"],
	"2 Players": ["2p", "2players"],
	"3 Players": ["3p", "3players"]
}
