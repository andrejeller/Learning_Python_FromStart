"""
Desafio 016
- Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.
Ex. Digite um número: 6.127
Print: O número 6.127 tem a parte inteira 6.s
"""
import math

n = float(input('Digite um numero com virgula: '))
parte_inteira = math.trunc(n)

print('O número {} tem a parte inteira {}.'.format(n, parte_inteira))
print('O número {} tem a parte inteira {:.0f}.'.format(n, n))
print('O número {} tem a parte inteira {}.'.format(n, int(n)))
