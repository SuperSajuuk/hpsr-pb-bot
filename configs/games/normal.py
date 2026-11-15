#
# Normal Boards
#
# Contains game mapping data for normal boards.
# This covers any game which doesn't have its own file.
#
GAME_CONFIG = "nm"
GAME_MAP_DATA = {
	"dbb": {
		"name": "Disney's Brother Bear",
		"aliases": ["disneysbrotherbear", "brotherbear"],
		"platforms": ["pc"],
		"slug": "disneys_brother_bear"
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
	},
	"sdmm": {
		"name": "Scooby Doo: Mystery Mayhem",
		"aliases": ["mysterymayhem", "sdmysterymayhem", "scoobydoomysterymayhem"],
		"platforms": ["ps2", "gcn", "xbox"],
		"slug": "scooby_doo_mystery_mayhem"
	},
	"sdno100f": {
		"name": "Scooby Doo: Night of 100 Frights",
		"aliases": ["n100f", "no100f", "no100frights", "nightof100frights", "sdnightof100frights", "scoobydoono100f", "scoobydoonightof100frights"],
		"platforms": ["ps2", "gcn", "xbox"],
		"slug": "n100f"
	}
}
