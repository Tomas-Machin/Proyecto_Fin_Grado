class Round:
    def __init__(self):
        self.bote = 0
        self.players_left = 7
        self.community_cards = []

        #objeto variable o hacer un objeto por ronda
        self.ronda_1 = {
            "Players left": 1,  # PREFLOP
            "Pot": self.bote,
        }

        self.ronda_2 = {
            "Players left": 2,  # POSTFLOP
            "Pot": self.bote,
            "Community cards": self.community_cards
        }

        self.ronda_3 = {
            "Players left": 3,  # TURN
            "Pot": self.bote,
            "Community cards": self.community_cards
        }

        self.ronda_4 = {
            "Players left": 4,  # RIVER
            "Pot": self.bote,
            "Community cards": self.community_cards
        }