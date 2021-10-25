"""
Ejercicio 04
Una empresa quiere hacer una compra de varias piezas de la misma clase a un fabricante de refacciones. La empresa dependiendo del monto total de
la compra, decidirá qué hacer para pagar al fabricante. Si el monto total de la compra excede de $5.000.000 COP la empresa tendrá la capacidad
de invertir de su propio dinero un 55% del monto de la compra, pedir prestado al banco un 30% y el resto lo pagará solicitando un crédito
al fabricante. Si el monto total de la compra no excede de $5.000.000 COP la empresa tendrá capacidad de invertir de su propio dinero
un 70% y el restante 30% lo pagará solicitando crédito al fabricante. El fabricante cobra por concepto de intereses un 20% sobre la cantidad
que se le pague a crédito. Calcule y muestre la cantidad a invertir de los fondos de la empresa, la  cantidad a pagar a crédito, el monto a
pagar por intereses y si es necesario, la cantidad prestada po el banco.

Entradas
Costo_Pieza --> Float --> C_P
Cantidad_Piezas --> Int --> C_PI

Salidas
Cantidad_Inversión_Empresa --> Float --> C_I_E
Cantidad_Pagar_Credito --> Float --> C_P_C
Cantidad_Pagar_Intereses --> Float --> C_P_I
Cantidad_Pagar_Banco --> Float --> C_P_B
"""
# Instrucciones al usuario
print("Este programa le permitira determinar como una empresa debe pagar una compra de piezas de refacción")
# Entradas
C_P = float(input(f"Digite el costo por una pieza: "))
C_PI = int(input(f"Digite la cantidad de piezas: "))
# Caja Negra
C_T = C_P*C_PI  # Costo total compra
if C_T > 5000000:
    C_I_E = C_T*0.55
    C_P_C = C_T*0.15
    C_P_I = C_P_C*0.20
    C_P_B = C_T*0.30
else:
    C_I_E = C_T*0.70
    C_P_C = C_T*0.30
    C_P_I = C_P_C*0.20
    C_P_B = 0
# Salidas
print(f"Dinero a invertir de los fondos de la empresa es de: ${C_I_E} COP")
print(f"Dinero a solicitar a crédito con el fabricante es de: ${C_P_C} COP")
print(f"Dinero a pagar de intereses por el crédito es de: ${C_P_I} COP")
print(f"Dinero a pedir prestado al banco es de: ${C_P_B} COP")
