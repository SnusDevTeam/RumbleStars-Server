# -*- coding: utf-8 -*-

import string
import random

def generateToken():
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(40))


class Player:

    Loaded = 0

    HighID = 0
    LowID = 0
    Token = None
    #PToken = generateToken()
    Name = f"GeneBrawl"
    NameSet = 0
    roomID = 0
    TutorialStep = 0
    selectedBrawler = 0
    practice = 0
    gems = 100
    chips = 0
    gold = 100
    isReady = False

    def __init__(self, device):
        self.device = device

    def encode(self):
        return None
