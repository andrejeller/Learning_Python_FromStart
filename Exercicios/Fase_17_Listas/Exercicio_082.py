"""
Desafio 082
- Crie um programa que vai ler vários numeros e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e ímpares digitados,
respactivamente.
Ao final, mostre o conteúdo das três listas geradas.

"""

"""
# eu fiz
op = 's'
lista = list()
while op in 'sS':
    num = int(input("Digite um número para adicionar a lista: "))
    lista.append(num)

    op = str(input('Deseja adicionar mais um número? [S/N] '))
    while op not in 'sSnN':
        op = str(input('Deseja adicionar mais um número? [S/N] '))

pares = []
impares = []

for n in lista:
    if n % 2:
        # print(n, 'IMPAR')
        impares.append(n)
    else:
        # print(n, 'PAR')
        pares.append(n)

print('-'*30)
print('A lista completa é: ', lista)
print('Os numeros pares são: ', pares)
print('Os numeros impares são: ', impares)
"""
# ele fez

lista = list()
pares = list()
impares = list()
while True:
    lista.append(int(input("Digite um número para adicionar a lista: ")))

    op = str(input('Deseja adicionar mais um número? [S/N] '))

    if op in 'nN':
        break

for i, v in enumerate(lista):
    if v % 2:
        impares.append(v)
    else:
        pares.append(v)

print('-' * 30)
print('A lista completa é: ', lista)
print('Os numeros pares são: ', pares)
print('Os numeros impares são: ', impares)
