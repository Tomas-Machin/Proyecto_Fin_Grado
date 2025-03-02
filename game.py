from deck import Deck
from player import Player
import json

# POSICIONES_POKER = ["UTG", "MP", "HJ", "CO", "BU", "SB", "BB"]

poker = {
    "POSICIONES_POKER": {
        "UTG": {},
        "MP": {},
        "HJ": {},
        "CO": {},
        "BU": {},
        "SB": {},
        "BB": {}
    }
}

#posiciones_poker_json = json.dumps(poker, indent=4)
#print(posiciones_poker_json)

POSICIONES_POKER = list(poker["POSICIONES_POKER"].keys())
#print("Las posiciones de póker son:", POSICIONES_POKER)

class PokerGame:
    def __init__(self, user_name, num_players, user_position):
        self.user_name = Player(user_name)
        self.num_players = num_players
        self.user_position = user_position.upper()
        self.rivals = [Player(f"Rival {i + 1}") for i in range(num_players - 1)]
        self.deck = Deck()
        self.validate_user_position()
        self.positions = {}  # Diccionario para almacenar información de posiciones
        self.assign_info_into_positions()

    def validate_user_position(self):
        if self.user_position not in POSICIONES_POKER:
            exit("Posición inválida.")

    def assign_info_into_positions(self):
        if self.user_position in POSICIONES_POKER:
            poker["POSICIONES_POKER"][self.user_position]["nombre"] = self.user_name.name
        else:
            exit("Posición inválida.")

    def start_game(self):
        self.deck.shuffle()
        self.deal_initial_cards()
        self.play_rounds()

    def deal_initial_cards(self):
        for player in [self.user_name] + self.rivals:
            player.hand = [self.deck.draw_card() for _ in range(2)]

    def game_information(self):
        posiciones_poker_json = json.dumps(poker, indent=4)

        print("\nCartas del jugador usuario:")
        print(f"{self.user_name.name}: {self.user_name.hand}")

        print("\nPosiciones y fichas de los jugadores:")
        print(posiciones_poker_json)

    def play_rounds(self):
        # Aquí irán las rondas de apuestas y lógica adicional
        pass
