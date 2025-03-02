from game import PokerGame

def solicitar_informacion_jugador():
    user_name = input("Introduce tu nombre: ")
    num_players = int(input("Introduce el número de jugadores (2-6): "))
    user_position = input("Introduce tu posición en la mesa (UTG, MP, HJ, CO, BU, SB, BB): ")
    # print(f"{user_name}, tu posicion es: {user_position} en una mesa de {num_players} jugadores.")
    return user_name, num_players, user_position

if __name__ == "__main__":
    nombre_usuario, num_players, user_position = solicitar_informacion_jugador()
    game = PokerGame(nombre_usuario, num_players, user_position)
    game.start_game()
    game.game_information()
