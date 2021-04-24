import random

palavra = input('Insira uma palavra ')

vetor_palavra = list(palavra)

random.shuffle(vetor_palavra)

print(vetor_palavra)