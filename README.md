# speedrun.com Run Finder web app

This is a web app that is used by Twitch bots, such as StreamElements, to provide command-based functionality for 
users to find runs and Personal Bests (PBs) from speedrun.com. The web app parses the users' input in the bot 
command and returns the run matching the search parameters, allowing the streamer to know on-the-fly what their last 
PB submission was.

Currently, this only supports Harry Potter leaderboards: support for searching up other games will be implemented in 
the future. To see what games are supported in the web app today, refer to [Supported Games](https://github.com/SuperSajuuk/hpsr-pb-bot/wiki/LR-Games) on the wiki.

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
!command add !pb ${customapi.https://<your-render-instance-name>.onrender.com/pb/${channel}/${1|nogame}/${2|noplatform}/${pathescape ${3|noboard}}/${queryescape ${4:}}}
```

!run:
```
!command add !run ${customapi.https://<your-render-instance-name>.onrender.com/run/${channel}/${1|nogame}/${2|noplatform}/${pathescape ${3|noboard}}/${queryescape ${4:}}}
```

!il:
```
!command add !il ${customapi.https://<your-render-instance-name>.onrender.com/il/${channel}/${1|nogame}/${2|noplatform}/${3|nolevel}/${pathescape ${4|noboard}}/${queryescape ${5:}}}
```

### Fossabot
FossaBot commands can be managed from their web interface, simply create two commands with the response being the 
text that is below:

!pb:
```
$(customapi https://<your-render-instance-name>.onrender.com/pb/$(channel)/$(1 nogame)/$(2 noplatform)/$(pathencode $(3 noboard))/$(urlencode $(fromindex4)))
```

!run:
```
$(customapi https://<your-render-instance-name>.onrender.com/run/$(channel)/$(1 nogame)/$(2 noplatform)/$(pathencode $(3 noboard))/$(urlencode $(fromindex4)))
```

!il:
```
$(customapi https://<your-render-instance-name>.onrender.com/il/$(channel)/$(1 nogame)/$(2 noplatform)/$(3 nolevel)/$(pathencode $(4 noboard))/$(urlencode $(fromindex5)))
```

## Usage
Please refer to the wiki for more details on how to use the commands, alongside supported values in various contexts and more.

## Pull Requests
Due to the rapid rise of bots on GitHub which submit entirely AI generated code as pull requests, this repository 
does not accept open pull requests from users. You are welcome to suggest new features, report bugs and recommend 
ways of improving the documentation by posting a new issue in the Issue Tracker. Not all features may be included, 
but you're welcome to make a fork of this repo to introduce your own functionality if you like!