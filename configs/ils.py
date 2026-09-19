#
# Individual Level Configs
#
# This file contains all the constants used for
# handling IL runs.
#
# As ILs are only ever used for main boards, these
# are just constants specific to variables or key
# names that represent IL boards. Some elements from
# normal.py are sourced from there.
#

# List of levels for a specific leaderboard.
# The structure of this constant is a multi-layer
# dictionary, where all the data is held to map to ILs.
#
# The top level key (in line with the main dictionary) has a name
# representing the internal key referencing this specific IL board.
#
# Its value is also a dictionary, which contains a key/value pair:
# - key name: the name of the IL itself.
# - key value: a dictionary which contains two key/value pairs to identify:
# -- the level ID, as given by speedrun.com
# -- the list of aliases provided by players which map to this level.
#
LEVELS_MAP = {
	"hp1_pc": {
		"Flipendo": {
			"level_id": "5d7ej0gw", "aliases": ["flipendo", "flipendochallenge", "flip", "flipchallenge", "flipendospell", "dada1"]
		},
		"Wingardium Leviosa": {
			"level_id": "kwj8kmn9", "aliases": ["wingardium", "wingardiumleviosa", "leviosa", "wingardiumleviosachallenge", "wingardiumspell", "charms"]
		},
		"Incendio": {
			"level_id": "owoemvod", "aliases": ["incendio", "incendiochallenge", "incendiospell", "herbology"]
		},
		"Forest Edge": {
			"level_id": "95k8mg09", "aliases": ["forest", "forestedge", "fireseeds"]
		},
		"Lumos": {
			"level_id": "ewpz26k9", "aliases": ["lumos", "lumoschallenge", "lumosspell", "dada2"]
		},
		"Potions": {
			"level_id": "o9xely6w", "aliases": ["potions", "ingredients", "dungeons", "snape"]
		},
		"Filch": {
			"level_id": "dqz1nrkd", "aliases": ["filch", "tower", "sneak"]
		},
		"Quidditch League": {
			"level_id": "z98ze679", "aliases": ["quidditch", "league", "quidditchleague"]
		},
		"Demo": {
			"level_id": "rdnlyx6w", "aliases": ["demo"]
		}
	},
	"hp2_pc": {
		"Rictusempra Challenge": {
			"level_id": "5wkp5k2d", "aliases": ["rictu", "rictusempra", "rictuchallenge", "rictusemprachallenge"]
		},
		"Skurge Challenge": {
			"level_id": "592520o9", "aliases": ["skurge", "skurgechallenge"]
		},
		"Diffindo Challenge": {
			"level_id": "29v24m3d", "aliases": ["diffindo", "diffindochallenge"]
		},
		"Spongify Challenge": {
			"level_id": "xd4x4029", "aliases": ["spongify", "spongifychallenge"]
		},
		"Willow": {
			"level_id": "y9m175x9", "aliases": ["willow", "whompingwillow"]
		},
		"Bicorn": {
			"level_id": "o9x3pk19", "aliases": ["bicorn", "dungeons"]
		},
		"Boomslang": {
			"level_id": "5wk15kpd", "aliases": ["boomslang"]
		},
		"Goyle": {
			"level_id": "rdq5xg1d", "aliases": ["goyle"]
		},
		"Slytherin": {
			"level_id": "5d7zolvw", "aliases": ["slytherin", "slytherincommonroom"]
		},
		"Forest": {
			"level_id": "kwj1n3zw", "aliases": ["forest", "forbiddenforest"]
		},
		"Aragog": {
			"level_id": "drp2v46w", "aliases": ["aragog"]
		},
		"Chamber": {
			"level_id": "owoqzlyd", "aliases": ["chamber", "chamberofsecrets"]
		},
		"Basilisk": {
			"level_id": "wlg3vx09", "aliases": ["basilisk"]
		},
		"Gold Cards": {
			"level_id": "xd1jq6do", "aliases": ["goldcards", "goldcardschallenge", "cards"]
		},
		"Gryffindor Challenge": {
			"level_id": "owo7py96", "aliases": ["gryffindor", "gryffindorchallenge", "bonus"]
		},
		"Demo": {
			"level_id": "z98zx519", "aliases": ["demo"]
		},
		"Demo 2": {
			"level_id": "495zp8m9", "aliases": ["demo2"]
		}
	},
	"hp3_pc": {
		"Carpe Retractum Challenge": {
			"level_id": "y9my5z09", "aliases": ["carpe", "carperetractum", "carpechallenge", "carperetractumchallenge", "dada"]
		},
		"Draconifors/Lapifors Challenge": {
			"level_id": "5wk8klxw",
			"aliases": ["draconifors", "lapifors", "draconiforslapifors", "draconiforschallenge", "lapiforschallenge", "transfig"]
		},
		"Glacius Challenge": {
			"level_id": "59230p6d",
			"aliases": ["glacius", "glaciuschallenge", "charms"]
		},
		"Carpe Retractum Final Exam": {
			"level_id": "29vjmpx9", "aliases": ["carpeexam", "carpefinal", "carpefinalexam", "carperetractumexam", "carperetractumfinalexam"]
		},
		"Draconifors/Lapifors Final Exam": {
			"level_id": "xd4n088w",
			"aliases": ["draconiforsexam", "lapiforsexam", "draconiforsfinal", "lapiforsfinal", "draconiforsfinalexam", "lapiforsfinalexam"]
		},
		"Glacius Final Exam": {
			"level_id": "xd0lkojd",
			"aliases": ["glaciusexam", "glaciusfinal", "glaciusfinalexam"]
		}
	},
	"hp4": {
		"First Task": {
			"level_id": "ldyq7lpw", "aliases": ["task1", "firsttask", "dragons", "triwizardtask1"]
		},
		"Second Task": {
			"level_id": "gdrr46ed", "aliases": ["task2", "secondtask", "lake", "triwizardtask2"]
		},
		"Third Task": {
			"level_id": "nwl0x4ow", "aliases": ["task3", "thirdtask", "maze", "triwizardtask3"]
		},
		"Dugbog Avifors": {
			"level_id": "ywe0kxl9", "aliases": ["dugbog", "avifors", "dugbogavifors", "moody1", "moodyschallenge1"]
		},
		"Levitation Challenge": {
			"level_id": "69z7oexw", "aliases": ["levitation", "wingardium1", "moodyschallenge2"]
		},
		"Exploding Cauldrons": {
			"level_id": "r9g60qjw", "aliases": ["cauldrons", "explodingcauldrons", "moodyschallenge3"]
		},
		"Bubotuber Fling": {
			"level_id": "o9x65r39", "aliases": ["bubotuber", "bubotuberfling", "moodyschallenge4"]
		},
		"Tower Blocks": {
			"level_id": "495poxmw", "aliases": ["tower", "towerblocks", "moodyschallenge5"]
		}
	},
	"hp5": {
		"Exploding Snap - Traditional": {
			"level_id": "592mgr7w", "aliases": ["snaptrad", "explodingsnaptrad", "snaptraditional", "snap1", "es1", "explodingsnaptraditional"]
		},
		"Exploding Snap - Match": {
			"level_id": "29vge0q9", "aliases": ["snapmatch", "explodingsnapmatch", "snap2", "es2", "explodingsnapmatch"]
		},
		"Gobstones - Traditional": {
			"level_id": "xd4p7eqd", "aliases": ["gobstonestrad", "stonestrad", "gobstonestraditional", "stonestraditional"]
		},
		"Gobstones - Jack Stone": {
			"level_id": "xd0prnmw", "aliases": ["gobstonesjack", "stonesjack", "jack", "jackstone", "gobstonesjackstone"]
		},
		"Gobstones - Snake Pit": {
			"level_id": "rw62pgpd", "aliases": ["gobstonessnake", "stonessnake", "snake", "snakepit", "gobstonessnakepit"]
		},
		"Gryffindor Chess": {
			"level_id": "n93k5z2w", "aliases": ["chess1", "gryffindor", "gryffindorchess"]
		},
		"Slytherin Chess": {
			"level_id": "z98pv4rw", "aliases": ["chess2", "slytherin", "slytherinchess"]
		},
		"Ravenclaw Chess": {
			"level_id": "rdn3j45w", "aliases": ["chess3", "ravenclaw", "ravenclawchess"]
		}
	},
	"hp72": {
		"Gringotts": {
			"level_id": "ldyl54j9", "aliases": ["gringotts"]
		},
		"The Streets of Hogsmeade": {
			"level_id": "gdr68k8d", "aliases": ["hogsmeade"]
		},
		"A Problem of Security": {
			"level_id": "nwl4ykp9", "aliases": ["security"]
		},
		"The Basilisk Fang": {
			"level_id": "ywexjzq9", "aliases": ["basilisk", "fang"]
		},
		"A Job to Do": {
			"level_id": "69zeqm69", "aliases": ["job", "jobtodo"]
		},
		"A Giant Problem": {
			"level_id": "r9gqjkqd", "aliases": ["giant", "giantproblem"]
		},
		"The Lost Diadem": {
			"level_id": "o9xrzm69", "aliases": ["diadem", "lostdiadem"]
		},
		"The Battle of Hogwarts": {
			"level_id": "495xrv2d", "aliases": ["battle", "hogwartsbattle", "hogwarts"]
		},
		"Surrender": {
			"level_id": "rdq436m9", "aliases": ["surrender"]
		},
		"A Turn of Events": {
			"level_id": "5d7qe65w", "aliases": ["events", "turnofevents"]
		},
		"Not my Daughter": {
			"level_id": "kwj48orw", "aliases": ["daughter", "notmydaughter"]
		},
		"Voldemort's Last Stand": {
			"level_id": "owo4egv9", "aliases": ["voldemort", "laststand", "voldemortslaststand"]
		}
	}
}

# Internal key mapping
# This ensures multiple combinations of internal keys become the same
# internal key value. Used for some game boards where the game is the
# same on multiple platforms.
INTERNAL_KEY_MAPPING = {
	"hp4": ["hp4_pc", "hp4_ps2", "hp4_xbox", "hp4_gcn"],
	"hp5": ["hp5_pc", "hp5_ps2", "hp5_ps3", "hp5_xbox", "hp5_wii"],
	"hp72": ["hp72_pc", "hp72_ps3", "hp71_xbox", "hp71_wii", "hp7.1_pc", "hp7.1_ps3", "hp7.1_xbox", "hp7.1_wii"]
}
