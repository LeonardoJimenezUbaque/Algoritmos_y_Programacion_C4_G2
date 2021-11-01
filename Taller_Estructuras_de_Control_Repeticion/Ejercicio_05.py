"""
Ejercicio 05
Calcule e imprima el número de términos necesarios para que el valor de la siguiente sumatoria se aproxime los más cercanamente a
1000 sin que lo exceda:
∑((k ∗∗2 + 1)/k, donde k=1,2,3,4,...

Entradas --> No hay como tal

Salidas
Número de terminos nesesarios para que la exprexión se acerque los mas posible a 1000 --> Int --> N
Sumatoria --> int --> B
"""
# Instrucciones al usuario
print("\nEste programa escribirá el número de terminos necesarios para que el valor de la sumatoria se aproxime lo maximo a 1000, asimismo el valor de la sumatoria")
# Caja negra
N = 1
while True:
    S = ((N**2)+1)/N
    if S > 1000:
        N = N - 1
        S = ((N**2)+1)/N
        break
    else:
        print(N)
        N = N + 1
# Salidas
print(F"\nEl número de terminos necesarios es: {N}")
print(F"El resultado de la sumatoria es: {S}, cuando K es: {N}\n")
