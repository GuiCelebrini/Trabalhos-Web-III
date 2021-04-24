letras = []

contador = 0
while contador <= 4:
    letra = input("Letra: ")
    letras.append(letra)
    contador += 1

contador = 0
contagem = 0
while contador <= 4:
    if letras[contador] not in 'aeiou':
        contagem += 1
    contador += 1

print (contagem)