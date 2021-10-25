"""
Ejercicio 07
Una  compañía  de  alquiler  de  automóviles  sin  conductor,  desea  calcular  y mostrar lo que debe pagar cada cliente, de acuerdo a las
siguientes condiciones:
a. Si no se rebasan los 300 km, se cancelan 50.000 COP.
b. Si la distancia recorrida es superior a 300 km
    b.1. Pero inferior a 1.000 km se cobran 70.000 COP más 30.000 COP por cada kilómetro superior a 300 km.
    B.2. Si es superior a 1.000 km se cobran 150.000 COP más 9.000 COP por cada kilómetro adicional.

Entradas
Distancia_Recorrida --> Float --> D_R

Salidas
Monto_Pagar --> Float --> M_P
"""
# Instrucciones al usuario
print("Este programa le permitira calcular el monto a pagar por la distancia conducida en un automovil alquilado")
# Entradas
D_R = float(input(f"Digite los kilómetros recorridos: "))
# Caja Negra
if D_R <= 300:
    M_P = 50000
elif D_R > 300 and D_R < 1000:
    M_P = 70000+(D_R-300)*30000
else:
    M_P = 150000+(D_R-1000)*9000
# Salidas
print(f"Su monto a pagar es: ${M_P} COP")
