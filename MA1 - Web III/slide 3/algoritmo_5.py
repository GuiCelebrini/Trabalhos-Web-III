import random

contador = 0
lista_num = []

while contador <= 15:
    numero = random.choice(range(10,101))
    if numero in lista_num:
        numero = random.choice(range(10,101))
    else:
        lista_num.append(numero)
        
    contador += 1

print(lista_num)