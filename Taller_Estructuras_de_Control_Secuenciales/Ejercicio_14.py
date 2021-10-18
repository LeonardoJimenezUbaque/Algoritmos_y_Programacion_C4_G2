"""
Ejercicio 14
Calcular y mostrar el monto total a pagar en un mes de luz eléctrica, teniendo como dato la lectura anterior,
la lectura actual y el costo por kilovatio.

Entradas
Lectura_Anterior --> Float --> L_A
Lectura_Actual --> Float --> L_AC
Precio_Kilovatio --> Float --> P_K

Salidas
Cantidad_Pagar --> Float --> C_P
"""
# Instrucciones al usuario
print("Para conocer cuanto dinero debe pagar en un mes de electricidad, escriba lo siguiente: ")
# Entradas
L_A = float(input("Digite la lectura del mes pasado: "))
L_AC = float(input("Digite la lectura actual: "))
P_K = float(input("Digite el costo del kilovatio: "))
# Caja negra
C_P = (L_A-L_AC)*P_K
# Salidas
print(f"El monto a pagar en el mes es de: {C_P}$")
