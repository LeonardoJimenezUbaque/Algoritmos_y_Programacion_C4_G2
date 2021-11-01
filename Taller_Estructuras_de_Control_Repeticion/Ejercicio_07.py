"""
Ejercicio 07
https://www.urionlinejudge.com.br/judge/es/problems/view/2172

Entradas
Multiplicador --> int --> M
XP --> int --> XP

Salidas
XP_Actual --> int --> C
"""
# Entradas, Caja negra y Salidas
while True:
    M, XP = input().split(" ")
    XP = int(XP)
    M = int(M)
    if XP == 0 and M == 0:
        break
    else:
        XP_A = M * XP
    print(XP_A)
