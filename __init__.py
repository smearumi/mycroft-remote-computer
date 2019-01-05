import re
import sys
import paramiko
import ipaddress
from wakeonlan import send_magic_packet

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.skills.core import intent_handler

__author__ = "smearumi"


class RemoteComputerSkill(MycroftSkill):
    def __init__(self):
        super(RemoteComputerSkill, self).__init__(name="RemoteComputerSkill")

    @intent_handler(IntentBuilder("TurnOnIntent").require("Turn")
                    .require("Computer").require("On"))
    def handle_turn_on_intent(self, message):
        try:
            config = self.config_core.get("RemoteComputerSkill", {})

            if not config == {}:
                mac_address = str(config.get("mac_address"))
            else:
                mac_address = str(self.settings.get("mac_address"))

            re_mac = "[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$"

            if re.match(re_mac, mac_address.lower()):
                if ':' in mac_address:
                    mac_address.replace(':', '.')
                elif '-' in mac_address:
                    mac_address.replace('-', '.')

                if self.ask_yesno("ask.confirmation",
                                  {"word": "power on"}) == "no":
                    self.speak_dialog("okay")
                    return

                send_magic_packet(mac_address)

                self.speak_dialog("computer.on")
            else:
                self.speak_dialog("invalid", {"word": "mac"})
                return

        except Exception as e:
            self.speak_dialog("connection.error")
            self.log.error(e)

    @intent_handler(IntentBuilder("TurnOffIntent").require("Turn")
                    .require("Computer").require("Off"))
    def handle_turn_off_intent(self, message):
        try:
            config = self.config_core.get("RemoteComputerSkill", {})

            if not config == {}:
                ip_address = str(self.config.get("ip_address"))
                port = int(self.config.get("port"))
                user = str(self.config.get("user"))
                user_password = str(self.config.get("user_password"))
                sudo_password = str(self.config.get("sudo_password"))
            else:
                ip_address = str(self.settings.get("ip_address"))
                port = int(self.settings.get("port"))
                user = str(self.settings.get("user"))
                user_password = str(self.settings.get("user_password"))
                sudo_password = str(self.settings.get("sudo_password"))

            try:
                ip = ipaddress.ip_address(ip_address)

            except ValueError:
                self.speak_dialog("invalid", {"word": "I.P"})
                return

            if self.ask_yesno("ask.confirmation",
                              {"word": "shut down"}) == "no":
                self.speak_dialog("okay")
                return

            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(
                        hostname=str(ip),
                        port=port,
                        username=user,
                        password=user_password)

            transport = client.get_transport()

            session = transport.open_session()
            session.set_combine_stderr(True)
            session.get_pty()

            if sys.platform.startswith('win'):
                session.exec_command("shutdown /s")
            else:
                session.exec_command("sudo -k shutdown -h now")

            stdin = session.makefile('wb', -1)
            stdout = session.makefile('rb', -1)
            stdin.write(sudo_password + '\n')
            stdin.flush()
            stdout.read()

            client.close()

            self.speak_dialog("computer.off")

        except Exception as e:
            self.speak_dialog("connection.error")
            self.log.error(e)

    def stop(self):
        pass


def create_skill():
    return RemoteComputerSkill()
