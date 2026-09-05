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
# This assumes base games, do not use this for category extensions.
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
	"ce": "Harry Potter Category Extensions",
	"multi": "Harry Potter Multiruns",

	# Selection of other games. Extend appropriately.
	"dbb": "Disney's Brother Bear"
}

# Category extension game mapping.
# This section should only be used for category extension boards.
# Key names must be abbreviations that would be called in !run ce
# commands: the values of each key are an SRDC URL slug.
#
# It's advisable to provide a comment next to each key/value pair
# so people know what it is.
CE_GAME_MAP = {
	"hp": "hpce",  # Harry Potter Category Extensions
	"rac": "racextras"  # Ratchet & Clank Category Extensions
}

# Board aliases. More relevant for CEs, but useful if
# you want multiple user input choices for a category
# to be found.
CE_BOARD_ALIASES = {
	"1pc": "1pc",
	"2pc": "2pc",
	"3pc": "3pc",
	"4pc": "4pc",
	"5pc": "5pc",
	"6pc": "6pc",
	"sy": "sy",
	"singleyear": "sy",
	"insane": "insane",
	"ins": "insane",
	"mr": "mr",
	"multiruns": "mr",
	"1ps1": "1ps1",
	"2ps1": "2ps1",
	"4psp": "4psp",
	"5psp": "5psp",
	"dvd": "dvd",
	"dvdgames": "dvd",
}

