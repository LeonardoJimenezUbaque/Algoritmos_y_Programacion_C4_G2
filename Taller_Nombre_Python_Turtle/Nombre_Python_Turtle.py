"""
Taller_Nombre_Python_Turtle

Usando Python Turtle escriba su primer o segundo nombre, sea creativo e investigue funciones y metodos de dicha
libreria que pueda aplicar.
"""
# Solución

import turtle  # Se importa la libreria turtle
import random  # Se importa la libreria random

# Genera un color hexadecimal aleatorio


def color_aleatorio():
    tortu.color(
        "#"+''.join([random.choice('0123456789ABCDEF')for j in range(6)]))


caso = int(input("""Digite el numero de la opcion que desea ver:
1) Generacion del nombre con colores aleatorios.
2) Generacion del nombre en color negro.
"""))

if caso == 1:
    tortu = turtle.Turtle()  # Creamos una nueva tortuga que se llama "tortu"
    v = turtle.Screen()  # Se crea la ventana en la que estara la tortuga
    # Asignamos un titulo a la ventana en la que estara la tortuga
    v.title("Taller_Nombre_Python_Turtle")
    v.screensize(2500, 1000)
    tortu.shape("turtle")
    tortu.speed(10)  # Asignamos una velocidad a la tortuga
    tortu.pensize(10)  # Asignamos un grosor al recorrido de la tortuga

    tortu.hideturtle()  # Esconde la tortuga
    tortu.penup()       # Sube el lapicero y evita que la tortuga escriba cuando se mueva
    # Mueve la tortuga hacia una ubicacion especifica (x,y)
    tortu.goto(-200, 150)
    # t.showturtle()  # Hace que la tortuga sea visible
    tortu.pendown()     # Baja el lapicero y hace que la tortuga escriba cuando se mueva

    # Creación Nombre LEONARDO

    # Letra L
    color_aleatorio()
    tortu.rt(90)
    tortu.fd(200)
    tortu.lt(90)
    tortu.fd(80)
    tortu.penup()
    tortu.goto(-100, -50)
    tortu.pendown()

    # Letra E
    color_aleatorio()
    tortu.lt(90)
    tortu.fd(200)
    tortu.rt(90)
    tortu.fd(80)
    tortu.bk(80)
    tortu.rt(90)
    tortu.fd(100)
    tortu.lt(90)
    tortu.fd(80)
    tortu.bk(80)
    tortu.rt(90)
    tortu.fd(100)
    tortu.lt(90)
    tortu.fd(80)
    tortu.penup()
    tortu.goto(0, -50)
    tortu.pendown()

    # Letra O
    color_aleatorio()
    tortu.fd(100)
    tortu.lt(90)
    tortu.fd(200)
    tortu.lt(90)
    tortu.fd(100)
    tortu.lt(90)
    tortu.fd(200)
    tortu.rt(90)
    tortu.penup()
    tortu.goto(120, -50)
    tortu.pendown()

    # Letra N
    color_aleatorio()
    tortu.rt(90)
    tortu.fd(200)
    tortu.rt(150)
    tortu.fd(230)
    tortu.lt(150)
    tortu.fd(200)
    tortu.rt(90)
    tortu.penup()
    tortu.goto(250, -50)
    tortu.pendown()

    # Letra A
    color_aleatorio()
    tortu.lt(70)
    tortu.fd(200)
    tortu.rt(140)
    tortu.fd(200)
    tortu.bk(100)
    tortu.lt(140)
    tortu.rt(70)
    tortu.lt(180)
    tortu.fd(65)
    tortu.rt(90)
    tortu.penup()
    tortu.goto(400, -50)
    tortu.pendown()

    # Letra R
    color_aleatorio()
    tortu.fd(200)
    tortu.bk(120)
    tortu.rt(90)
    tortu.circle(60, 180)
    tortu.lt(90)
    tortu.fd(120)
    tortu.goto(450, -50)
    tortu.penup()
    tortu.goto(480, -50)
    tortu.pendown()

    # Letra D
    color_aleatorio()
    tortu.lt(90)
    tortu.circle(100, 180)
    tortu.lt(90)
    tortu.fd(200)
    tortu.penup()
    tortu.goto(600, -50)
    tortu.lt(90)
    tortu.pendown()

    # Letra O
    color_aleatorio()
    tortu.fd(100)
    tortu.lt(90)
    tortu.fd(200)
    tortu.lt(90)
    tortu.fd(100)
    tortu.lt(90)
    tortu.fd(200)
    tortu.rt(90)
    tortu.penup()
    tortu.goto(-420, 30)
    tortu.pendown()

    # Espiral

    def Espiral_1():
        colores = ['red', 'purple', 'blue',
                   'green', 'black', 'orange']
        for x in range(200):
            tortu.pencolor(colores[x % 6])
            tortu.width(x/100 + 1)
            tortu.fd(x)
            tortu.lt(60)

    Espiral_1()

    # Espiral 2

    def Espiral_2():
        colores = ['red', 'purple', 'blue',
                   'green', 'black', 'orange']
        for x in range(200):
            tortu.pencolor(colores[x % 6])
            tortu.width(x/100 + 1)
            tortu.fd(x)
            tortu.lt(59)

    tortu.penup()
    tortu.goto(920, 30)
    tortu.pendown()
    Espiral_2()

