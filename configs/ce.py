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

# Board aliases. Useful if you want multiple
# user input choices to display the appropriate label.
BOARD_ALIASES = {
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
			"avc": ["avc", "vanishingcards", "allvanishingcards"]
		},
		"5pc": {
			"amg": ["amg", "allminigames"],
			"allp": ["ap", "allp", "allportraits"],
			"alls": ["as", "alls", "allsymbols"],
			"chess": ["chess", "chess%"]
		},
		"6pc": {
			"pr": ["pr", "potions", "potionsrush"]
		},
		"1ps1": {
			"awc": ["awc", "allwizardcards"],
			"superspeed": ["ss", "superspeed"],
			"ng": ["ng", "ngplus", "newgameplus", "ng+"]
		},
		"2ps1": {
			"awc": ["awc", "allwizardcards"],
			"superspeed": ["ss", "superspeed"],
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
			"hc": ["hc", "hogwarts", "hogwartschallenge"],
			"ww": ["ww", "wizarding", "wizardingworld"]
		}
	},
	"legacy_ce": {
		"fd": {

		}
	}
}
