# HPSR PB Bot

A Twitch chat command for looking up speedrun PBs from speedrun.com. Currently, this only supports Harry Potter
leaderboards, but support for searching up other games may be possible.

## Usage

To look up a PB of a player:

```
!pb <game> <category> [player]
```

Note that searching PBs is a slow operation on speedrun.com, so we recommend using this command for a quicker result:

```
!run <game> <category> [player]
```

In both commands, the "player" is optional: it always defaults to an SRDC username provided by the user

## StreamElements Setup

To support PB lookups, add the following custom command:

```
!command add !pb ${customapi.https://hpsr-pb-bot.onrender.com/pb/${channel}+${queryescape ${1:|' '}}}
```

To support looking up the latest run, add the following custom command (recommended to add this as its more
efficient than parsing PBs):

```
!command add !pb ${customapi.https://hpsr-pb-bot.onrender.com/run/${channel}+${queryescape ${1:|' '}}}
```

The bot will automatically provide the channel name for you, so no need to include that.

## Games

| Code                            | Game                               |
|---------------------------------|------------------------------------|
| `hp1pc`                         | Philosopher's Stone (PC)           |
| `hp2pc`                         | Chamber of Secrets (PC)            |
| `hp3pc`                         | Prisoner of Azkaban (PC)           |
| `hp4`                           | Goblet of Fire                     |
| `hp5`                           | Order of the Phoenix               |
| `hp6`                           | Half Blood Prince                  |
| `hp7.1`                         | Deathly Hallows Part 1             |
| `hp7.2`                         | Deathly Hallows Part 2             |
| `hp1ps1`                        | Philosopher's Stone (PS1)          |
| `hp2ps1`                        | Chamber of Secrets (PS1)           |
| `hp1_6gen`                      | Philosopher's Stone (PS2/GCN/Xbox) |
| `hp2_6gen`                      | Chamber of Secrets (GCN/Xbox)      |
| `hp2ps2`                        | Chamber of Secrets PS2             |
| `hp3_6gen`                      | Prisoner of Azkaban (PS2/Xbox/GCN) |
| `hp1gbc`                        | Philosopher's Stone (GBC)          |
| `hp2gbc`                        | Chamber of Secrets (GBC)           |
| `hp1gba`                        | Philosopher's Stone (GBA)          |
| `hp2gba`                        | Chamber of Secrets (GBA)           |
| `hp3gba`                        | Prisoner of Azkaban (GBA)          |
| `dbb`                           | Disney's Brother Bear              |
| `multi` / `hpmulti` / `hp123pc` | Harry Potter Multiruns             |
| `hpce`                          | Harry Potter Category Extensions   |

## Categories

| Code                         | Category            |
|------------------------------|---------------------|
| `any`                        | Any%                |
| `100`                        | 100%                |
| `warpless`                   | Warpless            |
| `glitchless` / `gless`       | Glitchless          |
| `awc`                        | All Wizard Cards    |
| `allreq`                     | All Requirements    |
| `ng`                         | NG+                 |
| `allshields`                 | All Shields         |
| `allcrests`                  | All Crests          |
| `boostless`                  | Boostless           |
| `trifecta`                   | PC Trifecta         |
| `octofecta`                  | PC Octofecta        |
| `7duo`                       | 7PC Duofecta        |
| `ps1duo`                     | PS1 Duofecta        |
| `6gentrifecta`               | 6th Gen Trifecta    |
| `fs`                         | Full Series         |
| `gbcduo`                     | GBC Duofecta        |
| `gbapenta`                   | GBA Pentafecta      |
| `handheldocto`               | Handheld Octofecta  |
| `chungus`                    | Chungus% (CE)       |
| `awcgless` / `awcglitchless` | AWC Glitchless (CE) |

## Examples

The below examples use the !pb command, however if you want to use !run instead, just replace `!pb` with `!run`:

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
