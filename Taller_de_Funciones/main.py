"""
Taller de Funciones
"""


frutas = open("C:/Users/jimen/Desktop/U EAN/Semestre 2/Algoritmos y Programación/Algoritmos_y_Programacion_C4_G2/Taller_de_Funciones/frutas.txt", "r")
numeros = open("C:/Users/jimen/Desktop/U EAN/Semestre 2/Algoritmos y Programación/Algoritmos_y_Programacion_C4_G2/Taller_de_Funciones/numeros.txt", "r")


# Llenar las lista con los datos del archivo frutas.txt
lista_frutas = []
for i in frutas:
    lista_frutas.append(i)
# print(lista_frutas)


# Llenar las lista con los datos del archivo numeros.txt
lista_numeros = []
for i in numeros:
    lista_numeros.append(i)
# print(lista_numeros)


# Ejercicio 01: Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
Entradas:
Lista(str) --> List --> lista
Caracter --> Str --> caracter

Salidas:
Lista(str) --> List --> lista_sin_caracter
"""

"""
def eliminar_un_caracter_de_toda_la_lista(lista: list, caracter: str) -> list:
    lista_aux = []
    for i in lista:
        a = i.replace(caracter, "")
        lista_aux.append(a)
    return lista_aux


if __name__ == "__main__":
    a = eliminar_un_caracter_de_toda_la_lista(lista_frutas, "\n")
    print(f"{a}\n")
    b = eliminar_un_caracter_de_toda_la_lista(lista_numeros, "\n")
    print(f"{b}\n")
"""

# Ejercicio 02: Realizar una funcion que retorne la copia de una funcion que pasa por parametro
"""
Entradas:
Lista(str) --> List --> lista

Salidas:
Lista_copia(str) --> List --> lista_copia
"""

"""
def copia_lista(lista: list) -> list:
    lista_copia = lista.copy()
    return lista_copia


if __name__ == "__main__":
    a = copia_lista(lista_frutas)
    print(f"{lista_frutas}\n")  # Lista original
    print(f"{a}\n")  # Lista copia
    b = copia_lista(lista_numeros)
    print(f"{lista_numeros}\n")  # Lista original
    print(f"{b}\n")  # Lista copia
"""

# Ejercicio 03: Realizar una funcion que retorne una lista de numeros enteros
"""
Entradas:
Lista(str) --> List --> lista

Salidas:
Lista_enteros(str) --> List --> lista_enteros
"""

"""
def numeros_enteros(lista: list) -> list:
    lista_aux = []
    for i in lista:
        lista_aux.append(int(float(i)))
    return lista_aux  # RetornaUnaLista


if __name__ == "__main__":
    a = numeros_enteros(lista_numeros)
    print(f"{a}\n")
"""

# Ejercicio 03.1: Realizar una funcion que retorne una lista de numeros enteros pares
"""
Entradas:
Lista(str) --> List --> lista

Salidas:
Lista_enteros_pares(str) --> List --> lista_enteros_pares
"""

"""
def numeros_pares(lista: list) -> list:
    lista_aux = []
    for i in lista:
        if(float(i) % 2 == 0):
            lista_aux.append(int(float(i)))
    return lista_aux  # RetornaUnaLista


if __name__ == "__main__":
    a = numeros_pares(lista_numeros)
    print(f"{a}\n")
"""

# Ejercicio 04: Realizar una funcion que elimine un elemento de una lista
"""
Entradas:
Lista(str) --> List --> lista
Elemento --> Str --> elemento

Salidas:
Lista_sin_elemento(str) --> List --> lista_sin_elemento
"""

"""
def elimina_elemento_lista(lista: list, elemento: str) -> list:
    for i in lista:
        if i == elemento:
            lista.remove(elemento)
    return lista # RetornaUnaLista


if __name__ == "__main__":
    a = elimina_elemento_lista(lista_frutas, "Arandano\n")
    print(f"{a}\n")
    b = elimina_elemento_lista(lista_numeros, "123\n")
    print(f"{b}\n")
"""

# Ejercicio 05: Retorna una lista con las palabras iniciales con la letra que pasa por parametro
"""
Entradas:
Lista(str) --> List --> lista
Letra --> Str --> letra

