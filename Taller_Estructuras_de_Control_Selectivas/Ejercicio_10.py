"""
Ejercicio 10
Construya un programa en Python que, dados como datos la categoría y el sueldo bruto del trabajador, calcule el aumento correspondiente
teniendo en cuenta la siguiente tabla:
Categoría     Aumento     Salario bruto
    1           10%       5.000.000 COP
    2           15%       4.300.000 COP
    3           20%       3.600.000 COP
    4           40%       2.000.000 COP
    5           60%         900.000 COP
Como salida, mostrar la categoría del trabajador y su nuevo sueldo bruto.

Entradas
Sueldo_Bruto --> Float --> S_B

Salidas
Categoría --> Int --> C
Sueldo_Neto --> Float --> S_N
"""
# Instrucciones al usuario
print("Para conocer cual sera su sueldo neto, escriba lo siguiente:")
# Entradas
S_B = int(input("Digite su salario bruto: "))
# Caja Negra
if S_B > 5000000:
    S_N = S_B+S_B*0.10
    C = 1
elif S_B > 4300000 and S_B <= 5000000:
    S_N = S_B+S_B*0.15
    C = 2
elif S_B > 3600000 and S_B <= 4300000:
    S_N = S_B+S_B*0.20
    C = 3
elif S_B > 2000000 and S_B <= 3600000:
    S_N = S_B+S_B*0.40
    C = 4
elif S_B > 900000 and S_B <= 2000000:
    S_N = S_B+S_B*0.60
    C = 5
else:
    S_N = "No existe ese sueldo"
    C = "No existe una categoria con ese sueldo"
# Salidas
print(f"Su salario neto corresponde a la categoría {C}, y es de: ${S_N} COP")