# Category extension: category aliases/mapping.
# This is used to map user input to the name that
# is used internally to reference a specific sub-board
# for a category extension.
CE_CATEGORY_ALIASES = {
	"hpce": {
		"1pc": {
			"100gless": "100gless", "allchests": "allchests", "boostless": "boostless", "highjump": "highjump", "lowcast": "lowcast",
		},
		"2pc": {
			"100gless": "100gless", "allchests": "allchests", "awcgless": "awcgless", "boostless": "boostless",	"chungus": "chungus",
			"cutscene": "cutscene", "hpwc": "hpwc",	"highjump": "highjump",	"jumpless": "jumpless",	"lowcast": "lowcast", "ng": "ng",
			"nmg": "nmg"
		},
		"3pc": {
			"any": "any"
		},
		"4pc": {
			"avc1p": "avc_1p", "avc2p": "avc_2p", "avc3p": "avc_3p"
		},
		"5pc": {
			"amg": "amg", "allportraits": "allportraits", "allsymbols": "allsymbols", "chess": "chess"
		},
		"6pc": {
			"pr": "pr"
		},
		"1ps1": {
			"awc": "awc", "ss": "ss", "ng": "ng"
		},
		"2ps1": {
			"awc": "awc", "ss": "ss"
		},
		"4psp": {
			"any": "any", "100": "100"
		},
		"5psp": {
			"any": "any", "100": "100"
		},
		"mr": {
			"glessduo": "glessduo", "rpgtri": "rpgtri"
		},
		"insane": {
			"hp1pc": "hp1_pc", "hp2pc": "hp2_pc", "hp3pc": "hp3_pc", "hp4pc": "hp4_pc", "hp5pc": "hp5_pc", "hp6pc": "hp6_pc",
			"hp71pc": "hp71_pc", "hp72pc": "hp72_pc", "1ps1": "1ps1", "2ps1": "2ps1", "hp2_6th": "hp2_6th_gen",
			"hp3_6th": "hp3_6th_gen", "hp1gba": "hp1_gba", "hp2gba": "hp2_gba", "hp3gba": "hp3_gba", "qwcgba": "qwc_gba",
			"hp6ds": "hp6_ds", "hp71ds": "hp71_ds", "hp72ds": "hp72_ds"
		},
		"sy": {
			"hp1any": "hp1_any", "hp2any": "hp2_any", "hp3any": "hp3_any", "hp4any": "hp4_any",	"hp5any": "hp5_any",
			"hp6any": "hp6_any", "hp71any": "hp71_any",	"hp72any": "hp72_any",
			"hp1hundo": "hp1_100", "hp2hundo": "hp2_100", "hp3hundo": "hp3_100", "hp4hundo": "hp4_100",
			"hp5hundo": "hp5_100", "hp6hundo": "hp6_100", "hp71hundo": "hp71_100", "hp72hundo": "hp72_100",
			"hp1100": "hp1_100", "hp2100": "hp2_100", "hp3100": "hp3_100", "hp4100": "hp4_100",
			"hp5100": "hp5_100", "hp6100": "hp6_100", "hp7_1100": "hp71_100", "hp7_2100": "hp72_100"
		},
		"dvd": {
			"hc": "hc", "ww": "ww"
		},
	}
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

# Map abbreviations passed by users to human-readable names.
# This should be used only for 'main' boards: ie not multiruns
# or category extensions. If someone queries a run that isn't
# described here, data from SRDC should be used as a fallback.
CATEGORY_MAP = {
	'any': 'Any%',
	'100': '100%',
	'glitchless': 'Glitchless',
	'gless': 'Glitchless',
	'nms': 'No Major Skips',
	'noeds': 'Any% No EDS',
	'awc': 'All Wizard Cards',
	'warpless': 'Warpless'
}
CE_CATEGORY_MAP = {
	'100gless': '100% Glitchless',
	'ng': 'NG+',
	'boostless': 'Boostless',
	'nmg': 'No Major Glitches',
	'allreq': 'All Requirements',
	'allshields': 'All Shields',
	'allcrests': 'All Crests',
	'cutscene': 'Cutscene%',
	'chungus': 'Chungus%'
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
	"hpce": {
		"categories": {
			"1pc_100gless": {
				"board": "1PC",
				"subcategory": "100-glitchless",
				"variables": [
					{"var_id": "xd1j7vwd-789x9o08", "value_id": "9qj95y0l"}
				]
			},
			"1pc_allchests": {
				"board": "1PC",
				"subcategory": "all-chests",
				"variables": [
					{"var_id": "xd1j7vwd-789x9o08", "value_id": "qj7o0j3q"}
				]
			},
			"1pc_boostless": {
				"board": "1PC",
				"subcategory": "boostless",
				"variables": [
					{"var_id": "xd1j7vwd-789x9o08", "value_id": "810prejl"}
				]
			},
			"1pc_highjump": {
				"board": "1PC",
				"subcategory": "high-jump",
				"variables": [
					{"var_id": "xd1j7vwd-789x9o08", "value_id": "qvv4doyq"}
				]
			},
			"1pc_lowcast": {
				"board": "1PC",
				"subcategory": "lowcast",
				"variables": [
					{"var_id": "xd1j7vwd-789x9o08", "value_id": "rqvj9v5q"}
				]
			},
			"2pc_100gless": {
				"board": "2PC",
				"subcategory": "100-glitchless",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "013pyekl"}
				]
			},
			"2pc_allchests": {
				"board": "2PC",
				"subcategory": "all-chests",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "le23je6l"}
				]
			},
			"2pc_awcgless": {
				"board": "2PC",
				"subcategory": "awc-glitchless",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "0q5p0erl"}
				]
			},
			"2pc_boostless": {
				"board": "2PC",
				"subcategory": "boostless",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "5lmp9jyl"}
				]
			},
			"2pc_chungus": {
				"board": "2PC",
				"subcategory": "chungus",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "rqv2jkw1"}
				]
			},
			"2pc_cutscene": {
				"board": "2PC",
				"subcategory": "cutscene",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "rqv9nw5l"}
				]
			},
			"2pc_hpwc": {
				"board": "2PC",
				"subcategory": "harry-potter-wizard-card",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "4lx9jwjl"}
				]
			},
			"2pc_highjump": {
				"board": "2PC",
				"subcategory": "blah",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "xqkpp04l"}
				]
			},
			"2pc_jumpless": {
				"board": "2PC",
				"subcategory": "jumpless",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "qyzx9721"}
				]
			},
			"2pc_lowcast": {
				"board": "2PC",
				"subcategory": "lowcast",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "814pnew1"}
				]
			},
			"2pc_ng": {
				"board": "2PC",
				"subcategory": "ng",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "81w9kw9l"}
				]
			},
			"2pc_nmg": {
				"board": "2PC",
				"subcategory": "nmg",
				"variables": [
					{"var_id": "zd3j7xr2-2lg3d4on", "value_id": "zqo97wgq"}
				]
			},
			"3pc_any": {
				"board": "3PC",
				"subcategory": "any",
				"variables": [
					{"var_id": "rn1zmxpl-02qwx172", "value_id": "014g7x21"}
				]
			},
			"4pc_avc_1p": {
				"board": "4PC",
				"subcategory": "All_Vanishing_Cards-1-Player",
				"variables": [
					{"var_id": "w20gevvk-5ly156yl", "value_id": "0q5p0zrl"},
					{"var_id": "2lgk0jo8", "value_id": "14oy0mkq"}
				]
			},
			"4pc_avc_2p": {
				"board": "4PC",
				"subcategory": "All_Vanishing_Cards-2-Players",
				"variables": [
					{"var_id": "w20gevvk-5ly156yl", "value_id": "0q5p0zrl"},
					{"var_id": "2lgk0jo8", "value_id": "192moe4q"}
				]
			},
			"4pc_avc_3p": {
				"board": "4PC",
				"subcategory": "All_Vanishing_Cards-3-Players",
				"variables": [
					{"var_id": "w20gevvk-5ly156yl", "value_id": "0q5p0zrl"},
					{"var_id": "2lgk0jo8", "value_id": "12vdyj2q"}
				]
			},
			"5pc_amg": {
				"board": "5PC",
				"subcategory": "all-minigames",
				"variables": [
					{"var_id": "rkl5jr82-rn1zmxpl", "value_id": "5q8pm8rl"}
				]
			},
			"5pc_allportraits": {
				"board": "5PC",
				"subcategory": "all-portraits",
				"variables": [
					{"var_id": "rkl5jr82-rn1zmxpl", "value_id": "4qy96o3l"}
				]
			},
			"5pc_allsymbols": {
				"board": "5PC",
				"subcategory": "all-symbols",
				"variables": [
					{"var_id": "rkl5jr82-rn1zmxpl", "value_id": "1dkow2jl"}
				]
			},
			"5pc_chess": {
				"board": "5PC",
				"subcategory": "chess",
				"variables": [
					{"var_id": "rkl5jr82-rn1zmxpl", "value_id": "mln92m6q"}
				]
			},
			"6pc_pr": {
				"board": "6PC",
				"subcategory": "potions-rush",
				"variables": [
					{"var_id": "z27zyz4k-gnx606jn", "value_id": "12v2om4q"}
				]
			},
			"1ps1_awc": {
				"board": "1PS1",
				"subcategory": "all-wizard-cards",
				"variables": [
					{"var_id": "zd3r5wvd-jlzx03x8", "value_id": "xqkxnyd1"}
				]
			},
			"1ps1_ss": {
				"board": "1PS1",
				"subcategory": "superspeed",
				"variables": [
					{"var_id": "zd3r5wvd-jlzx03x8", "value_id": "gq76xmpl"}
				]
			},
			"1ps1_ng": {
				"board": "1PS1",
				"subcategory": "ng",
				"variables": [
					{"var_id": "zd3r5wvd-jlzx03x8", "value_id": "21g3pz6q"}
				]
			},
			"2ps1_awc": {
				"board": "2PS1",
				"subcategory": "all-wizard-cards",
				"variables": [
					{"var_id": "02qwx172-yn23geel", "value_id": "q8kk0p6q"}
				]
			},
			"2ps1_ss": {
				"board": "2PS1",
				"subcategory": "superspeed",
				"variables": [
					{"var_id": "02qwx172-yn23geel", "value_id": "qoxkedgq"}
				]
			},
			"4psp_any": {
				"board": "4PSP",
				"subcategory": "any",
				"variables": [
					{"var_id": "9kv3g402-38de521n", "value_id": "qyzzymd1"}
				]
			},
			"4psp_100": {
				"board": "4PSP",
				"subcategory": "100",
				"variables": [
					{"var_id": "9kv3g402-38de521n", "value_id": "ln8807nl"}
				]
			},
			"5psp_any": {
				"board": "5PSP",
				"subcategory": "any",
				"variables": [
					{"var_id": "rklm84wd-r8rewy2l", "value_id": "q655xwol"}
				]
			},
			"5psp_100": {
				"board": "5PSP",
				"subcategory": "100",
				"variables": [
					{"var_id": "rklm84wd-r8rewy2l", "value_id": "lmoo4e01"}
				]
			},
			"mr_glessduo": {
				"board": "Multiruns",
				"subcategory": "pc-glitchless-duofecta",
				"variables": [
					{"var_id": "ndx314vd-p85rz75n", "value_id": "810prjjl"}
				]
			},
			"mr_rpgtri": {
				"board": "Multiruns",
				"subcategory": "rpg-trifecta",
				"variables": [
					{"var_id": "ndx314vd-p85rz75n", "value_id": "9qj95n0l"}
				]
			},
			"insane_hp1_pc": {
				"board": "Insane",
				"subcategory": "hp1-pc",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "21d7dm41"}
				]
			},
			"insane_hp2_pc": {
				"board": "Insane",
				"subcategory": "hp2-pc",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "klrw7rj1"}
				]
			},
			"insane_hp3_pc": {
				"board": "Insane",
				"subcategory": "hp3-pc",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "5q87zmgl"}
				]
			},
			"insane_hp4_pc": {
				"board": "Insane",
				"subcategory": "hp4-pc",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "5lezyezl"}
				]
			},
			"insane_hp5_pc": {
				"board": "Insane",
				"subcategory": "hp5-pc",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "0q5zw2nq"}
				]
			},
			"insane_hp6_pc": {
				"board": "Insane",
				"subcategory": "hp6-pc",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "4lxo2yrl"}
				]
			},
			"insane_hp71_pc": {
				"board": "Insane",
				"subcategory": "hp7-1-pc",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "814gm2j1"}
				]
			},
			"insane_hp72_pc": {
				"board": "Insane",
				"subcategory": "hp7-2-pc",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "z19yezkl"}
				]
			},
			"insane_1ps1": {
				"board": "Insane",
				"subcategory": "hp1-ps1",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "4qyd206q"}
				]
			},
			"insane_2ps1": {
				"board": "Insane",
				"subcategory": "hp2-ps1",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "mlnpvxo1"}
				]
			},
			"insane_hp2_6th_gen": {
				"board": "Insane",
				"subcategory": "hp2-gcn-xbox",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "013z2zyq"}
				]
			},
			"insane_hp3_6th_gen": {
				"board": "Insane",
				"subcategory": "hp3-6th-gen",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "5lm0z3j1"}
				]
			},
			"insane_hp1_gba": {
				"board": "Insane",
				"subcategory": "hp1-gba",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "jq663o3q"}
				]
			},
			"insane_hp2_gba": {
				"board": "Insane",
				"subcategory": "hp2-gba",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "q75dkjd1"}
				]
			},
			"insane_hp3_gba": {
				"board": "Insane",
				"subcategory": "hp3-gba",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "rqv025rl"}
				]
			},
			"insane_qwc_gba": {
				"board": "Insane",
				"subcategory": "qwc-gba",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "q654y2nl"}
				]
			},
			"insane_hp6_ds": {
				"board": "Insane",
				"subcategory": "hp6-ds",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "zqovk7g1"}
				]
			},
			"insane_hp71_ds": {
				"board": "Insane",
				"subcategory": "hp7-1-ds",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "1py422g1"}
				]
			},
			"insane_hp72_ds": {
				"board": "Insane",
				"subcategory": "hp7-2-ds",
				"variables": [
					{"var_id": "9d83xr72-7896d298", "value_id": "klrg73oq"}
				]
			},
			"sy_hp1_any": {
				"board": "Single_Year",
				"subcategory": "hp1-any",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "4qye4641"},
					{"var_id": "wl30dmyl", "value_id": "013erydq"}
				]
			},
			"sy_hp2_any": {
				"board": "Single_Year",
				"subcategory": "hp2-any",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "mln6320q"},
					{"var_id": "wl30dmyl", "value_id": "013erydq"}
				]
			},
			"sy_hp3_any": {
				"board": "Single_Year",
				"subcategory": "hp3-any",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "810e7rwq"},
					{"var_id": "wl30dmyl", "value_id": "013erydq"}
				]
			},
			"sy_hp4_any": {
				"board": "Single_Year",
				"subcategory": "hp4-any",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "9qjyd5eq"},
					{"var_id": "wl30dmyl", "value_id": "013erydq"}
				]
			},
			"sy_hp5_any": {
				"board": "Single_Year",
				"subcategory": "hp5-any",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "jq6k7j3l"},
					{"var_id": "wl30dmyl", "value_id": "013erydq"}
				]
			},
			"sy_hp6_any": {
				"board": "Single_Year",
				"subcategory": "hp6-any",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "5lmjn9jl"},
					{"var_id": "wl30dmyl", "value_id": "013erydq"}
				]
			},
			"sy_hp71_any": {
				"board": "Single_Year",
				"subcategory": "hp7-1-any",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "81ww8ko1"},
					{"var_id": "wl30dmyl", "value_id": "013erydq"}
				]
			},
			"sy_hp72_any": {
				"board": "Single_Year",
				"subcategory": "hp7-2-any",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "zqown7pl"},
					{"var_id": "wl30dmyl", "value_id": "013erydq"}
				]

			},
			"sy_hp1_100": {
				"board": "Single_Year",
				"subcategory": "hp1-100",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "4qye4641"},
					{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
				]
			},
			"sy_hp2_100": {
				"board": "Single_Year",
				"subcategory": "hp2-100",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "mln6320q"},
					{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
				]
			},
			"sy_hp3_100": {
				"board": "Single_Year",
				"subcategory": "hp3-100",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "810e7rwq"},
					{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
				]
			},
			"sy_hp4_100": {
				"board": "Single_Year",
				"subcategory": "hp4-100",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "9qjyd5eq"},
					{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
				]
			},
			"sy_hp5_100": {
				"board": "Single_Year",
				"subcategory": "hp5-100",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "jq6k7j3l"},
					{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
				]
			},
			"sy_hp6_100": {
				"board": "Single_Year",
				"subcategory": "hp6-100",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "5lmjn9jl"},
					{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
				]
			},
			"sy_hp71_100": {
				"board": "Single_Year",
				"subcategory": "hp7-1-100",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "81ww8ko1"},
					{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
				]
			},
			"sy_hp72_100": {
				"board": "Single_Year",
				"subcategory": "hp7-2-100",
				"variables": [
					{"var_id": "xd1vl0rd-2lgr1v7n", "value_id": "zqown7pl"},
					{"var_id": "wl30dmyl", "value_id": "rqvwdn71"}
				]
			},
			"dvd_hc": {
				"board": "Harry_Potter_DVD_Games",
				"subcategory": "hogwarts-challenge",
				"variables": [
					{"var_id": "jdr966xd-r8r7v77n", "value_id": "jqzd3e4l"}
				]
			},
			"dvd_ww": {
				"board": "Harry_Potter_DVD_Games",
				"subcategory": "wizarding-world",
				"variables": [
					{"var_id": "jdr966xd-r8r7v77n", "value_id": "klrm240q"}
				]
			},
			"platform": None
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
}

# Point to the docs if there is an error.
# Putting it as a constant means we don't need multiple
# references to it, and updating it just requires changing
# this one constant.
COMMAND_USAGE_DOC = "https://github.com/supersajuuk/hpsr-pb-bot/blob/main/README.md"
