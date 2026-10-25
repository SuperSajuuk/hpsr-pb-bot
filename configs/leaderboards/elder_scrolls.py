#
# The Elder Scrolls Series
#
# Contains all the leaderboard data for The Elder Scrolls games.
#
LEADERBOARD_DATA = {
	"skyrim": {
		"categories": {
			"Main Quest": {"aliases": ["mq", "main", "mainquest", "mquest"], "internal_name": "mq"},
			"Glitchless Main Quest": {
				"aliases": [
					"mqgless", "mqglitchless", "glessmq", "glitchlessmq",
					"maingless", "mainglitchless", "glessmain", "glitchlessmain",
					"mainquestgless", "mainquestglitchless", "glessmainquest", "glitchlessmainquest",
					"mquestgless", "mquestglitchless", "glessmquest", "glitchlessmquest"
				], "internal_name": "mqgless"
			},
			"Guilds": {"aliases": ["g", "gs", "guilds"], "internal_name": "guilds"},
			"Civil War": {"aliases": ["cw", "war", "civilwar", "cwar"], "internal_name": "cw"},
			"Marriage": {"aliases": ["marriage"], "internal_name": "marriage"},
			"DLC": {"aliases": ["dlc", "dg", "db", "dawnguard", "dragonborn"], "internal_name": "dlc"},
			"All Achievements": {"aliases": ["alla", "achievements", "allachievements"], "internal_name": "achievements"},
			"Main Quest Misc.": {"aliases": ["mqm", "miscmq", "mqmisc", "mainmisc", "mainquestmisc"], "internal_name": "miscmq"},
			"Guilds Misc.": {"aliases": ["gm", "gmisc", "guildsmisc", "miscg"], "internal_name": "gmisc"},
			"All Daedric Quests": {"aliases": ["adq", "alldq", "daedric", "alldaedric", "alldaedricquests"], "internal_name": "adq"},
			"Ebony Warrior": {"aliases": ["ew", "ebony", "warrior", "ebonyw", "ebonywarrior"], "internal_name": "ew"},
		},
		"platform_mapping": {
			"pc": ["pc"],
			"console": ["ps3", "ps4", "ps5", "xbone", "x360", "xbss", "xbsx", "switch"]
		},
		"metadata": {
			"Novice": {"aliases": ["n", "novice"], "var_key": "novice"},
			"Legendary": {"aliases": ["legend", "legendary"], "var_key": "legendary"},
			"All Guilds": {"aliases": ["ag", "allg", "guilds", "allguilds"], "var_key": "allg"},
			"Companions": {"aliases": ["c", "comp", "companions"], "var_key": "comp"},
			"Thieves Guild": {"aliases": ["tg", "thieves", "tguild", "thievesguilds"], "var_key": "tg"},
			"College of Winterhold": {"aliases": ["cow", "college", "winterhold", "collegeofwinterhold"], "var_key": "cow"},
			"Dark Brotherhood": {"aliases": ["db", "brotherhood", "darkbrotherhood"], "var_key": "db"},
			"Dawnguard": {"aliases": ["dg", "dguard", "dawnguard"], "var_key": "dg"},
			"Dragonborn": {"aliases": ["dborn", "dragonborn"], "var_key": "dborn"},
			"Base Game": {"aliases": ["bg", "base", "basegame"], "var_key": "base"},
			"Base Game + DLC": {"aliases": ["bgdlc", "basedlc", "baseanddlc", "basegameanddlc"], "var_key": "basedlc"},
			"All Main Quests (No Horse Tilts)": {
				"aliases": ["amq", "amqnht", "amqnohorse", "allmq", "allmqnht", "allmqnohorse", "allmainquests"],
				"var_key": "allmq"
			},
			"All Shouts": {"aliases": ["as", "alls", "shouts", "allshouts"], "var_key": "alls"},
			"Destroy the Dark Brotherhood!": {"aliases": ["ddb", "destroydb", "destroybrotherhood", "destroydarkbrotherhood"], "var_key": "ddb"},
			"Thieves Guild Master": {"aliases": ["tgm", "thievesmaster", "thievesguildmaster"], "var_key": "tgm"},
			"No Stone Unturned": {"aliases": ["nsu", "nostone", "unturned", "nostoneunturned"], "var_key": "nsu"}
		},
		"mq": {
			"variables": [
				{"name": "pc", "var_id": "jlz36082", "value_id": "013x3dk1"},
				{"name": "console", "var_id": "jlz36082", "value_id": "rqvx3g5l"}
			]
		},
		"mqgless": {
			"variables": [
				{"name": "pc", "var_id": "7891rq9n", "value_id": "rqv09g6l"},
				{"name": "console", "var_id": "7891rq9n", "value_id": "5le059kq"},
				{"name": "legendary", "var_id": "7891rq9n", "value_id": "le23mrpl"}
			]
		},
		"guilds": {
			"variables": [
				{"name": "allg", "var_id": "jlz2jk0l", "value_id": "qj7wxn0q"},
				{"name": "comp", "var_id": "jlz2jk0l", "value_id": "q65yzrnl"},
				{"name": "tg", "var_id": "jlz2jk0l", "value_id": "1w4e5o9q"},
				{"name": "cow", "var_id": "jlz2jk0l", "value_id": "lmo8g6y1"},
				{"name": "db", "var_id": "jlz2jk0l", "value_id": "qoxmrogq"},
				{"name": "pc", "var_id": "6njvoz5n", "value_id": "5q8gy0yl"},
				{"name": "console", "var_id": "6njvoz5n", "value_id": "4qyn0y61"},
				{"name": "gless", "var_id": "6njvoz5n", "value_id": "q655xvvl"}
			]
		},
		"cw": {
			"variables": [
				{"name": "pc", "var_id": "0nwp1er8", "value_id": "p12kpd41"},
				{"name": "console", "var_id": "0nwp1er8", "value_id": "81pz2p8l"},
				{"name": "gless", "var_id": "0nwp1er8", "value_id": "lmoo4281"}
			]
		},
		"marriage": {
			"variables": [
				{"name": "pc", "var_id": "yn2v7jj8", "value_id": "klr5g0o1"},
				{"name": "console", "var_id": "yn2v7jj8", "value_id": "21d20ypl"},
				{"name": "gless", "var_id": "yn2v7jj8", "value_id": "81w629ml"}
			]
		},
		"dlc": {
			"variables": [
				{"name": "dg", "var_id": "kn09p4on", "value_id": "q5vxgnrl"},
				{"name": "dborn", "var_id": "kn09p4on", "value_id": "lx50epj1"},
				{"name": "pc", "var_id": "gnxw41g8", "value_id": "810yyj2l"},
				{"name": "console", "var_id": "gnxw41g8", "value_id": "9qjoon3l"},
				{"name": "gless", "var_id": "gnxw41g8", "value_id": "81w2xr61"}
			]
		},
		"achievements": {
			"variables": [
				{"name": "base", "var_id": "68k1gryl", "value_id": "lmowo0j1"},
				{"name": "basedlc", "var_id": "68k1gryl", "value_id": "1w4r4xoq"},
				{"name": "pc", "var_id": "wleg2ekn", "value_id": "10v9vkwl"},
				{"name": "console", "var_id": "wleg2ekn", "value_id": "qj7e7keq"},
				{"name": "gless", "var_id": "wleg2ekn", "value_id": "q65g563l"}
			]
		},
		"miscmq": {
			"variables": [
				{"name": "allmq", "var_id": "wl3vp798", "value_id": "qj7en6gq"},
				{"name": "alls", "var_id": "wl3vp798", "value_id": "q65gr97l"}
			]
		},
		"gmisc": {
			"variables": [
				{"name": "ddb", "var_id": "68kwpvy8", "value_id": "qox2o82q"},
				{"name": "tgm", "var_id": "68kwpvy8", "value_id": "lx5dovr1"},
				{"name": "nsu", "var_id": "68kwpvy8", "value_id": "13947o31"},
				{"name": "pc", "var_id": "j84pw7j8", "value_id": "qvvzokwq"},
				{"name": "console", "var_id": "j84pw7j8", "value_id": "le2vz6zl"},
				{"name": "gless", "var_id": "j84pw7j8", "value_id": "q5v7z9nl"}
			]
		},
		"ew": {
			"variables": [
				{"name": "pc", "var_id": "kn0km008", "value_id": "13920rr1"},
				{"name": "console", "var_id": "kn0km008", "value_id": "qvvm7drq"},
				{"name": "gless", "var_id": "kn0km008", "value_id": "le2eo8ml"}
			]
		}
	}
}
