a = 2
def muda_e_imprime():
    a = 8 #usar global a antes referenciaria a de fora da função
    print(a)


print(a)
muda_e_imprime()
print(a)