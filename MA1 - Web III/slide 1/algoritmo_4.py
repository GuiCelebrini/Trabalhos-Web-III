minutos = int(input("Quantos minutos foram falados? "))

if minutos < 200:
    preco = 0.2 * minutos
elif minutos <= 400:
    preco = 0.18 * minutos
elif minutos <= 800:
    preco = 0.15 * minutos
else:
    preco = 0.08 * minutos

print(preco)