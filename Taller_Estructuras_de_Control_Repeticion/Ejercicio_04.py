"""
Ejercicio 04
Calcular el término doceavo y la suma de los doce primeros términos de la sucesión: 6, 11, 16, 21. Respuesta: a12=61, suma=402.

Entradas --> No hay como tal

Salidas
Termino_Doceavo --> Int --> T_D
Suma --> Int --> S
"""
# Instrucciones al usuario
print("\nEste programa escribirá la suma de los números de la sucesión y el doceavo termino de la misma")
# Caja negra
S = 6
for i in range(1, 12):
    T_D = 5*i + 6
    S = S + T_D
# Salidas
print(f"\nEl doceavo término de la suceción es: {T_D}")
print(
    f"La suma de los primeros 12 números de la sucesión corresponde a: {S}\n")
