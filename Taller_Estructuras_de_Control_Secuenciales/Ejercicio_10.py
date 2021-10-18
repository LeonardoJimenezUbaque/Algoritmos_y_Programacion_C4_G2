"""
Ejercicio 10
El cambio de divisas en la bolsa de Madrid el 25/08/1987 fue el siguiente:
100 chelines austríacos	=	956.871 pesetas
1 dólar EEUU	=	122.499 pesetas
100 dracmas griegos =	88.607 pesetas
100 francos belgas	=	323.728 pesetas
1 franco francés	=	20.110 pesetas
1 libra esterlina	=	178.938 pesetas
100 liras italianas	=	9.289 pesetas
Lea una cantidad en chelines austriacos e imprima el equivalente en pesetas. Lea una cantidad en dracmas griegos e imprima su equivalente en
francos franceses. Finalmente, lea una cantidad en pesetas e imprima su equivalente en dólares y liras italianas.

Entradas
Chelines_Austríacos --> Float --> C_A
Dracmas_Griegos --> Float --> D_G
Pesetas --> Float --> P

Salidas
Pesetas_Convertidas --> Float --> P_C
Francos_Franceses --> Float --> F_F
Dólares --> Float --> D
Liras_Italiana --> Float --> L_I
"""
# Instrucciones al usuario
print("Para conocer cual es el equivalente de sus divisas en otras segun la bolsa de Madrid del 25/08/1987, escriba lo siguiente: ")
# Entradas
C_A = float(input("Digite la cantidad de Chelines austriacos: "))
D_G = float(input("Digite la cantidad de Dracmas griegos: "))
P = float(input("Digite la cantidad de pesetas: "))
# Caja Negra
P_C = (956.871/100)*C_A
F_F = D_G*(88.607/100)/20.110
D = P/122.499
L_I = (100/9.289)*P
# Salidas
print(f"Sus Chelines austriacos equivalen a: {P_C} Pesetas")
print(f"Sus Dracmas griegos equivalen a: {F_F} Francos franceses ")
print(f"Sus Pesetas equivalen a: {D} Dólares")
print(f"Sus Pesetas equivalen a: {L_I} Liras italianas")
