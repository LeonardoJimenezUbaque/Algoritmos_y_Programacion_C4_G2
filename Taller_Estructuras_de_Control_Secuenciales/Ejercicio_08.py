"""
Ejercicio 08
Calcule el área de un triángulo en función de las longitudes de sus lados, utilizan la fórmula:

Entradas
Lado 1 --> Float --> L_1
Lado 2 --> Float --> L_2
Lado 3 --> Float --> L_3

Salidas
Área_Triángulo --> Float --> A_T

"""
# Instrucciones al usuario
print("Para conocer cual es el área de un triágulo, escriba lo siguiente: ")
# Entradas
L_1 = float(input("Digite la medida del lado 1:  "))
L_2 = float(input("Digite la medida del lado 2:  "))
L_3 = float(input("Digite la medida del lado 3:  "))
# Caja Negra
S = (L_1+L_2+L_3)/2  # Semiperímetro
A_T = (S*(S-L_1)*(S-L_2)*(S-L_3))**(1/2)
# Salidas
print(f"El área de su triángulo es de: {A_T} ")
