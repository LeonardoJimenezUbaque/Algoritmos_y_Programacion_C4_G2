"""
Ejercicio 02
Suponga que un individuo decide invertir su capital en un banco y desea saber cuánto dinero ganará
después de un mes si el banco paga a razón de 2% mensual.

Entradas
Capital_Inversion --> Float --> C_I

Salidas
Ganancia_2% --> Float --> G
Ganancia_Total --> Float --> G_T
"""
# Instrucciones al usuario
print("Para conocer cuanto ganara inviertiendo su capital a razón de un 2% en un mes, siga las siguientes instrucciones")
# Entradas
C_I = float(input("Digite el capital a invertir: "))
# Caja Negra
G = C_I*0.02
G_T = G+C_I
# Salidas
print(f"Su ganacia en un mes a razón de un 2% sera de: {G}$")
# La ganacia total se compone del capital invertido + la ganancia a razón de un 2%
print(f"Su ganancia total en un mes sera de: {G_T}$")
