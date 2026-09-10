#
# Category Extension Configs
#
# This file contains all the constants used for
# handling Category Extensions.
#

# Game mapping.
# Key names must be abbreviations that would be called in !run ce
# commands. The value of key is a dictionary which contains two
# keys: a human-readable name and the Slug URL ID.
GAME_MAP = {
	"hp": {"name": "Harry Potter Category Extensions", "id": "hpce"},
	"rac": {"name": "Ratchet & Clank Category Extensions", "id": "racextras"}
}

# Sub-category mapping.
# This refers to the second board under the top level board.
# The key name must be the human-readable board name: the value
# of each key is a list containing aliases that get mapped by
# user input.
SUB_CATEGORY_MAP = {
	"100% Glitchless": ["100gless", "hundogless", "100glitchless", "hundoglitchless"],
	"AWC Glitchless": ["awcgless", "awcglitchless", "allwizardcardsgless", "allwizardcardsglitchless"],
	"Boostless": ["boostless"],
	"Cutscene%": ["cs", "cutscene", "cutscene%"],
	"Chungus%": ["chungus", "chungus%"],
	"Harry Potter Wizard Card": ["hpwc", "hpwizardcard", "harrypotterwc", "harrypotterwizardcard"],
	"High Jump": ["hj", "highjump"],
	"Jumpless": ["jl", "jumpless"],
	"Lowcast": ["lc", "lowcast"],
	"NG+": ["ng", "ngplus", "newgameplus"],
	"No Major Glitches": ["nmg", "nomajorglitches"],
	"All Vanishing Cards - 1P": ["avc1p", "allvanishingcards1p", "avc1player", "allvanishingcards1player"],
	"All Vanishing Cards - 2P": ["avc2p", "allvanishingcards2p", "avc2player", "allvanishingcards2player", "avc2players", "allvanishingcards2players"],
	"All Vanishing Cards - 3P": ["avc3p", "allvanishingcards3p", "avc3player", "allvanishingcards3player", "avc3players", "allvanishingcards3players"],
	"All Crests": ["allcrests"],
	"All Minigames": ["amg", "allmg", "allminigames"],
	"All Portraits": ["ap", "allp", "allportraits"],
	"All Requirements": ["allreq", "allreqs", "allrequirements"],
	"All Shields": ["allshields"],
	"All Symbols": ["as", "allsymbols"],
	"Chess%": ["chess"],
	"Potions Rush": ["pr", "potions", "potionsrush"],
	"All Wizard Cards": ["awc", "allwizardcards"],
	"Superspeed": ["ss", "superspeed"],
	"PC Glitchless Duofecta": ["glessduo", "glessduofecta", "glitchlessduo", "glitchlessduofecta", "pcglessduo", "pcglessduofecta", "pcglitchlessduo", "pcglitchlessduofecta"],
	"RPG Trifecta": ["rpgtri", "rpgtrifecta"],
	"HP1 PC": ["hp1pc", "1pc"],
	"HP2 PC": ["hp2pc", "2pc"],
	"HP3 PC": ["hp3pc", "3pc"],
	"HP4 PC": ["hp4pc", "4pc"],
	"HP5 PC": ["hp5pc", "5pc"],
	"HP6 PC": ["hp6pc", "6pc"],
	"HP7.1 PC": ["hp71pc", "71pc"],
	"HP7.2 PC": ["hp72pc", "72pc"],
	"HP1 PS1": ["1ps1", "hp1ps1"],
	"HP2 PS1": ["2ps1", "hp2ps1"],
	"HP2 6th Gen": ["hp26thgen", "hp2xbox", "hp2gcn"],
	"HP3 6th Gen": ["hp36thgen", "hp3xbox", "hp3gcn", "hp3ps2"],
	"HP1 GBA": ["hp1gba", "1gba"],
	"HP2 GBA": ["hp2gba", "2gba"],
	"HP3 GBA": ["hp3gba", "3gba"],
	"QWC GBA": ["qwcgba", "quidditchworldcupgba"],
	"HP6 DS": ["hp6ds", "6ds"],
	"HP7.1 DS": ["hp71ds", "71ds"],
	"HP7.2 DS": ["hp72ds", "72ds"],
	"HP1 Any%": ["hp1any", "1any"],
	"HP2 Any%": ["hp2any", "2any"],
	"HP3 Any%": ["hp3any", "3any"],
	"HP4 Any%": ["hp4any", "4any"],
	"HP5 Any%": ["hp5any", "5any"],
	"HP6 Any%": ["hp6any", "6any"],
	"HP7.1 Any%": ["hp71any", "71any"],
	"HP7.2 Any%": ["hp72any", "72any"],
	"HP1 100%": ["hp1100", "hp1hundo", "1100", "1hundo"],
	"HP2 100%": ["hp2100", "hp2hundo", "2100", "2hundo"],
	"HP3 100%": ["hp3100", "hp3hundo", "3100", "3hundo"],
	"HP4 100%": ["hp4100", "hp4hundo", "4100", "4hundo"],
	"HP5 100%": ["hp5100", "hp5hundo", "5100", "5hundo"],
	"HP6 100%": ["hp6100", "hp6hundo", "6100", "6hundo"],
	"HP7.1 100%": ["hp71100", "hp71hundo", "71100", "71hundo"],
	"HP7.2 100%": ["hp72100", "hp72hundo", "72100", "72hundo"],
	"Hogwarts Challenge": ["hc", "hogwartschallenge"],
	"Wizarding World": ["ww", "wizardingworld"]
}

