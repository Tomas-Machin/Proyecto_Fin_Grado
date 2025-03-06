import random

class Deck:
    def __init__(self):
        self.rank = "23456789TJQKA"
        self.suit = "HSCD"
        self.cards = [f"{rank}{suit}" for rank in self.rank for suit in self.suit]   # "♠♥♦♣"

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()
