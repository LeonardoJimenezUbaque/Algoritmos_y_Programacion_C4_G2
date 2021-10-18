"""
Ejercicio 20
Un comerciante de computadores ofrece P precio por compra al contado ó 12 cuotas de T COP cada una. Desarrolle
un programa para calcular y mostrar cuál es el porcentaje que se cobra por el recargo en el pago del computador
por cuota.

Entradas
Precio_Compra_Contado --> Float --> P_C_C
Precio_Cuotas --> Float --> P_C

Salidas
Porcentaje_Recargo --> Float --> P_R
"""
# Instrucciones al usuario
print("Para conocer el porcentaje de recargo en el pago a cuotas, escriba lo siguiente: ")
# Entradas
P_C_C = float(input("Digite el precio del computador pagando de contado: "))
P_C = float(input("Digite el precio de cada cuota: "))
# Caja negra
T_C = P_C*12  # Total cuotas
Diferencia = T_C-P_C_C
P_R = (Diferencia*100)/P_C_C
# Salidas
print(f"El porcentaje de recargo pagando a cuotas es de: {P_R}%")
