# Crie um programa com uma tupla totalmente preenchida com uma contagem por extenso, de zero até 20.
# O programa deve ler o número em numeral e retornar o numero por escrito.

names_number = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')

while True:
    number = int(input('Digite um número: '))
    #verificar se é um número
    if str(number).isdigit() == False: 
        print('Você está digitando um valor que não é um número ou não é válido!')
    elif number < 0:
        print('O número digitado é menor que 0, portanto invalido! Digite apenas números iguais ou maiores que 0.')
    elif number > 20:
        print('O número digitado é maior que 20! Digite entre 0 e 20.')
    else:
        print(f'O número escrito por extenso de {number} é {names_number[number]}!')