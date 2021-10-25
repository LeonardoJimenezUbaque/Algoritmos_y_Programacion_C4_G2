"""
Ejercicio 11
Desarrolle un algoritmo, que dado como dato una temperatura en grados Fahrenheit, determine el deporte que es apropiado practicar a esa
temperatura, teniendo en cuenta la siguiente tabla:
Deporte          Temperatura
Natación         Temp.  >  85
Tenis          70 < Temp. <= 85
Golf           32 < Temp. <= 70
Esquí          10 < Temp. <= 32
Marcha           Temp.  <= 10

Entradas
Temperatura --> Float --> T

Salidas
Deporte --> Str --> D
"""
# Instrucciones al usuario
print("Este programa le permitira determinar el deporte apropiado para practicar dada la temperatura")
# Entradas
T = float(input("Digite la temperatura: "))
# Caja Negra
if T > 85:
    D = "Natación"
elif T > 70 and T <= 85:
    D = "Tenis"
elif T > 32 and T <= 70:
    D = "Golf"
elif T > 10 and T <= 32:
    D = "Esquí"
elif T >= 0 and T <= 10:
    D = "Marcha"
else:
    D = "No se ha encontrado un deporte"
# Salidas
print(f"El deporte apropiado para practicar es: {D}")
