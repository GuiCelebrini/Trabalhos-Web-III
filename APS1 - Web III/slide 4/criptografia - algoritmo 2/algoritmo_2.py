arquivo = open('mensagem.txt')
novo_arquivo = open('cripto.txt', 'w')
for linha in arquivo.readlines():
    for letra in linha:
        if letra in 'aeiou':
            novo_arquivo.write('*')
        else:
            novo_arquivo.write(letra)
novo_arquivo.close()
arquivo.close()

arquivo = open('mensagem.txt', 'r')
for linha in arquivo.readlines():
    print(linha)
arquivo.close()