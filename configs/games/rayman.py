#
# Rayman
#
# Contains all the game mapping data for Rayman normal boards.
#
GAME_CONFIG = "nm"
GAME_MAP_DATA = {
	"r1": {
		"name": "Rayman",
		"ordering": "pf",
		"aliases": ["rayman", "rayman1"],
		"platforms": ["ps1", "psx", "pc", "ds", "gba", "ss", "saturn", "segasaturn", "aj", "jaguar", "atari", "atarijaguar"],
		"slug": "rayman_1"
	},
	"r2": {
		"name": "Rayman 2: The Great Escape",
		"aliases": ["rayman2", "r2tge"],
		"platforms": ["ps1", "psx", "pc", "n64", "ds", "dc", "ps2"],
		"slugs": {
			"r2": [
				"r2_pc", "rayman2_pc", "r2tge_pc", "r2_n64", "rayman2_n64", "r2tge_n64",
				"r2_ds", "rayman2_ds", "r2tge_ds", "r2_dc", "rayman2_dc", "r2tge_dc"
			],
			"rayman_2_ps1": ["r2_ps1", "r2_psx", "rayman2_ps1", "rayman2_psx", "r2tge_ps1", "r2tge_psx"],
			"r2r": ["r2_ps2", "rayman2_ps2", "r2tge_ps2"]
		}
	},
	"r2r": {
		"name": "Rayman 2: Revolution",
		"aliases": ["raymanrevolution", "rayman2revolution"],
		"platforms": ["ps2"],
		"slug": "r2r"
	},
	"r3": {
		"name": "Rayman 3: Hoodlum Havoc",
		"ordering": "pf",
		"aliases": ["rayman3", "hoodlums", "hoodlumhavoc"],
		"platforms": ["gcn", "pc", "ps2", "hd", "ps3", "x360", "xss", "xbox"],
		"slug": "r3"
	}
}
