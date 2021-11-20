# -*- coding: utf-8 -*-
from Utils.Reader import ByteStream


class EndClientTurn(ByteStream):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        sam = []
        for x in range(20):
            sam.append(self.readHexa())

    def process(self):
        pass