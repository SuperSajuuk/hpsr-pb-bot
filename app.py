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

# Import all the packages we need
import flask
import config
import srcomapi
import utils
import srdc.normal as normal_run
import srdc.ce as ce_run
import srdc.pb as pb
from model import SpeedRun

# Instantiate Flask and the SRDC API
app = flask.Flask(__name__)
srdc_api = srcomapi.SpeedrunCom()
srdc_api.debug = 1

# Instantiate all our internal code for powering the actual program.
utils = utils.Utilities(srdc_api)
normal = normal_run.NormalRun(srdc_api, config.GAME_MAP, config.PLATFORM_MAP, config.CATEGORY_MAP, utils)
cat_ext = ce_run.CategoryExtension(srdc_api, config.CE_GAME_MAP, config.PLATFORM_MAP, config.CE_BOARD_ALIASES, config.CE_CATEGORY_ALIASES, utils)
srdc = pb.PersonalBest(srdc_api, config.GAME_MAP, config.PLATFORM_MAP, config.CATEGORY_MAP)


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


def process_multi_run(platform: str, multirun_key: str, board: str, extras: list[str], player: str, flags: dict):
	"""
	Parse the values of platform, multirun_key and board for a multi-run submission.
	This will then call SRDC using lookup_multi_run.
	"""
	multirun_categories = config.LEADERBOARD_CONFIG.get("hpmulti", {}).get("categories", {})
	# Prefer board if it matches a multirun category; otherwise try extras
	cat_key = board if board in multirun_categories else None
	if not cat_key:
		for t in extras:
			if t in multirun_categories:
				cat_key = t
				break
	# Fallback to 'any' if still missing
	if not cat_key:
		cat_key = "any"

	# Validate multirun_key (some callers may pass board as multirun_key)
	if multirun_key not in multirun_categories:
		# try extras for multirun key
		for t in extras:
			if t in multirun_categories:
				multirun_key = t
				break
	if multirun_key not in multirun_categories:
		return None

	# Call the SRDC multirun lookup. Adjust signature to your implementation.
	# Example assumed signature: srdc.lookup_multirun(multirun_key, platform, cat_key, player)
	run = srdc.lookup_multirun(multirun_key, platform, cat_key, player)

	if run is not None and flags.get("emulator", False):
		setattr(run, "emulator", True)
	return run


# -------------------------------
# process_category_extension
# -------------------------------
def process_category_extension(base_game: str, ce_board: str, extras: list[str], player: str, flags: dict) -> SpeedRun | None:
	"""
	Fully dynamic CE parser + CE run lookup.
	"""
	# Parse the base_game to see if we have a supported CE
	# board in the code. If not, there is an error.
	ce_key = config.CE_GAME_MAP.get(base_game)
	if not ce_key:
		return None

	# Parse the ce_key (which contains the game name) to see
	# if it exists. If not, there is an error.
	alias_table = config.CE_CATEGORY_ALIASES.get(ce_key)
	if not alias_table:
		return None

	# Now find the board they are actually looking for.
	# Due to length reasons, this may either be in the
	# ce_board variable, or it will come from the extras
	# due to overflow.
	# board may come from ce_board OR extras.
	board_token = ce_board.lower() if ce_board else None
	if not board_token or board_token not in alias_table:
		# Try extras
		for t in list(extras):
			if t in alias_table:
				board_token = t
				extras.remove(t)
				break

	# Nothing found, so assumed not to exist
	if not board_token:
		return None

	# Map the board_alias and set the runner to the relevant
	# player variable.
	board_alias_map = alias_table[board_token]
	sub_token = None
	runner = player

	# Check the extras for any sub-tokens of relevance
	# or assume a plyer override is given.
	for t in list(extras):
		if t in board_alias_map:
			sub_token = t
			extras.remove(t)
		else:
			# Anything not a subcategory becomes runner
			runner = t

	# Build the internal key and lookup the CE. Then return the run result.
	resolved_sub = board_alias_map[sub_token]
	internal_key = f"{board_token}_{resolved_sub}"
	run = cat_ext.lookup_ce_run(base_game, internal_key, runner, flags)
	return run


# Parse the list of extra data in the arguments.
# Used by latest_run and personal_best.
def split_extras(argstr: str) -> list[str]:
	return [] if not argstr else [p.strip().lower() for p in argstr.split('+') if p.strip()]


