"""
Desafio 020
- O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um
programa que leia os nomes dos quatro alunos e mostre a ordem sorteada.
"""

#import random
from random import shuffle

a1 = str(input('Aluno 01: '))
a2 = str(input('Aluno 02: '))
a3 = str(input('Aluno 03: '))
a4 = str(input('Aluno 04: '))

lista = [a1, a2, a3, a4]
#random.shuffle(lista)
shuffle(lista)

print('A ordem de apresentação será {}'.format(lista))
