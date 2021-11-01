"""
Ejercicio 06
Efectuar la división de dos números enteros, utilizando el método de las restas sucesivas. Observe el siguiente ejemplo:
Dividir 8 entre 2
8 – 2 = 6  |
6 – 2 = 4   |-->  Número de restas efectuadas es igual al cociente =4
4 – 2 = 2  |
2 – 2 = 0 --->    %resto de la división
Imprima el restante efectuado.

Entradas
Numero_1 --> Int --> N_1
Numero_2 --> Int --> N_2

Salidas
Cociente_División --> Float --> C
Modulo_División --> Int --> M
"""
# Instrucciones al usuario
print("\nEste programa efectura la división de dos números aplicando el método de restas sucesivas y mostrara el resto de la división")
# Entradas
N_1, N_2 = input(f"Digite sus números N1 y N2: ").split(" ")
N_1 = int(N_1)
N_2 = int(N_2)
# Caja negra
print()
Div = N_1//N_2  # Dos // solo arroja la parte entera de la division
C = 0

for i in range(Div):
    print(f"{N_1} - {N_2} = {N_1-N_2}")
    N_1 = N_1 - N_2
    C = C + 1

# Salidas
print(f"\nEl resto de la división es {N_1}")
print(f"El cociente de la dicisión es {C}\n")
