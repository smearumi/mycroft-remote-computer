# Remote Computer
A skill to control a remote computer via SSH and Wake on Lan. (Power OFF/ON)

## About
Turn OFF/ON your computer via SSH and WOL from mycroft. You must enable SSH Server on your remote computer 
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
YOu should be able to install this via `mycroft-msm install https://github.com/smearumi/mycroft-remote-computer.git` or you can install via Installer Skill from web interface (https://home.mycroft.ai/#/skill). It will take several minutes for installing requirements.

## Configuration
You can configure this skill via web interface (home.mycroft.ai). After a few minutes of having the skill installed, you should see configuration options in the https://home.mycroft.ai/#/skill location.

Fill this out with your appropriate information and hit save.

OR

If you desire total privacy, please edit your config file located at:

        ~/.mycroft/mycroft.conf

If it does not exist, create it. This file must be contain a valid json, add the following to it:

        "RemoteComputerSkill": {
            "ip_address": "YOUR IP ADDRESS",
            "mac_address": "YOUR MAC ADDRESS",
            "port": 22,
            "user": "USER NAME",
            "user_password": "USER PASSWORD",
            "sudo_password": "ROOT PASSWORD"
        }    

## Tags
#remote
#computer
#mycroft
#skill
#homeassistant
