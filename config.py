# Store all the key configuration settings here.
# By moving the keys to here, we can more easily update and manage it.
# Since these won't change without a reload, we should use constant
# variable formatting, ie the variables should be ALL CAPS.
#
# Platform mapping. This is used to provide more control and flexibility over
# bot commands.
PLATFORM_MAP = {
	"pc": "pc",
	"ps1": "ps1",
	"ps2": "ps2",
	"ps3": "ps3",
	"psp": "psp",
	"gba": "gba",
	"gbc": "gbc",
	"ds": "ds",
	"xbox": "6thgen",
	"gcn": "6thgen"
}

# Game mapping. This is used to define all known games that exist in the bot.
# This assumes base games, do not use this for category extensions. CE boards
# need to be defined in their own constants.
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
	"hpce": "Harry Potter Category Extensions",
	"multi": "Harry Potter Multiruns",

	# Selection of other games. Extend appropriately.
	"dbb": "Disney's Brother Bear"
}

# Category type mapping
# Needed for command parsing
CE_TYPE_MAP = {
	"standard": "standard",
	"std": "standard",
	"ce": "standard",
	"hpce": "standard",
	"insane": "insane",
	"ins": "insane",
	"multiruns": "multiruns",
	"multi": "multiruns",
	"mr": "multiruns",
	"singleyear": "single_year",
	"sy": "single_year",
	"year": "single_year"
}

# CE category mapping
# Needed for the more "simple" category extensions.
CE_CATEGORY_MAP = {
	"100gless": "100gless",
	"gless100": "100gless",
	"allchests": "allchests",
	"boostless": "boostless",
	"highjump": "highjump",
	"lowcast": "lowcast",
	"insane": "insane",
	"glitchlessduo": "glitchlessduo",
	"duo": "glitchlessduo",
	"rpgtrifecta": "rpgtrifecta",
	"trifecta": "rpgtrifecta",
	"any": "any",
	"100": "100"
}

