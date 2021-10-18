"""
Ejercicio 09
Calcular el salario neto de un trabajador en función del número de horas trabajadas, el precio de la hora y considerando un descuento fijo
al sueldo base por concepto de impuestos del 20%.

Entradas
Precio_Hora_Trabajo --> Float --> P_H
Horas_Trabajo --> Float --> H_T


Salidas
Salario_Neto --> Float --> S_N
"""
# Instrucciones al usuario
print("Para conocer cual es su salario neto, escriba lo siguiente: ")
# Entradas
P_H = float(input("Digite el precio de la hora de trabajo: "))
H_T = float(input("Digite la cantidad de horas trabajadas: "))
# Caja Negra
S = P_H*H_T  # Salario
S_N = S-S*0.20
# Salidas
print(f"Su salario neto corresponde a: {S_N}$")
