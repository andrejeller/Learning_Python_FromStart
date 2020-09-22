"""
Desafio 079
- Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o
número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem cresente.


"""

""" # Eu fiz
op = 's'
lista = list()
while op in 'sS':
    num = int(input("Digite um número para adicionar a lista: "))

    if num in lista:
        print('Este numero já foi adicionado...')
    else:
        print('Olha! Numero novo!!')
        lista.append(num)

    op = str(input('Deseja adicionar mais um número? [S/N] '))

    while op not in 'sSnN':
        op = str(input('Deseja adicionar mais um número? [S/N] '))

lista.sort()
print('Os números adicionados foram: ', lista)
"""

# Ele fez
lista = list()
while True:
    n = int(input("Digite um número para adicionar a lista: "))

    if n not in lista:
        lista.append(n)
        print('Olha! Numero novo!!')
    else:
        print('Este numero já foi adicionado...')

    op = str(input('Deseja adicionar mais um número? [S/N] '))
    if op in 'nN':
        break


lista.sort()
print('Os números adicionados foram: ', lista)
