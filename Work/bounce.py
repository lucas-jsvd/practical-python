# bounce.py
#
# Exercise 1.5
altura = 100
RESISTENCIA = 3/5

for queda in range(1, 11):
    altura = altura * RESISTENCIA
    print(queda, round(altura, 4))