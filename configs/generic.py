#
# Generic Configs
#
# This file contains generic configuration data
# which is non-specific and relevant to all aspects
# of the program.
#

# Platform mapping. Simply maps keys for user inputs
# to the name output that should be displayed.
PLATFORM_MAP = {
	"pc": {"name": "PC", "id": "8gej2n93"},
	"ps1": {"name": "PS1", "id": "wxeod9rn"},
	"ps2": {"name": "PS2", "id": "n5e17e27"},
	"ps3": {"name": "PS3", "id": "mx6pwe3g"},
	"ps4": {"name": "PS4", "id": "nzelkr6q"},
	"ps5": {"name": "PS5", "id": "4p9zjrer"},
	"psp": {"name": "PSP", "id": "5negk9y7"},
	"vita": {"name": "PlayStation Vita", "id": "4p9z70er"},
	"gba": {"name": "GBA", "id": "3167d6q2"},
	"gbc": {"name": "GBC", "id": "gde3g9k1"},
	"ds": {"name": "Nintendo DS", "id": "7g6m8erk"},
	"sms": {"name": "Sega Master System", "id": "83exwk6l"},
	"switch": {"name": "Nintendo Switch", "id": "7m6ylw9p"},
	"xbox": {"name": "Xbox", "id": "jm95zz9o"},
	"x360": {"name": "Xbox 360", "id": "n568oevp"},
	"xbone": {"name": "Xbox One", "id": "o7e2mx6w"},
	"xb1s": {"name": "Xbox One S", "id": "o064j163"},
	"xb1x": {"name": "Xbox One X", "id": "4p9z0r6r"},
	"xbss": {"name": "Xbox Series S", "id": "o7e2xj9w"},
	"xbsx": {"name": "Xbox Series X", "id": "nzelyv9q"},
	"gcn": {"name": "GameCube", "id": "4p9z06rn"},
	"wii": {"name": "Wii", "id": "v06dk3e4"}
}

# This is a set list of normal metadata that most
# boards will support in some form. This will be
# joined with game-specific metadata lists when
# processing any additional metadata.
METADATA_ALIASES = {
	"Single Player": {"aliases": ["1p", "sp", "singleplayer"], "var_key": "sp"},
	"Co-op": {"aliases": ["coop", "co-op"], "var_key": "coop"},
	"Standard": {"aliases": ["std", "standard"], "var_key": "std"},
	"No Major Glitches": {"aliases": ["nmg", "nomajorglitches"], "var_key": "nmg"},
	"Any%": {"aliases": ["any", "any%"], "var_key": "any"},
	"100%": {"aliases": ["100", "100%", "hundo"], "var_key": "100"},
	"Glitchless": {"aliases": ["gless", "glitchless"], "var_key": "gless"}
}

# Point to the docs if there is an error.
# Putting it as a constant means we don't need multiple
# references to it, and updating it just requires changing
# this one constant.
COMMAND_USAGE_DOC = "https://github.com/SuperSajuuk/hpsr-pb-bot/wiki"
