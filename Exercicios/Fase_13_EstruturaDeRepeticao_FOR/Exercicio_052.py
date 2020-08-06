"""
Desafio 052
- Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
Obs. Apenas dividido por 1 e por ele mesmo
"""

n = int(input('Digite um número: '))
cont = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[34m', end='')
        cont += 1
    else:
        print('\033[31m', end='')

    print('{} '.format(i), end='')
print('\n\033[mO numero {} foi divisível {} vezes.'.format(n, cont))
if cont == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO!')
