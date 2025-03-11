from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import numpy as np

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

# Realizar inferencia en la red
inferencia = VariableElimination(modelo)

# Ejemplo: Inferir la mejor acción si el usuario tiene cartas fuertes, hay 4 jugadores activos, las ciegas son altas y está en posición tardía
resultado = inferencia.query(
    variables=['DecisionUsuario'], 
    evidence={'CartasUsuario': 2, 'JugadoresActivos': 1, 'Ciegas': 1, 'PosicionUsuario': 2}
)

# Reemplazar valores numéricos por etiquetas
acciones = ['Fold', 'Check/Call', 'Raise']
print("+--------------------+------------------------+")
print("| DecisionUsuario    |   phi(DecisionUsuario) |")
print("+====================+========================+")
for i, accion in enumerate(acciones):
    print(f"| {accion:<18} | {resultado.values[i]:>22.4f} |")
print("+--------------------+------------------------+")