# Board aliases. Useful if you want multiple
# user input choices to display the appropriate label.
BOARD_ALIASES = {
	"1PC": ["1pc", "hp1pc"],
	"2PC": ["2pc", "hp2pc"],
	"3PC": ["3pc", "hp3pc"],
	"4PC": ["4pc", "hp4pc"],
	"5PC": ["5pc", "hp5pc"],
	"6PC": ["6pc", "hp6pc"],
	"Single Year": ["sy", "singleyear"],
	"Insane%": ["insane", "ins"],
	"Multiruns": ["mr", "hpmr", "multiruns", "hpmultiruns"],
	"1PS1": ["1ps1", "hp1ps1"],
	"2PS1": ["2ps1", "hp2ps1"],
	"4PSP": ["4psp", "hp4psp"],
	"5PSP": ["5psp", "hp5psp"],
	"DVD Games": ["dvd", "dvdgames", "hpdvdgames"]
}

# Board token aliases.
# This is used to map user input to the name that
# is used internally to reference a specific
# top-level board for a category extension.
BOARD_TOKEN_ALIASES = {
	"hpce": {
		"multirun": "mr",
		"multiruns": "mr",
		"singleyear": "sy",
		"dvdgames": "dvd",
		"hpdvdgames": "dvd"
	}
}

