"""

Desafio 088
- Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

"""
# eu fiz
"""
import random
from time import sleep

print('-'*40)
print('{:^40}'.format('MEGA SENA'))
print('-'*40)


jogos = int(input('Quantos jogos quer sortear? '))
jogada = list()

for i in range(jogos):
    for num in range(6):
        rand = random.randint(1, 60)
        while rand in jogada:
            rand = random.randint(1, 60)

        jogada.append(rand)

    print('Jogo ', i+1, ' - ', jogada)
    jogada.clear()
    sleep(1)

print('-'*40)
"""

# ele fez
from random import randint
from time import sleep

print('-' * 40)
print('{:^40}'.format('MEGA SENA'))
print('-' * 40)

lista = list()
jogos = list()

quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1

while total <= quantidade:

    count = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            count += 1

        if count >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print('-=' * 4, f'SORTEANDO {quantidade} JOGOS', '-=' * 4)
for i, jogo in enumerate(jogos):
    print(f'Jogo {i+1}: {jogo}')
    sleep(1)

print('-' * 40)
print('-='*5, '< BOA SORTE! >', '-='*5)
