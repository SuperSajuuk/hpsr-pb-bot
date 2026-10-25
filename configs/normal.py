#
# Normal Run Configs
#
# This file contains all the constants used for
# handling Normal runs (ie main boards: not CE's
# or multi-runs)
#

# Map abbreviations passed by users to human-readable names.
# This category is ONLY for standard/generic boards: aka,
# categories which are extremely common. Game-specific categories
# should be defined in the respective leaderboard config data.
CATEGORY_MAP = {
	"Any%": {"aliases": ["any", "any%"], "internal_name": "any"},
	"100%": {"aliases": ["100", "hundo", "100%"], "internal_name": "100"},
	"Glitchless": {"aliases": ["gless", "glitchless"], "internal_name": "gless"},
	"No Major Skips": {"aliases": ["nms", "nomajorskips", "any%nms", "any%nomajorskips"], "internal_name": "nms"},
	"No Major Glitches": {"aliases": ["nmg", "nomajorglitches", "any%nmg", "any%nomajorglitches"], "internal_name": "nmg"},
	"NG+": {"aliases": ["ng", "ngplus", "newgameplus", "ng+"], "internal_name": "ng"}
}