# Category extension game mapping.
# Here we will map all the different games for the category extensions
# boards on SRDC. Currently only supports hpce, but will expand in the future.
CE_GAME_MAP = {
	"hp1_pc": "1PC",
	"hp2_pc": "2PC",
	"hp3_pc": "3PC",
	"hp4_pc": "4PC",
	"hp5_pc": "5PC",
	"hp6_pc": "6PC",
	"hp1_ps1": "1PS1",
	"hp2_ps1": "2PS1",
	"hp4_psp": "4PSP",
	"hp5_psp": "5PSP"
}
CE_GAME_MAP_INSANE = {
	"hp1_pc": "Insane",
	"hp2_pc": "Insane",
	"hp3_pc": "Insane",
	"hp4_pc": "Insane",
	"hp5_pc": "Insane",
	"hp6_pc": "Insane",
	"hp7.1_pc": "Insane",
	"hp7.2_pc": "Insane",
	"qwc_pc": "Insane",
	"hp1_ps1": "Insane",
	"hp2_ps1": "Insane",
	"hp2_6thgen": "Insane",
	"hp3_6thgen": "Insane",
	"hp1_gba": "Insane",
	"hp2_gba": "Insane",
	"hp3_gba": "Insane",
	"qwc_gba": "Insane",
	"hp6_ds": "Insane",
	"hp7.1_ds": "Insane",
	"hp7.2_ds": "Insane"
}
CE_GAME_MAP_MULTIRUNS = {
	"multiruns_pc": "Multiruns",
	"multiruns_rpg": "Multiruns"
}
CE_GAME_MAP_SINGLE_YEAR = {
	"hp1": "Single_Year",
	"hp2": "Single_Year",
	"hp3": "Single_Year",
	"hp4": "Single_Year",
	"hp5": "Single_Year",
	"hp6": "Single_Year",
	"hp7.1": "Single_Year",
	"hp7.2": "Single_Year"
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

# This just sets a constant for the hpmulti game board.
MULTIRUN_SLUG = "hpmulti"

# Category extension mapping. This is needed to map
# all the sub-boards and variables correctly to the CE_GAME_MAP
# constants above.
CATEGORY_EXT_MAP_STANDARD = {
	"100gless": {
		"h_suffix": "100-glitchless",
		"var_ids": {"xd1j7vwd-789x9o08": "9qj95y0l"}
	},
	"allchests": {
		"h_suffix": "all-chests",
		"var_ids": {"xd1j7vwd-789x9o08": "qj7o0j3q"}
	},
	"boostless": {
		"h_suffix": "boostless",
		"var_ids": {"xd1j7vwd-789x9o08": "810prejl"}
	},
	"highjump": {
		"h_suffix": "high-jump",
		"var_ids": {"xd1j7vwd-789x9o08": "qvv4doyq"}
	},
	"lowcast": {
		"h_suffix": "lowcast",
		"var_ids": {"xd1j7vwd-789x9o08": "rqvj9v5q"}
	}
}

# Due to a quirk of the insane% boards, things are very consistent
# The dynamic parts will be filled in by other code in data.py
CATEGORY_EXT_MAP_INSANE = {
	"insane": {
		"h_suffix": None,
		"var_ids": {"9d83xr72-7896d298": None}
	}
}
CATEGORY_EXT_MAP_MULTIRUNS = {
	"glitchlessduo": {
		"h_suffix": "pc-glitchless-duofecta",
		"var_ids": {"ndx314vd-p85rz75n": "810prjjl"}
	},
	"rpgtrifecta": {
		"h_suffix": "rpg-trifecta",
		"var_ids": {"ndx314vd-p85rz75n": "9qj95n0l"}
	}
}
CATEGORY_EXT_MAP_SINGLE_YEAR = {
	"any": {
		"h_suffix": "any",
		"var_ids": {"xd1vl0rd-2lgr1v7n": None, "wl30dmyl": "013erydq"}
	},
	"100": {
		"h_suffix": "100",
		"var_ids": {"xd1vl0rd-2lgr1v7n": None, "wl30dmyl": "rqvwdn71"}
	}
}
CATEGORY_EXT_MAP = {
	"standard": CATEGORY_EXT_MAP_STANDARD,
	"insane": CATEGORY_EXT_MAP_INSANE,
	"multiruns": CATEGORY_EXT_MAP_MULTIRUNS,
	"single_year": CATEGORY_EXT_MAP_SINGLE_YEAR
}

# Value ID mapping. This is needed for category extensions.
CE_INSANE_VALUE_IDS = {
	"hp1_pc": "21d7dm41",
	"hp2_pc": "klrw7rj1",
	"hp3_pc": "5q87zmgl",
	"hp4_pc": "5lezyezl",
	"hp5_pc": "0q5zw2nq",
	"hp6_pc": "4lxo2yrl",
	"hp7.1_pc": "814gm2j1",
	"hp7.2_pc": "z19yezkl",
	"qwc_pc": "qoxyzp2q",
	"hp1_ps1": "4qyd206q",
	"hp2_ps1": "mlnpvxo1",
	"hp2_6thgen": "013z2zyq",
	"hp3_6thgen": "5lm0z3j1",
	"hp1_gba": "jq663o3q",
	"hp2_gba": "q75dkjd1",
	"hp3_gba": "rqv025rl",
	"qwc_gba": "q654y2nl",
	"hp6_ds": "zqovk7g1",
	"hp7.1_ds": "1py422g1",
	"hp7.2_ds": "klrg73oq"
}
CE_SINGLE_YEAR_GAME_VALUES = {
	"hp1": "4qye4641",
	"hp2": "mln6320q",
	"hp3": "810e7rwq",
	"hp4": "9qjyd5eq",
	"hp5": "jq6k7j3l",
	"hp6": "5lmjn9jl",
	"hp7.1": "81ww8ko1",
	"hp7.2": "zqown7pl"
}

# Map abbreviations for category to full API names
# % Symbol received by request will appear as "%25"
# Clean name returned in response for readability
CATEGORY_MAP = {
	# Glitched Categories
	'any': {'name': '<Category "Any%">', 'clean': 'Any%'},
	'100': {'name': '<Category "100%">', 'clean': '100%'},
	'ng': {'name': '<Category "NG+">', 'clean': 'NG+'},

	# Low-glitch / Glitchless Categories
	'glitchless': {'name': '<Category "Glitchless">', 'clean': 'Glitchless'},
	'gless': {'name': '<Category "Glitchless">', 'clean': 'Glitchless'},
	'warpless': {'name': '<Category "Warpless">', 'clean': 'Warpless'},
	'boostless': {'name': '<Category "Boostless">', 'clean': 'Boostless'},
	'nms': {'name': '<Category "No Major Skips">', 'clean': 'No Major Skips'},
	'nmg': {'name': '<Category "No Major Glitches">', 'clean': 'No Major Glitches'},
	'noeds': {'name': '<Category "Any% No EDS">', 'clean': 'Any% No EDS'},

	# All <blah> Categories
	'awc': {'name': '<Category "All Wizard Cards">', 'clean': 'All Wizard Cards'},
	'allreq': {'name': '<Category "All Requirements">', 'clean': 'All Requirements'},
	'allshields': {'name': '<Category "All Shields">', 'clean': 'All Shields'},
	'allcrests': {'name': '<Category "All Crests">', 'clean': 'All Crests'}
}

# Leaderboard configuration
# Sometimes, a board may contain sub-boards or sub-categories.
# We handle them here so that they can be detected and processed properly.
LEADERBOARD_CONFIG = {
	"hp2ps2": {
		"categories": {
			"any": {
				"var_id": "rklo0owk",
				"value": "any",
				"h": "any"
			},
			"100": {
				"var_id": "ndxvrvj2",
				"value": "100",
				"h": "100"
			},
			"noeds": {
				"var_id": "w209e9z2",
				"value": "no-major-skips",
				"h": "no-major-skips"
			},
		},
		"platform": {
			"var_id": "yn20gk2l",
			"values": {"console": "139v60r1", "emulator": "qvv4y7rq"}
		}
	},
	"hpmulti": {
		"categories": {
			"pc_trifecta_any": {
				"var_id": "0nw0e0kl",
				"value": "p12099kl",
				"h": "PC_Trifecta-Any"
			},
			"pc_trifecta_100": {
				"var_id": "0nw0e0kl",
				"value": "81p5eekl",
				"h": "PC_Trifecta-100"
			},
			"pc_trifecta_awc": {
				"var_id": "0nw0e0kl",
				"value": "p120927l",
				"h": "PC_Trifecta-AWC"
			},
			"pc_octofecta_any": {
				"var_id": "wl3dqd98",
				"value": "klr2xx21",
				"h": "PC_Octofecta-Any"
			},
			"pc_octofecta_100": {
				"var_id": "wl3dqd98",
				"value": "21de6vjl",
				"h": "PC_Octofecta-100"
			},
			"7pc_duofecta_any": {
				"var_id": "789dqd6n",
				"value": "xqknooyq",
				"h": "7PC_Duofecta-Any"
			},
			"7pc_duofecta_100": {
				"var_id": "789dqd6n",
				"value": "gq7x22yl",
				"h": "7PC_Duofecta-100"
			},
			"ps1_duofecta_any": {
				"var_id": "wlek5kkl",
				"value": "5q8942k1",
				"h": "PS1_Duofecta-Any"
			},
			"ps1_duofecta_100": {
				"var_id": "wlek5kkl",
				"value": "4qyw7571",
				"h": "PS1_Duofecta-100"
			},
			"ps1_duofecta_nms": {
				"var_id": "wlek5kkl",
				"value": "p120957l",
				"h": "PS1_Duofecta-NMS"
			},
			"6th_gen_trifecta_any": {
				"var_id": "68k737yl",
				"value": "mlnoeddq",
				"h": "6th_Gen_Trifecta-Any"
			},
			"6th_gen_trifecta_1001": {
				"var_id": "68k737yl",
				"value": "9qj82wg1",
				"h": "6th_Gen_Trifecta-1001"
			},
			"full_series_any": {
				"var_id": "38dm1m18",
				"value": "5lexn3zq",
				"h": "Full_Series-Any"
			},
			"full_series_100": {
				"var_id": "38dm1m18",
				"value": "0q534xn1",
				"h": "Full_Series-100"
			},
			"gbc_duofecta_any": {
				"var_id": "j84d0dj8",
				"value": "jq6evy7l",
				"h": "GBC_Duofecta-Any"
			},
			"gbc_duofecta_100": {
				"var_id": "j84d0dj8",
				"value": "5lmm284l",
				"h": "GBC_Duofecta-100"
			},
			"gba_pentafecta_any": {
				"var_id": "rn1jqjkn",
				"value": "81w07e5l",
				"h": "GBA_Pentafecta-Any"
			},
			"gba_pentafecta_100": {
				"var_id": "rn1jqjkn",
				"value": "zqovjm21",
				"h": "GBA_Pentafecta-100"
			},
			"handheld_octofecta_any": {
				"var_id": "p855j508",
				"value": "0136xw31",
				"h": "Handheld_Octofecta-Any"
			},
			"handheld_octofecta_100": {
				"var_id": "p855j508",
				"value": "rqvyx6wq",
				"h": "Handheld_Octofecta-100"
			}
		},
		"platform": None  # No platform variable is required for these multirun categories.
	},
}

# Point to the docs if there is an error.
# Putting it as a constant means we don't need multiple
# references to it, and updating it just requires changing
# this one constant.
COMMAND_USAGE_DOC = "https://github.com/supersajuuk/hpsr-pb-bot/blob/main/README.md"
