"""
Desafio 018
- Faça um programa que leia um ângulo quaquer e mosre na tela o valor do seno, cosseno e tangente desse ângulo.
#existe biblioteca
"""

#import math
from math import sin, cos, tan, radians
angulo = float(input('Digite um angulo: '))
cos = cos(radians(angulo))
sen = sin(radians(angulo))
tan = tan(radians(angulo))

print('O ângulo de {}° tem o SENO de {:.2f}.'.format(angulo, sen))
print('O ângulo de {}° tem o COSSENO de {:.2f}.'.format(angulo, cos))
print('O ângulo de {}° tem a TANGENTE de {:.2f}.'.format(angulo, tan))
#print('Dado {}°, seu seno é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}'.format(angulo, sen, cos, tan))
