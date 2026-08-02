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

	# Other Games
	"dbb": "Disney's Brother Bear",

	# Multiruns
	"multi": "Harry Potter Multiruns",
	"hpmulti": "Harry Potter Multiruns",
	"hp123pc": "Harry Potter Multiruns",

	# Category extensions
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
	'trifecta': {
		'name': '<Category "PC Trifecta">', 'clean': 'Trifecta',
		'variables': {'789k439l': {'any': '4qyn2371', '100': '810xn351'}}
	},
	'octofecta': {
		'name': '<Category "PC Octofecta">', 'clean': 'Octofecta',
		'variables': {'789k439l': {'any': '4qyn2371', '100': '810xn351'}}
	},
	'7duo': {
		'name': '<Category "7PC Duofecta">', 'clean': '7PC Duofecta',
		'variables': {'789k439l': {'any': '4qyn2371', '100': '810xn351'}}
	},
	'ps1duo': {
		'name': '<Category "PS1 Duofecta">', 'clean': 'PS1 Duofecta',
		'variables': {'789k439l': {'any': '4qyn2371', '100': '810xn351'}}
	},
	'6gentrifecta': {
		'name': '<Category "6th Gen Trifecta">', 'clean': '6th Gen Trifecta',
		'variables': {'789k439l': {'any': '4qyn2371', '100': '810xn351'}}
	},
	'fs': {
		'name': '<Category "Full Series">', 'clean': 'Full Series',
		'variables': {'789k439l': {'any': '4qyn2371', '100': '810xn351'}}
	},
	'gbcduo': {
		'name': '<Category "GBC Duofecta">', 'clean': 'GBC Duofecta',
		'variables': {'789k439l': {'any': '4qyn2371', '100': '810xn351'}}
	},
	'gbapenta': {
		'name': '<Category "GBA Pentafecta">', 'clean': 'GBA Pentafecta',
		'variables': {'789k439l': {'any': '4qyn2371', '100': '810xn351'}}
	},
	'handheldocto': {
		'name': '<Category "Handheld Octofecta">', 'clean': 'Handheld Octofecta',
		'variables': {'789k439l': {'any': '4qyn2371', '100': '810xn351'}}
	},
	'handheldoctofecta': {
		'name': '<Category "Handheld Octofecta">', 'clean': 'Handheld Octofecta',
		'variables': {'789k439l': {'any': '4qyn2371', '100': '810xn351'}}
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
	}
}

# Point to the docs if there is an error.
# Putting it as a constant means we don't need multiple
# references to it, and updating it just requires changing
# this one constant.
COMMAND_USAGE_DOC = "https://github.com/artfulinfo/hpsr-pb-bot/blob/main/README.md"
