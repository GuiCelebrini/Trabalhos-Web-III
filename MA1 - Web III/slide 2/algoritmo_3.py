lista_num = []
contador = 0
while contador <= 9:
    num = float(input("Insira um número "))
    lista_num.append(num)
    contador += 1

i = 9

while i >= 0:
    print(lista_num[i])
    i -= 1