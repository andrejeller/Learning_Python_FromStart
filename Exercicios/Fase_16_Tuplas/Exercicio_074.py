"""
Desafio 074
- Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listage, de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

from random import randint

"""
a = randint(0, 10)
b = randint(0, 10)
c = randint(0, 10)
d = randint(0, 10)
e = randint(0, 10)

tupla = (a, b, c, d, e)

print(tupla)
print(f'O menor numero é {sorted(tupla)[0]}')
print(f'O maior numero é {sorted(tupla)[len(tupla)-1]}')


"""

tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(tupla)
print(f'O menor numero é {max(tupla)}')
print(f'O maior numero é {min(tupla)}')

# TUPLAS tem a fun min() e max() que te retornam os maiores e menores valores dentro delas
