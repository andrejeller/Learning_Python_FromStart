"""
Desafio 019
- Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo
o nome deles e escrevendo o nome do escolhido.
"""

import random
#from random import choice
#from random import randint

a1 = input('Aluno 01: ')
a2 = input('Aluno 02: ')
a3 = input('Aluno 03: ')
a4 = input('Aluno 04: ')

lista = [a1, a2, a3, a4]
rand = random.randint(0, 4)  # maneira 01
escolhido = random.choice(lista)  # maneira 02

print('O aluno escolhido foi o {}'.format(lista[rand]))  # maneira 01
print('O aluno escolhido foi o {}'.format(escolhido))  # maneira 02
