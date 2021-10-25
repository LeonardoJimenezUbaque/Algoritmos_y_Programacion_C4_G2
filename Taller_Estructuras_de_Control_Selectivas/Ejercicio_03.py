"""
Ejercicio 03
Dados los datos A, B, C y D que representan números enteros; escriba un algoritmo que calcule el resultado de las siguientes expresiones:
Si D=0 -----------> (A-C)^2
Si D>0 -----------> (A-B)^3/D

Entradas
Datos --> Int --> A,B,C,D

Salidas
Resultado --> Expresión 1 sera un Int - Expresión 2 sera un Float --> R
"""
# Instrucciones al usuario
print("Este programa le permitira calcular el resultado de las expresiones dadas")
# Entradas
A, B, C, D = input(f"Digite sus números A,B,C,D: ").split(" ")
A = int(A)
B = int(B)
C = int(C)
D = int(D)
# Caja Negra
if D == 0:
    R = (A-C)**2
elif D > 0:
    R = ((A-B)**3)/D
# Salidas
print(f"Su resultado es: {R}")
