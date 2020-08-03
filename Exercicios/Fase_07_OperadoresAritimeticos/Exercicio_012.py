"""
Desafio 012
- Faça um algorítimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

preco = float(input('Preço: '))
desconto = preco * 0.95  # jeito 1
desconto2 = preco - (preco * 5 / 100)  # jeito 2
print('O novo preço do produto com 5% de desconto é de R${:.2f}.'.format(desconto))
