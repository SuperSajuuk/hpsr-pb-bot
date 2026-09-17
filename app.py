#
# Find PBs on Speedrun.com
#
# This program instantiates and runs a Flask microservice
# that queries the speedrun.com API.
#
# In a production environment, we should generally not touch
# this file: instead, all the logic should be abstracted out
# into separate files, which allows for easier maintenance
# and debugging, if something goes wrong. It is also far more
# readable and modular when we do this.
#
# app.py only handles the Flask routes: all the specific program
# codes can be found in the configs and srdc sub-folders. Some
# program-specific code below (namely around processing user input
# in the routes) will move into the respective classes in future
# commits.

# Import the core packages
import flask
import srcomapi

# Import the config data.
import configs.ce as ce_config
import configs.lego as lego_config
import configs.multi as mr_config
import configs.normal as nm_config
import configs.leaderboard as lb_config
import configs.generic as config
# import config

# Import everything else that is needed
import utils
import urllib.parse as url_parse
import srdc.normal as normal_run
import srdc.ce as ce_run
import srdc.pb as pb
import srdc.multi as multi
import srdc.lego as lego
from model import SpeedRun

# Instantiate Flask and the SRDC API
app = flask.Flask(__name__)
srdc_api = srcomapi.SpeedrunCom()
srdc_api.debug = 1

# Instantiate all our internal code for powering the actual program.
utils = utils.Utilities(srdc_api, lb_config.LEADERBOARD_CONFIG)
normal = normal_run.NormalRun(srdc_api, nm_config.GAME_MAP, config.PLATFORM_MAP, nm_config.CATEGORY_MAP, nm_config.BOARD_GAME_SLUG, utils)
lg = lego.LEGONormalRun(srdc_api, lego_config.GAME_MAP, lego_config.BOARD_ALIASES, utils)
cat_ext = ce_run.CategoryExtension(srdc_api, ce_config.GAME_MAP, config.PLATFORM_MAP, ce_config.CATEGORY_ALIASES, lb_config.LEADERBOARD_CONFIG, utils)
multirun = multi.MultiRun(srdc_api, mr_config.GAME_MAP, config.PLATFORM_MAP, mr_config.CATEGORY_ALIASES, lb_config.LEADERBOARD_CONFIG, utils)
per_best = pb.PersonalBest(
	srdc_api=srdc_api,
	game_map=(nm_config.GAME_MAP, ce_config.GAME_MAP, mr_config.GAME_MAP),
	category_map=(nm_config.CATEGORY_MAP, ce_config.SUB_CATEGORY_MAP, mr_config.SUB_CATEGORY_MAP),
	board_aliases=(ce_config.BOARD_ALIASES, mr_config.BOARD_ALIASES),
	board_slugs=nm_config.BOARD_GAME_SLUG,
	utils=utils
)


# Resolve the player, in case we just want to check for the channel owner.
# channel_owner is always provided, but player may not be:
def resolve_player(channel_owner: str, player: str | None) -> str:
	return channel_owner if player is None or player.strip() == "" else player


# Process a LEGO Games main board run.
def process_lego_main_board(game: str, board_name: str, flags: dict, player: str):
	# Check if the game provided is in the game map.
	lego_key = lego_config.GAME_MAP.get(game)
	if not lego_key:
		return None

	# Check if there is an alias table for this game.
	alias_table = lego_config.CATEGORY_ALIASES.get(game, {})
	if not alias_table:
		return None

	# Check if the top board is defined in the alias list.
	# If it isn't, the user might have provided an alternative
	# name, which needs to be checked
	if board_name not in alias_table:
		token_aliases = lego_config.BOARD_TOKEN_ALIASES.get(lego_key["slug"], None)
		if token_aliases is None:
			return None
		for name, aliases in token_aliases.items():
			if board_name in aliases:
				board_name = name
				break

		# Still not found, so just exit.
		if board_name is None:
			return None

	# Use the board_token (the top-level board) to find
	# actual internal token name (this is needed to ensure
	# random user input always maps to the correct internal
	# value).
	#
	# If this returns None, then whatever token they provided
	# does not exist in the alias table.
	sub_category_board = flags.get("main_sub_category", None)
	board_token = alias_table[board_name].get(sub_category_board, None)
	if not board_token:
		return None

	# Build an internal key based on the values of flags.
	is_nocut5_mode = flags.get("nocut_mode", None)
	is_restricted = flags.get("restricted_mode", None)
	ik_nocut_mode = ""
	ik_restricted_mode = ""
	scn_nocut_mode = ""
	scn_restricted_mode = ""
	if is_nocut5_mode is not None:
		ik_nocut_mode = "_nocut" if is_nocut5_mode else "_standard"
		scn_nocut_mode = " N0CUT5" if is_nocut5_mode else " Standard"
	if is_restricted is not None:
		ik_restricted_mode = "_restricted" if is_restricted else "_unrestricted"
		scn_restricted_mode = " Restricted" if is_restricted else " Unrestricted"

	internal_key = f"{board_name}_{sub_category_board}{ik_nocut_mode}{ik_restricted_mode}"
	run = lg.lookup_lego_run(game, internal_key, lego_key["slug"], board_name, player)

	# Produce a clean category name based on the alias value. This
	# allows one "output" name against lots of aliases for tidiness
	# of the board aliases.
	alias_name = None
	for name, aliases in lego_config.BOARD_ALIASES[game].items():
		if board_name in aliases:
			alias_name = name
			break

	# Unlike other boards, cat_clean_name can be derived from user flags
	sub_cat_name = None
	for name, aliases in lego_config.SUB_CATEGORY_ALIASES[game].items():
		if sub_category_board in aliases:
			sub_cat_name = name
			break

	# Produce the necessary alias name for the attempted category
	# solely based on various flags.
	new_sub_cat_name = f"{sub_cat_name}{scn_nocut_mode}{scn_restricted_mode}"
	return run, new_sub_cat_name, alias_name


