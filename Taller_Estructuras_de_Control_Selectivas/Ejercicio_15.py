"""
Ejercicio 15
Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos, un médico determina si una persona tiene anemia o no, lo cual
depende de su nivel de hemoglobina en la sangre, de su edad y de su sexo. Si el nivel de hemoglobina que tiene una persona es menor que el rango
que le corresponde, se determina su resultado como positivo y en caso contrario como negativo. La tabla en la que el médico se basa para obtener
el resultado es la siguiente:
EDAD                                                        NIVEL DE HEMOGLOBINA
0 meses - ­1 mes                                                13 - 26    g%
Mayor de 1 mes y menor o igual de 6 meses                      10 - 18    g%
Mayor de 6 meses y menor o igual de 12 meses                   11 - 15    g%
Mayor de 1 año  y menor o  igual que  5 años                   11.5 - 15    g%
Mayor de  5 año y  menor o  igual  que 10  años                12.6 - 15.5  g%
Mayor de  10 año  y  menor o  igual  que  15  años             13 - 15.5   g%
Mujeres  mayores  de  15  años                                 12 - 16    g%
Hombres  mayores  de  15  años                                 14 - 18    g%
Desarrolle  un  algoritmo  que  indique,  si  una  persona  tiene  Anemia  o  no.

Entradas
Edad --> Int --> E
Sexo --> Str --> S
Nivel_Hemoglobina --> Float --> N_H

Salidas
Resultado_Anemia --> Str --> R_A
"""
# Instrucciones al usuario
print("Este programa le permitira diagnosticar si una persona tiene o no anemia")
# Entradas
E = int(input("Digite la edad en meses: "))
N_H = float(input("Digite el nivel de hemoglobina en g%: "))
if E > 180:
    S = str(input("¿Cuál es el sexo? (Responda Hombre con 1 o Mujer con 2): "))
else:
    S = 0
S = int(S)
# Caja negra
if E >= 0 and E <= 1:
    if N_H >= 13 and N_H <= 26:
        R_A = "negativo"
    elif N_H < 13:
        R_A = "Positivo"
    else:
        N_H > 26
        R_A = "Error"
elif E > 1 and E <= 6:
    if N_H >= 10 and N_H <= 18:
        R_A = "Negativo"
    elif N_H < 10:
        R_A = "Positivo"
    else:
        N_H > 18
        R_A = "Error"
elif E > 6 and E <= 12:
    if N_H >= 11 and N_H <= 15:
        R_A = "Negativo"
    elif N_H < 11:
        R_A = "Positivo"
    else:
        N_H > 15
        R_A = "Error"
elif E > 12 and E <= 60:
    if N_H >= 11.5 and N_H <= 15:
        R_A = "Negativo"
    elif N_H < 11.5:
        R_A = "Positivo"
    else:
        N_H > 15
        R_A = "Error"
elif E > 60 and E <= 120:
    if N_H >= 12.6 and N_H <= 15.5:
        R_A = "Negativo"
    elif N_H < 12.6:
        R_A = "positivo"
    else:
        N_H > 15.5
        R_A = "Error"
elif E > 120 and E <= 180:
    if N_H >= 13 and N_H <= 15.5:
        R_A = "Negativo"
    elif N_H < 13:
        R_A = "Positivo"
    else:
        N_H > 15.5
        R_A = "Error"
elif E > 180 and S == 2:
    if N_H >= 12 and N_H <= 16:
        R_A = "Negativo"
    elif N_H < 12:
        R_A = "Positivo"
    else:
        N_H > 16
        R_A = "Error"
elif E > 180 and S == 1:
    if N_H >= 14 and N_H <= 18:
        R_A = "Negativo"
    elif N_H < 14:
        R_A = "Positivo"
    else:
        N_H > 18
        R_A = "Error"
# Salidas
print(f"Su diagnostico para anemia es: {R_A}")