# Category aliases
# Like board aliases, this is used to map user input
# to the name that is used internally to reference
# a specific sub-board for a category extension.
CATEGORY_ALIASES = {
	"hpce": {
		"1pc": {
			"100gless": ["100gless", "hundogless", "100glitchless", "hundoglitchless"],
			"allchests": ["allchests"],
			"boostless": ["boostless"],
			"highjump": ["highjump", "hj"],
			"lowcast": ["lowcast", "lc"]
		},
		"2pc": {
			"100gless": ["100gless", "hundogless", "100glitchless", "hundoglitchless"],
			"allchests": ["allchests"],
			"awcgless": ["awcgless", "awcglitchless", "allwizardcardsgless", "allwizardcardsglitchless"],
			"boostless": ["boostless"],
			"chungus": ["chungus", "chungus%"],
			"cutscene": ["cutscene", "cs", "cutscene%"],
			"hpwc": ["hpwc", "hpwizardcard", "harrypotterwc", "harrypotterwizardcard"],
			"highjump": ["highjump", "hj"],
			"jumpless": ["jumpless", "jl"],
			"lowcast": ["lowcast", "lc"],
			"ng": ["ng", "ngplus", "newgameplus"],
			"nmg": ["nmg", "nomajorglitches"]
		},
		"3pc": {
			"highjump": ["highjump", "hj"],
		},
		"4pc": {
			"avc_1p": ["avc1p", "allvanishingcards1p", "avc1player", "allvanishingcards1player"],
			"avc_2p": ["avc2p", "allvanishingcards2p", "avc2player", "allvanishingcards2player", "avc2players", "allvanishingcards2players"],
			"avc_3p": ["avc3p", "allvanishingcards3p", "avc3player", "allvanishingcards3player", "avc3players", "allvanishingcards3players"]
		},
		"5pc": {
			"amg": ["amg", "allminigames"],
			"allportraits": ["ap", "allp", "allportraits"],
			"allsymbols": ["as", "allsymbols"],
			"chess": ["chess"]
		},
		"6pc": {
			"pr": ["pr", "potions", "potionsrush"]
		},
		"1ps1": {
			"awc": ["awc", "allwizardcards"],
			"ss": ["ss", "superspeed"],
			"ng": ["ng", "ngplus", "newgameplus"]
		},
		"2ps1": {
			"awc": ["awc", "allwizardcards"],
			"ss": ["ss", "superspeed"],
		},
		"4psp": {
			"any": ["any"],
			"100": ["100", "hundo"]
		},
		"5psp": {
			"any": ["any"],
			"100": ["100", "hundo"]
		},
		"mr": {
			"glessduo": ["glessduo", "glessduofecta", "glitchlessduo", "glitchlessduofecta", "pcglessduo", "pcglessduofecta", "pcglitchlessduo", "pcglitchlessduofecta"],
			"rpgtri": ["rpgtri", "rpgtrifecta"]
		},
		"insane": {
			"hp1_pc": ["hp1pc", "1pc"],
			"hp2_pc": ["hp2pc", "2pc"],
			"hp3_pc": ["hp3pc", "3pc"],
			"hp4_pc": ["hp4pc", "4pc"],
			"hp5_pc": ["hp5pc", "5pc"],
			"hp6_pc": ["hp6pc", "6pc"],
			"hp71_pc": ["hp71pc", "71pc"],
			"hp72_pc": ["hp72pc", "72pc"],
			"1ps1": ["1ps1", "hp1ps1"],
			"2ps1": ["2ps1", "hp2ps1"],
			"hp2_6th_gen": ["hp2_6th", "hp26th", "hp26thgen", "hp2xbox", "hp2gcn"],
			"hp3_6th_gen": ["hp3_6th", "hp36th", "hp36thgen", "hp3xbox", "hp3gcn", "hp3ps2"],
			"hp1_gba": ["hp1gba", "1gba"],
			"hp2_gba": ["hp2gba", "2gba"],
			"hp3_gba": ["hp3gba", "3gba"],
			"qwc_gba": ["qwcgba", "quidditchworldcupgba"],
			"hp6_ds": ["hp6ds", "6ds"],
			"hp71_ds": ["hp71ds", "71ds"],
			"hp72_ds": ["hp72ds", "72ds"]
		},
		"sy": {
			"hp1_any": ["hp1any", "1any"],
			"hp2_any": ["hp2any", "2any"],
			"hp3_any": ["hp3any", "3any"],
			"hp4_any": ["hp4any", "4any"],
			"hp5_any": ["hp5any", "5any"],
			"hp6_any": ["hp6any", "6any"],
			"hp71_any": ["hp71any", "71any"],
			"hp72_any": ["hp72any", "72any"],
			"hp1_100": ["hp1hundo", "hp1100", "1100", "1hundo"],
			"hp2_100": ["hp2hundo", "hp2100", "2100", "2hundo"],
			"hp3_100": ["hp3hundo", "hp3100", "3100", "3hundo"],
			"hp4_100": ["hp4hundo", "hp4100", "4100", "4hundo"],
			"hp5_100": ["hp5hundo", "hp5100", "5100", "5hundo"],
			"hp6_100": ["hp6hundo", "hp6100", "6100", "6hundo"],
			"hp71_100": ["hp71hundo", "hp71100", "71100", "71hundo"],
			"hp72_100": ["hp72hundo", "hp72100", "72100", "72hundo"],
		},
		"dvd": {
			"hc": ["hc", "hogwartschallenge"],
			"ww": ["ww", "wizardingworld"]
		}
	}
}
