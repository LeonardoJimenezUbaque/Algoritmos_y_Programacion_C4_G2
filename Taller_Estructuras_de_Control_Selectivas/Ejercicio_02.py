"""
Ejercicio 02
Escriba  un  algoritmo,  que  dado  como  dato  el  sueldo  de  un  trabajador,  le aplique un aumento del 15% si su salario bruto es inferior
a $900.000 COP y 12% en caso contrario. Imprima el nuevo sueldo del trabajador.

Entradas
Sueldo_Bruto --> Float --> S_B

Salidas
Sueldo_Neto --> Float --> S_N
"""
# Instrucciones al usuario
print("Este programa le permitira determinar el sueldo neto de un trabajador aplicando un aumento")
# Entradas
S_B = float(input(f"Digite su salario bruto: "))
# Caja Negra
if(S_B < 900000):
    S_N = S_B*0.15+S_B
else:
    S_N = S_B*0.12+S_B
# Salidas
print(f"Su salario neto es de: ${S_N} COP")