# Process a normal run.
def process_normal_run(game: str, platform: str, board: str, player: str, flags: dict):
	"""
	Call SRDC via the lookup_run method.
	"""
	# Produce an internal key and search SRDC.
	# Return the value of lookup_run, directly to the caller.
	internal_key = f"{game}_{platform}"
	run = normal.lookup_run(internal_key, board, player, flags)
	return run


def process_multi_run(base_game: str, mr_board: str, mr_category_board: str, player: str) -> (SpeedRun | None, str | None):
	"""
	Using the provided variables, determine if the multi-run board
	is configured and whether there is a valid mr_board value.

	If all above board, pass the data over to lookup_ce_run,
	alongside the player and internal_key and find the run.

	Returns a SpeedRun object or None.
	"""
	# Parse the base_game to see if we have a supported multi-run
	# board in the code. If not, there is an error.
	mr_key = mr_config.GAME_MAP.get(base_game)
	if not mr_key:
		return None

	# Parse the mr_key (which contains the game name) to see
	# if it exists. If not, there is an error.
	alias_table = mr_config.CATEGORY_ALIASES.get(mr_key["id"])
	if not alias_table:
		return None

	# Check if the top board is defined in the alias list.
	# If it isn't, the user might have provided an alternative
	# name, which needs to be checked
	if mr_board not in alias_table:
		mr_board = mr_config.BOARD_TOKEN_ALIASES[mr_key["id"]].get(mr_board, None)
		if mr_board is None:
			return None

	# Use the board_token (the top-level board) to find
	# actual internal token name (this is needed to ensure
	# random user input always maps to the correct internal
	# value).
	#
	# If this returns None, then whatever token they provided
	# does not exist in the alias table.
	board_token = alias_table[mr_board].get(mr_category_board, None)
	if board_token is None:
		return None

	# Build the internal key and lookup the multi-run.
	internal_key = f"{mr_board}_{board_token}"
	run = multirun.lookup_multi_run(base_game, internal_key, player)

	# Produce a clean name based on the alias value. This allows one
	# "output" name against lots of aliases for tidiness of the
	# board aliases.
	alias_name = None
	cat_clean_name = None
	for name, aliases in mr_config.BOARD_ALIASES.items():
		if mr_board in aliases:
			alias_name = name
			break
	for name, aliases in mr_config.SUB_CATEGORY_MAP.items():
		if mr_category_board in aliases:
			cat_clean_name = name
			break

	# Return the run object and the alias_name produced.
	return run, cat_clean_name, alias_name


