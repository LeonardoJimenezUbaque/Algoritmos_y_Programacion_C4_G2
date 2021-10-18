"""
Ejercicio 07
Dada una cantidad en metros, se requiere que la convierta a pies y pulgadas, considerando lo siguiente:
1 metro = 39.27 pulgadas; 1 pie = 12 pulgadas.

Entradas
Metros --> Float --> M

Salidas
Pies --> Float --> P_I
Pulgadas --> Float--> P_U
"""
# Instrucciones al usuario
print("Para conocer cual es la cantidad de pies y pulgadas a las que equivale sus metros, escriba lo siguiente: ")
# Entradas
M = float(input("Digite la cantidad de metros:  "))
# Caja Negra
P_I = M*3.281
P_U = M*39.27
# Salidas
print(f"Su cantidad de metros en pies es igual a: {P_I} pies")
print(f"Su cantidad de metros en pulgadas es igual a: {P_U} pulgadas")
