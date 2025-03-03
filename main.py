from game import PokerGame

def info_registration():
    user_name = input("Introduce tu nombre: ")
    num_players = int(input("Introduce el número de jugadores (2-7): "))
    user_position = input("Introduce tu posición en la mesa (UTG, MP, HJ, CO, BU, SB, BB): ").upper()
    blinds = input("Introduce las ciegas de la mesa (Mín. 0.02): ")
    user_hand = input("Introduce tu mano con el formato (7H 9C) siendo los palos H, S, C, D (Hearts, Spades, Cloves, Diamonds): ").split()
    print(user_hand)
    #players_pockets = []
    """for i in range(0, num_players):
        print(i)
        money = input("Introduce el dinero del jugador en la posicion: ")"""

    validate_info(num_players, blinds)
    return user_name, num_players, user_position, blinds, user_hand

def validate_info(players, BB):
    if players < 2 | players > 7:
        exit("La cantidad de jugadores es incorrecta.")
    if float(BB) < 0.02:
        exit("La ciegas son demasiado pequeñas.")

if __name__ == "__main__":
    nombre_usuario, num_players, user_position, blinds, user_hand = info_registration()
    game = PokerGame(nombre_usuario, num_players, user_position, blinds, user_hand)
    game.start_game()
    game.game_information()
