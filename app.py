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
# The modular aspects of the code are in data.py. A future commit
# will split up data.py into more logical pieces so everything is much
# more understandable.

# Import the core packages
import flask
import srcomapi

# Import the config data.
import configs.ce as ce_config
import configs.multi as mr_config
import configs.normal as nm_config
import configs.leaderboard as lb_config
import configs.generic as config
# import config

# Import everything else that is needed
import utils
import srdc.normal as normal_run
import srdc.ce as ce_run
import srdc.pb as pb
import srdc.multi as multi
from model import SpeedRun

# Instantiate Flask and the SRDC API
app = flask.Flask(__name__)
srdc_api = srcomapi.SpeedrunCom()
srdc_api.debug = 1

# Instantiate all our internal code for powering the actual program.
utils = utils.Utilities(srdc_api, lb_config.LEADERBOARD_CONFIG)
normal = normal_run.NormalRun(srdc_api, nm_config.GAME_MAP, config.PLATFORM_MAP, nm_config.CATEGORY_MAP, utils)
cat_ext = ce_run.CategoryExtension(srdc_api, ce_config.GAME_MAP, config.PLATFORM_MAP, ce_config.CATEGORY_ALIASES, lb_config.LEADERBOARD_CONFIG, utils)
multirun = multi.MultiRun(srdc_api, mr_config.GAME_MAP, config.PLATFORM_MAP, mr_config.CATEGORY_ALIASES, lb_config.LEADERBOARD_CONFIG, utils)
per_best = pb.PersonalBest(srdc_api, nm_config.GAME_MAP, config.PLATFORM_MAP, nm_config.CATEGORY_MAP, ce_config.BOARD_ALIASES, ce_config.SUB_CATEGORY_MAP, utils)


# Resolve the player, in case we just want to check for the channel owner.
# channel_owner is always provided, but player may not be:
def resolve_player(channel_owner: str, player: str | None) -> str:
	return channel_owner if player is None or player.strip() == "" else player


# Process a normal run.
def process_normal_run(game: str, platform: str, board: str, extras: list[str], player: str, flags: dict):
	"""
	Parse the values of game, platform and board for a single game run,
	then call SRDC via the lookup_run method.
	"""
	# Validate category
	cat_key = board
	if extras:
		# If extras contains a known category, prefer it (first match)
		for t in extras:
			if t in config.CATEGORY_MAP:
				cat_key = t
				break

	# Check if cat_key is in the category map.
	# If it's not there, then the run is not valid and should return.
	if cat_key not in config.CATEGORY_MAP:
		return None

	# Produce an internal key and search SRDC.
	# Return the value of lookup_run, directly to the caller.
	internal_key = f"{game}_{platform}"
	run = normal.lookup_run(internal_key, cat_key, player, flags)
	return run


def process_multi_run(base_game: str, mr_board: str, extras: list[str], player: str, flags: dict) -> SpeedRun | None:
	"""
	Fully dynamic CE parser + CE run lookup.
	"""
	# Parse the base_game to see if we have a supported Multirun
	# board in the code. If not, there is an error.
	mr_key = mr_config.GAME_MAP.get(base_game)
	if not mr_key:
		return None

	# Parse the mr_key (which contains the game name) to see
	# if it exists. If not, there is an error.
	alias_table = mr_config.CATEGORY_ALIASES.get(mr_key["id"])
	if not alias_table:
		return None

	# Use the board_token (the top-level board) to find
	# actual internal token name (this is needed to ensure
	# random user input always maps to the correct internal
	# value).
	token = mr_board.lower() if mr_board else None
	board_token = mr_config.BOARD_TOKEN_ALIASES[mr_key["id"]].get(token, None)
	if token is None and board_token is None:
		return None
	if token is not None and board_token is None:
		board_token = token

	# Now find the board they are actually looking for.
	# This may be in board_token: if it isn't, we will check
	# the mr_board flag.
	if not board_token or board_token not in alias_table:
		mr_board_flag = flags.get("mr_board", None)
		if mr_board_flag is not None and mr_board_flag in alias_table:
			board_token = mr_board_flag

	# Nothing found, so assumed not to exist
	if not board_token:
		return None

	# Map the board_alias and set the runner to the relevant
	# player variable.
	board_alias_map = alias_table[board_token]
	sub_token = None
	runner = player

	# Check the extras for any sub-tokens of relevance
	# or assume a player override is given.
	for t in list(extras):
		if t in board_alias_map:
			sub_token = t
			extras.remove(t)
		else:
			# Anything not a subcategory becomes runner
			runner = t

	# Build the internal key and lookup the Multirun. Then return the run result.
	resolved_sub = board_alias_map[sub_token]
	internal_key = f"{board_token}_{resolved_sub}"
	run = multirun.lookup_multi_run(base_game, internal_key, runner, flags)
	return run


