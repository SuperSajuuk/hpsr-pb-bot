# Store all the key configuration settings here.
# By moving the keys to here, we can more easily update and manage it.
# Since these won't change without a reload, we should use constant
# variable formatting, ie the variables should be ALL CAPS.
#

# Map abbreviations passed by users to human-readable names.
# CATEGORY_MAP is for main boards, CE_CATEGORY_MAP is for the
# defined Category Extensions board, and MULTIRUN_CATEGORY_MAP
# is for the defined Multi Run board.
CATEGORY_MAP = {
	"any": "Any%",
	"100": "100%",
	"glitchless": "Glitchless",
	"gless": "Glitchless",
	"nms": "No Major Skips",
	"noeds": "Any% No EDS",
	"awc": "All Wizard Cards",
	"warpless": "Warpless"
}

# Point to the docs if there is an error.
# Putting it as a constant means we don't need multiple
# references to it, and updating it just requires changing
# this one constant.
COMMAND_USAGE_DOC = "https://github.com/supersajuuk/hpsr-pb-bot/blob/main/README.md"
