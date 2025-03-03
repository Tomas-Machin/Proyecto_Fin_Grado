import player
from deck import Deck
from player import Player
from table import Table

class PokerGame:
    def __init__(self, user_name, num_players, user_position, blinds, user_hand):
        self.table = Table(num_players, blinds)
        self.user_name = Player(user_name)
        self.user_hand = Player(user_hand)
        self.user_position = user_position
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
                self.table.poker["Positions"][self.user_position]["name"] = self.user_name.name

    def start_game(self):
        self.deck.shuffle()
        self.deal_initial_cards()
        # self.play_rounds()

    def deal_initial_cards(self):
        for position in self.table.positions:
            #if self.user_position == position:
            #    self.table.poker["Positions"][self.user_position]["hand"] = self.user_hand
            #else:
                self.table.poker["Positions"][position]["hand"] = [self.deck.draw_card() for _ in range(2)]

    def game_information(self):
        print("\nCartas del jugador usuario:")
        print(f"{self.user_name.name}: {self.user_name.hand}")

        print("\nPosiciones y ciegas de los jugadores:")
        print(self.table.get_table_info())

    """def play_rounds(self):
        # Aquí irán las rondas de apuestas y lógica adicional
        pass"""
