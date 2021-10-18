"""
Ejercicio 04
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.

Entradas
Valor_Compra --> Float --> V_C

Salidas
Descuento --> Float --> D
Total_Pagar --> Float --> T_P
"""
# Instrucciones al usuario
print("Para conocer el descuento sobre el valor de su compra y cuanto debe pagar, escriba lo siguiente: ")
# Entradas
V_C = float(input("Digite el valor de su compra: "))
# Caja Negra
D = V_C*0.15
T_P = V_C-D
# Salidas
print(f"El descuento de su compra es de: {D} ")
print(f"El valor total de su compra con el descuento aplicado es: {T_P}")