def process_category_extension(base_game: str, ce_top_board: str, ce_category_board: str, player: str) -> (SpeedRun | None, str | None):
	"""
	Using the provided variables, determine if the category
	extension is configured and whether there is a valid
	category_board value.

	If all above board, pass the data over to lookup_ce_run,
	alongside the player and internal_key and find the run.

	Returns a SpeedRun object or None.
	"""
	# Parse the base_game to see if we have a supported CE
	# board in the code. If not, there is an error.
	ce_key = ce_config.GAME_MAP.get(base_game)
	if not ce_key:
		return None

	# Parse the ce_key (which contains the game name) to see
	# if it exists. If not, there is an error.
	alias_table = ce_config.CATEGORY_ALIASES.get(ce_key["id"])
	if not alias_table:
		return None

	# Check if the top board is defined in the alias list.
	# If it isn't, the user might have provided an alternative
	# name, which needs to be checked
	if ce_top_board not in alias_table:
		ce_top_board = ce_config.BOARD_TOKEN_ALIASES[ce_key["id"]].get(ce_top_board, None)
		if ce_top_board is None:
			return None

	# Use the board_token (the top-level board) to find the
	# actual internal token name (this is needed to ensure
	# random user input always maps to the correct internal
	# value).
	board_token = None
	for name, aliases in alias_table.get(ce_top_board, {}).items():
		if ce_category_board in aliases:
			board_token = name
			break

	# After the loop above, if this is still None, then whatever
	# token they provided does not exist in the alias table.
	if board_token is None:
		return None

	# Build the internal key and lookup the CE.
	internal_key = f"{ce_top_board}_{board_token}"
	run = cat_ext.lookup_ce_run(base_game, internal_key, player)

	# Produce a clean name based on the alias value. This allows one
	# "output" name against lots of aliases for tidiness of the
	# board aliases.
	alias_name = None
	cat_alias_name = None
	for name, aliases in ce_config.BOARD_ALIASES.items():
		if ce_top_board in aliases:
			alias_name = name
			break
	for name, aliases in ce_config.SUB_CATEGORY_MAP.items():
		if ce_category_board in aliases:
			cat_alias_name = name
			break

	# Return the run object and the alias_name produced.
	return run, cat_alias_name, alias_name


# Parse the list of extra data in the arguments for handling
# by the extract_flags. This will split by the encoded plus
# signs first, then unquote individual values if they're also
# url-encoded (such as --player=someone).
def split_extras(argstr: str) -> list[str]:
	if not argstr:
		return []
	token_list = [p.strip().lower() for p in argstr.split('+') if p.strip()]
	return [url_parse.unquote(token) for token in token_list]


# Parse all arguments from "args"
# This effectively covers optional switches
# or behavioural changes
def extract_flags(tokens: list[str]) -> dict:
	# Set default flag values
	# These will then be used by the program to decide certain things
	flags = {
		"emulator": False, "player": None,
		"ce_board": None, "mr_board": None,
		"lego_md": {},
		"additional_metadata": {}
	}
	key_num = 1

	# Parse all the tokens and map them to things.
	#
	# For CE/MR tokens, we ignore the key name of each iteration
	# as that is only for output text: here we just care about
	# alias checks.
	#
	# Invalid tokens will be silently discarded by the program
	# and will not be processed.
	for token in tokens:
		# Check if the token is set to emulator
		if token == "emulator":
			flags["emulator"] = True
			continue

		# Check if the token represents a sub-board for category extensions.
		ce_match = False
		for _, aliases in ce_config.SUB_CATEGORY_MAP.items():
			if token in aliases:
				flags["ce_board"] = token
				ce_match = True
				break
		if ce_match:
			continue

		# Check if the token represents a sub-board for multi-runs.
		mr_match = False
		for _, aliases in mr_config.SUB_CATEGORY_MAP.items():
			if token in aliases:
				flags["mr_board"] = token
				mr_match = True
				break
		if mr_match:
			continue

		# Check if the token contains the string --player=
		# or its alias --p=. If no value is provided, it will
		# still be set to None and thus ignored.
		if "--player=" in token or "--p=" in token:
			p_name = token.split("=")[1]
			flags["player"] = p_name if len(p_name) > 0 else None

		# Check if the token is a string connected to LEGO boards
		# At the moment, this is a fairly restricted list, but plan
		# is to make this handler better in the future.
		if token in lego_config.FLAG_TOKEN_MATCHES:
			# Check which token it matched.
			match token:
				case _ if token in ["solo", "co-op", "coop"]:
					flags["lego_md"]["main_sub_category"] = token
				case _ if token in ["nocut5", "n0cut5", "standard"]:
					flags["lego_md"]["nocut_mode"] = True if token != "standard" else False
				case _ if token in ["restricted", "unrestricted"]:
					flags["lego_md"]["restricted_mode"] = True if token == "restricted" else False

		# Nothing was found. Perhaps its additional metadata:
		# add an incrementing key number value pair to the
		# metadata list
		flags["additional_metadata"][f"key_{key_num}"] = token
		key_num += 1

	return flags


