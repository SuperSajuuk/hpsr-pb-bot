# HPSR PB Bot

A Twitch chat command for looking up Harry Potter speedrun PBs from speedrun.com.

## Usage

```
!pb <game> <category> [player]
```

Player is optional — defaults to the channel owner's SRDC username.

## StreamElements Setup

Add a custom command:

```
!command add !pb ${customapi.https://hpsr-pb-bot.onrender.com/custom/yoursrdcusername+${queryescape ${1:|' '}}}
```

Replace `yoursrdcusername` with your speedrun.com username.

## Games

| Code | Game |
|------|------|
| `hp1` / `hp1pc` | Philosopher's Stone (PC) |
| `hp2` / `hp2pc` | Chamber of Secrets (PC) |
| `hp3` / `hp3pc` | Prisoner of Azkaban (PC) |
| `hp4` | Goblet of Fire |
| `hp5` | Order of the Phoenix |
| `hp6` | Half Blood Prince |
| `hp7.1` | Deathly Hallows Part 1 |
| `hp7.2` | Deathly Hallows Part 2 |
| `hp1ps1` | Philosopher's Stone (PS1) |
| `hp2ps1` | Chamber of Secrets (PS1) |
| `hp16gen` | Philosopher's Stone (PS2/GCN/Xbox) |
| `hp36gen` | Prisoner of Azkaban (PS2/Xbox/GCN) |
| `hp1gbc` | Philosopher's Stone (GBC) |
| `hp2gbc` | Chamber of Secrets (GBC) |
| `hp1gba` | Philosopher's Stone (GBA) |
| `hp2gba` | Chamber of Secrets (GBA) |
| `hp3gba` | Prisoner of Azkaban (GBA) |
| `dbb` | Disney's Brother Bear |
| `multi` / `hpmulti` / `hp123pc` | Harry Potter Multiruns |
| `hpce` | Harry Potter Category Extensions |

## Categories

| Code | Category |
|------|----------|
| `any` | Any% |
| `100` | 100% |
| `warpless` | Warpless |
| `glitchless` / `gless` | Glitchless |
| `awc` | All Wizard Cards |
| `allreq` | All Requirements |
| `ng` | NG+ |
| `allshields` | All Shields |
| `allcrests` | All Crests |
| `boostless` | Boostless |
| `trifecta` | PC Trifecta |
| `octofecta` | PC Octofecta |
| `7duo` | 7PC Duofecta |
| `ps1duo` | PS1 Duofecta |
| `6gentrifecta` | 6th Gen Trifecta |
| `fs` | Full Series |
| `gbcduo` | GBC Duofecta |
| `gbapenta` | GBA Pentafecta |
| `handheldocto` | Handheld Octofecta |
| `chungus` | Chungus% (CE) |
| `awcgless` / `awcglitchless` | AWC Glitchless (CE) |

## Examples

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
