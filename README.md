# speedrun.com Run Finder web app

This is a web app that is used by Twitch bots, such as StreamElements, to provide command-based functionality for 
users to find runs and Personal Bests (PBs) from speedrun.com. The web app parses the users' input in the bot 
command and returns the run matching the search parameters, allowing the streamer to know on-the-fly what their last 
PB submission was.

Currently, this only supports Harry Potter leaderboards: support for searching up other games will be implemented in 
the future, please refer to the [games section below](#Games) for the list of supported games.

An upcoming update will improve the functionality of these commands, such as:
* Game names will lose the inclusion of platforms, simplifying it to just "hp1".
* Platforms will become a required parameter where you set the platform (eg "pc", "ps1", "ps2", "xbox").
* Full Series will be handled behind the scenes transparently, without requiring new commands just to handle it (you 
  would tell the bot that you are looking for full series by just setting platform to "fs" and the rest is taken 
  care of for you).

I don't have a timeline for inclusion of this functionality, but keep an eye on the repository for more information!

## Usage
### Personal Bests
> [!WARNING]
> Searching a users' Personal Bests is a **slow operation**. Unlike looking up a specific run and getting a small 
> response output that is easily processable, the PB endpoint returns ALL personal bests, which can potentially 
> result in having thousands of runs, which have to be filtered. If you just want a specific run, we recommend using 
> the /run/ endpoint, which has much more specific filtering to only return a small number of results.
> 
To look up a PB of a player:
```
!pb <game> <platform> <category> [flags]
```
#### Game
The game parameter is used to define what game you are looking for. For the most part, this should follow the format 
of the values defined in the games header below, but you can also use the legacy format of defining category 
extensions by their full URL slugs.

#### Platform
The platform parameter is used as a filter to target the specific game version that is needed. All platforms 
supported are listed in the [platforms section](#Platforms) below.

When doing this for a CE, you should use the full name: eg `hp1pc`.

#### Category
The category parameter is used as a filter to target the specific primary category of the game and platform that is 
defined. All categories supported here are listed in the [categories section](#Categories) below.

When doing this for a CE board, the alias name for the sub-category should be used: eg `100gless`.

At some point, PB will be brought into alignment with the logic for the /run/ endpoint, so that sub-categories can 
be part of the "flags" optional argument. For now, "flags" in PB is only for setting console/emulator or a player 
override.

### Individual Runs
To look up the individual run of a player:
```
!run <game> <platform> <category> [flags]
```

#### Game
The game parameter is used to define what game you are looking for. This should follow the format of the values 
defined in the games header below (only these values are accepted, anything else will return an error).

If you are trying to look up a run in special boards (eg category extensions, multiruns or ILs), you define the 
relevant board here (eg `!run ce` tells the system that you are looking for a category extension run): the specific 
game series, primary board and the extension board are defined after this. See the examples at the end for how this 
works.

#### Platform
The platform parameter is used as a filter to target the specific game version that is needed. All platforms 
supported are listed in the [platforms section](#Platforms) below.

If the game parameter was set to CE, then platform should be the specific series you are looking for, rather than a 
platform. This is because there is usually only one Category Extensions board per game series, so the specific 
platforms are often defined by the top-level board category instead.

#### Category
The category parameter is used as a filter to target the specific primary category of the game and platform that is 
defined. All categories supported here are listed in the [categories section](#Categories) below.

If the game parameter was set to CE, then category should be set to the top-level category value (eg 1PC on the 
Harry Potter Category Extensions board), and NOT the actual sub-category that you are seeking. The specific 
sub-category/board should be defined in the flags section below.

#### Flags
The flags at the end of the command represent optional arguments that can be provided where additional information is 
needed. Flags which are supported at the moment include:
- The sub-board that was requested (this is largely only relevant for Category Extensions due to overflow)
- Whether a console or emulator run should be looked for.
- A different players' name (this is for situations where you want to compare the channel owners' run to someone else's)

Anything after the 3rd argument is grouped up with the flags and then processed for these kind of values. Invalid 
arguments will be ignored, and order of the arguments doesn't matter (eg `emulator nixxo` and `nixxo emulator` are 
handled in the same way).

Additional flags may be supported in the future, depending on relevant use cases.

## Setup

To support PB lookups, add the following custom command:

```
!command add !pb ${customapi.https://srdc-run-finder.onrender.com/pb/${channel}+${queryescape ${1:|' '}}}
```

To support looking up the latest run, add the following custom command (recommended to add this as its more
efficient than parsing PBs):

```
!command add !run ${customapi.https://srdc-run-finder.onrender.com/run/${channel}/${1|nogameprovided}/$
{2|noplatformprovided}/${3|noboardprovided}/${queryescape ${4:|' '}}}
```

The bot will automatically provide the channel name for you, so no need to include that. However, `${channel}` is 
based on the assumption that the Twitch channels' owner is the same as their username on speedrun.com: if it is not, 
replace `${channel}` with the appropriate SRDC username.

## Games

| Code    | Game                                        |
|---------|---------------------------------------------|
| `hp1`   | Harry Potter and the Philosopher's Stone    |
| `hp2`   | Harry Potter and the Chamber of Secrets     |
| `hp3`   | Harry Potter and the Prisoner of Azkaban    |
| `hp4`   | Harry Potter and the Goblet of Fire         |
| `hp5`   | Harry Potter and the Order of the Phoenix   |
| `hp6`   | Harry Potter and the Half Blood Prince      |
| `hp7.1` | Harry Potter and the Deathly Hallows Part 1 |
| `hp7.2` | Harry Potter and the Deathly Hallows Part 2 |
| `dbb`   | Disney's Brother Bear                       |
| `ce`    | Category Extensions                         |
| `multi` | Multiruns                                   |

## Platforms

| Code   | Platform             |
|--------|----------------------|
| `ps1`  | PlayStation 1        |
| `ps2`  | PlayStation 2        |
| `ps3`  | PlayStation 3        |
| `psp`  | PlayStation Portable |
| `gba`  | Game Boy Advance     |
| `gbc`  | Game Boy Colour      |
| `gcn`  | Nintendo GameCube    |
| `xbox` | Microsoft XBOX 360   |
| `pc`   | PC                   |

## Categories

| Code                         | Category                        |
|------------------------------|---------------------------------|
| `any`                        | Any%                            |
| `100`                        | 100%                            |
| `warpless`                   | Warpless                        |
| `glitchless` / `gless`       | Glitchless                      |
| `awc`                        | All Wizard Cards                |
| `allreq`                     | All Requirements                |
| `ng`                         | NG+                             |
| `allshields`                 | All Shields                     |
| `allcrests`                  | All Crests                      |
| `boostless`                  | Boostless                       |
| `trifecta`                   | PC Trifecta                     |
| `octofecta`                  | PC Octofecta                    |
| `7duo`                       | 7PC Duofecta                    |
| `ps1duo`                     | PS1 Duofecta                    |
| `6gentrifecta`               | 6th Gen Trifecta                |
| `fs`                         | Full Series                     |
| `gbcduo`                     | GBC Duofecta                    |
| `gbapenta`                   | GBA Pentafecta                  |
| `handheldocto`               | Handheld Octofecta              |
| `chungus`                    | Chungus% (CE)                   |
| `awcgless` / `awcglitchless` | AWC Glitchless (CE)             |
| `pctri`                      | Harry Potter PC Trifecta        |
| `7pcduo`                     | Harry Potter 7PC Duofecta       |
| `pcocto`                     | Harry Potter PC Octofecta       |
| `ps1duo`                     | Harry Potter PS1 Duofecta       |
| `6gentri`                    | Harry Potter 6th Gen Trifecta   |
| `gbcduo`                     | Harry Potter GBC Duofecta       |
| `gbapenta`                   | Harry Potter GBA Pentafecta     |
| `hhocto`                     | Harry Potter Handheld Octofecta |
| `fs`                         | Harry Potter Full Series        |

## Examples
### !pb
Below are some examples of commands to return PBs. Outputs are largely consistent:
- `!pb hp1 pc any nixxo` -> Looks for the PB in HP1 PC Any% for player "nixxo".
- `!pb hp1 ps1 100 nixxo` -> Looks for the PB in HP1 PS1 100% for player "nixxo".
- `!pb hp1 ps1 100` -> Looks for the PB in HP1 PS1 100% for the channel owner.
- `!pb hpce hp1pc 100gless nixxo` -> Looks for the PB in the HP Category Extensions board for HP1 PC 100% Glitchless 
  for player "nixxo".

The output for PBs will look something like this:
```
The current PB for {player} in {clean_name} is {result.time}, currently placing #{result.place}: {result.link}
```
All variables are filled in from the data provided and parsed by the bot.

### !run
Below are some examples of commands to return individual runs. Outputs are largely consistent:
- `!run hp1 pc any nixxo` -> Looks for the most recent run in HP1 PC Any% for player "nixxo".
- `!run hp1 ps1 100 nixxo` -> Looks for the most recent run in HP1 PS1 100% for player "nixxo".
- `!run hp1 ps1 100` -> Looks for the most recent run in HP1 PS1 100% for the channel owner.
- `!run ce hp 1pc 100gless nixxo` -> Looks for the most recent run in the HP Category Extensions board for HP1 PC 100% 
  Glitchless for player "nixxo".

The output for individual runs will look something like this:
```
The most recent verified run for {player} in {clean_name}{emulator_text} is {time} (#{place}): {link}
```
All variables are filled in from the data provided and parsed by the bot.