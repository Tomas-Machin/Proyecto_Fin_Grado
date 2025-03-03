import random

class Deck:
    def __init__(self):
        self.cards = [f"{rank}{suit}" for rank in "23456789TJQKA" for suit in "HSCD"]   # "♠♥♦♣"

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()
