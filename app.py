#
# Find ILs, Runs or PBs on Speedrun.com
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
# codes can be found in the configs and srdc sub-folders.
#

# Import the core packages
import flask
import srcomapi
import redis
import os

# Import the config data.
import configs.game_maps as games
import configs.ils as il_config
import configs.leaderboard as lb_config
import configs.generic as config

# Import everything else that is needed
import utils.api as api
import utils.func as func
import utils.exceptions as exc
import utils.cache as caching
import urllib.parse as url_parse
import srdc.wr as wr
import srdc.ils as ind_lvl
import srdc.normal as normal_run
import srdc.ce as ce_run
import srdc.cc as cc_run
import srdc.pb as pb
import srdc.multi as multi
import srdc.lego as lego
from utils.model import SpeedRun

# Instantiate Flask and the SRDC API
app = flask.Flask(__name__)
srdc_api = srcomapi.SpeedrunCom()
srdc_api.debug = 1

# Configure Redis client support with a connection pool.
pool = redis.ConnectionPool(
	host=os.getenv("REDIS_HOST"),
	port=int(os.getenv("REDIS_PORT")),
	db=int(os.getenv("REDIS_DATABASE")),
	username=os.getenv("REDIS_USERNAME"),
	password=os.getenv("REDIS_PASSWORD"),
	max_connections=8,
	decode_responses=True
)

# Instantiate various internal classes for caching, API and functions.
cache = caching.Caching(redis.Redis(connection_pool=pool))
api = api.API(srdc_api, cache)
utils = func.Utilities(api, lb_config.LEADERBOARD_CONFIG, config.PLATFORM_MAP)

# Instantiate the core program code that handles run management
world = wr.WorldRecords(
	srdc_api=srdc_api,
	api=api,
	game_map=games.NM_GAME_MAP,
	platform_map=config.PLATFORM_MAP,
	category_map=config.CATEGORY_MAP,
	md_aliases=config.METADATA_ALIASES,
	utils=utils
)
normal = normal_run.NormalRun(
	api=api,
	game_map=games.NM_GAME_MAP,
	platform_map=config.PLATFORM_MAP,
	category_map=config.CATEGORY_MAP,
	md_aliases=config.METADATA_ALIASES,
	wr=world,
	utils=utils
)
il = ind_lvl.IndividualLevel(
	srdc_api=srdc_api,
	api=api,
	game_map=games.NM_GAME_MAP,
	levels_map=il_config.LEVELS_MAP,
	category_map=config.CATEGORY_MAP,
	ik_mapping=il_config.INTERNAL_KEY_MAPPING,
	utils=utils
)
lg = lego.LEGONormalRun(
	api=api,
	game_map=games.LEGO_GAME_MAP,
	md_aliases=config.METADATA_ALIASES,
	lb_config=lb_config.LEADERBOARD_CONFIG,
	utils=utils
)
cat_ext = ce_run.CategoryExtension(
	api=api,
	game_map=games.CE_GAME_MAP,
	md_aliases=config.METADATA_ALIASES,
	lb_config=lb_config.LEADERBOARD_CONFIG,
	utils=utils
)
cust_con = cc_run.CustomContent(
	api=api,
	game_map=games.CC_GAME_MAP,
	md_aliases=config.METADATA_ALIASES,
	lb_config=lb_config.LEADERBOARD_CONFIG,
	utils=utils
)
multirun = multi.MultiRun(
	api=api,
	game_map=games.MR_GAME_MAP,
	lb_config=lb_config.LEADERBOARD_CONFIG,
	utils=utils
)
per_best = pb.PersonalBest(
	api=api,
	category_map=config.CATEGORY_MAP,
	platform_map=config.PLATFORM_MAP,
	md_aliases=config.METADATA_ALIASES,
	utils=utils
)


