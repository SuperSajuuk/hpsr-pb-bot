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
	"r1": {"name": "Rayman", "ordering": "pf", "aliases": ["rayman", "rayman1"]},
	"r3": {"name": "Rayman 3: Hoodlum Havoc", "ordering": "pf", "aliases": ["rayman3"]},
	"ssbfbbr": {"name": "SpongeBob SquarePants: Battle for Bikini Bottom - Rehydrated", "ordering": "pf", "aliases": ["bfbbr"]},
	"hm": {"name": "Hannah Montana", "aliases": ["montana", "hannahmontana"]},
	"shrek2": {"name": "Shrek 2", "aliases": ["s2"]},
	"traod": {"name": "Tomb Raider: The Angel of Darkness", "aliases": ["angelofdarkness", "aod", "tombraideraod"]},
	"popww": {"name": "Prince of Persia: Warrior Within", "aliases": ["warriorwithin"]}
}

# Map abbreviations passed by users to human-readable names.
# This is just for main boards: for CE's and Multiruns, use
# the ce.py and multi.py files under the configs folder.
CATEGORY_MAP = {
	"Any%": {"aliases": ["any", "any%"], "internal_name": "any"},
	"100%": {"aliases": ["100", "hundo", "100%"], "internal_name": "100"},
	"Glitchless": {"aliases": ["gless", "glitchless"], "internal_name": "gless"},
	"No Major Skips": {"aliases": ["nms", "nomajorskips", "any%nms", "any%nomajorskips"], "internal_name": "nms"},
	"No Major Glitches": {"aliases": ["nmg", "nomajorglitches", "any%nmg", "any%nomajorglitches"], "internal_name": "nmg"},
	"Any% No EDS": {"aliases": ["noeds", "anynoeds", "any%noeds"], "internal_name": "noeds"},
	"All Wizard Cards": {"aliases": ["awc", "wizardcards", "allwizardcards"], "internal_name": "awc"},
	"All Requirements": {"aliases": ["allreq", "allreqs", "requirements", "allrequirements"], "internal_name": "allreq"},
	"All Crests": {"aliases": ["ac", "crests", "allcrests"], "internal_name": "allc"},
	"Warpless": {"aliases": ["wl", "warpless"], "internal_name": "warpless"},
	"Boostless": {"aliases": ["bl", "boostless"], "internal_name": "boostless"},
	"All Shields": {"aliases": ["as", "shields", "allshields"], "internal_name": "allshields"},
	"Beat Hogwarts Cup": {"aliases": ["bhc", "hogwarts", "hogwartscup", "beathogwarts", "beathogwartscup"], "internal_name": "bhc"},
	"Beat World Cup": {"aliases": ["bwc", "world", "worldcup", "beatworld", "beatworldscup"], "internal_name": "bwc"},
	"Beat the Tutorial": {"aliases": ["btt", "tutorial", "beattutorial", "beatthetutorial"], "internal_name": "btt"},
	"NG+": {"aliases": ["ng", "ngplus", "newgameplus", "ng+"], "internal_name": "ng"},
	"Kill Ranrok": {"aliases": ["ranrok", "killranrok"], "internal_name": "ranrok"},
	"All Quests": {"aliases": ["aq", "quests", "allquests"], "internal_name": "allq"},
	"Glitched": {"aliases": ["glitched"], "internal_name": "glitched"},
	"All Teensies": {"aliases": ["at", "allt", "allteensies"], "internal_name": "allt"},
	"No Teensies": {"aliases": ["not", "noteensies"], "internal_name": "not"},
	"1 Spatula": {"aliases": ["1s", "1spat", "1spatula"], "internal_name": "1s"},
	"2 Spatulas": {"aliases": ["2s", "2spat", "2spatulas"], "internal_name": "2s"},
	"77 Spatulas": {"aliases": ["77s", "77spat", "77spatulas"], "internal_name": "77s"},
	"100 Spatulas": {"aliases": ["100s", "100spat", "100spatulas"], "internal_name": "100s"},
	"All Mysteries": {"aliases": ["am", "allm", "mysteries", "allmysteries"], "internal_name": "mysteries"},
	"Better than Glitchless": {"aliases": ["bettergless", "bg", "btg", "betterglitchless"], "internal_name": "btg"},
	"True Ending": {"aliases": ["te", "ending", "trueending"], "internal_name": "te"},
	"Sax%": {"aliases": ["sax", "mrsax", "sax%", "mrsax%"], "internal_name": "sax"},
	"Skops%": {"aliases": ["skops", "mrskops", "skops%", "mrskops%"], "internal_name": "skops"}
}

# Platform category map
# This is an alternative version of CATEGORY_MAP, but designed
# for game boards which set the top category to platform names
PLATFORM_CATEGORY_MAP = {
	"r1": {
		"PS1": ["ps1", "psx"],
		"PC": ["pc"],
		"DSI": ["ds"],
		"GBA": ["gba"],
		"Sega Saturn": ["saturn", "segasaturn", "ss"],
		"Atari Jaguar": ["jaguar", "atari", "atarijaguar", "aj"]
	},
	"r3": {
		"GCN": ["gcn", "wii"],
		"GCN Emu": ["gcn"],
		"HD": ["hd", "ps3", "x360", "xss"],
		"PC": ["pc"],
		"PS2": ["ps2"],
		"Xbox": ["xbox"]
	},
	"ssbfbbr": {
		"PC": ["pc"],
		"Console": ["ps4", "ps5", "xbone", "xboxone"],
		"Mobile": ["iOS", "ios", "android"]
	}
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
	"legacy": ["legacy_pc_story", "legacy_pc_hard", "legacy_ps4_story", "legacy_ps4_hard", "legacy_ps5_story", "legacy_ps5_hard"],
	"r1": ["r1_ps1", "r1_pc", "r1_ds", "r1_ss", "r1_aj"],
	"r3": ["r3_gcn", "r3_ps3", "r3_x360", "r3_ps2", "r3_pc"],
	"rehydrated": ["ssbfbbr_pc_nla", "ssbfbbr_pc_la"],
	"hannah_montana": ["hm_ds", "montana_ds", "hannahmontana_ds", "hannah_montana_ds"],
	"shrek_2": ["shrek2_pc", "s2_pc"],
	"shrek_2_c": [
		"shrek2_ps2_sp", "shrek2_ps2_coop", "shrek2_gcn_sp", "shrek2_gcn_coop", "shrek2_xbox_sp", "shrek2_xbox_coop",
		"s2_ps2_sp", "s2_ps2_coop", "s2_gcn_sp", "s2_gcn_coop", "s2_xbox_sp", "s2_xbox_coop"
	],
	"traod": ["traod_pc", "angelofdarkness_pc", "aod_pc", "tombraideraod_pc"],
	"pop_ww": ["popww_pc_std", "popww_pc_zl", "popww_pc_nmg", "popww_ps2_std", "popww_ps2_zl", "popww_ps2_nmg"]
}
