from game import PokerGame

def solicitar_informacion_jugador():
    user_name = input("Introduce tu nombre: ")
    num_players = int(input("Introduce el número de jugadores (2-7): "))
    user_position = input("Introduce tu posición en la mesa (UTG, MP, HJ, CO, BU, SB, BB): ")
    #blinds = input("Introduce las ciegas de la mesa: ")
    #user_hand = input("Introduce tu mano con el formato {[número][palo] [número][palo]} siendo los palos H, S, C, D (Hearts, Spades, Cloves, Diamonds): ")
    players_pockets = []
    """for i in range(0, num_players):
        print(i)
        money = input("Introduce el dinero del jugador en la posicion: ")"""

    return user_name, num_players, user_position

if __name__ == "__main__":
    nombre_usuario, num_players, user_position = solicitar_informacion_jugador()
    game = PokerGame(nombre_usuario, num_players, user_position)
    game.start_game()
    game.game_information()
