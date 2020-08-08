"""
Desafio 067
- Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.

"""

while True:
    print('=' * 30)
    print('TABUADA COM WHILE E BREAK')
    print('-' * 30)
    num = int(input('Digite um número para saber a tabuada: '))

    if num < 0:
        break

    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')

    print('=' * 30)

print('PROGRAMA DA TABUADA ENCERRADO, VOLTE SEMPRE!')