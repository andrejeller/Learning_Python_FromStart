"""

Desafio 084
- Faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final, mostre:
'A. Quantas pessoas foram cadastradas.
'B. Uma listagem com as pessoas mais pesadas.
'C. Uma listagem com as pessoas mais leves.

"""

pessoa = list()
grupo = list()

while True:

    nome = str(input('Digite um nome: '))
    peso = int(input('Digite um peso: '))

    pessoa.append(nome)
    pessoa.append(peso)
    grupo.append(pessoa[:])
    pessoa.clear()

    op = str(input('Deseja continuar? [S/N] '))
    if op in 'nN':
        break


print(f'Você cadastrou {len(grupo)} pessoas.')

print('Estão acima de 80Km.. ', end='')
for p in grupo:
    if p[1] > 80:
        print(f'{p[0]}', end='... ')

print('\nEstão abaixo de 80Km.. ', end='')
for p in grupo:
    if p[1] < 80:
        print(f'{p[0]}', end='... ')
int(f'{p[0]}', end='... ')