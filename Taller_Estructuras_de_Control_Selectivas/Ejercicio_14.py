"""
Ejercicio 14
Desarrolle  un  programa  en  Python  que  calcule  y  muestre  el  monto  que  debe pagar un suscriptor por concepto de consumo de luz eléctrica
y servicio de aseo urbano. Dicho monto se calcula multiplicando la diferencia de la lectura anterior y la lectura actual por el costo de cada
Kilovatio hora, según la siguiente escala:

0 ­- 100 --> 4.600 COP/Kwh
101 - 300 --> 80.00 COP/Kwh
301 - 500 --> 100.000 COP /Kwh
501 - en Adelante --> 120.000 COP/Khw

Entradas
Lectura_Anterior --> Float --> L_AN
Lectura_Actual --> Float --> L_AC

Salidas
Monto_Pagar --> Float --> M_P
"""
# Instrucciones al usuario
print("Este programa le permitira calcular el monto que debe pagar por concepto de luz eléctrica y servicio de aseo urbano")
# Entradas
L_AN = float(input("Digite la lectura anterior: "))
L_AC = float(input("Digite la lectura actual: "))
# Caja negra
if (L_AN >= 0 and L_AC <= 100):
    M_P = (L_AC-L_AN)*4600
elif (L_AN >= 101 and L_AC <= 300):
    M_P = (L_AC-L_AN)*80000
elif (L_AN >= 301 and L_AC <= 500):
    M_P = (L_AC-L_AN)*100000
else:
    (L_AN >= 501 and L_AC > 501)
    M_P = (L_AC-L_AN)*120000
# Salidas
print(f"El monto que debe pagar por servicios de luz y aseo es de: {M_P}")
