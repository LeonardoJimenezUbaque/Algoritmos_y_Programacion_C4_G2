"""
Ejercicio 05
Una empresa que comercializa cosméticos tiene organizados a sus vendedores en tres departamentos y ha establecido un programa de incentivos
para incrementar su productividad. El gerente, al final del mes, pide el importe global de las ventas de los tres departamentos y aquellos
que excedan el 33% de las ventas totales se les paga una cantidad extra equivalente al 20% de su salario bruto mensual. Si todos los vendedores
ganan lo mismo, determinar cuánto recibirán los vendedores de los tres departamentos al finalizar el mes.

Entradas
Sueldo_Vendedores --> Float --> S_V
Ventas_Departamento_1 --> Float --> V_D_1
Ventas_Departamento_2 --> Float --> V_D_2
Ventas_Departamento_3 --> Float --> V_D_3

Salidas
Sueldo_Vendedores_Departamento_1 ---> Float --> S_V_D_1
Sueldo_Vendedores_Departamento_2 ---> Float --> S_V_D_2
Sueldo_Vendedores_Departamento_3 ---> Float --> S_V_D_3
"""
# Instrucciones al usuario
print("Este programa le permitira calcular el sueldo de los trabajadores de 3 departamentos y la aplicacion de un estimulo en el salario")
# Entradas
S_V = float(input(f"Digite el sueldo bruto de los vendedores: "))
V_D_1 = int(input(f"Digite el total de ventas del departamento 1: "))
V_D_2 = int(input(f"Digite el total de ventas del departamento 2: "))
V_D_3 = int(input(f"Digite el total de ventas del departamento 3: "))

# Caja Negra
T_V_D = V_D_1+V_D_2+V_D_3  # Total ventas de los 3 departamentos
I = T_V_D*0.33  # Monto de ventas que se debe superar para obtener el incentivo
if V_D_1 > I:
    S_V_D_1 = S_V+S_V*0.20
else:
    S_V_D_1 = S_V
if V_D_2 > I:
    S_V_D_2 = S_V+S_V*0.20
else:
    S_V_D_2 = S_V
if V_D_3 > I:
    S_V_D_3 = S_V+S_V*0.20
else:
    S_V_D_3 = S_V
# Salidas
print(
    f"El sueldo neto de los vendedores del departamento 1 será de: ${S_V_D_1}")
print(
    f"El sueldo neto de los vendedores del departamento 2 será de: ${S_V_D_2}")
print(
    f"El sueldo neto de los vendedores del departamento 3 será de: ${S_V_D_3}")