# Resolve the player, in case we just want to check for the channel owner.
# channel_owner is always provided, but player may not be:
def resolve_player(channel_owner: str, player: str | None) -> str:
	return channel_owner if player is None or player.strip() == "" else player


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
def extract_flags(game: str, tokens: list[str]) -> dict:
	# Set default flag values
	# These will then be used by the program to decide certain things
	flags = {
		"emulator": False, "world_record": False, "player": None,
		"ce_board": None, "cc_board": None, "mr_board": None,
		"lego_board": None, "place_num": -1, "additional_metadata": {}
	}
	key_num = 1

	# Parse all the tokens and map them to things.
	#
	# For CE/MR tokens, we ignore the key name of each iteration
	# as that is only for output text: here we just care about
	# alias checks.
	#
	# Tokens which meet none of the defined conditions below will
	# be added to additional_metadata. These are then processed
	# later in the routes, and anything invalid will simply be
	# ignored.
	for token in tokens:
		# Check if the token refers to emulator boards.
		if token in ["emu", "emulator"]:
			flags["emulator"] = True
			continue

		# Check if the token represents a sub-board for custom content.
		# Game must be set to CC or custom to actually trigger this block.
		cc_match = False
		if game in ["cc", "custom"]:
			if token in lb_config.CC_TOKEN_LOOKUP:
				flags["cc_board"] = token
				cc_match = True
		if cc_match:
			continue

		# Check if the token represents a sub-board for category extensions.
		# Game must be ce/catext to actually trigger this block.
		ce_match = False
		if game in ["ce", "catext"]:
			if token in lb_config.CE_TOKEN_LOOKUP:
				flags["ce_board"] = token
				ce_match = True
		if ce_match:
			continue

		# Check if the token represents a sub-board for multi-runs.
		# Game must be in the list to trigger this block.
		mr_match = False
		if game in ["multirun", "multi", "mr"]:
			if token in lb_config.MR_TOKEN_LOOKUP:
				flags["mr_board"] = token
				mr_match = True
		if mr_match:
			continue

		# Check if the token is a string connected to LEGO boards
		# At the moment, this is a fairly restricted list, but plan
		# is to make this handler better in the future.
		if game == "lego" and token in ["solo", "co-op", "coop"]:
			flags["lego_board"] = token
			continue

		# Check if the token starts with --player= or its alias --p=.
		if token.startswith(("--player=", "--p=")):
			_, _, p_name = token.partition("=")
			p_name = p_name.lstrip("=")
			flags["player"] = p_name if p_name else None
			continue

		# Check if the token contains --position or its aliases.
		# This is used when a requestor wants to know who submitted
		# a run at a specific place on a leaderboard. The default value
		# is -1, which will be ignored.
		if token.startswith(("--position=", "--pos=", "--place=")):
			_, _, pos_num = token.partition("=")
			pos_num = pos_num.lstrip("=")
			try:
				flags["place_num"] = int(pos_num)
			except ValueError:
				pass
			continue

		# Check if the token contains either --world-record or
		# the alias --wr. This tells the system only to look
		# for the current world record run.
		if token in ["--world-record", "--wr"]:
			flags["world_record"] = True
			continue

		# Nothing was found: simply add an incrementing
		# key number value pair to the metadata list, where
		# the value is the un-matched token.
		flags["additional_metadata"][f"key_{key_num}"] = token
		key_num += 1

	return flags


# Given a specific player, game, level and category, return either
# - the requested players' level submission for game and category OR
# - return the current world record IL submission for game and category.
#
# The IL route borrows heavily from latest_run, but with tweaks to accommodate
# that the IL system is much more primitive and doesn't have as many drilldown
# variables compared to regular boards.
@app.route('/il/<owner>/<game>/<platform>/<level>/<category>/', defaults={'args': None})
@app.route('/il/<owner>/<game>/<platform>/<level>/<category>/<path:args>')
def individual_level(owner, game, platform, level, category, args):
	# I can't imagine that these will be in upper-case,
	# but just make sure everything is lower-case.
	channel_owner = owner.strip().lower()
	game = game.strip().lower()
	platform = platform.strip().lower()
	level = level.strip().lower()
	category = url_parse.unquote(category.strip().lower())

	# Parse everything in the arguments, if anything is there.
	extras = split_extras(args)
	flags = extract_flags(game, extras)
	player = resolve_player(channel_owner, flags["player"])

	# Hand over results processing to the processor. This will either
	# return a SpeedRun object or None, if nothing was found.
	result, il_cat_name, game_name = il.process_il(game, platform, level, category, player, flags["world_record"])
	if not result:
		return "No individual level submission could be found with these parameters."

	# Output the relevant text, after minor processing.
	# Note that the output will be dependent on the flag "--world-record".
	# platform_repl is a bodge to support a specific set of ILs.
	platform_repl = platform.replace("cc", "pc")
	clean_name = f'{game_name} ({config.PLATFORM_MAP[platform_repl]["name"]} - {il_cat_name})'
	if flags["world_record"]:
		return f"The current IL world record for {clean_name} is held by {result.player} with a time of {result.time}: {result.link}"
	return f"The most recent IL run for {player} in {clean_name} is {result.time} (#{result.place}): {result.link}"


