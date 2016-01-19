import cmd
import nmcli
from tabulate import tabulate


class Cmdline(cmd.Cmd):
    def do_prompt(self, line):
        self.prompt = "wifi: "
    
    def do_scan(self, line):
        networks = nmcli.scan()
        print tabulate(map(lambda i: i.get_list(), networks), 
                headers=["SSID", "BSSID", "MODE", "FREQ", 
                        "RATE", "SIGNAL", "SECURITY", "ACTIVE"])

    def help_scan(self):
        print "\n".join(["scan", "Scan wifi networks"])

    def do_info(self, line):
        connections = nmcli.current_connections()
        print tabulate(map(lambda i: i.to_list(), connections),
                headers=["NAME", "UUID", "DEVICES", "DEFAULT", "VPN", "MASTER-PATH"])

    def help_info(self):
        print "\n".join("info", "List all connections and their information")
        

    def do_EOF(self, line):
        return True

