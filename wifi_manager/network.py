"""
Network Object
"""


class Network(object):
    """
    Network Object
    """
    def __init__(self, info):
        self.ssid = info[0]
        self.bssid = info[1]
        self.mode = info[2]
        self.freq = info[3]
        self.rate = info[4]
        self.signal = info[5]
        self.security = info[6]
        self.active = info[7]
        
        # Cleaning up security
        self.security = self.security.strip()

        if self.security == "--":
            self.security = None

    def __str__(self):
        return str(self.get_list())

    def get_list(self):
        return [self.ssid, self.bssid, self.mode, self.freq,
               self.rate, self.signal, self.security, self.active]

