"""
Ejercicio 18
Calcule qué tanto por ciento anual cobraron por un préstamo de Bolívares X, si se pagaron Bolívares Y de intereses
en 4 años. La fórmula del interés es: I= CAPITAL TIEMPO RAZON / 100

Entradas
Prestamo_Bolivares --> Float --> P_B_X
Intereses_Bolivares --> Float --> I_B_Y

Salidas
Porcentaje_Anual_Cobro --> Float --> I
"""
# Instrucciones al usuario
print("Para conocer el porcentaje de interes que se cobro anualmente para el prestamo, escriba lo siguiente: ")
# Entradas
P_B_X = float(input("Digite valor del prestamo: "))
I_B_Y = float(input("Digite valor de los intereses pagados: "))
# Caja negra
I = (I_B_Y*100)/(P_B_X*4)
# Salidas
print(f"El porcentaje de interes cobrado anualmente corresponde a: {I}%")
