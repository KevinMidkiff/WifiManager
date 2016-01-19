"""
WiFi Manager
"""
import argparse
from tabulate import tabulate
import nmcli
import cmdline


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "command", choices=["scan", "connect", "disconnect"], 
            help="Command")
    return parser.parse_args()


def main():
    #args = parse_args()
    # networks = nmcli.scan()

    # print tabulate(map(lambda i: i.get_list(), networks), 
    #         headers=["SSID", "BSSID", "MODE", "FREQ", 
    #                  "RATE", "SIGNAL", "SECURITY", "ACTIVE"])
    cmdline.Cmdline().cmdloop()
    # nmcli.current_connection()


if __name__ == "__main__":
    main()


