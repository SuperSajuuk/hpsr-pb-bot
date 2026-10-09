#
# Harry Potter and the Goblet of Fire
#
# Contains all the leaderboard data for HP4
#
LEADERBOARD_DATA = {
	"hp1_pc": {
		"categories": {
			"All Wizard Cards": {
				"aliases": ["awc", "wizardcards", "allwizardcards"],
				"board_id": "w20w3n5d",
				"internal_name": "awc"
			}
		}
	},
	"hp2_pc": {
		"categories": {
			"All Wizard Cards": {
				"aliases": ["awc", "wizardcards", "allwizardcards"],
				"board_id": "vdoo1yvd",
				"internal_name": "awc"
			},
			"Warpless": {
				"aliases": ["wl", "warpless"],
				"board_id": "02qpyqpd",
				"internal_name": "warpless"
			}
		}
	},
	"hp3_pc": {
		"categories": {
			"All Wizard Cards": {
				"aliases": ["awc", "wizardcards", "allwizardcards"],
				"board_id": "xk995n4k",
				"internal_name": "awc"
			},
			"All Requirements": {
				"aliases": ["ar", "allreq", "allreqs", "requirements", "allrequirements"],
				"board_id": "z27lr5gd",
				"internal_name": "allreq"
			}
		}
	},
	"hp4": {
		"categories": {
			"All Shields": {
				"aliases": ["as", "shields", "allshields"],
				"board_id": "wkp197jk",
				"internal_name": "allshields"
			}
		},
		"any": {
			"variables": [
				{"name": "1p", "default": True, "aliases": ["1player"], "var_id": "dlo3pjrl", "value_id": "5lerwd5q"},
				{"name": "2p", "aliases": ["2players"], "var_id": "dlo3pjrl", "value_id": "klr786oq"},
				{"name": "3p", "aliases": ["3players"], "var_id": "dlo3pjrl", "value_id": "gq7gyzyq"}
			]
		},
		"100": {
			"variables": [
				{"name": "1p", "default": True, "aliases": ["1player"], "var_id": "dlo3pjrl", "value_id": "5lerwd5q"},
				{"name": "2p", "aliases": ["2players"], "var_id": "dlo3pjrl", "value_id": "klr786oq"},
				{"name": "3p", "aliases": ["3players"], "var_id": "dlo3pjrl", "value_id": "gq7gyzyq"}
			]
		},
		"allshields": {
			"variables": [
				{"name": "1p", "default": True, "aliases": ["1player"], "var_id": "dlo3pjrl", "value_id": "5lerwd5q"},
				{"name": "2p", "aliases": ["2players"], "var_id": "dlo3pjrl", "value_id": "klr786oq"},
				{"name": "3p", "aliases": ["3players"], "var_id": "dlo3pjrl", "value_id": "gq7gyzyq"}
			]
		}
	},
	"hp4_gba": {
		"any": {
			"variables": [{"var_id": "j84k0x2n", "value_id": "21gjm281"}]
		},
		"100": {
			"variables": [{"var_id": "j84k0x2n", "value_id": "21gjm281"}]
		}
	},
	"hp4_ds": {
		"any": {
			"variables": [
				{"name": "console", "default": True, "var_id": "j84k0x2n", "value_id": "jqz6jx81"},
				{"name": "emulator", "var_id": "j84k0x2n", "value_id": "rqv8m951"}
			],
		},
		"100": {
			"variables": [
				{"name": "console", "default": True, "var_id": "j84k0x2n", "value_id": "jqz6jx81"},
				{"name": "emulator", "var_id": "j84k0x2n", "value_id": "rqv8m951"}
			]
		}
	},
	"hp5gbads": {
		"categories": {
			"Any% NSC": {
				"aliases": ["nsc", "nosavecorrupt", "anynsc", "anynosavecorrupt", "any%nsc", "any%nosavecorrupt"],
				"internal_name": "anynsc"
			}
		},
		"any": {
			"variables": [
				{"name": "gba", "default": True, "var_id": "r8r4pv5n", "value_id": "qyzn3841"},
				{"name": "emulator", "var_id": "r8r4pv5n", "value_id": "jq6eyz3l"},
				{"name": "ds", "var_id": "r8r4pv5n", "value_id": "5lmm8gjl"}
			]
		},
		"100": {
			"variables": [
				{"name": "gba", "default": True, "var_id": "5lyx4k2n", "value_id": "ln85rk0l"},
				{"name": "emulator", "var_id": "5lyx4k2n", "value_id": "81w0e5ol"},
				{"name": "ds", "var_id": "5lyx4k2n", "value_id": "zqovmrp1"}
			]
		},
		"anynsc": {
			"variables": [
				{"name": "gba", "default": True, "var_id": "rn1y09on", "value_id": "qj7gjeeq"},
				{"name": "emulator", "var_id": "rn1y09on", "value_id": "10vx39wl"}
			]
		}
	},
	"hp6": {
		"categories": {
			"All Crests": {
				"aliases": ["ac", "crests", "allcrests"],
				"board_id": "xd17168d",
				"internal_name": "allc"
			}
		}
	},
	"hpquidditch": {
		"categories": {
			"Beat Hogwarts Cup": {"aliases": ["bhc", "hogwarts", "hogwartscup", "beathogwarts", "beathogwartscup"], "internal_name": "bhc"},
			"Beat World Cup": {"aliases": ["bwc", "world", "worldcup", "beatworld", "beatworldscup"], "internal_name": "bwc"},
			"Beat the Tutorial": {"aliases": ["btt", "tutorial", "beattutorial", "beatthetutorial"], "internal_name": "btt"}
		}
	}
}
