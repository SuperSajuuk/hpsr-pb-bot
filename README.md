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
!pb <game> <category> [platform] [player]
```

Note that searching PBs is a slow operation on speedrun.com, because a user can have many hundreds of PBs that have 
to be returned and then filtered. If you just want to check up a specific run of a user, we recommend using this 
command for a quicker result (the output should be the same between both commands):
```
!run <game> <category> [platform] [player]
```

In both commands, the "player" is optional: it always defaults to the channel owners' name.

"platform" is also optional: this is used where an additional platform filter exists, eg console/emulator splits. In 
some cases, such as HP2 PS2, it may be ideal to provide this parameter to get the right output.

## StreamElements Setup

To support PB lookups, add the following custom command:

```
!command add !pb ${customapi.https://srdc-run-finder.onrender.com/pb/${channel}+${queryescape ${1:|' '}}}
```

To support looking up the latest run, add the following custom command (recommended to add this as its more
efficient than parsing PBs):

```
!command add !run ${customapi.https://srdc-run-finder.onrender.com/run/${channel}+${queryescape ${1:|' '}}}
```

The bot will automatically provide the channel name for you, so no need to include that. However, `${channel}` is 
based on the assumption that the Twitch channels' owner is the same as their username on speedrun.com: if it is not, 
replace `${channel}` with the appropriate SRDC username.

## Games

| Code       | Game                               |
|------------|------------------------------------|
| `hp1pc`    | Philosopher's Stone (PC)           |
| `hp2pc`    | Chamber of Secrets (PC)            |
| `hp3pc`    | Prisoner of Azkaban (PC)           |
| `hp4`      | Goblet of Fire                     |
| `hp5`      | Order of the Phoenix               |
| `hp6`      | Half Blood Prince                  |
| `hp7.1`    | Deathly Hallows Part 1             |
| `hp7.2`    | Deathly Hallows Part 2             |
| `hp1ps1`   | Philosopher's Stone (PS1)          |
| `hp2ps1`   | Chamber of Secrets (PS1)           |
| `hp1_6gen` | Philosopher's Stone (PS2/GCN/Xbox) |
| `hp2_6gen` | Chamber of Secrets (GCN/Xbox)      |
| `hp2ps2`   | Chamber of Secrets PS2             |
| `hp3_6gen` | Prisoner of Azkaban (PS2/Xbox/GCN) |
| `hp1gbc`   | Philosopher's Stone (GBC)          |
| `hp2gbc`   | Chamber of Secrets (GBC)           |
| `hp1gba`   | Philosopher's Stone (GBA)          |
| `hp2gba`   | Chamber of Secrets (GBA)           |
| `hp3gba`   | Prisoner of Azkaban (GBA)          |
| `dbb`      | Disney's Brother Bear              |
| `hpce`     | Harry Potter Category Extensions   |
| `multi`    | Harry Potter Multiruns             |

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