Salidas:
Lista_palabras_iniciales_letra(str) --> List --> lista_palabras_iniciales_letra
"""

"""
def letra(lista: list, letra: str) -> list:
    lista_aux = []
    for i in lista:
        if i[0] == letra:
            lista_aux.append(i)
    return lista_aux


if __name__ == "__main__":
    a = letra(lista_frutas, "A")
    print(f"{a}\n")
"""

# Ejercicio 06: Realizar una funcion que retorne el tamaño de una lista
"""
Entradas:
Lista(str) --> List --> lista

Salidas:
Tamaño_lista --> Int --> tamaño
"""

"""
def tamano_lista(lista: list) -> list:
    tamaño = len(lista)
    return tamaño  # RetornaUnEntero


if __name__ == "__main__":
    a = tamano_lista(lista_frutas)
    print(f"{a}\n")
    b = tamano_lista(lista_numeros)
    print(f"{b}\n")
"""

# Ejercicio 07: Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas:
Lista(str) --> List --> lista

Salidas:
Tamaño_lista --> Int --> tamaño
Tipo_datos --> Str --> tipo_dato
"""

"""
def informacion_lista(lista: list):
    tamaño = len(lista)
    tipo_dato = type(lista[0])
    return tamaño, tipo_dato


if __name__ == "__main__":
    a = informacion_lista(lista_frutas)
    print(f"{a}\n")
    b = informacion_lista(lista_numeros)
    print(f"{b}\n")
"""

# Ejercicio 08: Retornar una lista con los numero negativos
"""
Entradas:
Lista(str) --> List --> lista

Salidas:
Numeros_negativos --> Int --> numeros_negativos
"""

"""
def numeros_negativos(lista: list) -> int:
    lista_aux = []
    for i in lista:
        if(i[0] == "-"):
            lista_aux.append(int(float(i)))
    return lista_aux


if __name__ == "__main__":
    a = numeros_negativos(lista_numeros)
    print(f"{a}\n")
"""

# Ejercicio 09: Realizar una funcion que retorne la posicion de un elemento que pasa por parametro
"""
Entradas:
Lista(str) --> List --> lista
Elemento --> Str --> elemento

Salidas:
Posicion_parametro --> Int --> posicion_parametro
"""

"""
def posicion_elemento(lista: list, elemento: str) -> int:
    posicion = 0
    for i in lista:
        if elemento == i:
            posicion += 1
            break
        else:
            posicion += 1
    return posicion


if __name__ == "__main__":
    a = posicion_elemento(lista_frutas, "Kiwi\n")
    print(f"{a}\n")
    b = posicion_elemento(lista_numeros, "-132\n")
    print(f"{b}\n")
"""

# Ejercicio 10: Realizar una funcion que agregue al final de archivo frutas una fruta
"""
Entradas:
Lista(str) --> List --> lista
Elemento_agregar --> Str --> elemento

Salidas:
Lista_elemento_agregado --> Int --> lista_elemento_agregado
"""

"""
def frutas(lista: list, elemento: str) -> list:
    l_mod = open("C:/Users/jimen/Desktop/U EAN/Semestre 2/Algoritmos y Programación/Algoritmos_y_Programacion_C4_G2/Taller_de_Funciones/frutas.txt", "a")
    l_mod.write(elemento)
    l_mod.close()


if __name__ == "__main__":
    a = frutas(lista_frutas, "\nGranadilla")
    print(f"{a}\n")
"""

# Ejercicio 11: Realizar una funcion que cuente el numero de veces que se repite un elemento
"""
Entradas:
Lista(str) --> List --> lista
Elemento --> Str --> elemento

Salidas:
Elemento_repetido --> Int --> elemento_repetido
"""

"""
def repetir(lista: list, elemento: str) -> int:
    elemento_reptido = 0
    for i in lista:
        if i == elemento:
            elemento_reptido += 1
    return elemento_reptido


if __name__ == "__main__":
    a = repetir(lista_frutas, "Kiwi\n")
    print(f"{a}\n")
    b = repetir(lista_numeros, "-2\n")
    print(f"{b}\n")
"""

frutas.close()
numeros.close()