# Given a specific player, game and category, return the most
# recently verified run that the player has submitted.
# This code is much more efficient than parsing out every PB
# the user has submitted, particularly if you just want to look
# at one game.
@app.route('/run/<owner>/<game>/<platform>/<board>/', defaults={'args': None})
@app.route('/run/<owner>/<game>/<platform>/<board>/<path:args>')
def latest_run(owner, game, platform, board, args):
	# I can't imagine that these will be in upper-case,
	# but just make sure everything is lower-case.
	owner = owner.strip().lower()
	game = game.strip().lower()
	platform = platform.strip().lower()
	board = board.strip().lower()

	# Parse everything in the arguments, if anything is there.
	extras = split_extras(args)
	flags = extract_flags(extras)
	runner_override = flags.get("player", None)

	# Resolve the player. This will always be the channel owner,
	# unless the player flag has been set.
	player = runner_override if runner_override is not None else owner
	player = resolve_player(owner, player)

	# Process the provided data and match it to value of "game".
	# This will set the code off to finding a run that matches
	# the search parameters.
	match game:
		case _ if game in ("ce", "catext"):
			# This is a category extension: pass everything to
			# the processor and store the result in a variable.
			result, cat_clean_name, alias_name = process_category_extension(platform, board, flags["ce_board"], player)
			clean_name = f'{ce_config.GAME_MAP[platform]["name"]} ({alias_name} - {cat_clean_name})'
		case _ if game in ("multirun", "multi", "mr"):
			# This is a multi-run: pass everything to
			# the processor and store the result in a variable.
			result, cat_clean_name, alias_name = process_multi_run(platform, board, flags["mr_board"], player)
			clean_name = f'{mr_config.GAME_MAP[platform]["name"]} ({alias_name} - {cat_clean_name})'
		case "lego":
			# This is a LEGO main-board game.
			# Due to LEGO games having more sub-categories than regular
			# main board categories, they're handled separately due to
			# extra metadata being needed.
			result, cat_clean_name, alias_name = process_lego_main_board(platform, board, flags["lego_md"], player)
			clean_name = f'{lego_config.GAME_MAP[platform]["name"]} ({alias_name} - {cat_clean_name})'
		case _:
			# This is a normal main board run which is not a LEGO game:
			# check if game, platform and board represent real entities
			# and show an error if not.
			if game not in nm_config.GAME_MAP:
				return f"Unknown game: '{game}'. Refer to the docs for the supported games: {config.COMMAND_USAGE_DOC}", 400
			if platform not in config.PLATFORM_MAP:
				return f"Unknown platform: '{platform}'. Refer to the docs for the supported platforms: {config.COMMAND_USAGE_DOC}", 400

			# Check if the board name is in the category list.
			not_board = True
			category_name = None
			for board_name, aliases in nm_config.CATEGORY_MAP.items():
				if board in aliases:
					not_board = False
					category_name = board_name
					break

			if not_board:
				return f"Unknown category/board: '{board}'.  Refer to the docs for the supported categories: {config.COMMAND_USAGE_DOC}", 400

			# Process the data and return SpeedRun or None.
			result = process_normal_run(game, platform, board, player, flags)
			clean_name = f'{nm_config.GAME_MAP[game]} ({config.PLATFORM_MAP[platform].upper()} - {category_name})'

	# Check if a run object was returned, or if it is None.
	if result is None:
		return "No run found for this criteria."

	# Output the relevant text, after a little processing,
	emulator_text = " (Emulator)" if result.emulator and result.platform != "8gej2n93" else ""
	place = getattr(result, "place", "?")
	time = getattr(result, "time", "unknown time")
	link = getattr(result, "link", "no link")
	return f"The most recent verified run for {player} in {clean_name}{emulator_text} is {time} (#{place}): {link}"


