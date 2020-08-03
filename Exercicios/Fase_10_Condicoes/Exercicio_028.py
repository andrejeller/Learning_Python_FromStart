"""
Desafio 028
- Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para
o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.


"""

import random
from time import sleep

rand = random.randint(0, 5)
n = int(input('Tente descobrir o número que eu escolhi: '))

print('PROCESSANDO.....')
sleep(3)

print('Se eu escolhi {}, você '.format(rand), end='')

if rand == n:
    print('Acertou!')
else:
    print('Errou!')

