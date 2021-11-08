archivo = open("C:/Users/jimen/Desktop/U EAN/Semestre 2/Algoritmos y Programación/Algoritmos_y_Programacion_C4_G2/Taller_Estructuras_de_Control_For/paises.txt", "r")

# Ejemplo 01 = Imprima la posicion de colombia
"""
c = 0
lista = []
for i in archivo:
    lista.append(i)
    a = " ".join(lista)
    c = c+1
    if(a == "Colombia: Bogota \n"):
        break
    lista = []
print(c)
"""

# Ejemplo 02 = Imprima todos los paises
"""
lista = []
for i in archivo:
    a = i.index(":")
    for r in range(0, a):
        lista.append(i[r])
    a = "".join(lista)
    print(a)
    lista = []
"""

# Ejemplo 03 = Imprima todas las Capitales
"""
lista = []
for i in archivo:
    a = i.index(":")
    for r in range(a+2, len(i)):
        lista.append(i[r])
    a = "".join(lista)
    print(a)
    lista = []
"""

# Ejemplo 04 = Imprimir todos los paises que inicien con la letra C
"""
lista = []
paises = []
for i in archivo:
    a = i.index(":")
    for r in range(0, a):
        lista.append(i[r])
    a = "".join(lista)
    paises.append(a)
    lista = []
for i in paises:
    if(i[0] == "C"):
        print(i)
"""

# Ejemplo 05 = Imprima todas las capitales que inicien con la leta B
"""
lista = []
ciudad = []
for i in archivo:
    a = i.index(":")
    for r in range(a+2, len(i)):
        lista.append(i[r])
    a = "".join(lista)
    ciudad.append(a)
    lista = []
for i in ciudad:
    if(i[0] == "B"):
        print(i)
"""

