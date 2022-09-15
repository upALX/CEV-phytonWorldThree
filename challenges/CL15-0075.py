# Escreva um programa que leia 4 números e mostre numa tupla os valores digitados. Mostre: quantas vezes o valor 9 aparece. Onde é a primeira ocorrencia do valor 3. Quantos dos valores digitados são pares.
counter_loop = 1
list_user_values = []

while counter_loop < 5:
    value_user = int(input('Informe um valor: '))
    list_user_values.append(value_user)

    counter_loop += 1

tuple_values = tuple(list_user_values)

print(f'Os valores digitados foram: {tuple_values} e estão armazenados em: {type(tuple_values)}')

# Quantas vezes o valor 9 aparece
counter_nine = 0
for index_position, value in enumerate(tuple_values):
    if value == 9:
        counter_nine += 1

print(f'O valor 9 aparece {counter_nine} vezes!')

# Onde é a primeira ocorrencia do valor 3.
print(f'A primeira ocorrencia do valor 3 é foi na posição {tuple_values.index(3)}')

# Quantos dos valores digitados são pares.
counter_par = 0
for value in tuple_values:
    if value % 2 == 0:
        counter_par += 1

print(f'Existem {counter_par} números pares na tupla!')