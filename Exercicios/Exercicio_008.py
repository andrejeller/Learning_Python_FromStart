"""
Desafio 008
- Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e melímetros.

Extra: mostrar a medida em "mm, cm, dm, dam, hm, km"
"""

metros = float(input('Quantos metros você quer converter? '))
centimetros = metros * 100
melimetros = metros * 1000

print('Resultado: {:.3} metros são {:.0f}cm e {:.1f}ml.'.format(metros, centimetros, melimetros))
