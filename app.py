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
import srcomapi.datatypes as dt
import datetime
import re
import data

# Instantiate the Flask and SRDC classes for use the code.
app = flask.Flask(__name__)
srdc = data.SRDCRuns(config.GAME_MAP, config.CATEGORY_MAP)


# Resolve the player, in case we just want to check for the channel owner.
# channel_owner is always provided, but player may not be:
def resolve_player(channel_owner: str, player: str | None) -> str:
	return channel_owner if player is None or player.strip() == "" else player


# Given a specific player, game and category, return the most
# recently verified run that the player has submitted.
# This code is much more efficient than parsing out every PB
# the user has submitted, particularly if you just want to look
# at one game.
@app.route('/run/<owner>/<path:args>')
def latest_run(owner, args):
	# Parse the arguments to get the required details.
	# Player is always owner unless we overwrite it in the args.
	parts = [p.lower() for p in args.split("+")]
	ce_mode = False
	ce_type = None
	ce_category = None
	platform = None
	game = None
	cat = None
	player = owner

	# Parse arguments from the parts variables.
	# For cleanliness, we will use match so that you can actually
	# read the control flow.
	for p in parts:
		match p:
			case "ce":  # If the first argument is "ce", we are looking for a category extension.
				ce_mode = True
			case _ if ce_mode and p in config.CE_TYPE_MAP:  # check if the argument is in CE_TYPE_MAP
				ce_type = config.CE_TYPE_MAP[p]
			case _ if ce_mode and p in config.CE_CATEGORY_MAP:  # check if the argument is in CE_CATEGORY_MAP
				ce_category = config.CE_CATEGORY_MAP[p]
			case _ if p in config.CATEGORY_MAP:  # Check if the argument is in CATEGORY_MAP
				cat = p
			case _ if p in config.PLATFORM_MAP:  # check if the argument is in PLATFORM_MAP
				platform = p
			case _ if p in config.GAME_MAP:  # check if the argument is in GAME_MAP
				game = p
			case _:  # The argument wasn't in any of the keys, so it's a player name override.
				player = p

	# Resolve the player, then check for whether we wanted a Category Extension.
	print(f"Platform: {platform}")
	print(f"Game: {game}")
	print(f"Category: {cat}")
	player = resolve_player(owner, player)
	if ce_mode:
		# Validate CE arguments
		match ce_type:
			case None:
				return "Error: CE run requires a CE type", 400
			case "standard" | "insane" if not platform:
				return "Error: this CE type requires a platform", 400

		# Return errors if ce_category or game are None
		if ce_category is None:
			return "Error: CE run requires a CE category", 400
		if game is None:
			return "Error: CE run requires a game", 400

		# Try looking for a category extension run.
		# If none is found, return an error.
		try:
			result = srdc.lookup_ce_run(game, platform, ce_type, ce_category, player)
		except ValueError:
			return "No CE run found for this criteria."

		# result may have returned None, instead of ValueError, check for that
		if not result:
			return "No CE run found for this criteria."

		clean_name = f"{ce_type}:{ce_category}"
		is_emulator = " (Emulator) " if getattr(result, "emulator", False) else " "
		return f"{player.capitalize()} most recent verified CE run in {clean_name}{is_emulator}is {result.time} (#{result.place}): {result.link}"

	# Now check if we are in multi-run mode (thus looking at hpmulti).
	is_multirun = cat in config.CATEGORY_MAP and config.CATEGORY_MAP[cat].get("multirun", False)
	if is_multirun:
		# Try looking up a multi-run entry.
		try:
			result = srdc.lookup_multirun(cat, player)
		except ValueError:
			return "No run found for this criteria."
	else:
		# Just a regular run, try finding it.
		match (game, platform, cat):
			case (None, _, _) | (_, None, _) | (_, _, None):
				return "Error: this route requires platform+game+category", 400

		internal_key = f"{game}_{platform}"
		if internal_key not in config.BOARD_GAME_SLUG:
			return "Invalid platform/game combination", 400

		try:
			result = srdc.lookup_run(internal_key, cat, player)
		except ValueError:
			return "No run found for this criteria."

	# If result is returned as False, that means there was no run to be found
	if not result:
		return "No run found for this criteria."

	# Output the data provided.
	clean_name = config.CATEGORY_MAP[cat]["clean"]
	is_emulator = " (Emulator) " if getattr(result, "emulator", False) else " "
	return f"{player.capitalize()} most recent verified run in {clean_name}{is_emulator}is {result.time} (#{result.place}): {result.link}"


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
	app.run()