if caso == 2:
    tortu = turtle.Turtle()  # Creamos una nueva tortuga que se llama "tortu"
    v = turtle.Screen()  # Se crea la ventana en la que estara la tortuga
    # Asignamos un titulo a la ventana en la que estara la tortuga
    v.title("Taller_Nombre_Python_Turtle")
    v.screensize(2500, 1000)
    tortu.shape("turtle")
    tortu.speed(10)  # Asignamos una velocidad a la tortuga
    tortu.pensize(10)  # Asignamos un grosor al recorrido de la tortuga

    tortu.hideturtle()  # Esconde la tortuga
    tortu.penup()       # Sube el lapicero y evita que la tortuga escriba cuando se mueva
    # Mueve la tortuga hacia una ubicacion especifica (x,y)
    tortu.goto(-200, 150)
    # t.showturtle()  # Hace que la tortuga sea visible
    tortu.pendown()     # Baja el lapicero y hace que la tortuga escriba cuando se mueva

    # Creación Nombre LEONARDO

    # Letra L
    tortu.rt(90)
    tortu.fd(200)
    tortu.lt(90)
    tortu.fd(80)
    tortu.penup()
    tortu.goto(-100, -50)
    tortu.pendown()

    # Letra E
    tortu.lt(90)
    tortu.fd(200)
    tortu.rt(90)
    tortu.fd(80)
    tortu.bk(80)
    tortu.rt(90)
    tortu.fd(100)
    tortu.lt(90)
    tortu.fd(80)
    tortu.bk(80)
    tortu.rt(90)
    tortu.fd(100)
    tortu.lt(90)
    tortu.fd(80)
    tortu.penup()
    tortu.goto(0, -50)
    tortu.pendown()

    # Letra O
    tortu.fd(100)
    tortu.lt(90)
    tortu.fd(200)
    tortu.lt(90)
    tortu.fd(100)
    tortu.lt(90)
    tortu.fd(200)
    tortu.rt(90)
    tortu.penup()
    tortu.goto(120, -50)
    tortu.pendown()

    # Letra N
    tortu.rt(90)
    tortu.fd(200)
    tortu.rt(150)
    tortu.fd(230)
    tortu.lt(150)
    tortu.fd(200)
    tortu.rt(90)
    tortu.penup()
    tortu.goto(250, -50)
    tortu.pendown()

    # Letra A
    tortu.lt(70)
    tortu.fd(200)
    tortu.rt(140)
    tortu.fd(200)
    tortu.bk(100)
    tortu.lt(140)
    tortu.rt(70)
    tortu.lt(180)
    tortu.fd(65)
    tortu.rt(90)
    tortu.penup()
    tortu.goto(400, -50)
    tortu.pendown()

    # Letra R
    tortu.fd(200)
    tortu.bk(120)
    tortu.rt(90)
    tortu.circle(60, 180)
    tortu.lt(90)
    tortu.fd(120)
    tortu.goto(450, -50)
    tortu.penup()
    tortu.goto(480, -50)
    tortu.pendown()

    # Letra D
    tortu.lt(90)
    tortu.circle(100, 180)
    tortu.lt(90)
    tortu.fd(200)
    tortu.penup()
    tortu.goto(600, -50)
    tortu.lt(90)
    tortu.pendown()

    # Letra O
    tortu.fd(100)
    tortu.lt(90)
    tortu.fd(200)
    tortu.lt(90)
    tortu.fd(100)
    tortu.lt(90)
    tortu.fd(200)
    tortu.rt(90)
    tortu.penup()
    tortu.goto(-420, 30)
    tortu.pendown()

    # Espiral

    def Espiral_1():
        colores = ['red', 'purple', 'blue',
                   'green', 'black', 'orange']
        for x in range(200):
            tortu.pencolor(colores[x % 6])
            tortu.width(x/100 + 1)
            tortu.fd(x)
            tortu.lt(60)

    Espiral_1()

    # Espiral 2

    def Espiral_2():
        colores = ['red', 'purple', 'blue',
                   'green', 'black', 'orange']
        for x in range(200):
            tortu.pencolor(colores[x % 6])
            tortu.width(x/100 + 1)
            tortu.fd(x)
            tortu.lt(59)

    tortu.penup()
    tortu.goto(920, 30)
    tortu.pendown()
    Espiral_2()
