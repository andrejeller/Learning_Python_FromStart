"""
Desafio 060
- Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex. 5! = 5x4x3x2x1 = 120

"""

from math import factorial

num = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(num)

print('O fatorial de {} é {}. '.format(num, f))


