#
# Harry Potter
#
# Contains all the game mapping data for Harry Potter normal boards.
#
GAME_CONFIG = "nm"
GAME_MAP_DATA = {
	"hp1": {
		"name": "Harry Potter and the Philosopher's Stone",
		"platforms": ["ps1", "ps2", "xbox", "gcn", "pc", "gba", "gbc"],
		"slugs": {
			"hp1ps1": ["hp1_ps1"],
			"hp1pc": ["hp1_pc"],
			"hp1_6th_gen": ["hp1_ps2", "hp1_xbox", "hp1_gcn"],
			"hp1gba": ["hp1_gba"],
			"hp1gbc": ["hp1_gbc"]
		}
	},
	"hp2": {
		"name": "Harry Potter and the Chamber of Secrets",
		"platforms": ["ps1", "ps2", "xbox", "gcn", "pc", "gba", "gbc"],
		"slugs": {
			"hp2ps1": ["hp2_ps1"],
			"hp2pc": ["hp2_pc"],
			"hp2ps2": ["hp2_ps2"],
			"hp2_6th_gen": ["hp2_xbox", "hp2_gcn"],
			"hp2gba": ["hp2_gba"],
			"hp2gbc": ["hp2_gbc"]
		}
	},
	"hp3": {
		"name": "Harry Potter and the Prisoner of Azkaban",
		"platforms": ["ps2", "xbox", "gcn", "pc", "gba"],
		"slugs": {
			"hp3pc": ["hp3_pc"],
			"hp3_6th_gen": ["hp3_ps2", "hp3_xbox", "hp3_gcn"],
			"hp3gba": ["hp3_gba"]
		}
	},
	"hp4": {
		"name": "Harry Potter and the Goblet of Fire",
		"platforms": ["ps2", "xbox", "gcn", "pc", "gba", "ds"],
		"slugs": {
			"hp4": ["hp4_pc", "hp4_ps2", "hp4_xbox", "hp4_gcn"],
			"hp4gba": ["hp4_gba", "hp4_ds"]
		}
	},
	"hp5": {
		"name": "Harry Potter and the Order of the Phoenix",
		"platforms": ["ps2", "ps3", "xbox", "wii", "x360", "pc", "gba", "ds"],
		"slugs": {
			"hp5": ["hp5_pc", "hp5_ps2", "hp5_ps3", "hp5_xbox", "hp5_x360", "hp5_wii"],
			"hp5gbads": ["hp5_gba", "hp5_ds"]
		}
	},
	"hp6": {
		"name": "Harry Potter and the Half Blood Prince",
		"platforms": ["ps2", "ps3", "xbox", "wii", "x360", "pc", "ds"],
		"slugs": {
			"hp6": ["hp6_pc", "hp6_ps2", "hp6_ps3", "hp6_xbox", "hp6_x360", "hp6_wii"],
			"hp6ds": ["hp6_ds"]
		}
	},
	"hp7.1": {
		"name": "Harry Potter and the Deathly Hallows Part 1",
		"aliases": ["hp71", "hp7p1"],
		"platforms": ["ps3", "xbox", "wii", "x360", "pc", "ds"],
		"slugs": {
			"hp7p1": [
				"hp71_ps3", "hp71_xbox", "hp71_pc", "hp71_wii", "hp7p1_ps3", "hp7p1_xbox",
				"hp7p1_pc", "hp7p1_wii", "hp7.1_ps3", "hp7.1_xbox", "hp7.1_pc", "hp7.1_wii"
			],
			"hp7p1ds": ["hp7.1_ds", "hp71_ds", "hp7p1_ds"]
		}
	},
	"hp7.2": {
		"name": "Harry Potter and the Deathly Hallows Part 2",
		"aliases": ["hp72", "hp7p2"],
		"platforms": ["ps3", "xbox", "wii", "x360", "pc", "ds"],
		"slugs": {
			"hp7p2": [
				"hp72_pc", "hp7.2_pc", "hp7p2_pc", "hp7.2_ps3", "hp7.2_ps3", "hp7p2_ps3",
				"hp7.2_xbox", "hp7.2_xbox", "hp7p2_xbox", "hp7.2_wii" "hp7.2_wii", "hp7p2_wii"
			],
			"hp7p2ds": ["hp7.2_ds", "hp72_ds", "hp7p2_ds"]
		}
	},
	"qwc": {
		"name": "Harry Potter: Quidditch World Cup",
		"aliases": ["hpqwc"],
		"platforms": ["gba", "gcn", "ps2", "xbox", "pc"],
		"slugs": {
			"hpquidditch": ["qwc_pc", "qwc_ps2", "qwc_gcn", "qwc_xbox"],
			"quidditch_gba": ["qwc_gba"]
		}
	},
	"legacy": {
		"name": "Hogwarts Legacy",
		"aliases": ["hl", "hogwartslegacy"],
		"platforms": ["ps4", "ps5", "pc", "xbone", "xbss", "xbsx"],
		"slug": "legacy"
	}
}
