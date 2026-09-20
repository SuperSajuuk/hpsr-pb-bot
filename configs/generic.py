#
# Generic Configs
#
# This file contains generic configuration data
# which is non-specific and relevant to all aspects
# of the program.
#

# Platform mapping. This is used to provide more
# control and flexibility over bot commands.
PLATFORM_MAP = {
	"pc": "pc",
	"ps1": "ps1",
	"ps2": "ps2",
	"ps3": "ps3",
	"ps4": "ps4",
	"ps5": "ps5",
	"psp": "psp",
	"gba": "gba",
	"gbc": "gbc",
	"ds": "ds",
	"xbox": "6thgen",
	"x360": "6thgen",
	"xboxss": "xss",
	"xss": "xss",
	"gcn": "6thgen",
	"wii": "wii"
}

# Point to the docs if there is an error.
# Putting it as a constant means we don't need multiple
# references to it, and updating it just requires changing
# this one constant.
COMMAND_USAGE_DOC = "https://github.com/SuperSajuuk/hpsr-pb-bot/wiki"
