notas = []
media = 0

contador = 0
while contador <= 3:
    nota = float(input("Insira a nota "))
    notas.append(nota)
    contador += 1

media = (notas[0] + notas[1] + notas[2] + notas[3])/4

print(notas)
print(media)