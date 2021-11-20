from Utils.Writer import Writer


class KeepAliveOk(Writer):

    def __init__(self, device):
        self.id = 20108
        self.device = device
        super().__init__(self.device)
        
    def decode(self):
        pass

    def encode(self):
        print('[DUDKA] KeepAliveOk sent')