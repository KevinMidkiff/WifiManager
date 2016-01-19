"""
nmcli wrapper
"""
import re
import subprocess as sub
from network import Network
from connection_status import ConnectionStatus


_SCAN_REGEX = re.compile(
    "(?:')(.+)(?:')(?:\s+)([0-9A-Fa-f:]+)(?:\s+)([a-zA-Z]+)"+
    "(?:\s+)([0-9]+)(?:\s+MHz\s+)([0-9]+)(?:\s+MB/s\s+)([0-9]+)" +
    "(?:\s+)(.+)(yes|no)")


def scan():
    p = sub.Popen(
        ["nmcli", "d", "wifi", "list"],
        stdout=sub.PIPE,
        stderr=sub.PIPE)
    output, err = p.communicate()
    
    assert p.returncode == 0, "RETURN " + p.returncode
    
    result = _SCAN_REGEX.findall(output)
    networks = {}

    for i in result:
        network = Network(i)
        networks[network.bssid] = network

    return networks.values()


def connect():
    pass


def disconnect():
    pass


def current_connections():
    p = sub.Popen(
            ["nmcli", "-t", "-f", "NAME,UUID,DEVICES,DEFAULT,VPN,MASTER-PATH", 
                "connection", "status"],
            stdout=sub.PIPE,
            stderr=sub.PIPE)
    output, err = p.communicate()

    assert p.returncode == 0, "RETURN " + str(p.returncode)

    result = output.split("\n")
    connections = []

    for i in result:
        if i != "":
            connections.append(ConnectionStatus(i.split(":")))

    return connections

