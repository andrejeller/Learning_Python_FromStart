"""
Desafio 068
- Faça um programa que jogue par ou ímpar com o computador. O jogo será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

"""
from random import randint

total_vitorias = 0

while True:
    print('='*30)
    print('JOGUE PAR OU IMPAR')
    print('-'*30)

    pc = randint(0, 10)
    num = int(input('Digite um número: '))
    joga = str(input('Escolha PAR ou IMPAR [P/I]: ')).upper().strip()[0]

    soma = pc + num
    print(f'Voce jogou {num} e o computador {pc}. Total = {soma}')

    if soma % 2 == 0 and joga in 'Pp':
        total_vitorias += 1
        print('Parabens! Voce ganhou, eu tinha pensado em ', pc)

    elif soma % 2 == 1 and joga in 'Ii':
        total_vitorias += 1
        print('Parabens! Voce ganhou, eu tinha pensado em ', pc)

    else:
        break

    print(f'voce jogou {num} e o computador {pc}. Total = {soma}')
"""
    if joga in 'Pp' and pc % 2 == 0:
        total_vitorias += 1
        print('Parabens! Voce ganhou, eu tinha pensado em ', pc)
    elif joga in 'Ii' and pc % 2 == 1:
        total_vitorias += 1
        print('Parabens! Voce ganhou, eu tinha pensado em ', pc)

"""
print('')
print('=-'*30)
print('FIM DE JOGO')
print(f'Voce jogou bem e teve {total_vitorias} vitorias.')
