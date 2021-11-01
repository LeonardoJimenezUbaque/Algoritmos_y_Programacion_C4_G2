"""
Ejercicio 09
https://www.urionlinejudge.com.br/judge/es/problems/view/1134

Entradas
Combustible --> Int --> C

Salidas
MUITO OBRIGADO --> Str --> MUITO OBRIGADO
Alcool --> Str --> Alcool
Gasolina --> Str --> Gasolina
Diesel --> Str --> Diesel

"""
# Entradas, Caja negra y Salidas
Alcool = 0
Gasolina = 0
Diesel = 0
while True:
    C = int(input())
    if C == 1:
        Alcool = Alcool + 1
    elif C == 2:
        Gasolina = Gasolina + 1
    elif C == 3:
        Diesel = Diesel + 1
    elif C == 4:
        break
    else:
        C = C
# Salidas
print("MUITO OBRIGADO")
print(f"Alcool: {Alcool}")
print(f"Gasolina: {Gasolina}")
print(f"Diesel: {Diesel}")
