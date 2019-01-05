# <img src='https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/desktop.svg' card_color='#000000' width='50' height='50' style='vertical-align:bottom'/> Remote Computer
Control a remote computer via SSH and Wake on Lan. (Power OFF/ON)

## About 
Turn OFF/ON your computer via SSH and WOL from mycroft. You must enable SSH Server on your remote computer for Power OFF and also you have to enable Wake on Lan for Power ON.

For Power OFF (Supported Remote Computer OS with SSH Server):
* Linux (Tested)
* Mac (Tested)
* Windows (Tested)

For Power ON (Wake on LAN):
* Not Tested.

## Installation
You should be able to install skill via `mycroft-msm install https://github.com/smearumi/mycroft-remote-computer.git` or you can install this skill via Installer Skill from web interface (https://home.mycroft.ai/#/skill). It will take several minutes for installing requirements.

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

## Examples 
* "turn off my computer"
* "turn my computer off"
* "shut down the computer"
* "turn on the computer"
* "wake up my computer"

## Credits 
S. M. Estiaque Ahmed (@smearumi)



## Category
**IoT**

## Tags
#mycroft
#skill
#remote
#computer
#homeassistant
