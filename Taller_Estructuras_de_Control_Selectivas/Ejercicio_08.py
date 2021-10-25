"""
Ejercicio 08
Dados como datos los valores enteros P y Q, determine si los mismos satisfacen la siguiente expresión: P^3 + Q^4 – 2*P^2 > 680. En caso afirmativo
debe mostrar los valores de “P y Q satisfacen la expresión”, de lo contrario muestre un mensaje “P y Q no Satisfacen la expresión”. Utilice la
concatenación para mostrar los valores.

Entradas
Datos --> Int --> P,Q

Salidas
Resultado_Expresión --> Str --> R_E
"""
# Instrucciones al usuario
print("Este programa le permitira conocer si los datos satisfacen o no la expresión dada")
# Entradas
P, Q = input(f"Digite los valores de P y Q correspondientemente: ").split(" ")
P = int(P)
Q = int(Q)
# Caja Negra y Salidas
R_E = P**3 + Q**4 - 2*P**2
if R_E > 680:
    print(f"{P} y {Q} satisfacen la expresión")
else:
    print(f"{P} y {Q} no Satisfacen la expresión")
