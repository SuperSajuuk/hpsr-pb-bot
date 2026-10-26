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
			"hp7p1": ["hp7.1_ps3", "hp7.1_xbox", "hp7.1_pc", "hp7.1_wii"],
			"hp7p1ds": ["hp7.1_ds"]
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
		"slugs": {
			"legacy": ["legacy_pc", "legacy_ps4", "legacy_ps5"]
		}
	},
	"dbb": {
		"name": "Disney's Brother Bear",
		"aliases": ["disneysbrotherbear", "brotherbear"],
		"platforms": ["pc"],
		"slugs": {
			"disneys_brother_bear": ["dbb_pc"]
		}
	},
	"r1": {
		"name": "Rayman",
		"ordering": "pf",
		"aliases": ["rayman", "rayman1"],
		"platforms": ["ps1", "psx", "pc", "ds", "gba", "ss", "saturn", "segasaturn", "aj", "jaguar", "atari", "atarijaguar"],
		"slugs": {
			"rayman_1": ["r1_ps1", "r1_pc", "r1_ds", "r1_ss", "r1_aj"]
		}
	},
	"r3": {
		"name": "Rayman 3: Hoodlum Havoc",
		"ordering": "pf",
		"aliases": ["rayman3"],
		"platforms": ["gcn", "pc", "ps2", "hd", "ps3", "x360", "xss", "xbox"],
		"slugs": {
			"r3": ["r3_gcn", "r3_ps3", "r3_x360", "r3_ps2", "r3_pc"]
		}
	},
	"ssbfbbr": {
		"name": "SpongeBob SquarePants: Battle for Bikini Bottom - Rehydrated",
		"ordering": "pf",
		"aliases": ["bfbbr"],
		"platforms": ["ps4", "xbone", "pc", "xboxone"],
		"slugs": {
			"rehydrated": ["ssbfbbr_pc"]
		}
	},
	"hm": {
		"name": "Hannah Montana",
		"aliases": ["hm", "montana", "hannahmontana"],
		"platforms": ["ds"],
		"slugs": {
			"hannah_montana": ["hm_ds", "montana_ds", "hannahmontana_ds", "hannah_montana_ds"]
		}
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
	"traod": {
		"name": "Tomb Raider: The Angel of Darkness",
		"aliases": ["angelofdarkness", "aod", "tombraideraod"],
		"platforms": ["ps2", "pc"],
		"slugs": {
			"traod": ["traod_pc", "angelofdarkness_pc", "aod_pc", "tombraideraod_pc"]
		}
	},
	"popww": {
		"name": "Prince of Persia: Warrior Within",
		"aliases": ["warriorwithin"],
		"platforms": ["gcn", "ps2", "ps3", "pc", "psp", "xbox", "psvita", "vita", "wii"],
		"slugs": {
			"pop_ww": ["popww_pc", "popww_ps2"]
		}
	},
	"kao2": {
		"name": "Kao the Kangaroo: Round 2",
		"aliases": ["ktk2", "ktkr2"],
		"platforms": ["gcn", "ps2", "xbox", "pc", "wii"],
		"slugs": {
			"kao2": [
				"kao2_gcn", "kao2_ps2", "kao2_xbox", "kao2_pc", "kao2_wii",
				"ktk2_gcn", "ktk2_ps2", "ktk2_xbox", "ktk2_pc", "ktk2_wii",
				"ktkr2_gcn", "ktkr2_ps2", "ktkr2_xbox", "ktkr2_pc", "ktkr2_wii"
			]
		}
	},
	"pepsiman": {
		"name": "Pepsiman",
		"aliases": ["pman", "pepsi"],
		"platforms": ["ps1", "ps2", "ps3"],
		"slugs": {
			"pepsiman": [
				"pepsiman_ps1", "pman_ps1", "pepsi_ps1",
				"pepsiman_ps2", "pman_ps2", "pepsi_ps2",
				"pepsiman_ps3", "pman_ps3", "pepsi_ps3"
			]
		}
	},
	"cnst": {
		"name": "Crash Bandicoot: N. Sane Trilogy",
		"aliases": ["crashnst", "cnsane", "crashnsane"],
		"platforms": ["pc", "ps4", "ps5", "xbone", "xb1x", "xbss", "xbsx"],
		"slugs": {
			"crashnst": [
				"cnst_ps4", "cnst_ps5", "cnst_xbone", "cnst_xb1x", "cnst_xbss", "cnst_xbsx",
				"crashnst_ps4", "crashnst_ps5", "crashnst_xbone", "crashnst_xb1x", "crashnst_xbss", "crashnst_xbsx",
				"cnsane_ps4", "cnsane_ps5", "cnsane_xbone", "cnsane_xb1x", "cnsane_xbss", "cnsane_xbsx",
				"crashnsane_ps4", "rashnsane_ps5", "crashnsane_xbone", "crashnsane_xb1x", "crashnsane_xbss", "crashnsane_xbsx"
			]
		},
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
		"slugs": {
			"dx": ["dx_pc", "dx_ps2", "dex_pc", "dex_ps2", "deusex_pc", "deusex_ps2"]
		}
	},
	"skyrim": {
		"name": "The Elder Scrolls V: Skyrim",
		"aliases": ["tesv", "tesskyrim", "esvskyrim", "tesvs"],
		"platforms": ["pc", "ps3", "ps4", "ps5", "xbone", "x360", "xbss", "xbsx", "switch"],
		"slugs": {
			"skyrim": [
				"skyrim_pc", "skyrim_ps3", "skyrim_ps4", "skyrim_ps5", "skyrim_xbone", "skyrim_x360",
				"skyrim_xbss", "skyrim_xbsx", "skyrim_switch", "tesv_pc", "tesv_ps3", "tesv_ps4",
				"tesv_ps5", "tesv_xbone", "tesv_x360", "tesv_xbss", "tesv_xbsx", "tesv_switch",
				"tesskyrim_pc", "tesskyrim_ps3", "tesskyrim_ps4", "tesskyrim_ps5", "tesskyrim_xbone",
				"tesskyrim_x360", "tesskyrim_xbss", "tesskyrim_xbsx", "tesskyrim_switch", "esvskyrim_pc",
				"esvskyrim_ps3", "esvskyrim_ps4", "esvskyrim_ps5", "esvskyrim_xbone", "esvskyrim_x360",
				"esvskyrim_xbss", "esvskyrim_xbsx", "esvskyrim_switch", "tesvs_pc", "tesvs_ps3",
				"tesvs_ps4", "tesvs_ps5", "tesvs_xbone", "tesvs_x360", "tesvs_xbss", "tesvs_xbsx",
				"tesvs_switch"
			]
		}
	},
	"rs1": {
		"name": "Resident Evil (1996)",
		"aliases": ["rs", "residentevil", "revil"],
		"ordering": "pf",
		"platforms": ["pc", "ps1", "psx", "ps2", "ps3", "ps4", "ps5", "psp", "vita"],
		"slugs": {
			"residentevil": [
				"rs1_pc", "rs1_ps1", "rs1_psx", "rs1_ps2", "rs1_ps3", "rs1_ps4", "rs1_ps5", "rs1_psp",
				"rs1_vita", "rs_pc", "rs_ps1", "rs_psx", "rs_ps2", "rs_ps3", "rs_ps4", "rs_ps5",
				"rs_psp", "rs_vita", "residentevil_pc", "residentevil_ps1", "residentevil_psx",
				"residentevil_ps2", "residentevil_ps3", "residentevil_ps4",	"residentevil_ps5",
				"residentevil_psp", "residentevil_vita", "revil_pc", "revil_ps1", "revil_psx",
				"revil_ps2", "revil_ps3", "revil_ps4", "revil_ps5", "revil_psp", "revil_vita"
			]
		}
	}
}
