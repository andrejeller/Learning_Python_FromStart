"""

Desafio 096
- Faça um programa que tanha uma função chamada area(), que receba as dimenções de um terreno retangular(largura e
comprimento) e mostre a área do terreno.

"""


def area(l, c):
    print(f'A área de um terreno {l}x{c} é de {l * c}m²')


print('Controle de Terrenos')
print('-' * 50)

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
