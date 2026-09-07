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
	"psp": "psp",
	"gba": "gba",
	"gbc": "gbc",
	"ds": "ds",
	"xbox": "6thgen",
	"gcn": "6thgen"
}

# Board slug mapping. This is used to map the values produced by
# concatenating platform and game in the code. The ordering of the
# keys is to ensure they are grouped by platform commonalities for
# easier reading.
BOARD_GAME_SLUG = {
	"hp1_ps1": "hp1ps1",
	"hp2_ps1": "hp2ps1",
	"hp1_pc": "hp1pc",
	"hp2_pc": "hp2pc",
	"hp3_pc": "hp3pc",
	"hp4_pc": "hp4",
	"hp5_pc": "hp5",
	"hp6_pc": "hp6",
	"hp7.1_pc": "hp7p1",
	"hp7.2_pc": "hp7p2",
	"hp1_ps2": "hp1_6th_gen",
	"hp2_ps2": "hp2ps2",
	"hp3_ps2": "hp3_6th_gen",
	"hp4_ps2": "hp4",
	"hp5_ps2": "hp5",
	"hp6_ps2": "hp6",
	"hp1_xbox": "hp1_6th_gen",
	"hp2_xbox": "hp2_6th_gen",
	"hp3_xbox": "hp3_6th_gen",
	"hp4_xbox": "hp4",
	"hp5_xbox": "hp5",
	"hp6_xbox": "hp6",
	"hp7.1_xbox": "hp7p1",
	"hp7.2_xbox": "hp7p2",
	"hp1_gcn": "hp1_6th_gen",
	"hp2_gcn": "hp2_6th_gen",
	"hp3_gcn": "hp3_6th_gen",
	"hp4_gcn": "hp4",
	"hp1_gba": "hp1gba",
	"hp2_gba": "hp2gba",
	"hp3_gba": "hp3gba",
	"hp4_gba": "hp4gba",
	"hp5_gba": "hp5gbads",
	"hp1_gbc": "hp1gbc",
	"hp2_gbc": "hp2gbc",
	"hp4_ds": "hp4gba",
	"hp5_ds": "hp5gbads",
	"hp6_ds": "hp6ds",
	"hp7.1_ds": "hp7p1ds",
	"hp7.2_ds": "hp7p2ds"
}

# Point to the docs if there is an error.
# Putting it as a constant means we don't need multiple
# references to it, and updating it just requires changing
# this one constant.
COMMAND_USAGE_DOC = "https://github.com/supersajuuk/hpsr-pb-bot/blob/main/README.md"
