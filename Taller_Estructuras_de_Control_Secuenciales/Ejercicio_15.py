"""
Ejercicio 15
Dados como datos el precio final pagado por un producto y su precio de venta al público (PVP), se requiere
que calcule y muestre el porcentaje de descuento que le ha sido aplicado.

Entradas
Precio_Final_Pagado --> Float --> P_F
Precio_Venta_Publico --> Float --> P_V_P

Salidas
Porcentaje_Descuento --> Float --> P_D
"""
# Instrucciones al usuario
print("Para conocer el porcentaje de descuento, escriba lo siguiente: ")
# Entradas
P_F = float(input("Digite el precio final pagado por el producto: "))
P_V_P = float(input("Digite el precio de venta al público del producto: "))
# Caja negra
P_D = ((P_V_P-P_F)/P_V_P)*100
# Salidas
print(f"El porcentaje de descuento aplicado es de: {P_D}%")
