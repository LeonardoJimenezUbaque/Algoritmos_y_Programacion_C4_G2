"""
Ejercicio 13
Determine cuánto dinero hay en un banco que contiene N1 billetes de 50000, N2 billetes de 20000, N3 billetes de
10000, N4 billetes de 5000, N5 billetes de 2000, N6 billetes 1000, N7 billetes de 500 y N8 billetes de 100.

Entradas
Billetes_50000 --> Int -->N1
Billetes_20000 --> Int -->N2
Billetes_10000 --> Int -->N3
Billetes_5000 --> Int -->N4
Billetes_2000 --> Int -->N5
Billetes_1000 --> Int -->N6
Billetes_500 --> Int -->N7
Billetes_100 --> Int -->N8

Salidas
Cantidad_Dinero --> Float--> C_D
"""
# Instrucciones al usuario
print("Para conocer cuanto dinero hay, escriba lo siguiente: ")
# Entradas
N1 = int(input("Digite la cantidad de billetes de 50000: "))
N2 = int(input("Digite la cantidad de billetes de 20000: "))
N3 = int(input("Digite la cantidad de billetes de 10000: "))
N4 = int(input("Digite la cantidad de billetes de 5000: "))
N5 = int(input("Digite la cantidad de billetes de 2000: "))
N6 = int(input("Digite la cantidad de billetes de 1000: "))
N7 = int(input("Digite la cantidad de billetes de 500: "))
N8 = int(input("Digite la cantidad de billetes de 100: "))
# Caja negra
C_D = (N1*50000+N2*20000+N3*10000+N4*5000+N5*2000+N6*1000+N7*500+N8*100)
# Salidas
print(f"La cantidad total de dinero en el banco es de: {C_D}$")
