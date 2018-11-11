# Remote Computer
A skill to control a remote computer via SSH and Wake on Lan. (Power OFF/ON)

## About
Turn ON/OFF your computer via SSH and WOL from mycroft. You must enable SSH Server on your remote computer 
for Power OFF and also you have to enable Wake on Lan for Power ON.

For Power OFF (Supported Remote Computer OS with SSH Server):
* Linux (Tested)
* Mac (Tested)
* Windows (Tested)

For Power ON (Wake on LAN):
* Not Tested.

## Examples 
* "computer off"
* "turn off my computer"
* "turn off the computer"
* "computer on"
* "turn on the computer"
* "turn the computer on"

## Installation
Should be able to install this via `msm install https://github.com/smearumi/mycroft-remote-computer.git` or you can install via Installer Skill from web interface (https://home.mycroft.ai/#/skill). It will take several minutes for installing requirements.

## Configuration
This skill utilizes the skillsettings.json file which allows you to configure this skill via web interface (home.mycroft.ai). After a few minutes of having the skill installed, you should see configuration options in the https://home.mycroft.ai/#/skill location.

Fill this out with your appropriate information and hit save.

## Tags
#remote
#computer
#homeassistant
