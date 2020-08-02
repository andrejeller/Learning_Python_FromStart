"""
Desafio 008
- Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e melímetros.
"""

metros = float(input('Quantos metros você quer converter? '))
centimetros = metros * 100
melimetros = centimetros * 100

print('Resultado: {:.3} metros são {:.2} centimetros e {:.3} melimetros.'.format(metros, centimetros, melimetros))
