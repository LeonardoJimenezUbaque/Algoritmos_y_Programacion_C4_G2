"""
Ejercicio 01
Sea N y K dos enteros positivos, con K < N. Se desea escribir un programa que escriba el valor de N,N­1,N­2,..., y así sucesivamente
hasta llegar al valor de K.

Entradas
Números enteros positivos N y K --> Int --> N,K

Salidas
Números enteros desde N hasta K --> int --> N
"""
# Instrucciones al usuario
print("\nEste programa escribirá los números que van desde N hasta K")
# Entradas
N, K = input(f"Digite sus números N y K: ").split(" ")
N = int(N)
K = int(K)
# Caja negra y Salidas
while K >= N:
    print("\nEl valor de N debe ser mayor al valor de K")
    N, K = input(f"\nDigite sus números N y K: ").split(" ")
    N = int(N)
    K = int(K)
X = N - K + 1
for Y in range(X):
    print(N)
    N = N-1
