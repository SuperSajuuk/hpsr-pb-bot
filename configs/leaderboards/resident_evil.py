#
# Resident Evil Series
#
# Contains all the leaderboard data for Resident Evil games.
#
LEADERBOARD_DATA = {
	"residentevil": {
		"categories": {
			"Jill": {"aliases": ["j", "jill"], "internal_name": "jill"},
			"Chris": {"aliases": ["c", "chris"], "internal_name": "chris"}
		},
		"platform_categories": {
			"PC": ["pc"],
			"EMU": ["ps1", "psx"],
			"PlayStation": ["ps2", "ps3", "ps4", "ps5"],
			"Sega Saturn": ["saturn", "segasaturn", "ss"]
		},
		"metadata": {
			"PSN": {"aliases": ["psn"], "cat_override": "PSN"},
			"PC - Cutscene Skip": {"aliases": ["csskip", "cutsceneskip"], "cat_override": "PC - Cutscene Skip"},
			"Bad Ending": {"aliases": ["bade", "badending"], "var_key": "bade"},
			"Best Ending": {"aliases": ["beste", "bestending"], "var_key": "beste"},
			"Major Glitches": {"aliases": ["mg", "majorglitches"], "var_key": "mg"},
			"No Restriction": {"aliases": ["nr", "nores", "norestriction"], "var_key": "nores"},
			"Knife Only": {"aliases": ["ko", "knife", "knifeonly"], "var_key": "ko"},
			"Original": {"aliases": ["o", "orig", "original"], "var_key": "orig"},
			"Arrange": {"aliases": ["a", "arrange"], "var_key": "arrange"},
			"DuckStation": {"aliases": ["ds", "duck", "ducks", "duckstation"], "var_key": "ds", "no_extend": True},
			"Legacy Emu": {"aliases": ["le", "legacy", "lemu", "legacyemu"], "var_key": "le", "no_extend": True}
		},
		"jill": {
			"variables": [
				{"var_id": "p85077ng", "value_id": "21gny96l"},
				{"name": "bade", "var_id": "yn2koen5", "value_id": "5le2d2ml"},
				{"name": "beste", "var_id": "yn2koen5", "value_id": "0q5vkv7l"},
				{"name": "mg", "platform_vars": {
					"PC": {"var_id": "9l7rp9n1", "value_id": "9qjk6014"},
					"EMU": {"var_id": "dloregrl", "value_id": "jqzzr4gq"},
					"PlayStation": {"var_id": "9l7rgw9n", "value_id": "4qygv44q"},
					"PSN": {"var_id": "gnx2z3g8", "value_id": "21den35l"}
				}},
				{"name": "nmg", "platform_vars": {
					"PC": {"var_id": "9l7rp9n1", "value_id": "810kojqv"},
					"EMU": {"var_id": "dloregrl", "value_id": "21gzwgnl"},
					"PlayStation": {"var_id": "9l7rp9n1", "value_id": "5q8wxzgq"},
					"PSN": {"var_id": "gnx2z3g8", "value_id": "klr2dym1"}
				}},
				{"name": "nores", "var_id": "ql6m0x89", "value_id": "81py8yv1"},
				{"name": "ko", "var_id": "ql6m0x89", "value_id": "xqke7edq"},
				{"name": "orig", "var_id": "ylpy3klg", "value_id": "4qyzxn41"},
				{"name": "arrange", "var_id": "ylpy3klg", "value_id": "mln8y50l"},
				{"name": "ds", "var_id": "2lg3e66n", "value_id": "21dwdzjl"},
				{"name": "le", "var_id": "2lg3e66n", "value_id": "5q8oz6k1"}
			]
		},
		"chris": {
			"variables": [
				{"var_id": "p85077ng", "value_id": "jqznkg2q"},
				{"name": "bade", "var_id": "yn2koen5", "value_id": "5le2d2ml"},
				{"name": "beste", "var_id": "yn2koen5", "value_id": "0q5vkv7l"},
				{"name": "mg", "platform_vars": {
					"PC": {"var_id": "9l7rp9n1", "value_id": "9qjk6014"},
					"EMU": {"var_id": "dloregrl", "value_id": "jqzzr4gq"},
					"PlayStation": {"var_id": "9l7rgw9n", "value_id": "4qygv44q"},
					"PSN": {"var_id": "gnx2z3g8", "value_id": "21den35l"}
				}},
				{"name": "nmg", "platform_vars": {
					"PC": {"var_id": "9l7rp9n1", "value_id": "810kojqv"},
					"EMU": {"var_id": "dloregrl", "value_id": "21gzwgnl"},
					"PlayStation": {"var_id": "9l7rp9n1", "value_id": "5q8wxzgq"},
					"PSN": {"var_id": "gnx2z3g8", "value_id": "klr2dym1"}
				}},
				{"name": "nores", "var_id": "ql6m0x89", "value_id": "81py8yv1"},
				{"name": "ko", "var_id": "ql6m0x89", "value_id": "xqke7edq"},
				{"name": "orig", "var_id": "ylpy3klg", "value_id": "4qyzxn41"},
				{"name": "arrange", "var_id": "ylpy3klg", "value_id": "mln8y50l"},
				{"name": "ds", "var_id": "2lg3e66n", "value_id": "21dwdzjl"},
				{"name": "le", "var_id": "2lg3e66n", "value_id": "5q8oz6k1"}
			]
		}
	}
}
