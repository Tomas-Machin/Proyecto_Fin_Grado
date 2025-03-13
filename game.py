from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import numpy as np

from deck import Deck
from player import Player
from table import Table
from round import Round
from validations import Validations

class PokerGame:
    def __init__(self, user_name, num_players, user_position, blinds, user_hand, players_pockets, bets):
        self.rivals = [Player("Rival", []) for _ in range(num_players - 1)]
        self.user_position = user_position
        self.table = Table(num_players, blinds)
        self.user = Player(user_name, user_hand)
        self.players_pockets = players_pockets
        self.deck = Deck()
        self.round = Round(bets, [], blinds)
        self.validations = Validations(num_players, user_position, self.table.positions, blinds, user_hand, players_pockets)
        self.assign_user_into_positions()

    def assign_user_into_positions(self):
        for position in self.table.positions:
            if self.user_position == position:
                self.table.poker["Positions"][self.user_position]["name"] = self.user.name

    def deal_cards_and_assign_money(self):
        for index, position in enumerate(self.table.positions):
            if self.user_position == position:
                self.table.poker["Positions"][self.user_position]["Chips"] = self.players_pockets[index]
                self.user.chips = self.players_pockets[index]
                self.table.poker["Positions"][self.user_position]["hand"] = self.user.hand
            else:
                self.table.poker["Positions"][position]["Chips"] = self.players_pockets[index]
                #self.table.poker["Positions"][position]["hand"] = [self.deck.draw_card() for _ in range(2)]

    """def deal_community_cards(self,):
        if(self.round.ronda['Round'] == 1):
            cards = [self.deck.draw_card() for _ in range(4)].pop(0)
            self.round = Round(self.round.pot, cards)"""

# ---------------------------------------------------------------------------------------------------------------------------
    def network_data(self):
        # Posición del usuario
        posiciones = {
            "UTG": 0,  # Temprana
            "MP": 0,   # Temprana
            "HJ": 1,   # Media
            "CO": 1,   # Media
            "BU": 2,   # Tardía
            "SB": 2,   # Tardía
            "BB": 2    # Tardía
        }

        posicion = posiciones[self.user_position]
        #posicion = posiciones(self.user_position, 0)

        # Dependiendo del valor de la ciega, determinamos si son altas o bajas -> si no puedes jugar 5 manos | 10 manos
        ciegas_tipo = 0 if float(self.user.chips) / float(self.table.poker["Blinds"]) < 5 else 1

        # Mapeamos la mano a categorías de "Débil", "Media" o "Fuerte"
        # evaluar la mano como conjunto de max 4 y menos 0 y de ahi evaluar alto-medio-bajo
        manos_fuertes = {"AS", "KS", "QS", "JS", "10S", "AC", "KC", "QC", "JC", "10C", "AH", "KH", "QH", "JH", "10H", "AD", "KD", "QD", "JD", "10D"}
        manos_intermedias = {"9S", "8S","9C", "8C","9H", "8H", "9D", "8D"}
        potencial_mano = 0  # Mano débil
        for carta in self.user.hand:
            if carta in manos_fuertes:
                potencial_mano = potencial_mano + 1  # Mano fuerte
            elif carta in manos_intermedias:
                potencial_mano = potencial_mano + 0.5  # Mano media
            else:
                potencial_mano = potencial_mano + 0  # Mano debil

        if potencial_mano <= 0.5:
            potencial_mano = 0
        elif potencial_mano <= 1.5:
            potencial_mano = 1
        else:
            potencial_mano = 2 

        total_players = 0
        if self.table.poker["Players"] < 4:
            total_players = 0
        elif self.table.poker["Players"] < 6:
            total_players = 1
        else:
            total_players = 2

        return posicion, ciegas_tipo, potencial_mano, total_players

    def network(self):
        # Definir la estructura del modelo
        modelo = BayesianNetwork([
            ('CartasUsuario', 'DecisionUsuario'),
            ('JugadoresActivos', 'DecisionUsuario'),
            ('Ciegas', 'DecisionUsuario'),
            ('FichasUsuario', 'DecisionUsuario'),
            ('PosicionUsuario', 'DecisionUsuario')
        ])

        # Definir las distribuciones de probabilidad condicional (CPDs)
        cpd_cartas_usuario = TabularCPD(variable='CartasUsuario', variable_card=3, values=[[0.3], [0.4], [0.3]])
        cpd_jugadores_activos = TabularCPD(variable='JugadoresActivos', variable_card=3, values=[[0.2], [0.5], [0.3]])
        cpd_ciegas = TabularCPD(variable='Ciegas', variable_card=2, values=[[0.5], [0.5]])
        cpd_fichas_usuario = TabularCPD(variable='FichasUsuario', variable_card=3, values=[[0.3], [0.4], [0.3]])
        cpd_posicion_usuario = TabularCPD(variable='PosicionUsuario', variable_card=3, values=[[0.33], [0.34], [0.33]])

        # Generar una matriz de probabilidad aleatoria válida para DecisionUsuario
        num_combinations = 3 * 3 * 2 * 3 * 3  # 162 combinaciones posibles de entrada
        values = np.random.rand(3, num_combinations)  # Matriz de valores aleatorios
        values /= values.sum(axis=0)  # Normalizar para que cada columna sume 1

        cpd_decision_usuario = TabularCPD(
            variable='DecisionUsuario', variable_card=3,
            values=values,
            evidence=['CartasUsuario', 'JugadoresActivos', 'Ciegas', 'FichasUsuario', 'PosicionUsuario'],
            evidence_card=[3, 3, 2, 3, 3]
        )

        # Agregar CPDs al modelo
        modelo.add_cpds(
            cpd_cartas_usuario, cpd_jugadores_activos, cpd_ciegas, cpd_fichas_usuario, 
            cpd_posicion_usuario, cpd_decision_usuario
        )

        # Comprobar si la red es válida
        assert modelo.check_model()

        posicion, ciegas_tipo, potencial_mano, total_players = self.network_data()

        # Realizar inferencia en la red
        inferencia = VariableElimination(modelo)

        resultado = inferencia.query(
        variables=['DecisionUsuario'], 
        evidence={'CartasUsuario': potencial_mano, 
                'JugadoresActivos': total_players, 
                #'Ciegas': table_info.poker["Blinds"], 
                'Ciegas': ciegas_tipo, 
                'PosicionUsuario': posicion}
        )

        return resultado

    def result_network(self):
        resultado = self.network()
        # Reemplazar valores numéricos por etiquetas
        acciones = ['Fold', 'Check/Call', 'Raise']
        print(f"Las probabilidades de las jugadas son:")
        print("+--------------------+------------------------+")
        print("| DecisionUsuario    |   phi(DecisionUsuario) |")
        print("+====================+========================+")
        for i, accion in enumerate(acciones):
            print(f"| {accion:<18} | {resultado.values[i]:>22.4f} |")
        print("+--------------------+------------------------+")
# ---------------------------------------------------------------------------------------------------------------------------

    def start_game(self):
        self.deck.shuffle()
        self.deal_cards_and_assign_money()
        self.validations.confirm_data()
        self.network()
        # self.play_rounds()

    def game_information(self):
        print("\nCartas del jugador usuario:")
        print(f"{self.user.name}: {self.user.hand}")

        print("\nPosiciones y ciegas de los jugadores:")
        print(self.table.get_table_info())

        print("\nRonda 1:")
        print(self.round.ronda)
        
        print("\nRed Bayesiana:")
        print(self.result_network())


    """def play_rounds(self):
        # Aquí irán las rondas de apuestas y lógica adicional
        pass"""
