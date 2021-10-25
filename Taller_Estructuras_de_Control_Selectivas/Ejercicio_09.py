"""
Ejercicio 09
En una tienda efectúan un descuento a los clientes dependiendo del monto de la compra. El descuento se efectúa con base en el siguiente criterio:
a. Si el monto es inferior a $50.000 COP, no hay descuento.
b. Si  está comprendido entre $50.000 COP y $100.000 COP inclusive, se hace un descuento del 5%
c. Si está comprendido entre $100.000 COP y $700.000 COP inclusive, se  hace  un  descuento del 11%
d. Si está comprendido entre $700.000 COP y $1.500.000 COP inclusive, el descuento es del 18%
e. Si el monto es mayor a $1.500.000., hay un 25% de descuento.
Calcule y muestre el nombre del cliente, el monto de la compra, monto a pagar y descuento recibido.

Entradas
Nombre_Cliente --> Str --> N
Monto_Compra --> Float --> M_C

Salidas
Nombre_Cliente --> Str --> N
Monto_Compra --> Float --> M_C
Descuento --> Float --> D
Monto_Pagar --> Float --> M_P
"""
# Instrucciones al usuario
print("Este programa le permitira conocer el descuento efectuado y el monto a pagar en una tienda")
# Entradas
N = str(input(f"Digite su nombre: "))
M_C = float(input(f"Digite el monto de su compra: "))
# Caja Negra
if M_C < 50000:
    D = M_C*0
    d = "0%"
    M_P = M_C - D
elif M_C >= 50000 and M_C < 100000:
    D = M_C*0.05
    d = "5%"
    M_P = M_C - D
elif M_C >= 100000 and M_C < 700000:
    D = M_C*0.11
    d = "11%"
    M_P = M_C - D
elif M_C >= 700000 and M_C < 1500000:
    D = M_C*0.18
    d = "18%"
    M_P = M_C - D
else:
    D = M_C*0.25
    d = "18%"
    M_P = M_C - D
# Salidas
print(f"Estimado {N}")
print(f"EL monto de su compra es de: {M_C} COP")
print(f"Se ha aplicado un descuento de {d} equivalente a: {D} COP")
print(f"EL monto que debe pagar es de: {M_P} COP")
