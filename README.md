# speedrun.com Run Finder web app

This is a web app that is used by Twitch bots, such as StreamElements, to provide command-based functionality for 
users to find runs and Personal Bests (PBs) from speedrun.com. The web app parses the users' input in the bot 
command and returns the run matching the search parameters, allowing the streamer to know on-the-fly what their last 
PB submission was.

Currently, this only supports Harry Potter leaderboards: support for searching up other games will be implemented in 
the future. To see what games are supported in the web app today, refer to [Supported Games](https://github.com/SuperSajuuk/hpsr-pb-bot/wiki/LR-Games) on the wiki.

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
supported are listed in the platforms section of the wiki.

When doing this for a CE, you should use the full name: eg `hp1pc`.

#### Category
The category parameter is used as a filter to target the specific primary category of the game and platform that is 
defined. All categories supported here are listed in the categories section of the wiki.

When doing this for a CE board, the alias name for the sub-category should be used: eg `100gless`.

At some point, PB will be brought into alignment with the logic for the /run/ endpoint, so that sub-categories can 
be part of the "flags" optional argument. For now, "flags" in PB is only for setting console/emulator or a player 
override.

## Setup
> [!IMPORTANT]
> The text `<your-render-instance-name>` in the command definitions below should be replaced with the name of your 
> deployed instance of this code. A private production instance is available for selected individuals: anyone using 
> that production instance will know the relevant render instance name to use.

This command functionality is supported in both StreamElements and FossaBot. The commands to add are separated as 
each both handles customapi support in different ways.

The bot will automatically provide the channel name for you, so no need to include that. However, `${channel}` is 
based on the assumption that the Twitch channels' owner is the same as their username on speedrun.com: if it is not, 
replace `${channel}` with the appropriate SRDC username.

### StreamElements
!pb:
```
!command add !pb ${customapi.https://<your-render-instance-name>.onrender.com/pb/${channel}/${1|nogame}/${2|noplatform}/${3|noboard}/${queryescape ${4:|' '}}}
```

!run:
```
!command add !run ${customapi.https://<your-render-instance-name>.onrender.com/run/${channel}/${1|nogame}/${2|noplatform}/${3|noboard}/${queryescape ${4:|' '}}}
```

### Fossabot
FossaBot commands can be managed from their web interface, simply create two commands with the response being the 
text that is below:

!pb:
```
${customapi https://<your-render-instance-name>.onrender.com/pb/${channel}/${1 nogame}/${2 noplatform}/${3 noboard}/${urlencode ${fromindex4}}}
```

!run:
```
${customapi https://<your-render-instance-name>.onrender.com/run/${channel}/${1 nogame}/${2 noplatform}/${3 noboard}/${urlencode ${fromindex4}}}
```

## Usage
Please refer to the wiki for more details on how to use the commands, alongside supported values in various contexts and more.

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
