"""
Desafio 081
- Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
'A. Quantos números foram digitados.
'B. A lista de todos os valores, ordenada de forma decrescente.
'C. Se o valor 5 foi digitado e está ou não na lista.

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

lista.sort(reverse=True)

print('Você adicionou {} numeros'.format(len(lista)))
print('Os números adicionados foram: ', lista)
if 5 in lista:
    print('O numero 5 foi adicionado.')
else:
    print('O numero 5 NÃO foi adicionado.')

"""

# Ele fez

lista = []
while True:
    lista.append(int(input("Digite um número para adicionar a lista: ")))

    op = str(input('Deseja adicionar mais um número? [S/N] '))

    if op in 'nN':
        break



print('Você adicionou {} numeros'.format(len(lista)))

lista.sort(reverse=True)
print('Os números adicionados foram: ', lista)
if 5 in lista:
    print('O numero 5 foi adicionado.')
else:
    print('O numero 5 NÃO foi adicionado.')
