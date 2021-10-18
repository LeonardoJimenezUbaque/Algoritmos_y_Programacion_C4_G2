"""
Ejercicio 03
Un vendedor recibe un sueldo base, más un 10% extra por comisiones de sus ventas. El vendedor desea saber cuánto dinero obtendrá por concepto de
comisiones por las tres ventas que realizó en el mes y el total que recibirá tomando en cuenta su sueldo base y sus comisiones.

Entradas
Sueldo_Base --> Float --> S_B
Venta_1 --> Float --> V_1
Venta_2 --> Float --> V_2
Venta_3 --> Float --> V_3

Salidas
Comision_Ventas --> Float --> C_V
Dinero_Total --> Float --> D_T
"""
# Instrucciones al usuario
print("Para conocer cuanto ganara en comisones y su sueldo total en el mes, escriba lo siguiente: ")
# Entradas
S_B = float(input("Digite el sueldo base: "))
print("Valor de las ventas realizadas en el mes (3): ")
V_1 = float(input("Venta 1: "))
V_2 = float(input("Venta 2: "))
V_3 = float(input("Venta 3: "))
# Caja Negra
C_V = (V_1+V_2+V_3)*0.1
D_T = C_V+S_B
# Salidas
print(f"Su dinero por comisiones de venta durante el mes es: {C_V}$")
print(f"El dinero total que recibira en el mes es: {D_T}$")
