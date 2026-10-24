#
# Harry Potter Custom Content
#
# Contains all the leaderboard data for the HPCC board
#
ROOT_KEY = "hpcc"
LEADERBOARD_DATA = {
	"board_type": "cc",
	"categories": {
		"[1PC] Fixed Movement": {
			"aliases": ["fm", "fixed", "movement", "fixedmovement", "1fm"], "board_id": "wkplrn82", "internal_name": "fm"
		},
		"[1PC] Restored": {
			"aliases": ["rs", "restored", "1rs"], "board_id": "w204ny5k", "internal_name": "rs"
		},
		"[1PC] Tourney Client": {
			"aliases": ["tc", "1tc", "1tourney", "tc1", "tourney1", "tourneyclient1", "1tourneyclient"], "board_id": "02q0y09k", "internal_name": "1tc"
		},
		"[2PC] Bingo": {
			"aliases": ["bingo", "2bingo"], "board_id": "wdm1r8od", "internal_name": "bingo"
		},
		"[2PC] Tourney Client": {
			"aliases": ["tc", "2tc", "2tourney", "tc2", "tourney2", "tourneyclient2", "2tourneyclient"], "board_id": "z27zn8ok", "internal_name": "2tc"
		}
	},
	"sub_categories": {
		"Any%": {
			"aliases": ["any", "any%"], "internal_name": "any"
		},
		"100%": {
			"aliases": ["100", "hundo", "100%"], "internal_name": "100"
		},
		"Glitchless": {
			"aliases": ["gl", "gless", "glitchless"], "internal_name": "gless"
		},
		"All Wizard Cards": {
			"aliases": ["awc", "wizardcards", "allwizardcards"], "internal_name": "awc"
		},
		"Warpless": {
			"aliases": ["wl", "wless", "warpless"], "internal_name": "wl"
		},
		"Single": {
			"aliases": ["single"], "internal_name": "single"
		},
		"Triple": {
			"aliases": ["triple"], "internal_name": "triple"
		},
		"Blackout": {
			"aliases": ["bo", "bout", "blackout"], "internal_name": "blackout"
		}
	},
	"metadata": {
		"Random Seed": {"aliases": ["random", "rs", "randomseed"]},
		"Set Seed": {"aliases": ["set", "ss", "setseed"]}
	},
	"hp_fm": {
		"variables": [
			{"name": "any", "var_id": "e8mp25x8", "value_id": "14o9nevq"},
			{"name": "100", "var_id": "e8mp25x8", "value_id": "12v98e4q"},
			{"name": "gless", "var_id": "e8mp25x8", "value_id": "192xwg8q"}
		]
	},
	"hp_rs": {
		"variables": [
			{"name": "any", "var_id": "ylpgx6vl", "value_id": "qj729meq"},
			{"name": "gless", "var_id": "ylpgx6vl", "value_id": "lmo2p3j1"}
		]
	},
	"hp_1tc": {
		"variables": [
			{"name": "any", "var_id": "ylpkge68", "value_id": "1w439g6q"},
			{"name": "gless", "var_id": "ylpkge68", "value_id": "1393p0y1"},
			{"name": "awc", "var_id": "ylpkge68", "value_id": "qvv397yq"}
		]
	},
	"hp_bingo": {
		"variables": [
			{"name": "single", "var_id": "0nwgdpk8", "value_id": "1w4792oq"},
			{"name": "triple", "var_id": "0nwgdpk8", "value_id": "qoxj9epq"},
			{"name": "blackout", "aliases": ["bo", "bout"], "var_id": "0nwgdpk8", "value_id": "139xpkd1"},
			{"name": "random", "var_id": "7893m168", "value_id": "qvvx927q"},
			{"name": "set", "var_id": "7893m168", "value_id": "le2n5y5l"}
		]
	},
	"hp_2tc": {
		"variables": [
			{"name": "wl", "var_id": "r8rrqw28", "value_id": "12v2j7vq"},
			{"name": "gless", "var_id": "r8rrqw28", "value_id": "le2eyppl"},
			{"name": "awc", "var_id": "r8rrqw28", "value_id": "1pyxk9e1"}
		]
	}
}
