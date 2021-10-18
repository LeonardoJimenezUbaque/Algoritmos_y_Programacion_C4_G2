"""
Ejercicio 16
Resuelva el problema que tienen en una gasolinera. Los surtidores de la misma registran lo que surten en
galones, pero el precio de la gasolina está fijado en litros. Se requiere que calcule y muestre lo que hay que
cobrarle a un cliente, considerando que: (a) cada galón tiene 3.785 litros; (b) el precio del litro es de 50.000 COP

Entradas
Galones --> Float --> G

Salidas
Precio_Galones --> Float --> P
"""
# Instrucciones al usuario
print("Para conocer el precio que va a ser cobrado, escriba lo siguiente: ")
# Entradas
G = float(input("Digite número de galones: "))
# Caja negra
P = G*3.785*50000
# Salidas
print(f"El cliente debe pagar: {P}COP")