def process_category_extension(base_game: str, ce_top_board: str, ce_category_board: str, player: str) -> SpeedRun | None:
	"""
	Using the provided variables, determine if the category
	extension is configured, there is a valid category_board
	value,
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

	# Use the board_token (the top-level board) to find
	# actual internal token name (this is needed to ensure
	# random user input always maps to the correct internal
	# value).
	#
	# If this returns None, then whatever token they provided
	# does not exist in the alias table.
	board_token = alias_table[ce_top_board].get(ce_category_board, None)
	if board_token is None:
		return None

	# Build the internal key and lookup the CE. Then return the run result.
	internal_key = f"{ce_top_board}_{board_token}"
	run = cat_ext.lookup_ce_run(base_game, internal_key, player)
	return run


# Parse the list of extra data in the arguments.
# Used by latest_run and personal_best.
def split_extras(argstr: str) -> list[str]:
	return [] if not argstr else [p.strip().lower() for p in argstr.split('+') if p.strip()]


# Parse all arguments from "args"
# This effectively covers optional switches
# or behavioural changes
def extract_flags(tokens: list[str]) -> dict:
	# Set default flag values
	# These will then be used by the program to decide certain things
	flags = {
		"emulator": False, "player": None,
		"ce_board": None, "mr_board": None
	}

	# Parse all the tokens and map them to things.
	for token in tokens:
		# Check if the token is set to emulator
		if token == "emulator":
			flags["emulator"] = True
			continue

		# Check if the token represents a sub-board for category extensions.
		if token in ce_config.SUB_CATEGORY_MAP:
			flags["ce_board"] = token
			continue

		# Check if the token represents a sub-board for multi-runs.
		if token in mr_config.SUB_CATEGORY_MAP:
			flags["mr_board"] = token
			continue

		# The token did not match anything in the defined list.
		# Assuming that the token means a player override.
		flags["player"] = token

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
	extras_raw = args

	# Parse everything in the arguments, if anything is there.
	extras = split_extras(extras_raw)
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
		case "ce":
			# This is a category extension, pass everything to
			# the processor and store the result in a variable.
			cat_clean_name = ce_config.SUB_CATEGORY_MAP[flags["ce_board"]]
			result = process_category_extension(platform, board, flags["ce_board"], player)
			clean_name = f'{ce_config.GAME_MAP[platform]["name"]} ({ce_config.BOARD_ALIASES[board]} - {cat_clean_name})'
		case _ if game in ("multirun", "multi"):
			# This is a category extension, pass everything to
			# the processor and store the result in a variable.
			cat_clean_name = mr_config.SUB_CATEGORY_MAP[flags["mr_board"]]
			result = process_multi_run(platform, board, extras, player, flags)
			clean_name = f'{mr_config.GAME_MAP[platform]["name"]} ({mr_config.BOARD_ALIASES[board]} - {cat_clean_name})'
		case _:
			# Normal single-game run
			# Validate that the values in game, platform and board actually match something.
			if game not in config.GAME_MAP:
				return f"Unknown game: '{game}'. Refer to the docs for the supported games: {config.COMMAND_USAGE_DOC}", 400
			if platform not in config.PLATFORM_MAP:
				return f"Unknown platform: '{platform}'. Refer to the docs for the supported platforms: {config.COMMAND_USAGE_DOC}", 400
			if board not in config.CATEGORY_MAP:
				return f"Unknown category/board: '{board}'.  Refer to the docs for the supported categories: {config.COMMAND_USAGE_DOC}", 400

			# Process the data and return SpeedRun or None.
			result = process_normal_run(game, platform, board, extras, player, flags)
			clean_name = f'{config.GAME_MAP[game]} ({config.PLATFORM_MAP[platform].upper()} - {config.CATEGORY_MAP[board]})'

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
	extras_raw = args

	# Parse everything in the arguments, if anything is there.
	extras = split_extras(extras_raw)
	flags = extract_flags(extras)
	runner_override = flags.get("player", None)

	# Resolve the player. This will always be the channel owner,
	# unless the player flag has been set.
	player = runner_override if runner_override is not None else owner
	player = resolve_player(owner, player)

	# Validate category
	cat_key = board
	is_ce_pb = False
	if extras:
		# If extras contains a known category, prefer it (first match)
		for t in extras:
			if t in config.CATEGORY_MAP:
				cat_key = t
				break
			if t in ce_config.SUB_CATEGORY_MAP:
				cat_key = t
				is_ce_pb = True
				break

	# Check if cat_key is in the category map.
	# If it's not there, then the run is not valid and should return.
	if cat_key not in config.CATEGORY_MAP and cat_key not in ce_config.SUB_CATEGORY_MAP:
		return f"Unknown category key: {cat_key}. Try again, or refer to the docs: {config.COMMAND_USAGE_DOC}"

	# Produce an internal key. If this is a CE, get it from aliases.
	internal_key = f"{game}_{platform}"
	board_name = None
	if is_ce_pb or cat_key in ce_config.SUB_CATEGORY_MAP:
		ce_aliases = lb_config.LEADERBOARD_CONFIG[game].get("aliases", {})
		if platform not in ce_aliases:
			return f"CE alias cannot be found internally: either this is a bug, or you specified an invalid CE alias. Check the docs: {config.COMMAND_USAGE_DOC}"

		# Set board name, then find it in the board list
		board_name = ce_aliases[platform]
		for key, data in lb_config.LEADERBOARD_CONFIG[game]["categories"].items():
			if data["board"] == board_name:
				internal_key = key
				break

	# Query SRDC to find the most recent PB of the player for this game/category.
	try:
		result = per_best.lookup_pb(game, internal_key, board, player, extras, flags)
	except ValueError:
		return "No PB found for this criteria."

	# Was there any results?
	if not result:
		return "No PB found for this criteria."

	# Print the standard string to represent this PB.
	is_emulator = " (Emulator)" if result.emulator else ""
	if is_ce_pb or cat_key in ce_config.SUB_CATEGORY_MAP:
		clean_name = f"{config.GAME_MAP[game]} ({board_name} - {ce_config.SUB_CATEGORY_MAP[board]})"
	else:
		clean_name = f"{config.GAME_MAP[game]} ({config.PLATFORM_MAP[platform].upper()} - {config.CATEGORY_MAP[cat_key]}{is_emulator})"
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
	return f"Encountered an error in your request, or could not find a run: {str(error)}."


@app.errorhandler(408)
def timeout_error(error):
	# Return timeout error
	return f"Request timed out, try again later: {str(error)}."


if __name__ == "__main__":
	app.run()
