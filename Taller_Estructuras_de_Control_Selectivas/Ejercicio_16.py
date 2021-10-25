"""
Ejercicio 16
Confeccionar un algoritmo que permita resolver una ecuación de segundo grado, de la forma: AX^2 + BX + C = 0, sabiendo que el discriminante (D)
se calcula con la fórmula: D = Bˆ2­ - 4 * A *C. El valor obtenido se evalúa y se aplica la fórmula correspondiente, según muestra la siguiente tabla:

Valor de la discriminante                Fórmula a utilizar
Si D = 0  entonces                      X1 =  X2  =  -­B/(2*a)
Si D > 0  entonces                 X1 = (-­B + SQRT(Bˆ2­4*A*C))/(2*A)
Si D > 0  entonces                  X2 = (-­B ­ SQRT(Bˆ2­4*A*C))/(2*A)
Si D < 0  entonces                 No tiene solución en los Reales.

Entradas
A --> Float --> A
B --> Float --> B
C --> Float --> C

Salidas
X1 --> Float --> X1
X2 --> Float --> X2
"""
# Instrucciones al usuario
print("Este programa le permitira resolver una ecuación de segundo grado")
# Entradas
A, B, C = input(
    f"Digite los valores de A,B,C correspondientemente: ").split(" ")
A = float(A)
B = float(B)
C = float(C)
# Caja Negra
D = (B**2)-4*A*C  # Discriminante
if D == 0:
    X1 = X2 = -B/(2*A)
elif D > 0:
    X1 = (-B+(B**2-4*A*C)**(0.5))/(2*A)
    X2 = (-B-(B**2-4*A*C)**(0.5))/(2*A)
else:
    X1 = X2 = "No tiene solución en los reales"
# Salida
print(f"El valor de X1 corresponde a: {X1}")
print(f"El valor de X2 corresponde a: {X2}")
