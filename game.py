from deck import Deck
from player import Player

POSICIONES_POKER = ["UTG", "UTG + 1", "UTG + 2", "MP 1", "MP 2", "HJ", "CO", "BU", "SB", "BB"]

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
        # Inicializar los jugadores en las posiciones
        total_players = [self.user_name] + self.rivals
        user_index = POSICIONES_POKER.index(self.user_position)
        print(total_players)

        # Asignar jugadores a posiciones rotando la lista
        ordered_players = total_players[user_index:] + total_players[:user_index]

        for position, player in zip(POSICIONES_POKER, ordered_players):
            self.positions[position] = {
                "nombre": player.name,
                "fichas": player.chips if hasattr(player, "chips") else 1000,  # Supongamos que inician con 1000 fichas
            }
            player.position = position  # Asignar posición al jugador

    def start_game(self):
        self.deck.shuffle()
        self.deal_initial_cards()
        self.play_rounds()

    def deal_initial_cards(self):
        for player in [self.user_name] + self.rivals:
            player.hand = [self.deck.draw_card() for _ in range(2)]

    def game_information(self):
        print("\nCartas del jugador usuario:")
        print(f"{self.user_name.name}: {self.user_name.hand}")

        print("\nPosiciones y fichas de los jugadores:")
        for position, info in self.positions.items():
            print(f"Posición: {position}, Nombre: {info['nombre']}, Fichas: {info['fichas']}")

    def play_rounds(self):
        # Aquí irán las rondas de apuestas y lógica adicional
        pass
