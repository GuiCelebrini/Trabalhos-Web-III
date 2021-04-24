import random

contador = 0
lista_num = []

while contador <= 15:
    numero = random.choice(range(10,101))
    lista_num.append(numero)
    contador += 1

print(lista_num)