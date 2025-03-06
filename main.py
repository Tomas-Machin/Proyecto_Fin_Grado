from game import PokerGame

Poker_positions = ["UTG", "MP", "HJ", "CO", "BU", "SB", "BB"]

def info_registration():
    user_name = input("Introduce tu nombre: ")

    try:
        num_players = int(input("Introduce el número de jugadores (2-7): "))
    except:
        exit('\nEl dato introducido es inválido.\n')

    user_position = input("Introduce tu posición en la mesa (UTG, MP, HJ, CO, BU, SB, BB): ").upper()
    blinds = input("Introduce las ciegas de la mesa (Mín. 0.02): ")
    user_hand = input("Introduce tu mano con el formato (7H 9C) siendo los palos H, S, C, D (Hearts, Spades, Cloves, Diamonds): ").split()

    players_pockets = []
    for i in range(0, num_players):
        money = input(f"Introduce las ciegas del jugador en la posicion: {Poker_positions[i]}: ")
        players_pockets.append(money)

    return user_name, num_players, user_position, blinds, user_hand, players_pockets


if __name__ == "__main__":
    nombre_usuario, num_players, user_position, blinds, user_hand, players_pockets = info_registration()
    game = PokerGame(nombre_usuario, num_players, user_position, blinds, user_hand, players_pockets)
    game.start_game()
    game.game_information()

    # cadenas de markov - teoria de juegos
