#
# Hogwarts Legacy
#
# Contains all the leaderboard data for Hogwarts Legacy,
# both main boards and CE's
#
LEADERBOARD_DATA = {
	"legacy_pc": {
		"categories": {
			"Kill Ranrok": {
				"aliases": ["ranrok", "killranrok"], "board_id": "mke8rznk", "internal_name": "ranrok"
			},
			"All Quests": {
				"aliases": ["aq", "quests", "allq", "allquests"], "board_id": "5dwv880k", "internal_name": "allq"
			}
		},
		"ranrok": {
			"variables": [
				{"var_id": "e8mqwzvn", "value_id": "10vomkpl"},
				{"name": "story", "var_id": "r8r4kz2n", "value_id": "1dkjyxgl"},
				{"name": "hard", "var_id": "r8r4kz2n", "value_id": "q8kx0w6q"}
			]
		},
		"any": {
			"variables": [
				{"var_id": "e8mqwzvn", "value_id": "10vomkpl"},
				{"name": "story", "var_id": "r8r4kz2n", "value_id": "1dkjyxgl"},
				{"name": "hard", "var_id": "r8r4kz2n", "value_id": "q8kx0w6q"}
			]
		},
		"100": {
			"variables": [
				{"var_id": "e8mqwzvn", "value_id": "10vomkpl"},
				{"name": "story", "var_id": "r8r4kz2n", "value_id": "1dkjyxgl"},
				{"name": "hard", "var_id": "r8r4kz2n", "value_id": "q8kx0w6q"}
			]
		},
		"allq": {
			"variables": [
				{"var_id": "e8mqwzvn", "value_id": "10vomkpl"},
				{"name": "story", "var_id": "r8r4kz2n", "value_id": "1dkjyxgl"},
				{"name": "hard", "var_id": "r8r4kz2n", "value_id": "q8kx0w6q"}
			]
		}
	},
	"legacy_ce": {
		"categories": {
			"First Day": {"aliases": ["fd", "first", "firstday"], "internal_name": "fd"},
			"All Beasts": {"aliases": ["ab", "allb", "allbeasts"], "internal_name": "allb"},
			"All Achievements": {"aliases": ["aa", "alla", "allachievements"], "internal_name": "alla"},
			"Dark Arts%": {"aliases": ["da", "darkarts", "darkarts%"], "internal_name": "da"},
			"Flight School": {"aliases": ["fs", "flight", "flightschool"], "internal_name": "fs"},
			"Map Chamber": {"aliases": ["mc", "map", "chamber", "mapchamber"], "internal_name": "mc"},
			"First Trial": {"aliases": ["ft1", "trial1", "firsttrial", "1sttrial", "percival", "rackham"], "internal_name": "t1"},
			"Second Trial": {"aliases": ["st", "trial2", "secondtrial", "2ndtrial", "charles", "rookwood"], "internal_name": "t2"},
			"Third Trial": {"aliases": ["tt", "trial3", "thirdtrial", "3rdtrial", "niamh", "fitzgerland"], "internal_name": "t3"},
			"Fourth Trial": {"aliases": ["ft4", "trial4", "fourthtrial", "4thtrial", "sanbakar", "bakar"], "internal_name": "t4"}
		},
		"sub_categories": {
			"Intro": ["intro"],
			"No Intro": ["ni", "nointro", "noint"]
		},
		"legacy_fd": {
			"board": "First Day",
			"board_id": "wdm1on4d",
			"variables": [
				{"name": "intro", "var_id": "dlo9jj5l", "value_id": "qyz57m61"},
				{"name": "nointro", "aliases": ["ni", "noint"], "var_id": "dlo9jj5l", "value_id": "ln8de7ol"},
				{"name": "story", "var_id": "jlz2447l", "value_id": "10v06nol"},
				{"name": "hard", "var_id": "jlz2447l", "value_id": "qj7w2m7q"},
				{"name": "pc", "var_id": "9l79jjzn", "value_id": "q65yvovl"},
				{"name": "console", "var_id": "9l79jjzn", "value_id": "lmo82381"},
			]
		}
	}
}
