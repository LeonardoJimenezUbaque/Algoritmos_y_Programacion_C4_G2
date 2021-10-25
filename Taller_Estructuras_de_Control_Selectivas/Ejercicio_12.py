"""
Ejercicio 12
Dada una cantidad entera de COP, desarrolle un algoritmo que permita desglosar dicha cantidad en los billetes y monedas de curso legal en el País.
Recuerde que estos son:
Billetes
100.000 COP,
50.000 COP,
20.000 COP,
10.000 COP,
5.000 COP,
2.000 COP,
1.000 COP
Monedas
500 COP,
200 COP,
100 COP,
50 COP
Nota: si la cantidad tiene unidades no las tenga en cuenta
Ejemplo:
Entrada:2251
Salida: 2.000,200,50

Entradas
Monto_COP --> Float --> M_COP

Salidas
Billetes_100000 --> Int --> B_1
Billetes_50000 --> Int --> B_2
Billetes_20000 --> Int --> B_3
Billetes_10000 --> Int --> B_4
Billetes_5000 --> Int --> B_5
Billetes_2000 --> Int --> B_6
Billetes_1000 --> Int --> B_7
Monedas_500 --> Int --> M_1
Monedas_200 --> Int --> M_2
Monedas_100 --> Int --> M_3
Monedas_50 --> Int --> M_4
"""
# Instrucciones al usuario
print("Este programa le permitira conocer cuantos billetes de distintas denominaciones necesita dada una cantidad en COP")
# Entradas
M_COP = int(input("Ingrese cantidad de dinero: $"))
# Caja Negra y Salidas
B_1 = (M_COP-M_COP % 100000)/100000
M_COP = M_COP % 100000
B_2 = (M_COP-M_COP % 50000)/50000
M_COP = M_COP % 50000
B_3 = (M_COP-M_COP % 20000)/20000
M_COP = M_COP % 20000
B_4 = (M_COP-M_COP % 10000)/10000
M_COP = M_COP % 10000
B_5 = (M_COP-M_COP % 5000)/5000
M_COP = M_COP % 5000
B_6 = (M_COP-M_COP % 2000)/2000
M_COP = M_COP % 2000
B_7 = (M_COP-M_COP % 1000)/1000
M_COP = M_COP % 1000
M_1 = (M_COP-M_COP % 500)/500
M_COP = M_COP % 500
M_2 = (M_COP-M_COP % 200)/200
M_COP = M_COP % 200
M_3 = (M_COP-M_COP % 100)/100
M_COP = M_COP % 100
M_4 = (M_COP-M_COP % 50)/50
M_COP = M_COP % 50
if B_1 > 0:
    print(f"La Cantidad de billetes de 100000 es de: {B_1}")
if B_2 > 0:
    print(f"La Cantidad de billetes de 50000 es de: {B_2}")
if B_3 > 0:
    print(f"La Cantidad de billetes de 20000 es de: {B_3}")
if B_4 > 0:
    print(f"La Cantidad de billetes de 10000 es de: {B_4}")
if B_5 > 0:
    print(f"La Cantidad de billetes de 5000 es de: {B_5}")
if B_6 > 0:
    print(f"La Cantidad de billetes de 2000 es de: {B_6}")
if B_7 > 0:
    print(f"La Cantidad de billetes de 1000 es de: {B_7}")
if M_1 > 0:
    print(f"La Cantidad de monedas de 500 es de: {M_1}")
if M_2 > 0:
    print(f"La Cantidad de monedas de 200 es de: {M_2}")
if M_3 > 0:
    print(f"La Cantidad de monedas de 100 es de: {M_3}")
if M_4 > 0:
    print(f"La Cantidad de monedas de 50 es de: {M_4}")
