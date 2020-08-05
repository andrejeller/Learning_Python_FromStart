"""
Desafio 045
- Crie um prgrama que faça o computador jogar JOKENPÔ com você.


"""

import random
from time import sleep
lista = ['Pedra', 'Papel', 'Tesoura']


print(""" .... VAMOS JOGAR PEDRA PAPEL E TESOURA....""")
print("""ESCOLHA:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
""")

jogador = int(input('Sua Escolha: '))
computador = random.randint(1, 3)

sleep(1)
print('PEEEDRA...', end=' ')
sleep(1)
print('PAAPEL...', end=' ')
sleep(1)
print('TESOUURA...')
sleep(1)

print('Eu escolhi {} e voce {}, portanto'.format(lista[computador - 1], lista[jogador - 1]), end=' ')

# Maneira 01
if computador == 1:  # Computador jogou pedra
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCE GANHOU')
    elif jogador == 3:
        print('EU GANHEI')
    else:
        print('Jogada Invalida')
elif computador == 2:
    if jogador == 1:
        print('GANHEI')
    elif jogador == 2:
        print('EMPATE')
    elif jogador == 3:
        print('VOCE GANHOU')
    else:
        print('Jogada Invalida')
elif computador == 3:
    if jogador == 1:
        print('VOCE VENCEU')
    elif jogador == 2:
        print('EU VENCI')
    elif jogador == 3:
        print('EMPATE')
    else:
        print('Jogada Invalida')

"""
# Maneira 02
if player == 1 and pc == 1:
    print('EMPATAMOS.')
elif player == 1 and pc == 2:
    print('eu ganhei.')
elif player == 1 and pc == 3:
    print('você ganhou.')

elif player == 2 and pc == 1:
    print('voce ganhou.')
elif player == 2 and pc == 2:
    print('EMPATAMOS.')
elif player == 2 and pc == 3:
    print('eu ganhei.')

elif player == 3 and pc == 1:
    print('eu ganhei.')
elif player == 3 and pc == 2:
    print('você ganhou.')
elif player == 3 and pc == 3:
    print('')
"""