"""
Ejercicio 03
Desarrolle un algoritmo o programa que permita calcular y mostrar la suma de todos los números pares comprendidos entre 97 y 1003.
Respuesta: 249150

Entradas --> No hay como tal

Salidas
Suma de todos los numeros pares entre 97 a 1003 --> Int --> S
"""
# Instrucciones al usuario
print("\nEste programa escribirá la suma de los números pares comprendidos entre 97 a 1003")
# Caja negra y Salidas
S = 0
for i in range(98, 1004, 2):
    S = S + i
print(f"\n{S}")
