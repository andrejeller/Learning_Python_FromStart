"""
Desafio 006
- Crie um algorítimo que leia um número e mostre seu dobro, triplo e raiz quadrada.
"""

n = float(input('Digite um numero: '))
do = n * 2
tr = n * 3
rz = n ** (1/2)
print('O dobro do numero {} é {}, seu triplo é {} e a raiz quarada é {}.'.format(n, do, tr, rz))
