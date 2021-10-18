"""
Ejercicio 17
En un hospital rural existen tres áreas: Ginecología, Pediatría y Traumatología. El presupuesto anual del hospital
se reparte conforme a la siguiente tabla:

Área	          Porcentaje del presupuesto
Ginecología	                 40%
Traumatología	             30%
Pediatría	                 30%
Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestado.

Entradas
Presupuesto_Anual --> Float --> P_A

Salidas
Presupuesto_Anual_Ginecología --> Float --> G
Presupuesto_Anual_Traumatologia --> Float --> T
Presupuesto_Anual_Pediatría --> Float --> P
"""
# Instrucciones al usuario
print("Para conocer el presupuesto que recibira cada área del hospítal, escriba lo siguiente: ")
# Entradas
P_A = float(input("Digite el presupuesto anual del hospital: "))
# Caja negra
G = P_A*0.40
T = P_A*0.30
P = P_A*0.30
# Salidas
print(f"A ginecología le corresponde del presupuesto anual: {G}$")
print(f"A traumatología le corresponde del presupuesto anual: {T}$")
print(f"A pediatría le corresponde del presupuesto anual: {P}$")
