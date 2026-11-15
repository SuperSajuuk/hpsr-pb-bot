#
# Rayman Series
#
# Contains all the leaderboard data for Rayman main boards
#
LEADERBOARD_DATA = {
	"rayman_1": {
		"categories": {
			"Sax%": {"aliases": ["sax", "mrsax", "sax%", "mrsax%"], "internal_name": "sax"},
			"Skops%": {"aliases": ["skops", "mrskops", "skops%", "mrskops%"], "internal_name": "skops"}
		},
		"platform_categories": {
			"PS1": ["ps1", "psx"],
			"PC": ["pc"],
			"DSI": ["ds"],
			"GBA": ["gba"],
			"Sega Saturn": ["saturn", "segasaturn", "ss"],
			"Atari Jaguar": ["jaguar", "atari", "atarijaguar", "aj"]
		},
		"100": {
			"variables": [
				{"var_id": "2lgzx5o8", "value_id": "xqkr5ky1"}
			]
		},
		"any": {
			"variables": [
				{"var_id": "2lgzx5o8", "value_id": "gq7npey1"}
			]
		},
		"sax": {
			"variables": [
				{"var_id": "2lgzx5o8", "value_id": "21gj5vn1"}
			]
		},
		"skops": {
			"variables": [
				{"var_id": "2lgzx5o8", "value_id": "192xy60q"}
			]
		}
	},
	"r2": {
		"categories": {
			"All Masks": {"aliases": ["am", "allm", "masks", "allmasks"], "internal_name": "am"},
			"All Cages": {"aliases": ["ac", "allc", "cages", "allcages"], "internal_name": "ac"}
		},
		"platform_mapping": {
			"pc": ["pc"],
			"n64": ["n64", "ds"],
			"dreamcast": ["dc", "3ds"]
		},
		"any": {
			"variables": [
				{"name": "pc", "var_id": "ql6r9m7l", "value_id": "klrro3jl"},
				{"name": "n64", "var_id": "ql6r9m7l", "value_id": "gq76m5nl"},
				{"name": "dreamcast", "var_id": "ql6r9m7l", "value_id": "q5vv5jvl"}
			]
		},
		"nmg": {
			"variables": [
				{"name": "pc", "var_id": "wl3dv4v8", "value_id": "5lm90oy1"},
				{"name": "n64", "var_id": "wl3dv4v8", "value_id": "0q50jvr1"},
				{"name": "dreamcast", "var_id": "wl3dv4v8", "value_id": "lx5587g1"}
			]
		},
		"100": {
			"variables": [
				{"name": "pc", "var_id": "wlek344l", "value_id": "81wkx491"},
				{"name": "n64", "var_id": "wlek344l", "value_id": "4lxj75jq"},
				{"name": "dreamcast", "var_id": "wlek344l", "value_id": "14oov0kq"}
			]
		},
		"am": {
			"variables": [
				{"name": "pc", "var_id": "68k7wx3l", "value_id": "zqo76xg1"},
				{"name": "n64", "var_id": "68k7wx3l", "value_id": "814n0owl"},
				{"name": "dreamcast", "var_id": "000", "value_id": "000"}
			]
		},
		"ac": {
			"variables": [
				{"name": "pc", "var_id": "p855w078", "value_id": "5lew72pl"},
				{"name": "n64", "var_id": "p855w078", "value_id": "81pgmee1"},
				{"name": "dreamcast", "var_id": "p855w078", "value_id": "1pyy0mn1"}
			]
		}
	},
	"r2r": {
		"categories": {
			"All Masks": {"aliases": ["am", "allm", "masks", "allmasks"], "internal_name": "am"},
			"Any% No Memory Card": {
				"aliases": [
					"nmc", "nocard", "nomemory", "anynmc", "anynocard", "anynomemory",
					"anynomemorycard", "any%nmc", "any%nocard", "any%nomemory", "any%nomemorycard"
				], "internal_name": "nmc"
			},
			"All Teensies": {"aliases": ["at", "allt", "allteensies"], "internal_name": "allt"}
		},
		"any": {
			"variables": [
				{"name": "console", "default": True, "var_id": "jlzx4782", "value_id": "81p9nnq7"},
				{"name": "emulator", "var_id": "jlzx4782", "value_id": "xqkv84l9"}
			]
		},
		"am": {
			"variables": [
				{"name": "console", "default": True, "var_id": "jlzx4782", "value_id": "81p9nnq7"},
				{"name": "emulator", "var_id": "jlzx4782", "value_id": "xqkv84l9"}
			]
		},
		"nmc": {
			"variables": [
				{"name": "console", "default": True, "var_id": "jlzx4782", "value_id": "81p9nnq7"},
				{"name": "emulator", "var_id": "jlzx4782", "value_id": "xqkv84l9"}
			]
		},
		"allt": {
			"variables": [
				{"name": "console", "default": True, "var_id": "jlzx4782", "value_id": "81p9nnq7"},
				{"name": "emulator", "var_id": "jlzx4782", "value_id": "xqkv84l9"}
			]
		},
		"100": {
			"variables": [
				{"name": "console", "default": True, "var_id": "jlzx4782", "value_id": "81p9nnq7"},
				{"name": "emulator", "var_id": "jlzx4782", "value_id": "xqkv84l9"}
			]
		},
		"gless": {
			"variables": [
				{"name": "console", "default": True, "var_id": "jlzx4782", "value_id": "81p9nnq7"},
				{"name": "emulator", "var_id": "jlzx4782", "value_id": "xqkv84l9"}
			]
		}
	},
	"r3": {
		"categories": {
			"Glitched": {"aliases": ["glitched"], "internal_name": "glitched"},
			"All Teensies": {"aliases": ["at", "allt", "allteensies"], "internal_name": "allt"},
			"No Teensies": {"aliases": ["not", "noteensies"], "internal_name": "not"}
		},
		"platform_categories": {
			"GCN": ["gcn", "wii"],
			"GCN Emu": ["gcn"],
			"HD": ["hd", "ps3", "x360", "xss"],
			"PC": ["pc"],
			"PS2": ["ps2"],
			"Xbox": ["xbox"]
		},
		"any": {
			"variables": [
				{"var_id": "6nj2zjl4", "value_id": "gq75p5r1"}
			]
		},
		"allt": {
			"variables": [
				{"var_id": "6nj2zjl4", "value_id": "5q8kv5yq"}
			]
		},
		"not": {
			"variables": [
				{"var_id": "6nj2zjl4", "value_id": "jqzn9nkq"}
			]
		},
		"nmg": {
			"variables": [
				{"var_id": "6nj2zjl4", "value_id": "z19xm8k1"}
			]
		},
		"glitched": {
			"variables": [
				{"var_id": "6nj2zjl4", "value_id": "klrxvn2l"}
			]
		},
		"100": {
			"variables": [
				{"var_id": "6nj2zjl4", "value_id": "21gn5nol"}
			]
		}
	}
}
