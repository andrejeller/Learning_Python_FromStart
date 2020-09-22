"""
Desafio 078
- Faça um programa que leia 5 valores e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

"""
"""
menor = maior = 0
numeros = []

for i in range(0, 5):
    a = int(input(f'Digite o {i+1}° número: '))
    numeros.append(i)
    if i == 0:
        menor = maior = a
    else:
        if i < menor:
            menor = a
        if i > maior:
            maior = a

print('Maior valor digitado foi ', maior, 'na posicao ', numeros.index(maior))
print('Menor valor digitado foi ', menor, 'na posicao ', numeros.index(menor))
"""

# O que ele fez

menor = maior = 0
numeros = []

for i in range(0, 5):
    numeros.append(int(input(f'Digite o {i+1}° número: ')))

    if i == 0:
        menor = maior = numeros[i]

    else:
        if numeros[i] < menor:
            menor = numeros[i]
        if numeros[i] > maior:
            maior = numeros[i]

print('-'*30)
print('Voce digitou os valores: ', numeros)

print('Maior valor digitado foi ', maior, 'nas posicoes ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i+1}... ', end=' ')

print('\nMenor valor digitado foi ', menor, 'nas posicoes ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i+1}... ', end=' ')
