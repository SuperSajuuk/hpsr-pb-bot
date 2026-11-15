#
# Normal Boards
#
# Contains all the game mapping data for normal boards.
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
			"hp1gbc": ["hp1_gbc"],
			"hpcc": ["hp1_cc"]
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
			"hp2gbc": ["hp2_gbc"],
			"hpcc": ["hp2_cc"]
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
	},
	"dbb": {
		"name": "Disney's Brother Bear",
		"aliases": ["disneysbrotherbear", "brotherbear"],
		"platforms": ["pc"],
		"slug": "disneys_brother_bear"
	},
	"r1": {
		"name": "Rayman",
		"ordering": "pf",
		"aliases": ["rayman", "rayman1"],
		"platforms": ["ps1", "psx", "pc", "ds", "gba", "ss", "saturn", "segasaturn", "aj", "jaguar", "atari", "atarijaguar"],
		"slug": "rayman_1"
	},
	"r3": {
		"name": "Rayman 3: Hoodlum Havoc",
		"ordering": "pf",
		"aliases": ["rayman3"],
		"platforms": ["gcn", "pc", "ps2", "hd", "ps3", "x360", "xss", "xbox"],
		"slug": "r3"
	},
	"ssbfbbr": {
		"name": "SpongeBob SquarePants: Battle for Bikini Bottom - Rehydrated",
		"ordering": "pf",
		"aliases": ["bfbbr"],
		"platforms": ["ps4", "xbone", "pc", "xboxone"],
		"slug": "rehydrated"
	},
	"hm": {
		"name": "Hannah Montana",
		"aliases": ["montana", "hannahmontana"],
		"platforms": ["ds"],
		"slug": "hannah_montana"
	},
	"shrek2": {
		"name": "Shrek 2",
		"aliases": ["s2"],
		"platforms": ["pc", "ps2", "xbox", "gcn"],
		"slugs": {
			"shrek_2": ["shrek2_pc", "s2_pc"],
			"shrek_2_c": ["shrek2_ps2", "shrek2_gcn", "shrek2_xbox", "s2_ps2", "s2_gcn", "s2_xbox"]
		}
	},
	"shrek2rm": {
		"name": "Shrek 2 Remastered",
		"aliases": ["s2rm", "shrek2remastered", "s2remastered"],
		"platforms": ["pc", "switch", "ps5", "xbss", "xbsx"],
		"slug": "Shrek_2_Remastered"
	},
	"traod": {
		"name": "Tomb Raider: The Angel of Darkness",
		"aliases": ["angelofdarkness", "aod", "tombraideraod"],
		"platforms": ["ps2", "pc"],
		"slug": "traod"
	},
	"popww": {
		"name": "Prince of Persia: Warrior Within",
		"aliases": ["warriorwithin"],
		"platforms": ["gcn", "ps2", "ps3", "pc", "psp", "xbox", "psvita", "vita", "wii"],
		"slug": "pop_ww"
	},
	"kao2": {
		"name": "Kao the Kangaroo: Round 2",
		"aliases": ["ktk2", "ktkr2"],
		"platforms": ["gcn", "ps2", "xbox", "pc", "wii"],
		"slug": "kao2"
	},
	"pepsiman": {
		"name": "Pepsiman",
		"aliases": ["pman", "pepsi"],
		"platforms": ["ps1", "ps2", "ps3"],
		"slug": "pepsiman"
	},
	"cnst": {
		"name": "Crash Bandicoot: N. Sane Trilogy",
		"aliases": ["crashnst", "cnsane", "crashnsane"],
		"platforms": ["pc", "ps4", "ps5", "xbone", "xb1x", "xbss", "xbsx"],
		"slug": "crashnst",
		"shortcuts": {
			"c1nst": {"board_name": "crash1", "aliases": ["crash1nst", "c1nsane"]},
			"c2nst": {"board_name": "crash2", "aliases": ["crash2nst", "c2nsane"]},
			"c3nst": {"board_name": "crash3", "aliases": ["crash3nst", "c3nsane"]}
		}
	},
	"dx": {
		"name": "Deus Ex",
		"aliases": ["dex", "deusex"],
		"platforms": ["pc", "ps2"],
		"slug": "dx"
	},
	"morrowind": {
		"name": "The Elder Scrolls III: Morrowind",
		"aliases": ["tesiii", "tes3", "esiiim", "es3m"],
		"platforms": ["pc", "xbone", "xbox", "x360", "xb1s", "xb1x", "xbss", "xbsx"],
		"slug": "morrowind"
	},
	"skyrim": {
		"name": "The Elder Scrolls V: Skyrim",
		"aliases": ["tesv", "tesskyrim", "esvskyrim", "tesvs"],
		"platforms": ["pc", "ps3", "ps4", "ps5", "xbone", "x360", "xbss", "xbsx", "switch"],
		"slug": "skyrim"
	},
	"rs1": {
		"name": "Resident Evil (1996)",
		"aliases": ["rs", "residentevil", "revil"],
		"ordering": "pf",
		"platforms": ["pc", "ps1", "psx", "ps2", "ps3", "ps4", "ps5", "psp", "vita"],
		"slug": "residentevil"
	},
	"shar": {
		"name": "The Simpsons: Hit and Run",
		"aliases": ["shr", "hitandrun", "simpsonshar", "simpsonshitandrun"],
		"platforms": ["pc", "ps2", "gcn", "xbox"],
		"slug": "shar"
	}
}