# Find a PB for the given player and category.
# This is less efficient than just finding the most
# recent run in a specific game, because the user may
# have a LOT of submitted PBs in their name.
# Daily/regular use should be to use the !run
# command, which calls the /run route above.
@app.route('/pb/<owner>/<game>/<platform>/<board>/', defaults={'args': None})
@app.route('/pb/<owner>/<game>/<platform>/<board>/<path:args>')
def personal_best(owner, game, platform, board, args):
	# I can't imagine that these will be in upper-case,
	# but just make sure everything is lower-case.
	owner = owner.strip().lower()
	game = game.strip().lower()
	platform = platform.strip().lower()
	board = board.strip().lower()

	# Parse everything in the arguments, if anything is there.
	extras = split_extras(args)
	flags = extract_flags(extras)
	runner_override = flags.get("player", None)

	# Resolve the player. This will always be the channel owner,
	# unless the player flag has been set.
	player = runner_override if runner_override is not None else owner
	player = resolve_player(owner, player)

	# Parse the board value in both the CE and MR category maps.
	not_main = True
	not_in_ce = True
	not_in_mr = True
	mode = None
	category_name = None
	for main_cat_name, aliases in nm_config.CATEGORY_MAP.items():
		if board in aliases:
			not_main = False
			category_name = main_cat_name
			break
	for sub_cat_name, aliases in ce_config.SUB_CATEGORY_MAP.items():
		if board in aliases:
			not_in_ce = False
			category_name = sub_cat_name
			mode = "ce"
			break
	for sub_cat_name, aliases in mr_config.SUB_CATEGORY_MAP.items():
		if board in aliases:
			not_in_mr = False
			category_name = sub_cat_name
			mode = "mr"
			break

	# Check if board is in the category map.
	# If it's not there, then the run is not valid and should return.
	if not_main and not_in_ce and not_in_mr:
		return f"Unknown category: {board}. Try again, or refer to the docs: {config.COMMAND_USAGE_DOC}"

	# Produce an internal key.
	internal_key = f"{game}_{platform}"
	board_name = None
	match mode:
		case "ce":
			# Check if the platform name is in the alias list.
			alias_found = False
			for name, aliases in ce_config.BOARD_ALIASES.items():
				if platform in aliases:
					board_name = name
					alias_found = True
					break

			# If alias_found is False, then the alias is invalid.
			if not alias_found:
				return f"CE alias cannot be found internally: either this is a bug, or you specified an invalid CE alias. Check the docs: {config.COMMAND_USAGE_DOC}"

			# Capture the internal key based on board_name
			for key, data in lb_config.LEADERBOARD_CONFIG[game].items():
				if data["board"] == board_name:
					internal_key = key
					break
		case "mr":
			# Check if the platform name is in the alias list.
			alias_found = False
			for name, aliases in mr_config.BOARD_ALIASES.items():
				if platform in aliases:
					board_name = name
					alias_found = True
					break

			# If alias_found is False, then the alias is invalid.
			if not alias_found:
				return f"Multi-run alias cannot be found internally: either this is a bug, or you specified an invalid alias. Check the docs: {config.COMMAND_USAGE_DOC}"

			# Capture the internal key based on board_name
			for key, data in lb_config.LEADERBOARD_CONFIG[game].items():
				if data["board"] == board_name:
					internal_key = key
					break

	# Query SRDC to find the most recent PB of the player for this game/category.
	try:
		result = per_best.lookup_pb(mode, game, internal_key, board, player, flags)
	except ValueError as e:
		return str(e)

	# Was there any results?
	if not result:
		return "No PB found for this criteria."

	# Match the mode to generate a clean name.
	match mode:
		case "ce":
			game_name = None
			for key, val in ce_config.GAME_MAP.items():
				if val["id"] == game:
					game_name = val["name"]
					break
			clean_name = f"{game_name} ({board_name} - {category_name})"
		case "mr":
			game_name = None
			for key, val in mr_config.GAME_MAP.items():
				if val["id"] == game or game in val.get("aliases", []):
					game_name = val["name"]
					break
			clean_name = f"{game_name} ({board_name} - {category_name})"
		case _:
			is_emulator = " (Emulator)" if result.emulator else ""
			clean_name = f"{nm_config.GAME_MAP[game]} ({config.PLATFORM_MAP[platform].upper()} - {category_name}{is_emulator})"

	# Return the standard string to represent this PB.
	return f"The current PB for {player} in {clean_name} is {result.time}, currently placing #{result.place}: {result.link}"


# Provide help and support to users calling the routes.
@app.route("/help")
def command_help():
	return f"This bot can search SRDC for the latest run or a personal best. See the docs for commands/usage: {config.COMMAND_USAGE_DOC}"


# Common error handlers
@app.errorhandler(ValueError)
def value_error_handler(error):
	return str(error)


# @app.errorhandler(KeyError)
# def key_error_handler(error):
# 	return f"One or more of the inputs provided couldn't be found: '{str(error)}'"


@app.errorhandler(500)
def internal_error(error):
	return f"Encountered an error in your request, or could not find a run: {str(error)}"


@app.errorhandler(408)
def timeout_error(error):
	# Return timeout error
	return f"Request timed out, try again later: {str(error)}."


if __name__ == "__main__":
	app.run()
