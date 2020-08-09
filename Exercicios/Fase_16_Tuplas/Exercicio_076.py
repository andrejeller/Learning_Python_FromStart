"""
Desafio 076
- Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequencia.
No final mostre ums listagem de preços, organizando os dados em forma tabular.
"""


tupla = ('Batata', 5.00, 'Pao', 2.32, 'Presunto', 8.99, 'Carne Moida', 25.25)


print('='*40)
print(f'{"SUPER-MERCADO":-^30}')
print('='*40)

for i in range(len(tupla)):
    if i % 2 == 0:
        print(f'{tupla[i]:.<30}', end='')
    else:
        print(f'R${tupla[i]:>8.2f}')
"""

print('='*30)
print('{:-^30}'.format(' SUPER-MERCADO '))
print('='*30)

for i in range(len(tupla)):
    if not str(tupla[i]).isnumeric():
        # print(f'{tupla[i]} ......... R${tupla[i+1]}')
        nome = tupla[i]
        preco = 'R$' + str(tupla[i+1])
        print('{:.<15}{:.>15}'.format(nome, preco))

print('-'*30)
"""