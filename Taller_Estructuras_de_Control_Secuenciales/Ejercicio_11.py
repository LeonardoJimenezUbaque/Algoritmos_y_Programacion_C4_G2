"""
Ejercicio 11
Se conoce de un trabajador su nombre, el número de horas normales trabajadas, el pago de una hora normal y el número de horas extras trabajadas.
Además, que, cada hora extra se paga 25% más del valor de una hora normal. Si se deducen al trabajador sobre el sueldo base 5% del pago forzoso,
2% de política habitacional y 7% para caja de ahorro. Si se le asignan 250.000 COP por actualización académica, 173.000 COP por cada hijo y una
prima por hogar de 180000 COP. Calcule y muestre las asignaciones, las deducciones y el sueldo neto del trabajador para el mes de diciembre.

Entradas
Nombre --> Str --> N
NUmero_Hijos --> Int --> N_H
Numero_Horas_Normales_Trabajadas --> Float --> N_H_N_T
Valor_Hora_Trabajo --> Float --> V_H_T
Numero_Horas_Extra_Trabajadas --> Float --> N_H_E_T

Salidas
Asignaciones --> Float --> A
Deducciones --> Float --> D
Sueldo_Neto --> Float --> S_N
"""
# Instrucciones al usuario
print("Para conocer cuales son las asignaciones, deducciones y el sueldo neto para el mes de diciembre, escriba lo siguiente: ")
# Entradas
N = str(input("Ingrese su nombre: "))
N_H = int(input("Digite su numero de hijos: "))
N_H_N_T = float(input("Digite las horas normales trabajadas: "))
V_H_T = float(input("Digite el valor de la hora normal de trabajo: "))
N_H_E_T = float(input("Digite las horas extra trabajadas: "))
# Caja negra
Sueldo_Normal = V_H_T*N_H_N_T
Valor_Hora_Extra = V_H_T+(V_H_T*0.25)
Horas_Extra_Pago = N_H_E_T*Valor_Hora_Extra
S_C_H_E = Sueldo_Normal+Horas_Extra_Pago  # Sueldo con horas extra
D = (S_C_H_E*0.05+S_C_H_E*0.02+S_C_H_E*0.007)
A = 250000+173000*N_H+180000
S_N = S_C_H_E-D+A
# Salidas
print(f"Estimado {N}")
print("Sus asignaciones son de:", A, "COP")
print(f"Sus deducciones son de: {D}COP")
print(f"Su salario neto corresponde a: {S_N}COP")