"""
--------------------------------------------------------------------------------------------------------------------------
Ejercicios Taller_Estructuras_de_Control_ For

01. Cuente e imprima cuantas ciudades inician con la latra M

02. Imprima todos los paises y capitales, cuyo inicio sea con la letra U

03. Cuente e imprima cuantos paises que hay en el archivo

04. Busque e imprima la ciudad de Singapur

05. Busque e imprima el pais de Venezuela y su capital

06. Cuente e imprima las ciudades que su pais inicie con la letra E

07. Busque e imprima la Capiltal de Colombia

08. Imprima la posicion del pais de Uganda

09. Imprima la posicion del pais de Mexico

10. El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de
países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya
contento por su trabajo. Utilice un For para cambiar ese Dato

11. Agregue un país que no esté en la lista
--------------------------------------------------------------------------------------------------------------------------
"""
"""
------------
| SOLUCIÓN |
------------

NOTA: Se utilizo el archivo paises.txt modificado sin caracteres especiales, ¡TENER ESTO EN CUENTA PARA CORRER EL CODIGO!
"""
# 01. Cuente e imprima cuantas ciudades inician con la latra M
"""
print("\nEste programa imprimira el número de ciudades que inician con la letra M")
lista = []
ciudad = []
contador = 0
for i in archivo:
    a = i.index(":")
    for r in range(a+2, len(i)):
        lista.append(i[r])
    a = "".join(lista)
    ciudad.append(a)
    lista = []
for i in ciudad:
    if(i[0] == "M"):
        contador += 1
print(f"\nLa cantidad de ciudades que inician con letra M es de: {contador}\n")
"""
# 02. Imprima todos los paises y capitales, cuyo inicio sea con la letra U
"""
print("\nEste programa imprimira los paises y capitales que inician con la letra U")
lista = []
paises = []
ciudades = []
for i in archivo:
    a = i.index(":")
    b = i.index(":")
    for x in range(0, a):
        lista.append(i[x])
    a = "".join(lista)
    paises.append(a)
    lista = []
    for r in range(b+2, len(i)):
        lista.append(i[r])
    b = "".join(lista)
    ciudades.append(b)
    lista = []
print("\nLos paises que inician con la letra U son:\n")
for i in paises:
    if(i[0] == "U"):
        print(f"{i}\n")
print("\nLas ciudades que inician con la letra U son:\n")
for i in ciudades:
    if(i[0] == "U"):
        print(i)
"""
# 03. Cuente e imprima cuantos paises que hay en el archivo
"""
print("\nEste programa imprimira la cantidad de paises presentes en el archivo")
lista = []
contador = 0
for i in archivo:
    a = i.index(":")
    for r in range(0, a):
        lista.append(i[r])
    a = "".join(lista)
    contador += 1
    print(f"{contador} -> {a}")
    lista = []
print(f"\nLa cantidad de paises en el archivo es de: {contador}\n")
"""
# 04. Busque e imprima la ciudad de Singapur
"""
print("\nEste programa buscara en el archivo la ciudad de Singapur y la imprimira")
lista = []
for i in archivo:
    lista.append(i)
    a = "".join(lista)
    if(a[0] == "S" and a[3] == "g" and a[7] == "r"):
        B = a.index(":")
        lista = []
        break
    lista = []
for i in range(B+2, len(a)):
    lista.append(a[i])
a = "".join(lista)
print(f"\n{a}\n")
"""
# 05. Busque e imprima el pais de Venezuela y su capital
"""
print("\nEste programa buscara en el archivo el pais de Venezuela junto a su capital y los imprimira")
lista = []
for i in archivo:
    lista.append(i)
    a = "".join(lista)
    if(a[0] == "V" and a[4] == "z" and a[8] == "a"):
        print(f"\n{a}\n")
        lista = []
        break
    lista = []
"""
# 06. Cuente e imprima las ciudades que su pais inicie con la letra E
"""
print("\nEste programa buscara y contara en el archivo los paises que inician por la letra E y imprimira sus ciudades")
lista = []
paises = []
for i in archivo:
    a = len(i)
    for r in range(0, a):
        lista.append(i[r])
    a = "".join(lista)
    paises.append(a)
    lista = []
contador = 0
print()
for i in paises:
    if(i[0] == "E"):
        a = i.index(":")
        contador += 1
        for r in range(a+2, len(i)):
            lista.append(i[r])
        a = "".join(lista)
        print(f"{contador} -> {a}")
    lista = []
print(f"\nCantidad de ciudades con país que inicia con E es: {contador}\n")
"""
# 07. Busque e imprima la Capiltal de Colombia
"""
print("\nEste programa buscara e imprimira la capital de Colombia")
lista = []
for i in archivo:
    lista.append(i)
    a = "".join(lista)
    if(a == "Colombia: Bogota\n"):
        b = a.index(":")
        lista = []
        break
    lista = []
for i in range(b+2, len(a)):
    lista.append(a[i])
a = "".join(lista)
print(f"\n{a}")
"""
# 08. imprima la posicion del pais de Uganda
"""
print("\nEste programa buscara e imprimira la posición del pais Uganda")
lista = []
contador = 0
for i in archivo:
    lista.append(i)
    a = "".join(lista)
    contador += 1
    if(a[0] == "U" and a[3] == "n" and a[4] == "d"):
        B = a.index(":")
        lista = []
        break
    lista = []
print(f"\nLa posición del pais Uganda en el archivo es: {contador}\n")
"""
# 09. Imprima la posicion del pais de Mexico
"""
print("\nEste programa buscara e imprimira la posición del pais Mexico")
lista = []
contador = 0
for i in archivo:
    lista.append(i)
    a = "".join(lista)
    contador += 1
    if(a[0] == "M" and a[3] == "i" and a[5] == "o"):
        B = a.index(":")
        lista = []
        break
    lista = []
print(f"\nLa posición del pais Mexico en el archivo es: {contador}\n")
"""
""" 10. El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de
países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya
contento por su trabajo. Utilice un For para cambiar ese Dato"""
"""
print("\nEste programa corregira el archivo paises.txt, de tal modo que la capital de Madagascar deje de ser rey julien y pase a ser Antananarivo")
lista = []
for i in archivo:
    lista.append(i)
archivo1 = open("C:/Users/jimen/Desktop/U EAN/Semestre 2/Algoritmos y Programación/Algoritmos_y_Programacion_C4_G2/Taller_Estructuras_de_Control_For/paises.txt", "w")
for i in lista:
    if (i == "Madagascar: rey julien\n"):
        archivo1.write("Madagascar: Antananarivo\n")
    else:
        archivo1.write(i)
archivo1.close()
"""
# 11. Agregue un país que no esté en la lista
"""
print("\nEste programa agregara al archivo paises.txt un pais que no se encuentre en la lista")
archivo2 = open("C:/Users/jimen/Desktop/U EAN/Semestre 2/Algoritmos y Programación/Algoritmos_y_Programacion_C4_G2/Taller_Estructuras_de_Control_For/paises.txt", "a")
archivo2.write("\nAldea Oculta del Pais del Fuego: Konoha")
archivo2.close()
"""
archivo.close()
