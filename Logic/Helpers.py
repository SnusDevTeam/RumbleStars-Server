def getBrawlerRarity(card):
    if card == 0:
        return 0
    if card == 4:
        return 0
    if card == 8:
        return 1
    if card == 12:
        return 0
    if card == 16: # trickshot
        return 1
    if card == 20:
        return 3
    if card == 24:
        return 1
    if card == 28:
        return 0
    if card == 32:
        return 0
    if card == 36:
        return 0
    if card == 40:
        return 0
    if card == 44:
        return 2
    if card == 48:
        return 3
    if card == 52:
        return 1
    if card == 56:
        return 2
    if card == 60:
        return 2
    if card == 64:  # Minigunner
        return 2
