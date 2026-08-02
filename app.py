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
srdc = data.SRDCRuns(config.PER_GAME_MAP, config.CATEGORY_MAPPING)


# Our two routes to get latest run or a PB might return
# dictionaries when the run is a multi-run. If that happens,
# process it here and return the joined up pieces.
def format_multirun_output(result: dict[str, any]) -> str:
	"""
	Convert a multirun dict {'any': SpeedRun, '100': SpeedRun}
	into a formatted string like:
	'Any%: 3:44:12 (#5) link | 100%: 5:12:33 (#2) link'
	"""
	parts = []
	if "any" in result:
		r = result["any"]
		parts.append(f"Any%: {r.time} (#{r.place}) {r.link}")
	if "100" in result:
		r = result["100"]
		parts.append(f"100%: {r.time} (#{r.place}) {r.link}")
	return " | ".join(parts)


# Resolve the player, in case we just want to check for the channel owner.
# channel_owner is always provided, but player may not be:
def resolve_player(channel_owner: str, player: str | None) -> str:
	if player is None or player.strip() == "":
		return channel_owner
	return player


# Given a specific player, game and category, return the most
# recently verified run that the player has submitted.
# This code is much more efficient than parsing out every PB
# the user has submitted, particularly if you just want to look
# at one game.
@app.route('/run/<path:args>')
def latest_run(args):
	# Parse the arguments and check we have 3.
	parts = args.split("+")
	if len(parts) < 3:
		return "Error: this route requires owner+game+cat to be provided", 400

	# Set the variables on argument order
	owner = parts[0]
	game = parts[1]
	cat = parts[2]
	platform = None
	player = None
	for p in parts[3:]:
		if p.lower() in ["console", "emulator"]:
			platform = p.lower()
		else:
			player = p

	# Validate game/category exist in the mapping.
	# At some point, the game check should be removed, so
	# that this can be used to find a PB for any game by the
	# user. Category filter would be ideal though.
	player = resolve_player(owner, player)
	game = game.lower()
	cat = cat.lower()
	if game not in config.PER_GAME_MAP.keys():
		return f"Invalid game. See supported options: {config.COMMAND_USAGE_DOC}"
	if cat not in config.CATEGORY_MAPPING.keys():
		return f"Invalid category. See supported options: {config.COMMAND_USAGE_DOC}"

	# Query SRDC to find the latest run submitted by the player for this game/category.
	try:
		result = srdc.lookup_run(game, cat, player, platform)
	except ValueError:
		return "No run found for this criteria."

	# Was there any results returned? If none, then it's because the
	# player did not submit any verified run to the board.
	if not result:
		return "No run found for this criteria."

	# If this returned a dictionary, it's a multi-run and needs
	# to be processed differently.
	if isinstance(result, dict):
		joined = format_multirun_output(result)
		return f"{player.capitalize()} most recent verified runs in {game.upper()} {config.CATEGORY_MAPPING[cat]['clean']}: {joined}"

	# Just a regular run, so print the standard text supporting the latest run.
	is_emulator = " (Emulator) " if result.emulator else " "
	return f"{player.capitalize()} most recent verified run in {game.upper()} {config.CATEGORY_MAPPING[cat]['clean']}{is_emulator}is {result.time} (#{result.place}): {result.link}"


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
	if game not in config.PER_GAME_MAP.keys():
		return f"Invalid game. See supported options: {config.COMMAND_USAGE_DOC}"
	if cat not in config.CATEGORY_MAPPING.keys():
		return f"Invalid category. See supported options: {config.COMMAND_USAGE_DOC}"

	# Query SRDC to find the most recent PB of the player for this game/category.
	try:
		result = srdc.lookup_pb(game, cat, player, platform)
	except ValueError:
		return "No PB found for this criteria."

	# Was there any results?
	if not result:
		return "No PB found for this criteria."

	# This may be a multi-run PB, or a single PB. Check for a multi-run.
	if isinstance(result, dict):
		joined = format_multirun_output(result)
		return f"{player.capitalize()} PBs for {game.upper()} {category_map[cat]['clean']}: {joined}"

	# Print the standard string to represent this PB.
	pb = result[0]
	is_emulator = " (Emulator)" if pb.emulator else ""
	return f"{player.capitalize()} has a PB of {pb.time} (#{pb.place}) in {game.upper()} {config.CATEGORY_MAPPING[cat]['clean']}{is_emulator}: {pb.link}"


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