# Parse the player and other flags in the token list.
def extract_player_and_flags(tokens: list[str]) -> tuple[list[str], str | None, dict]:
	flags = {"emulator": False}
	remaining: list[str] = []
	player_candidate: str | None = None
	for token in tokens:
		# Check if the token is set to emulator
		# This usually means we're looking up a 6th gen run with console/emulator splits.
		if token == "emulator":
			flags["emulator"] = True
			continue
		# Keep platform tokens for mode-specific parsing
		if token in config.PLATFORM_MAP:
			remaining.append(token)
			continue
		# CE tokens
		if token in getattr(config, "CE_TYPE_MAP", {}) or token in getattr(config, "CE_CATEGORY_MAP", {}):
			remaining.append(token)
			continue
		# Top-level categories or multirun keys
		if token in config.CATEGORY_MAP or token in config.LEADERBOARD_CONFIG.get("hpmulti", {}).get("categories", {}):
			remaining.append(token)
			continue
		# Token doesn't match anything: it's probably an alternative runner we're looking for.
		player_candidate = token

	return remaining, player_candidate, flags


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
	remaining, player_override, flags = extract_player_and_flags(extras)

	# Resolve the player. This will always be the channel owner,
	# unless the player_override has been set.
	player = player_override if player_override else owner
	player = resolve_player(owner, player)

	# Process the provided data and match it to value of "game".
	# This will set the code off to finding a run that matches
	# the search parameters.
	match game:
		case "ce":
			# This is a category extension, pass everything to
			# the processor and store the result in a variable.
			cat_clean_name = config.CE_CATEGORY_MAP[extras[0]]
			result = process_category_extension(platform, board, extras, player, flags)
			clean_name = f'{config.GAME_MAP[game]} ({config.CE_BOARD_ALIASES[board].upper()} - {cat_clean_name})'
		case _ if game in ("multirun", "multi"):
			# This is multi-run mode. Pull in the necessary config data and parse it.
			# As a quirk of the command syntax, if board doesn't look like a multirun key,
			# it might be in the extras.
			multirun_key = board
			multirun_categories = config.LEADERBOARD_CONFIG.get("hpmulti", {}).get("categories", {})
			if multirun_key not in multirun_categories:
				for t in list(extras):
					if t in multirun_categories:
						multirun_key = t
						extras.remove(t)
						break

			# Check if the multirun_key is in the category list.
			if multirun_key not in multirun_categories:
				return "Unknown multirun key. Provide a valid multirun (e.g., pctrifecta).", 400

			# Process a multi-run: returns SpeedRun or None.
			result = process_multi_run(owner, platform, multirun_key, board, extras, player, flags)
			clean_name = multirun_key
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
	emulator_text = " (Emulator)" if result.emulator else ""
	place = getattr(result, "place", "?")
	time = getattr(result, "time", "unknown time")
	link = getattr(result, "link", "no link")
	return f"The most recent verified run for {player} in {clean_name}{emulator_text} is {time} (#{place}): {link}"


# Find a PB for the given player and category.
# This is less efficient than just finding the most
# recent run in a specific game, because the user may
# have a LOT of submitted PBs in their name.
# Recommend that daily use should be to use the !run
# command instead.
@app.route('/pb/<path:args>')
def personal_best(args):
	# Parse the arguments and check we have 3.
	parts = args.split("+")
	if len(parts) < 3:
		return "Error: this route requires owner+game+cat to be provided", 400

	# Set vars based on the parts (order must be consistent)
	owner = parts[0]
	game = parts[1]
	cat = parts[2]
	platform = parts[3] if len(parts) > 3 else None
	player = parts[4] if len(parts) > 4 else None

	# Validate game/category exist in the mapping.
	# At some point, the game check should be removed, so
	# that this can be used to find a PB for any game by the
	# user. Category filter would be ideal though.
	player = resolve_player(owner, player)
	game = game.lower()
	cat = cat.lower()
	if game not in config.GAME_MAP:
		return f"Invalid game. See supported options: {config.COMMAND_USAGE_DOC}"
	if cat not in config.CATEGORY_MAP:
		return f"Invalid category. See supported options: {config.COMMAND_USAGE_DOC}"

	# Query SRDC to find the most recent PB of the player for this game/category.
	try:
		result = srdc.lookup_pb(game, cat, player, platform)
	except ValueError:
		return "No PB found for this criteria."

	# Was there any results?
	if not result:
		return "No PB found for this criteria."

	# Print the standard string to represent this PB.
	pb = result[0]
	is_emulator = " (Emulator)" if pb.emulator else ""
	return f"{player.capitalize()} has a PB of {pb.time} (#{pb.place}) in {game.upper()} {config.CATEGORY_MAP[cat]['clean']}{is_emulator}: {pb.link}"


# Provide help and support to users calling the routes.
@app.route("/help")
def command_help():
	return f"This bot can search SRDC for the latest run or a personal best. See the docs for commands/usage: {config.COMMAND_USAGE_DOC}"


@app.route("/pb-options")
def pb_command_options():
	return f"Format: '!pb gamecode categorycode srdcusername' | Example: '!pb hp1 any% nixxo' | Full list of options: {config.COMMAND_USAGE_DOC}"


@app.route("/run-options")
def run_command_options():
	return f"Format: '!run gamecode categorycode srdcusername' | Example: '!pb hp1 any% nixxo' | Full list of options: {config.COMMAND_USAGE_DOC}"


@app.route("/<game>")
def missing_game(game):
	if len(game) > 1:
		return f"A game and category must be defined. Please refer to the documentation for how to use the command: {config.COMMAND_USAGE_DOC}"
	else:
		return f"To find a PB, use this command: '!pb gamecode categorycode srdcusername'. For more info, check the docs: {config.COMMAND_USAGE_DOC}"


# Common error handlers
@app.errorhandler(500)
def internal_error(error):
	return "Encountered an error in your request, or could not find a run."


@app.errorhandler(408)
def timeout_error(error):
	# Return timeout error
	return "Request timed out, please try typing the command again."


if __name__ == "__main__":
	app.run(debug=True)
