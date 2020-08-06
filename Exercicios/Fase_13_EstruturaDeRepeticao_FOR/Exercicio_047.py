"""
Desafio 047
- Crie um programa que mostre na tela todos os numero pares que estão no intervalo entre 1 e 50.

"""

for i in range(1, 51):
    print('.', end='')
    if i % 2 == 0:
        print(i, end=' ')

print('Acabou')

for i in range(2, 51, 2):
    print('.', end='')
    print(i, end=' ')

print('Acabou')