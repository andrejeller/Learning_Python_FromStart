"""
Desafio 058
- Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

-- Desafio 028
--- "Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para
---- o usuário tentar descobrir qual foi o número escolhido pelo computador.
---- O programa deverá escrever na tela se o usuário venceu ou perdeu."

"""


import random
from time import sleep

rand = random.randint(0, 10)
n = -1
palpites = 0

print('Sou seu computadpr... Acabei de pensar em um núdemro entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')

while rand != n:
    n = int(input('Qual é o seu palpite?: '))
    palpites += 1

    if rand > n:
        print('Mais... Tente mais uma vez.')
    elif rand < n:
        print('Menos... Tente mais uma vez.')


print('Acertou com {} tentativas. Parabéns! '.format(palpites))
