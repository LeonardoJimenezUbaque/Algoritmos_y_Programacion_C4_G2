"""
Ejercicio 06
Un maestro desea saber qué porcentaje de hombres y qué porcentaje de mujeres hay en un grupo de estudiantes.

Entradas
Total_Hombres--> Int --> T_H
Total_Mujeres--> Int --> T_M

Salidas
Porcentaje_Hombres--> Float --> P_H
Porcentaje_Mujeres--> Float --> P_M
"""
# Instrucciones al usuario
print("Para conocer cual es el porcentaje de estudiantes de cada sexo, escriba lo siguiente: ")
# Entradas
T_H = int(input("Digite la cantidad de hombres en el salon de clase:  "))
T_M = int(input("Digite la cantidad de mujeres en el salon de clase:  "))
# Caja Negra
T_E = T_H+T_M  # Total Estudiantes
P_H = (T_H/T_E)*100
P_M = (T_M/T_E)*100
# Salidas
print(f"El porcentaje de hombres en el salon de clase es de: {P_H}%")
print(f"El porcentaje de mujeres en el salon de clase es de: {P_M}%")
