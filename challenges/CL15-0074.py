# Escreva um programa que sorteie 5 valores e coloque esses dentro de uma tuple. Depois, pegue o maior e o menor valor de dentro dessa tuple e mostre eles assim como a tuple com os valores sorteados.

from random import randrange

list_numbers = []

for counter in range(0, 5):
    generator_number = randrange(0, 9)
    list_numbers.append(generator_number)

tuple_numbers = tuple(list_numbers)

print(f'Os valores criados foram armazenados na tupla: {tuple_numbers}')
print(f'O menor valor é igual a: {min(tuple_numbers)}')
print(f'O maior valor é igual a: {max(tuple_numbers)}')