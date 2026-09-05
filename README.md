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

To look up a PB of a player:
```
!pb <game> <platform> <category> [flags]
```

Note that searching PBs is a slow operation on speedrun.com, because a user can have many hundreds of PBs that have 
to be returned and then filtered to find the one that you actually asked for. If you just want to check up a specific 
run of a user, we recommend using this command for a quicker result (the output should be the same between both 
commands):
```
!run <game> <platform> <category> [flags]
```

### Game
The game parameter is used to define what game you are looking for. This should follow the format of the values 
defined in the games header below (only these values are accepted, anything else will return an error).

If you are trying to look up a run in special boards (eg category extensions, multiruns or ILs), you define the 
relevant board here (eg `!run ce` tells the system that you are looking for a category extension run): the specific 
game series, primary board and the extension board are defined after this. See the examples at the end for how this 
works.

### Platform
The platform parameter is used as a filter to target the specific game version that is needed. All platforms 
supported are listed in the [platforms section](#Platforms) below.

If the game parameter was set to CE, then platform should be the specific series you are looking for, rather than a 
platform. This is because there is usually only one Category Extensions board per game series, so the specific 
platforms are often defined by the top-level board category instead.

### Category
The category parameter is used as a filter to target the specific primary category of the game and platform that is 
defined. All categories supported here are listed in the [categories section](#Categories) below.

If the game parameter was set to CE, then category should be set to the top-level category value (eg 1PC on the 
Harry Potter Category Extensions board), and NOT the actual sub-category that you are seeking. The specific 
sub-category/board should be defined in the flags section below.

### Flags
The flags at the end of the command represent optional arguments that can be provided where additional information is 
needed. Flags which are supported at the moment include:
- The sub-board that was requested (this is largely only relevant for Category Extensions due to overflow)
- Whether a console or emulator run should be looked for.
- A different players' name (this is for situations where you want to compare the channel owners' run to someone else's)

Anything after the 3rd argument is grouped up with the flags and then processed for these kind of values. Invalid 
arguments will be ignored, and order of the arguments doesn't matter (eg `emulator nixxo` and `nixxo emulator` are 
handled in the same way).

Additional flags may be supported in the future, depending on relevant use cases.

## StreamElements Setup

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

The below examples use the !pb command, however if you want to use !run instead, just replace `!pb` with `!run`. In 
most cases, !pb and !run will return the same output, but you may want to use `!run` for regular check-ups to avoid 
the slower PB route.

```
!pb hp1 any nixxo
→ Nixxo has a PB of 0:29:45 (#1) in HP1 Any% https://...

!pb hp2 100
→ (defaults to channel owner's PB)

!pb hp4 any artfulinfo
→ Artfulinfo has a PB of 1:02:33 (#10) in HP4 Any% https://...

!pb multi trifecta artfulinfo
→ Artfulinfo has Trifecta PBs of: 2:15:00 (#3) in Any% https://... | 5:30:00 (#2) in 100% https://...

!pb hpce chungus artfulinfo
→ Artfulinfo has a PB of 0:45:12 (#1) in HPCE Chungus% https://...
```

## Response Format

```
<player> has a PB of <time> (#<place>) in <game> <category> <link>
```
