"""
Ejercicio 01
Un hombre desea saber cuánto dinero se generará por concepto de intereses sobre la cantidad que tiene en inversión en el banco. El decidirá
reinvertir los intereses siempre y cuando éstos excedan a $100.000 COP y en ese caso, desea saber cuánto dinero tendrá finalmente en su cuenta.

Entradas
Inversión_Banco --> Float --> I_B
Tasa_Interés --> Float --> T_I

Salidas
Dinero_Final --> Float --> D_F
"""
# Instrucciones al usuario
print("Este programa le permitira conocer cuanto dinero se generará por concepto de intereses de una inversión en un banco")
# Entradas
I_B = float(input("Digite su inversión en el banco: "))
T_I = float(input("Digite su tasa de interes (Ejemplo 0.15): "))
# Caja Negra y Salidas
I = I_B*T_I  # Interés
D_F = I_B+I
if I > 100000:
    print(
        f"Sus intereses generados son mayores a 100000 COP, son: {I} COP  ¡Puede reinvertir!")
else:
    print(f"Sus intereses generados son menores a 100000 COP, son: {I} COP")
print(f"Su dinero final en la cuenta es de: ${D_F} COP")