# Given a specific player, game and category, return the most
# recently verified run that the player has submitted.
#
# This code is much more efficient than parsing out every PB
# the user has submitted, particularly if you just want to look
# at one game.
@app.route('/run/<owner>/<game>/<platform>/<board>/', defaults={'args': None})
@app.route('/run/<owner>/<game>/<platform>/<board>/<path:args>')
def latest_run(owner, game, platform, board, args):
	# I can't imagine that these will be in upper-case,
	# but just make sure everything is lower-case.
	channel_owner = owner.strip().lower()
	game = game.strip().lower()
	platform = platform.strip().lower()
	board = url_parse.unquote(board.strip().lower())

	# Parse everything in the arguments, if anything is there.
	extras = split_extras(args)
	flags = extract_flags(game, extras)
	player = resolve_player(channel_owner, flags["player"])

	# Process the provided data and match it to value of "game".
	# This will set the code off to finding a run that matches
	# the search parameters.
	match game:
		case _ if game in ("cc", "custom"):
			# This is a custom content run: pass everything to
			# the processor and store the result in a variable.
			result, board_name, cat_clean_name = cust_con.process_custom_content(platform, board, flags["cc_board"], player, flags)
			clean_name = f'{games.CC_GAME_MAP[platform]["name"]} ({board_name} - {cat_clean_name})'
		case _ if game in ("ce", "catext"):
			# This is a category extension: pass everything to
			# the processor and store the result in a variable.
			result, cat_clean_name, alias_name = cat_ext.process_category_extension(platform, board, flags["ce_board"], player, flags)
			clean_name = f'{games.CE_GAME_MAP[platform]["name"]} ({alias_name} - {cat_clean_name})'
		case _ if game in ("multirun", "multi", "mr"):
			# This is a multi-run: pass everything to
			# the processor and store the result in a variable.
			result, cat_clean_name, alias_name = multirun.process_multi_run(platform, board, flags["mr_board"], player, flags)
			clean_name = f'{games.MR_GAME_MAP[platform]["name"]} ({alias_name} - {cat_clean_name})'
		case "lego":
			# This is a LEGO main-board game.
			# Due to LEGO games having more sub-categories than regular
			# main board categories, they're handled separately due to
			# extra metadata being needed.
			result, cat_clean_name, alias_name = lg.process_lego_main_board(platform, board, flags["lego_board"], player, flags)
			clean_name = f'{games.LEGO_GAME_MAP[platform]["name"]} ({alias_name} - {cat_clean_name})'
		case _:
			# This is a normal main board run which didn't meet any of
			# the specific conditions above. Pass to the processor and
			# store the result in a variable.
			result, category_name, game_name = normal.process_normal_run(game, platform, board, player, flags)
			get_platform = utils.resolve_platform_id(getattr(result, "platform", None))
			platform_name = get_platform["name"] if get_platform is not None else platform.upper()
			clean_name = f'{game_name} ({platform_name} - {category_name})'

	# Check if a run object was returned, or if it is None.
	if result is None:
		return "No run found for this criteria."

	# Return the relevant output text to the user, based on the run data.
	emulator_text = " (Emulator)" if result.emulator and result.platform != "8gej2n93" else ""
	is_current_wr = "👑 " if result.place == 1 else ""
	if flags["world_record"]:
		return f"The current world record for {clean_name}{emulator_text} is held by {result.player} with a time of {result.time}: {result.link}"
	if flags["place_num"] > 0:
		return f"{is_current_wr}{result.player} holds position {result.place} in {clean_name}{emulator_text} with a time of {result.time}: {result.link}"
	return f"{is_current_wr}The most recent verified run for {player} in {clean_name}{emulator_text} is {result.time} (#{result.place}): {result.link}"


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
	player = owner.strip().lower()
	game = game.strip().lower()
	platform = platform.strip().lower()

	# Parse everything in the arguments, if anything is there.
	# We ignore the flags["player"] key in this route because
	# this route is only for looking up one persons' data.
	extras = split_extras(args)
	flags = extract_flags(game, extras)

	# Process the game argument and return a Slug URL.
	# This will then be used to return all PBs the user has for that
	# game. The other arguments (platform, board, args etc.) are handled
	# afterward.
	sub_cat = None
	match game:
		case _ if game in ("cc", "custom"):
			game_name, slug, int_key, ordering_mode = per_best.process_game_arg(games.CC_GAME_MAP, platform)
			sub_cat = flags["cc_board"]
		case _ if game in ("ce", "catext"):
			game_name, slug, int_key, ordering_mode = per_best.process_game_arg(games.CE_GAME_MAP, platform)
			sub_cat = flags["ce_board"]
		case _ if game in ("multirun", "multi", "mr"):
			game_name, slug, int_key, ordering_mode = per_best.process_game_arg(games.MR_GAME_MAP, platform)
			sub_cat = flags["mr_board"]
			int_key = f"{platform}_{board}"
		case "lego":
			game_name, slug, int_key, ordering_mode = per_best.process_game_arg(games.LEGO_GAME_MAP, platform)
			board = url_parse.unquote(board.strip().lower())
			sub_cat = flags["lego_board"]
			int_key = f"{board}_{sub_cat}"
		case _:
			game_name, slug, int_key, ordering_mode = per_best.process_game_arg(games.NM_GAME_MAP, game, platform)
			board = url_parse.unquote(board.strip().lower())

	# Check for PBs with this Slug URL.
	game_id, game_cats = api.get_game_code(slug)
	pbs = api.search_pbs(player, game_id)
	if not pbs:
		return "No PBs can be found for this criteria."

	# Using the list of PBs, generate all the arguments needed
	# to obtain the one we asked for.
	var_filters, category_id, top_board_name, cat_clean_name = per_best.generate_args(slug, game_cats, ordering_mode, platform, int_key, board, flags, sub_cat_board=sub_cat)
	valid_pbs = per_best.filter_pbs_by_category(pbs, category_id)
	valid_pbs = per_best.filter_pbs_by_vars(valid_pbs, var_filters)
	if not valid_pbs:
		return "No PBs can be found for this criteria."

	# Almost there, just need to set up the clean_name parameter
	# based on mode.
	entry = valid_pbs[0]
	result = utils.extract_run(entry["run"], player, entry["place"])
	is_emulator = " (Emulator)" if result.emulator else ""
	is_current_wr = "👑 " if result.place == 1 else ""
	match game:
		case _ if game in ("cc", "custom"):
			clean_name = f'{games.CC_GAME_MAP[platform]["name"]} ({top_board_name} - {cat_clean_name})'
		case _ if game in ("ce", "catext"):
			clean_name = f'{games.CE_GAME_MAP[platform]["name"]} ({top_board_name} - {cat_clean_name})'
		case _ if game in ("multirun", "multi", "mr"):
			clean_name = f'{games.MR_GAME_MAP[platform]["name"]} ({top_board_name} - {cat_clean_name})'
		case "lego":
			clean_name = f'{games.LEGO_GAME_MAP[platform]["name"]} ({top_board_name} - {cat_clean_name})'
		case _:
			clean_name = f'{game_name} ({config.PLATFORM_MAP[platform]["name"]} - {cat_clean_name}){is_emulator}'

	# Return the string for the user.
	return f"{is_current_wr}The current PB for {player} in {clean_name} is {result.time}, currently placing #{result.place}: {result.link}"


