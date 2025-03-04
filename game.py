from deck import Deck
from player import Player
from table import Table

class PokerGame:
    def __init__(self, user_name, num_players, user_position, blinds, user_hand, players_pockets):
        self.table = Table(num_players, blinds)
        self.user = Player(user_name, user_hand)
        self.user_position = user_position
        self.rivals = [Player("Rival", []) for _ in range(num_players - 1)]
        self.players_pockets = players_pockets
        self.deck = Deck()
        self.validate_user_position()
        self.assign_name_into_positions()

    def validate_user_position(self):
        if self.user_position not in self.table.positions:
            exit("Posición inválida.")

    def assign_name_into_positions(self):
        for position in self.table.positions:
            if self.user_position == position:
                self.table.poker["Positions"][self.user_position]["name"] = self.user.name

    def start_game(self):
        self.deck.shuffle()
        self.deal_cards_and_assign_money()
        # self.play_rounds()

    def deal_cards_and_assign_money(self):
        for index, position in enumerate(self.table.positions):
            if self.user_position == position:
                self.table.poker["Positions"][self.user_position]["Chips"] = self.players_pockets[index]
                self.table.poker["Positions"][self.user_position]["hand"] = self.user.hand
            else:
                self.table.poker["Positions"][position]["Chips"] = self.players_pockets[index]
                #self.table.poker["Positions"][position]["hand"] = [self.deck.draw_card() for _ in range(2)]

    def game_information(self):
        print("\nCartas del jugador usuario:")
        print(f"{self.user.name}: {self.user.hand}")

        print("\nPosiciones y ciegas de los jugadores:")
        print(self.table.get_table_info())

    """def play_rounds(self):
        # Aquí irán las rondas de apuestas y lógica adicional
        pass"""
