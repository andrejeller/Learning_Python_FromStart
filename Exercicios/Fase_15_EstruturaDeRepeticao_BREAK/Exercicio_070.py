"""
Desafio 070
- Crie um programa que leia  o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
no final mostre:
'A qual é o total gasto na compra.
'B Quantos produtos custam mais de R$1000,00
'C Qual é o nome do produto mais barato.

"""


soma = 0
cont_produtos_caros = 0
produto_mais_barato = ''
valor_produto_barato = 0

print('=' * 30)
print('SUPER MEGA MERCADO')

while True:

    print('-' * 30)

    nome = str(input('Digite o nome do produto: ')).strip()
    preco = int(input('Digite o valor do produto: R$ '))

    soma += preco

    if preco >= 1000:
        cont_produtos_caros += 1

    if produto_mais_barato == '':
        produto_mais_barato = nome
        valor_produto_barato = preco

    elif preco < valor_produto_barato:
        valor_produto_barato = preco
        produto_mais_barato = nome

    op = ' '
    while op not in 'SN':
        op = str(input('Deseja cadastrar mais produtos? [S/N] ')).strip().upper()[0]

    if op == 'N':
        break


print('~'*40)
print('{:~^40}'.format('FIM DA COMPRA'))
print('~'*40)
print(f'O total da compra é {soma}.')
print(f'{cont_produtos_caros} produtos custam mais de R$ 1000,00.')
print(f'O produto mais barato é {produto_mais_barato} e custa {valor_produto_barato}.')
