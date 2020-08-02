"""
Desafio 011
- Faça um programa que leia a largura e a altura de uma parede em metros, calcula a sua área e a quantidade
de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
"""

largura = float(input('Largura: '))
altura = float(input('Altura: '))

area = largura * altura
tintas = area / 2
print('Sendo uma parede de {}x{} você vai precisar de {} latas de tinta.'.format(largura, altura, tintas))
