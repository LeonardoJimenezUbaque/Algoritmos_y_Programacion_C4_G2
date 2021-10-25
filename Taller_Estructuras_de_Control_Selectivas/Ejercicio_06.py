"""
Ejercicio 06
Se tienen 4 dígitos en las variables A, B, C, D que forman un entero positivo N. Se desea  redondear N a la centena más próxima y mostrar
el  resultado. Considere los siguientes ejemplos: Si A es 2, B es 3, C es 6 y D es 2, entonces N es 2362 y el resultado redondeado es 2400.
Si N es 2342, el resultado redondeado será 2300 y si N es 2962, el resultado redondeado será 3000.

Entradas
Dígitos_N --> Int que se convertiran a Str --> A,B,C,D

Salidas
Resultado_Redondeado --> Int --> R_R
"""
# Instrucciones al usuario
print("Este programa le permitira redondear un numero entero positivo N")
# Entradas
A, B, C, D = input(f"Digite sus números A,B,C,D que forman N: ").split(" ")
A = str(A)
B = str(B)
C = str(C)
D = str(D)
# Caja Negra
N = A+B+C+D  # Suma de los Str para generar el número N
N = int(N)  # Transformación de N a un número de tipo Int
if N <= (int(A) * 1000 + int(B)*100 + 50):
    N = N - int(C+D)
elif N > (int(A) * 1000 + int(B)*100 + 50):
    N = (N - int(C+D))+100
# Salidas
print(f"Su resultado redondeado es: {N}")
