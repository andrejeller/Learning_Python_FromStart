"""
Desafio 017
- Faça um programa que leia o cateto oposto e do cateto adjacente de um triangulo retângulo, calcule e mostre o
comprimento da hipotenusa.
a² = b² + c²
"""

import math
#from math import hypot

cateto_oposto = float(input('Cateto Oposto: '))
cateto_adjacente = float(input('Cateto Adjacente: '))
#hipotensa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
#hipotenusa = math.sqrt(math.pow(cateto_oposto, 2) + math.pow(cateto_adjacente, 2))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print('Dado CO sendo {} e CA sendo {}, H será {:.2f}.'.format(cateto_oposto, cateto_adjacente, hipotenusa))

