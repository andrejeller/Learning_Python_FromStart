"""

Desafio 091
- Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionario. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

"""
"""
from random import randint
from time import sleep
jogador = dict()
todos = list()

print('Jogando o dado: ')
for i in range(1, 5):
    tirou = randint(1, 6)
    jogador = {'nome': f'jogador{i}', 'valor': tirou}
    todos.append(jogador.copy())
    print(f'- O {jogador["nome"]} tirou {jogador["valor"]}.')
    sleep(1)

print('Ranking: ')
# parei por aqui, na parte de ordenar

print('')
"""

from time import sleep
from random import randint
from operator import itemgetter
jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
ranking = dict()  # vira uma list()

print('Valores sorteador: ')
for k, v in jogo.items():
    print(f'{k} tirou valor {v} no dado.')
    sleep(0.5)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('='*30)
print('=== RANKING DOS JOGADORES ===')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.5)

print(ranking)
