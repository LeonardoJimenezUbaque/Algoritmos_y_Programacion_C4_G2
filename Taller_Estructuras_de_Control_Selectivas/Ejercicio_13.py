"""
Ejercicio 13
Desarrolle un algoritmo que reciba como dato de entrada la fecha de nacimiento de una persona y a continuación escriba el nombre del signo
del zodiaco correspondiente;  así  como  su  edad.  Considere  la  siguiente  tabla  de  signos:

Signo               Día y mes
Sagitario        22/11 al 21/12
Capricornio      22/12 al 20/01
Acuario          21/01 al 19/02
Piscis           20/02 al 19/03
Aries            21/03 al 20/04
Tauro            21/04 al 21/05
Géminis          22/05 al 21/06
Cáncer           22/06 al 22/07
Leo              23/07 al 23/08
Virgo            24/08 al 22/09
Libra            23/09 al 22/10
Escorpión        23/10 al 21/11

Entradas
Fecha_Nacimiento --> Str --> D,M,A

Salidas
Signo --> Str --> S
Edad --> Int --> E
"""
# Instrucciones al usuario
from datetime import date  # Se uso la libreria datetime
print("Este programa le permitira determinar el signo del zodiaco y la edad de una persona")
# Entradas
D, M, A = input("Digite su fecha de nacimiento (dia/mes/año): ").split(" ")
D = int(D)
M = int(M)
A = int(A)
# Caja Negra
D_A = date.today().day  # Dia actual
M_A = date.today().month  # Mes actual
A_A = date.today().year  # Año actual

E = A_A-A
if M <= M_A and D <= D_A:
    E = E
elif M < M_A:
    E = E
else:
    E = E-1

if D >= 22 and M == 11 or D <= 21 and M == 12:
    S = "Sagitario"
elif D >= 22 and M == 12 or D <= 20 and M == 1:
    S = "Capricornio"
elif D >= 21 and M == 1 or D <= 19 and M == 2:
    S = "Acuario"
elif D >= 20 and M == 2 or D <= 19 and M == 3:
    S = "Piscis"
elif D >= 21 and M == 3 or D <= 20 and M == 4:
    S = "Aries"
elif D >= 21 and M == 4 or D <= 21 and M == 5:
    S = "Tauro"
elif D >= 22 and M == 5 or D <= 21 and M == 6:
    S = "Géminis"
elif D >= 22 and M == 6 or D <= 22 and M == 7:
    S = "Cáncer"
elif D >= 23 and M == 7 or D <= 23 and M == 8:
    S = "Leo"
elif D >= 24 and M == 8 or D <= 22 and M == 9:
    S = "Virgo"
elif D >= 23 and M == 9 or D <= 22 and M == 10:
    S = "Libra"
elif D >= 23 and M == 10 or D <= 22 and M == 11:
    S = "Escorpión"
# Salidas
print(f"La edad es: {E} Años")
print(f"El signo zodiacal es: {S}")
