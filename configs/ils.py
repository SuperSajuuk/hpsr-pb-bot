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
	}
}
