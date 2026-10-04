#
# Custom Content Configs
#
# This file contains all the constants used for
# handling Custom Content categories.
#

# Game mapping.
# Key names must be abbreviations that would be called in !run cc
# commands. The value of key is a dictionary which contains two
# keys: a human-readable name and the Slug URL ID.
GAME_MAP = {
	"hp": {"name": "Harry Potter Custom Content", "id": "hpcc"}
}

# Sub-category mapping.
# This refers to the second board under the top level board.
# The key name must be the human-readable board name: the value
# of each key is a list containing aliases that get mapped by
# user input.
SUB_CATEGORY_MAP = {
	"[1PC] Fixed Movement": ["fm", "fixed", "movement", "fixedmovement"],
	"[1PC] Restored": ["rs", "restored"],
	"[1PC] Tourney Client": ["tc", "1tc", "1tourney", "tc1", "tourney1", "tourneyclient1", "1tourneyclient"],
	"[2PC] Bingo": ["bingo"],
	"[2PC] Tourney Client": ["tc", "2tc", "2tourney", "tc2", "tourney2", "tourneyclient2", "2tourneyclient"]
}

# Board aliases. Useful if you want multiple
# user input choices to display the appropriate label.
BOARD_ALIASES = {
	"1PC": ["hp1"],
	"2PC": ["hp2"]
}

# Category aliases
# Like board aliases, this is used to map user input
# to the name that is used internally to reference
# a specific sub-board for custom content.
CATEGORY_ALIASES = {
	"hpcc": {
		"hp1": {
			"fm": ["fm", "fixed", "movement", "fixedmovement"],
			"rs": ["rs", "restored"],
			"tc": ["tc", "1tc", "1tourney", "tc1", "tourney1", "tourneyclient1", "1tourneyclient"]
		},
		"hp2": {
			"bingo": ["bingo"],
			"tc": ["tc", "2tc", "2tourney", "tc2", "tourney2", "tourneyclient2", "2tourneyclient"]
		}
	}
}
