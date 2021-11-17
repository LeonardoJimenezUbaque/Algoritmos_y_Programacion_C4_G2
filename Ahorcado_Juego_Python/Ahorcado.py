"""
Clase 10/11/2021

Crear juego ahorcado, maximo 4 intentos
"""
# lIBRERIAS
import random

# INSTRUCIONES AL USUARIO
print("\nBienvenido al juego del ahorcado\n")
print("El objetivo de este juego es adivinar la palabra desconocida, para este juego sera un color")
print("Tendra un maximo de 4 vidas, A continuación digite letra por letra, ¡Mucha suerte!\n")
print("""
 SSSSS  UU   UU EEEEEEE RRRRRR  TTTTTTT EEEEEEE
SS      UU   UU EE      RR   RR   TTT   EE
 SSSSS  UU   UU EEEEE   RRRRRR    TTT   EEEEE
     SS UU   UU EE      RR  RR    TTT   EE
 SSSSS   UUUUU  EEEEEEE RR   RR   TTT   EEEEEEE
\n""")

# LISTA DE PALABRAS


def palabra() -> str:
    palabras = ["azul", "amarillo", "rojo", "verde", "morado",
                "violeta", "negro", "blanco", "gris", "cafe"]
    palabra_aleatoria = random.randint(0, len(palabras)-1)
    return palabras[palabra_aleatoria]


a = palabra()
letra = " "
vidas = 4  # NUMERO DE INTENTOS DISPONIBLES PARA EL USUARIO
jugar = True
letras_palabra_adivinar = []
letras_adivinadas = []
letras_palabra_adivinar = list(a)

# REEMPLAZAR PALABRA POR NUMERO DE ESPACIOS DE LA LETRA CON _
for i in letras_palabra_adivinar:
    letras_adivinadas.append("_")

while jugar:

    print(" ".join(letras_adivinadas))
    letra = input("\nEscriba una letra: ")
    letra = letra.lower()
    if letra not in letras_palabra_adivinar:
        vidas -= 1
        if vidas >= 1:
            print(f"¡Incorrecto! Te quedan {vidas} intentos")
    else:
        for x, y in enumerate(letras_palabra_adivinar):
            if y == letra:
                letras_adivinadas[x] = y
    if vidas == 0:
        jugar = False
        print(f"Has perdido, la palabra era {a}")
    elif letras_palabra_adivinar == letras_adivinadas:
        jugar = False
        print(f"Has ganado, la palabra era {a}\n")
        print("""
              FFFFFFF EEEEEEE LL      IIIII  CCCCC  IIIII DDDDD     AAA   DDDDD   EEEEEEE  SSSSS
              FF      EE      LL       III  CC      a III  DD  DD   AAAAA  DD  DD  EE      SS
              FFFF    EEEEE   LL       III  CC       III  DD   DD AA   AA DD   DD EEEEE    SSSSS
              FF      EE      LL       III  CC       III  DD   DD AAAAAAA DD   DD EE           SS
              FF      EEEEEEE LLLLLLL IIIII  CCCCC  IIIII DDDDDD  AA   AA DDDDDD  EEEEEEE  SSSSS
              """)
