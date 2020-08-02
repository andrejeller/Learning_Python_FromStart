"""
Desafio 012
- Faça um algorítimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

a = float(input('Preço: '))
desconto = a * 0.95
print('O novo preço do produto é de R${:.2}.'.format(desconto))
