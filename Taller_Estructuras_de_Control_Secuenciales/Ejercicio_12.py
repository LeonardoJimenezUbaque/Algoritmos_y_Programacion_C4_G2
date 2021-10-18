"""
Ejercicio 12
Calcule y muestre, a un alumno, cuál será su promedio general en las tres materias más difíciles que cursa y cuál será el promedio que obtendrá en
cada una de ellas. Estas materias se evalúan como se muestra a continuación:
Matemática		Examen 90%  y	10% del promedio de tres tareas.
Física	    	Examen 80%  y	20% del promedio de dos tareas.
Química	       Examen 85%  y	15% del promedio de tres tareas.


Entradas
Examen_Matemáticas --> Float-->E_M
Tarea_Matemáticas_1 --> Float-->T_M_1
Tarea_Matemáticas_2 --> Float-->T_M_2
Tarea_Matemáticas_3 --> Float-->T_M_3
Examen_Física --> Float-->E_F
Tarea_Física_1 --> Float-->T_F_1
Tarea_Física_2 --> Float-->T_F_2
Examen_Química --> Float-->E_Q
Tarea_Química_1 --> Float-->T_Q_1
Tarea_Química_2 --> Float-->T_Q_2
Tarea_química_3 --> Float-->T_Q_3

Salidas
Promedio_Matemáticas --> Float-->´P_M
Promedio_Física --> Float--> P_F
Promedio_Química --> Float--> P_Q
Promedio_General --> Float--> P_G
"""
# Instrucciones al usuario
print("Para conocer cuales son los promedioS en las materias, escriba lo siguiente: ")
# Entradas
E_M = float(input("Digite la nota del examen de matemáticas: "))
T_M_1 = float(input("Digite la nota de la tarea de matemáticas 1: "))
T_M_2 = float(input("Digite la nota de la tarea de matemáticas 2: "))
T_M_3 = float(input("Digite la nota de la tarea de matemáticas 3: "))
E_F = float(input("Digite la nota del examen de física: "))
T_F_1 = float(input("Digite la nota de la tarea de física 1: "))
T_F_2 = float(input("Digite la nota de la tarea de física 2: "))
E_Q = float(input("Digite la nota del examen de química: "))
T_Q_1 = float(input("Digite la nota de la tarea de química 1: "))
T_Q_2 = float(input("Digite la nota de la tarea de química 2: "))
T_Q_3 = float(input("Digite la nota de la tarea de química 3: "))
# Caja negra
P_M = (((T_M_1+T_M_2+T_M_3)/3)*0.10)+(E_M*0.90)
P_F = E_F*0.80+((T_F_1+T_F_2)/2)*0.20
P_Q = E_Q*0.85+((T_Q_1+T_Q_2+T_Q_3)/3)*0.15
P_G = (P_M+P_F+P_Q)/3
# Salidas
print(f"El promedio en matemáticas es de: {P_M}")
print(f"El promedio en física es de: {P_F}")
print(f"El promedio en química es de: {P_Q}")
print(f"El promedio general es de: {P_G}")
