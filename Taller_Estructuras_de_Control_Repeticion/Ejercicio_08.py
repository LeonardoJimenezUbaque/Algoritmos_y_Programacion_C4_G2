"""
Ejercicio 08
https://www.urionlinejudge.com.br/judge/es/problems/view/1114

Entradas
Contraseña --> Int --> C

Salidas
Correcta --> Str --> Acesso Permitido
Incorreta --> Str --> Senha Invalida
"""
# Entradas, Caja negra y Salidas
C = 0000
while (C != 2002):
    C = int(input())
    if C != 2002:
        print("Senha Invalida")
print("Acesso Permitido")
