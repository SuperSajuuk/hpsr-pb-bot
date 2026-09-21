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

# Additional metadata aliases
# Converts the value of the key_1 key in the additional
# metadata to a human-readable value. Very small list for
# a rare number of instances
METADATA_ALIASES = {
	"Story": {"aliases": ["story"], "int_key": "story"},
	"Hard": {"aliases": ["hard"], "int_key": "hard"},
	"1 Player": {"aliases": ["1p", "1player"], "int_key": "1p"},
	"2 Players": {"aliases": ["2p", "2players"], "int_key": "2p"},
	"3 Players": {"aliases": ["3p", "3players"], "int_key": "3p"},
	"No Lag Abuse": {"aliases": ["nla", "nolag", "nolagabuse"], "int_key": "nla"},
	"Lag Abuse": {"aliases": ["la", "lag", "lagabuse"], "int_key": "la"},
	"Single Player": {"aliases": ["1p", "sp", "single", "singleplayer"], "int_key": "sp"},
	"Co-op": {"aliases": ["coop", "co-op"], "int_key": "coop"},
	"Standard": {"aliases": ["std", "standard"], "int_key": "std"},
	"Zipless": {"aliases": ["zl", "zless", "zipless"], "int_key": "zl"},
	"No Major Glitches": {"aliases": ["nmg", "nomajorglitches"], "int_key": "nmg"}
}

# Point to the docs if there is an error.
# Putting it as a constant means we don't need multiple
# references to it, and updating it just requires changing
# this one constant.
COMMAND_USAGE_DOC = "https://github.com/SuperSajuuk/hpsr-pb-bot/wiki"
