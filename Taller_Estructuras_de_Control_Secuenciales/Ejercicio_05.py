"""
Ejercicio 05
Un alumno desea saber cuál será su calificación final en la materia de computación. Dicha calificación se compone de los siguientes porcentajes:
55% del promedio de sus tres calificaciones parciales, 30% de la calificación del examen final y 15% de la calificación de un trabajo final.

Entradas
Nota_Parcial_1 --> Float --> NP_1
Nota_Parcial_2 --> Float --> NP_2
Nota_Parcial_3 --> Float --> NP_3
Nota_Examen_Final --> Float --> NEF
Nota_Trabajo_Final --> Float --> NTF

Salidas
Calificacion_Final_Computacion --> Float --> CFC

"""
# Instrucciones al usuario
print("Para conocer cual sera su nota final, escriba lo siguiente: ")
# Entradas
NP_1 = float(input("Nota del primer parcial: "))
NP_2 = float(input("Nota del segundo parcial: "))
NP_3 = float(input("Nota del tercer parcial: "))
NEF = float(input("Nota del examen final: "))
NTF = float(input("Nota del trabajo final: "))
# Caja Negra
P_P = ((NP_1+NP_2+NP_3)/3)*0.55  # Procentaje Parciales
P_E_F = NEF*0.3  # Porcentaje Examen Final
P_T_F = NTF*0.15  # Porcentaje Trabajo Final
CFC = P_P+P_E_F+P_T_F
# Salidas
print(f"Su calificación final en la materia de computación es: {CFC}")
