#
# Crash Bandicoot
#
# Contains all the leaderboard data for Crash Bandicoot games.
#
LEADERBOARD_DATA = {
	"crashnst": {
		"categories": {
			"Crash Bandicoot": {"aliases": ["c1", "cb1", "crash1"], "board_id": "ndxp0312", "internal_name": "cb1"},
			"CB2: Cortex Strikes Back": {"aliases": ["c2", "cb2", "crash2"], "board_id": "w2015qvk", "internal_name": "cb2"},
			"CB3: Warped": {"aliases": ["c3", "cb3", "crash3"], "board_id": "wdm475xd", "internal_name": "cb3"}
		},
		"platform_mapping": {
			"pc": ["pc"],
			"console": ["ps4", "ps5", "xbone", "xbsx", "xbss", "switch"]
		},
		"metadata": {
			"All Gems": {"aliases": ["ag", "allg", "gems", "allgems"]},
			"102%": {"aliases": ["102", "102%"]},
			"105%": {"aliases": ["105", "105%"]},
			"108%": {"aliases": ["108", "108%"]},
			"Any% No OOB": {"aliases": ["nooob", "anynooob", "any%nooob"]},
			"Secret Ending": {"aliases": ["se", "secret", "ending", "secretending"]},
			"Major Glitches": {"aliases": ["mg", "majorglitches"]}
		},
		"cb1": {
			"variables": [
				{"name": "any", "var_id": "789763nw", "value_id": "8149w3vq"},
				{"name": "ag", "aliases": ["allg", "gems", "allgems"], "var_id": "789763nw", "value_id": "81p4xgv1"},
				{"name": "105", "aliases": ["105%"], "var_id": "789763nw", "value_id": "21gex06l"},
				{"name": "se", "aliases": ["secret", "ending", "secretending"], "var_id": "789763nw", "value_id": "9qjjzgoq"},
				{"name": "mg", "aliases": ["majorglitches"], "var_id": "jlz2zyql", "value_id": "1dk4yn5l"},
				{"name": "nmg", "var_id": "jlz2zyql", "value_id": "q8ke033q"},
				{"name": "pc", "var_id": "onv7o7wn", "value_id": "21dn4dpl"},
				{"name": "console", "var_id": "onv7o7wn", "value_id": "5q83ezy1"}
			]
		},
		"cb2": {
			"variables": [
				{"name": "any", "var_id": "38d2m4n0", "value_id": "81w7065q"},
				{"name": "100", "var_id": "38d2m4n0", "value_id": "0q5x4or1"},
				{"name": "102", "aliases": ["102%"], "var_id": "38d2m4n0", "value_id": "zqojvz21"},
				{"name": "pc", "var_id": "0nw7z758", "value_id": "810y5mol"},
				{"name": "console", "var_id": "0nw7z758", "value_id": "9qjoz47l"}
			]
		},
		"cb3": {
			"variables": [
				{"name": "any", "var_id": "5ly2x284", "value_id": "5lenxpzl"},
				{"name": "nooob", "aliases": ["anynooob", "any%nooob"], "var_id": "5ly2x284", "value_id": "192xez8q"},
				{"name": "108", "aliases": ["108%"], "var_id": "5ly2x284", "value_id": "xqkzjd9q"},
				{"name": "pc", "var_id": "68koeoqn", "value_id": "21g6j46q"},
				{"name": "console", "var_id": "68koeoqn", "value_id": "jqzw652q"}
			]
		}
	}
}
