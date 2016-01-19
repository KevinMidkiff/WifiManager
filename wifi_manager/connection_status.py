

class ConnectionStatus(object):
    """
    Connection Status Object
    """
    def __init__(self, status):
        self.name = status[0]
        self.uuid = status[1]
        self.device = status[2]
        self.default = status[3]
        self.vpn = status[4]
        self.master_path  = status[5]

    def to_list(self):
        return [self.name, self.uuid, self.device, self.default, 
                self.vpn, self.master_path]

