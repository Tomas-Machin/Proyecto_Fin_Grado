from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definir la estructura del modelo
modelo = BayesianNetwork([('Lluvia', 'CespedMojado'), ('Rociador', 'CespedMojado')])

# Definir las distribuciones de probabilidad condicional (CPDs)
cpd_lluvia = TabularCPD(variable='Lluvia', variable_card=2, values=[[0.7], [0.3]])
cpd_rociador = TabularCPD(variable='Rociador', variable_card=2, values=[[0.6], [0.4]])
cpd_cesped = TabularCPD(
    variable='CespedMojado', variable_card=2,
    values=[[0.99, 0.80, 0.90, 0.00],  # Probabilidad de que el césped NO esté mojado
            [0.01, 0.20, 0.10, 1.00]], # Probabilidad de que el césped esté mojado
    evidence=['Lluvia', 'Rociador'],
    evidence_card=[2, 2]
)

# Agregar CPDs al modelo
modelo.add_cpds(cpd_lluvia, cpd_rociador, cpd_cesped)

# Comprobar si la red es válida
assert modelo.check_model()

# Realizar inferencia en la red
inferencia = VariableElimination(modelo)

# Calcular la probabilidad de que haya llovido dado que el césped está mojado
resultado = inferencia.query(variables=['Lluvia'], evidence={'CespedMojado': 1})
print(resultado)
