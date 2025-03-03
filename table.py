import json

class Table:
    def __init__(self, num_players):
        self.num_players = num_players
        self.positions = self.assign_positions()
        self.poker = {
            "POSICIONES_POKER": {
                position: {"nombre": "Rival"} for position in self.positions
            }
        }

    def assign_positions(self):
        position_options = {
            2: ["SB", "BB"],
            3: ["BU", "SB", "BB"],
            4: ["CO", "BU", "SB", "BB"],
            5: ["HJ", "CO", "BU", "SB", "BB"],
            6: ["MP", "HJ", "CO", "BU", "SB", "BB"],
            7: ["UTG", "MP", "HJ", "CO", "BU", "SB", "BB"]
        }
        return position_options.get(self.num_players, [])

    def get_poker_info(self):
        return json.dumps(self.poker, indent=4)
