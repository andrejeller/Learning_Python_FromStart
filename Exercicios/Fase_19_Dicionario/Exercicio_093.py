"""

Desafio 093
- Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

"""

# eu fiz
"""
jogador = {
    'nome': str(input('Nome do Jogador: ')),
    'partidas': int(input('Jogou quantas partidas jogou? '))
}

gols = list()
for i in range(0, jogador['partidas']):
    gols.append(int(input(f'Quantos gols ele fez na {i+1} partida? ')))

jogador['gols'] = gols[:]
print('='*30)
print(jogador)

print('='*30)
for k, v in jogador.items():
    print(f'  - O campo {k} tem valor {v}')

print('='*30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas:')
count = 0
for i, v in enumerate(jogador['gols']):
    print(f'  - Na partida {i+1} ele fez {v} gols.')
    count += v

print(f'Foi um total de {count} gols.')
"""

# ele fez
jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for i in range(0, total):
    partidas.append(int(input(f'Quantos gols na partida {i+1}: ')))

# print(partidas)
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-='*30)
print(jogador)

print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')

print('-='*30)
print(f'O Jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i + 1}, fez {v} gols')

print(f'Foi um total de {jogador["total"]} gols.')



print('-='*30)




