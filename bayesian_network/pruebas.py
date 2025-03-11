from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import numpy as np

from table import Table
from game import PokerGame
from player import Player

# Definir la estructura del modelo
modelo = BayesianNetwork([
    ('CartasUsuario', 'DecisionUsuario'),
    ('JugadoresActivos', 'DecisionUsuario'),
    ('Ciegas', 'DecisionUsuario'),
    ('FichasUsuario', 'DecisionUsuario'),
    ('PosicionUsuario', 'DecisionUsuario')
    #('DecisionRival', 'DecisionUsuario')
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

# trato de datos introducidos por el usuario
table_info = Table()
game_info = PokerGame()
player_info = Player()

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

posicion = posiciones[game_info.user_position]

# Dependiendo del valor de la ciega, determinamos si son altas o bajas
ciegas_tipo = 0 if table_info.poker["Blinds"] < 100 else 1

# Mapeamos la mano a categorías de "Débil", "Media" o "Fuerte"
manos_fuertes = {"A", "K", "Q", "J", "10"}  # evaluar la mano como conjunto de max 4 y menos 0 y de ahi evaluar alto-medio-bajo
mano_usuario = 0  # Mano débil
for carta in manos_fuertes:
    if carta in player_info.hand:
        mano_usuario = 2  # Mano fuerte
        break
if mano_usuario == 0:  # Si no es fuerte, puede ser media o débil
    if "9" in player_info.hand or "8" in player_info.hand:
        mano_usuario = 1  # Mano media
    else:
        mano_usuario = 0  # Mano débil

# Realizar inferencia en la red
inferencia = VariableElimination(modelo)

# Ejemplo: Inferir la mejor acción si el usuario tiene cartas fuertes, hay 4 jugadores activos, las ciegas son altas y está en posición tardía
"""resultado = inferencia.query(
    variables=['DecisionUsuario'], 
    evidence={'CartasUsuario': 2, 'JugadoresActivos': 1, 'Ciegas': 1, 'PosicionUsuario': 2}
)"""

resultado = inferencia.query(
    variables=['DecisionUsuario'], 
    evidence={'CartasUsuario': mano_usuario, 'JugadoresActivos': table_info.poker["Players"], 'Ciegas': table_info.poker["Blinds"], 'PosicionUsuario': game_info.user_position}
)

# Reemplazar valores numéricos por etiquetas
acciones = ['Fold', 'Check/Call', 'Raise']
print("+--------------------+------------------------+")
print("| DecisionUsuario    |   phi(DecisionUsuario) |")
print("+====================+========================+")
for i, accion in enumerate(acciones):
    print(f"| {accion:<18} | {resultado.values[i]:>22.4f} |")
print("+--------------------+------------------------+")
