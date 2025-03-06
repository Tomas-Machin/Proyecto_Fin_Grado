from game import PokerGame
from round import Round

Poker_positions = ["UTG", "MP", "HJ", "CO", "BU", "SB", "BB"]

def info_registration():
    user_name = input("Introduce tu nombre: ")

    try:
        num_players = int(input("Introduce el número de jugadores (2-7): "))
        user_position = input("Introduce tu posición en la mesa (UTG, MP, HJ, CO, BU, SB, BB): ").upper()
        blinds = float(input("Introduce las ciegas de la mesa (Mín. 0.02): "))
    except:
        exit('\nLos datos introducidos son inválidos.\n')

    user_hand = input("Introduce tu mano con el formato (7H 9C) siendo los palos H, S, C, D (Hearts, Spades, Cloves, Diamonds): ").split()

    players_pockets = []
    for i in range(0, num_players):
        money = input(f"Introduce las ciegas del jugador en la posicion: {Poker_positions[i]}: ")
        players_pockets.append(money)

    pot_in_bets = []
    for i in range(0, num_players):
        bet = float(input(f"Introduce la apuesta del jugador en la posicion: {Poker_positions[i]}: "))
        if bet == 0:
            players_left = num_players - 1  # reducir el numero de jugadores
            pot_in_bets.append(bet)

    return user_name, num_players, user_position, blinds, user_hand, players_pockets, pot_in_bets

if __name__ == "__main__":
    # inicio
    nombre_usuario, num_players, user_position, blinds, user_hand, players_pockets, pot_in_bets = info_registration()
    game = PokerGame(nombre_usuario, num_players, user_position, blinds, user_hand, players_pockets, pot_in_bets)
    game.start_game()
    game.game_information()


    # cadenas de markov - teoria de juegos