# Provide help and support to users calling the routes.
@app.route("/")
def home_page_nothing():
	return (
		f"This web app is designed to support speedrunners on Twitch by enabling a single platform to look up ILs, PBs, runs or world records. "
		f"For more information, such as supported games and command use, refer to the wiki: <a href='{config.COMMAND_USAGE_DOC}'>{config.COMMAND_USAGE_DOC}</a>"
	)


# Common error handlers
@app.errorhandler(exc.UserInputException)
def user_input_handler(error):
	guidance = f" For guidance on resolving this issue, refer to the docs: {config.COMMAND_USAGE_DOC}." if not isinstance(error, exc.UnsupportedGame) else ""
	err = f"{error}{guidance}"
	return err


@app.errorhandler(exc.MissingInternalData)
def missing_int_data(error):
	return str(error)


@app.errorhandler(ValueError)
def value_error_handler(error):
	return str(error), 400


@app.errorhandler(500)
def internal_error(error):
	return f"Encountered an error in your request: {str(error)}"


@app.errorhandler(408)
def timeout_error(error):
	return f"Request timed out, try again later: {str(error)}."


if __name__ == "__main__":
	try:
		prod_mode = int(os.getenv("PRODUCTION_MODE"))
		debug_mode = False if prod_mode > 0 else True
	except ValueError:
		debug_mode = False
	app.run(debug=debug_mode)
