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
	"legohp": {"name": "LEGO Harry Potter Category Extensions", "id": "lhpce"},
	"rac": {"name": "Ratchet & Clank Category Extensions", "id": "racextras"},
	"legacy": {"name": "Hogwarts Legacy Category Extensions", "id": "legacy_ce"}
}

# Sub-category mapping.
# This refers to the second board under the top level board.
# The key name must be the human-readable board name: the value
# of each key is a list containing aliases that get mapped by
# user input.
SUB_CATEGORY_MAP = {
	"100% Glitchless": ["100gless", "hundogless", "100%gless", "100glitchless", "hundoglitchless", "100%glitchless"],
	"AWC Glitchless": ["awcgless", "awcglitchless", "allwizardcardsgless", "allwizardcardsglitchless"],
	"Boostless": ["bl", "boostless"],
	"Cutscene%": ["cs", "cutscene", "cutscene%"],
	"Chungus%": ["chungus", "chungus%"],
	"Harry Potter Wizard Card": ["hpwc", "hpwizardcard", "harrypotterwc", "harrypotterwizardcard"],
	"High Jump": ["hj", "highjump"],
	"Jumpless": ["jl", "jumpless"],
	"Lowcast": ["lc", "lowcast"],
	"NG+": ["ng", "ngplus", "newgameplus", "ng+"],
	"No Major Glitches": ["nmg", "nomajorglitches"],
	"All Vanishing Cards - 1P": ["avc1p", "allvanishingcards1p", "avc1player", "allvanishingcards1player"],
	"All Vanishing Cards - 2P": ["avc2p", "allvanishingcards2p", "avc2player", "allvanishingcards2player", "avc2players", "allvanishingcards2players"],
	"All Vanishing Cards - 3P": ["avc3p", "allvanishingcards3p", "avc3player", "allvanishingcards3player", "avc3players", "allvanishingcards3players"],
	"All Chests": ["ac", "allchests"],
	"All Minigames": ["amg", "allmg", "allminigames"],
	"All Portraits": ["ap", "allp", "allportraits"],
	"All Symbols": ["as", "allsymbols"],
	"Chess%": ["chess", "chess%"],
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
	"HP1": ["hp1"],
	"HP2": ["hp2"],
	"HP3": ["hp3"],
	"HP4": ["hp4"],
	"HP5": ["hp5"],
	"HP6": ["hp6"],
	"HP7.1": ["hp71", "hp7.1", "7.1", "hp7p1"],
	"HP7.2": ["hp72", "hp7.2", "7.2", "hp7p2"],
	"Hogwarts Challenge": ["hc", "hogwartschallenge"],
	"Wizarding World": ["ww", "wizardingworld"],
	"Intro": ["intro"],
	"No Intro": ["nointro", "noint"]
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
	"Insane%": ["insane", "ins", "insane%"],
	"Multiruns": ["mr", "hpmr", "multiruns", "hpmultiruns"],
	"1PS1": ["1ps1", "hp1ps1"],
	"2PS1": ["2ps1", "hp2ps1"],
	"4PSP": ["4psp", "hp4psp"],
	"5PSP": ["5psp", "hp5psp"],
	"DVD Games": ["dvd", "dvdgames", "hpdvdgames"],
	"First Day": ["fd", "first", "firstday"],
	"All Beasts": ["ab", "allb", "allbeasts"],
	"All Achievements": ["aa", "alla", "allachievements"],
	"Dark Arts%": ["da", "darkarts", "darkarts%"],
	"Flight School": ["fs", "flight", "flightschool"],
	"Map Chamber": ["mc", "map", "chamber", "mapchamber"],
	"First Trial": ["ft1", "trial1", "firsttrial", "1sttrial", "percival", "rackham"],
	"Second Trial": ["st", "trial2", "secondtrial", "2ndtrial", "charles", "rookwood"],
	"Third Trial": ["tt", "trial3", "thirdtrial", "3rdtrial", "niamh", "fitzgerland"],
	"Fourth Trial": ["ft4", "trial4", "fourthtrial", "4thtrial", "sanbakar", "bakar"]
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
	},
	"legacy_ce": {
		"firstday": "fd"
	}
}

# Category aliases
# Like board aliases, this is used to map user input
# to the name that is used internally to reference
# a specific sub-board for a category extension.
CATEGORY_ALIASES = {
	"hpce": {
		"1pc": {
			"100gless": ["100gless", "100%gless", "hundogless", "100glitchless", "100%glitchless", "hundoglitchless"],
			"allchests": ["ac", "allchests"],
			"boostless": ["bl", "boostless"],
			"highjump": ["hj", "highjump"],
			"lowcast": ["lc", "lowcast"]
		},
		"2pc": {
			"100gless": ["100gless", "100%gless", "hundogless", "100glitchless", "100%glitchless", "hundoglitchless"],
			"allchests": ["ac", "allchests"],
			"awcgless": ["awcgless", "awcglitchless", "allwizardcardsgless", "allwizardcardsglitchless"],
			"boostless": ["bl", "boostless"],
			"chungus": ["chungus", "chungus%"],
			"cutscene": ["cutscene", "cs", "cutscene%"],
			"hpwc": ["hpwc", "hpwizardcard", "harrypotterwc", "harrypotterwizardcard"],
			"highjump": ["highjump", "hj"],
			"jumpless": ["jumpless", "jl"],
			"lowcast": ["lowcast", "lc"],
			"ng": ["ng", "ngplus", "newgameplus", "ng+"],
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
			"chess": ["chess", "chess%"]
		},
		"6pc": {
			"pr": ["pr", "potions", "potionsrush"]
		},
		"1ps1": {
			"awc": ["awc", "allwizardcards"],
			"ss": ["ss", "superspeed"],
			"ng": ["ng", "ngplus", "newgameplus", "ng+"]
		},
		"2ps1": {
			"awc": ["awc", "allwizardcards"],
			"ss": ["ss", "superspeed"],
		},
		"4psp": {
			"any": ["any", "any%"],
			"100": ["100", "hundo", "100%"]
		},
		"5psp": {
			"any": ["any", "any%"],
			"100": ["100", "hundo", "100%"]
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
			"hp1": ["hp1"],
			"hp2": ["hp2"],
			"hp3": ["hp3"],
			"hp4": ["hp4"],
			"hp5": ["hp5"],
			"hp6": ["hp6"],
			"hp71": ["hp71", "hp7.1", "7.1", "hp7p1"],
			"hp72": ["hp72", "hp7.2", "7.2", "hp7p2"]
		},
		"dvd": {
			"hc": ["hc", "hogwartschallenge"],
			"ww": ["ww", "wizardingworld"]
		}
	},
	"legacy_ce": {
		"fd": {

		}
	}
}
