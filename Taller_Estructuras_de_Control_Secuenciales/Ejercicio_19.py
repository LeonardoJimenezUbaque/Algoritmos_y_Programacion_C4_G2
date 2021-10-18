"""
Ejercicio 19
Un mayorista compra a un agricultor un lote de X naranjas a Bs. Y la docena. Después de vender todas las naranjas
a los detallistas, obtiene Bs. K. Calcular el porcentaje de ganancia obtenida en la inversión. Pruebe su programa
con los siguientes valores: X=48000, Y=6, K=42000 para obtener 75% como resultado.

Entradas
Lote_Naranjas_Comprado --> Int --> L_N
Precio_Naranjas_Docena --> Float --> P_N_D
Dinero_Ganado_Venta --> Float --> D_G_V

Salidas
Porcentaje_Ganancia --> Float --> P_G
"""
# Instrucciones al usuario
print("Para conocer el porcentaje de ganancia, escriba lo siguiente: ")
# Entradas
L_N = int(input("Digite el lote de naranjas compradas: "))
P_N_D = float(input("Digite el precio por docena de las naranjas: "))
D_G_V = float(
    input("Digite el dinero obtenido por la venta de las naranjas: "))
# Caja negra
D = L_N/12  # Docenas
G_A = D*P_N_D  # Gastos
G = D_G_V-G_A
P_G = (G/G_A)*100
# Salidas
print(f"El porcentaje de ganancias que se obtiene es de {P_G}%")
