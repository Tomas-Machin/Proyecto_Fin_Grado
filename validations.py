from deck import Deck
class Validations:
    deck = Deck()
    def validate_number_of_players(self, num_players):
        if num_players < 2 or num_players > 7:
            exit("\nLa cantidad de jugadores no es correcta.\n")

    def validate_user_position(self, user_position, positions):
        if user_position not in positions:
            exit("\nLa posición introducida es inválida o no esta en una mesa de ese tamaño.\n")

    def validate_blinds(self, blinds):
        if float(blinds) < 0.02: # falla y ns porque - if isinstance(blinds, str) or float(blinds) < 0.02:
            exit("\nLas ciegas introducidas no son válidas.\n")

    def validate_user_hand(self, hand):
        if len(hand) != 2 or not (card in self.deck.cards for card in hand) or hand[0] == hand[1]:
            exit("\nLa mano introducida no son válidas.\n")

    def validate_chips(self, chips):
        for player_chips in chips:
            if int(player_chips) <= 0:
                exit("\nLas fichas de algun jugador no son válidas.\n")
