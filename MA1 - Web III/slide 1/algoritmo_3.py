velocidade = int(input("Qual é a velocidade do seu carro? "))

if velocidade > 110:
    excesso = velocidade - 110
    multa = excesso * 5
    print("Sua velocidade está acima, sua multa é: ")
    print(multa)