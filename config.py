# Store all the key configuration settings here.
# By moving the keys to here, we can more easily update and manage it.
# Since these won't change without a reload, we should use constant
# variable formatting, ie the variables should be ALL CAPS.
#
# Map abbreviations to full game names
PER_GAME_MAP = {
	# PC
	"hp1pc": "Harry Potter and the Philosopher's Stone (PC)",
	"hp2pc": "Harry Potter and the Chamber of Secrets (PC)",
	"hp3pc": "Harry Potter and the Prisoner of Azkaban (PC)",
	"hp4": "Harry Potter and the Goblet of Fire",
	"hp5": "Harry Potter and the Order of the Phoenix",
	"hp6": "Harry Potter and the Half Blood Prince",
	"hp7.1": "Harry Potter and the Deathly Hallows Part 1",
	"hp7.2": "Harry Potter and the Deathly Hallows Part 2",

	# PS1
	"hp1ps1": "Harry Potter and the Philosopher's Stone (PS1)",
	"hp2ps1": "Harry Potter and the Chamber of Secrets (PS1)",

	# 6th Gen
	"hp1_6gen": "Harry Potter and the Philosopher's Stone (PS2,GCN,Xbox)",
	"hp2_6gen": "Harry Potter and the Chamber of Secrets (GCN/Xbox)",
	"hp2ps2": "Harry Potter and the Chamber of Secrets (PS2)",
	"hp3_6": "Harry Potter and the Prisoner of Azkaban (PS2,Xbox,GCN)",

	# GBC
	"hp1gbc": "Harry Potter and the Philosopher's Stone (GBC)",
	"hp2gbc": "Harry Potter and the Chamber of Secrets (GBC)",

	# GBA
	"hp1gba": "Harry Potter and the Philosopher's Stone (GBA)",
	"hp2gba": "Harry Potter and the Chamber of Secrets (GBA)",
	"hp3gba": "Harry Potter and the Prisoner of Azkaban (GBA)",

	# Other Games (non-HP, extend this as appropriate)
	"dbb": "Disney's Brother Bear",

	# Others
	"multi": "Harry Potter Multiruns",
	"hpce": "Harry Potter Category Extensions"
}

# Map abbreviations for category to full API names
# % Symbol received by request will appear as "%25"
# Clean name returned in response for readability
CATEGORY_MAPPING = {
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
	'allcrests': {'name': '<Category "All Crests">', 'clean': 'All Crests'},

	# Multirun Categories
	'pctri': {
		'name': '<Category "PC Trifecta">', 'clean': 'PC Trifecta',
		'variables': {'0nw0e0kl': {'any': 'p12099kl', '100': '81p5eekl', 'awc': 'p120927l'}}
	},
	'pcocto': {
		'name': '<Category "PC Octofecta">', 'clean': 'PC Octofecta',
		'variables': {'wl3dqd98': {'any': 'klr2xx21', '100': '21de6vjl'}}
	},
	'7duo': {
		'name': '<Category "7PC Duofecta">', 'clean': '7PC Duofecta',
		'variables': {'789dqd6n': {'any': 'xqknooyq', '100': 'gq7x22yl'}}
	},
	'ps1duo': {
		'name': '<Category "PS1 Duofecta">', 'clean': 'PS1 Duofecta',
		'variables': {'wlek5kkl': {'any': '5q8942k1', '100': '4qyw7571', 'nms': 'p120957l'}}
	},
	'6gentri': {
		'name': '<Category "6th Gen Trifecta">', 'clean': '6th Gen Trifecta',
		'variables': {'68k737yl': {'any': 'mlnoeddq', '1001': '9qj82wg1'}}
	},
	'fs': {
		'name': '<Category "Full Series">', 'clean': 'Full Series',
		'variables': {'38dm1m18': {'any': '5lexn3zq', '100': '0q534xn1'}}
	},
	'gbcduo': {
		'name': '<Category "GBC Duofecta">', 'clean': 'GBC Duofecta',
		'variables': {'j84d0dj8': {'any': 'jq6evy7l', '100': '5lmm284l'}}
	},
	'gbapenta': {
		'name': '<Category "GBA Pentafecta">', 'clean': 'GBA Pentafecta',
		'variables': {'rn1jqjkn': {'any': '81w07e5l', '100': 'zqovjm21'}}
	},
	'hhocto': {
		'name': '<Category "Handheld Octofecta">', 'clean': 'Handheld Octofecta',
		'variables': {'p855j508': {'any': '0136xw31', '100': 'rqvyx6wq'}}
	},

	# Category Extensions
	'awcgless': {'name': '<Category "2PC">', 'clean': 'AWC Glitchless', 'cecode': '0q5p0erl'},
	'awcglitchless': {'name': '<Category "2PC">', 'clean': 'AWC Glitchless', 'cecode': '0q5p0erl'},
	'chungus': {'name': '<Category "2PC">', 'clean': 'Chungus%', 'cecode': 'rqv2jkw1'}
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
COMMAND_USAGE_DOC = "https://github.com/artfulinfo/hpsr-pb-bot/blob/main/README.md"
