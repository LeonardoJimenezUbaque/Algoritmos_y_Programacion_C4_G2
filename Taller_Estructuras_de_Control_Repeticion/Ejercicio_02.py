"""
Ejercicio 02
Escriba un programa que imprima todos los enteros positivos impares menores que 100 omitiéndose aquellos que sean divisibles por 7.

Entradas --> No hay como tal

Salidas
Numeros enteros impares menores que 100, omitiendo multiplos de 7 --> Int --> N
"""
# Instrucciones al usuario
print("\nEste programa escribirá los números enteros positivos impares menores a 100, omitiendo aquellos divisibles en 7")
# Caja negra y Salidas
N = 1
for i in range(50):
    if (N % 7) != 0:
        print(N)
        N = N + 2
    else:
        N = N + 2
