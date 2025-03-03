from deck import Deck
from player import Player
from table import Table

class PokerGame:
    def __init__(self, user_name, num_players, user_position):
        self.table = Table(num_players)
        self.user_name = Player(user_name)
        self.user_position = user_position.upper()
        self.rivals = [Player("Rival") for _ in range(num_players - 1)]
        self.deck = Deck()
        self.validate_user_position()
        self.assign_info_into_positions()

    def validate_user_position(self):
        if self.user_position not in self.table.positions:
            exit("Posición inválida.")

    def assign_info_into_positions(self):
        for position in self.table.positions:
            if self.user_position == position:
                self.table.poker["POSICIONES_POKER"][self.user_position]["nombre"] = self.user_name.name
            else:
                self.table.poker["POSICIONES_POKER"][position]["nombre"] = "Rival"

    def start_game(self):
        self.deck.shuffle()
        self.deal_initial_cards()
        # self.play_rounds()

    def deal_initial_cards(self):
        for player in [self.user_name] + self.rivals:
            player.hand = [self.deck.draw_card() for _ in range(2)]
            print(player.hand)

    def game_information(self):
        print("\nCartas del jugador usuario:")
        print(f"{self.user_name.name}: {self.user_name.hand}")

        print("\nPosiciones y fichas de los jugadores:")
        print(self.table.get_poker_info())

    """def play_rounds(self):
        # Aquí irán las rondas de apuestas y lógica adicional
        pass"""
