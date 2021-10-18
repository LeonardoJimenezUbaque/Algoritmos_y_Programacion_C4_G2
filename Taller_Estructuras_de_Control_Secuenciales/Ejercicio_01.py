"""
Ejercicio 01
Obtener el promedio de edad de tres personas.

Entradas
Edad_1 --> Int --> E_1
Edad_2 --> Int --> E_2
Edad_3 --> Int --> E_3

Salidas
Promedio_Edad --> Float -->P_E
"""
# Instrucciones al usuario
print("Para conocer el promedio de la edad de tres personas, siga las siguientes instrucciones")
# Entradas
E_1 = int(input("Digite la primera edad: "))
E_2 = int(input("Digite la segunda edad: "))
E_3 = int(input("Digite la tercera edad: "))
# Caja Negra
P_E = (E_1+E_2+E_3)/3  # El resultado sera de tipo float
# Salidas
print(f"El promedio de edad es: {P_E}")
