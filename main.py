from game import PokerGame

Poker_positions = ["UTG", "MP", "HJ", "CO", "BU", "SB", "BB"]

def info_registration():
    user_name = input("Introduce tu nombre: ")
    num_players = int(input("Introduce el número de jugadores (2-7): "))
    user_position = input("Introduce tu posición en la mesa (UTG, MP, HJ, CO, BU, SB, BB): ").upper()
    blinds = input("Introduce las ciegas de la mesa (Mín. 0.02): ")
    user_hand = input("Introduce tu mano con el formato (7H 9C) siendo los palos H, S, C, D (Hearts, Spades, Cloves, Diamonds): ").split()
    print(user_hand)
    players_pockets = []
    for i in range(0, num_players):
        money = input(f"Introduce las ciegas del jugador en la posicion: {Poker_positions[i]}: ")
        players_pockets.append(money)

    validate_info(num_players, blinds)
    return user_name, num_players, user_position, blinds, user_hand, players_pockets

def validate_info(players, BB):
    if players < 2 | players > 7:
        exit("La cantidad de jugadores es incorrecta.")
    if float(BB) < 0.02:
        exit("La ciegas son demasiado pequeñas.")

if __name__ == "__main__":
    nombre_usuario, num_players, user_position, blinds, user_hand, players_pockets = info_registration()
    game = PokerGame(nombre_usuario, num_players, user_position, blinds, user_hand, players_pockets)
    game.start_game()
    game.game_information()
