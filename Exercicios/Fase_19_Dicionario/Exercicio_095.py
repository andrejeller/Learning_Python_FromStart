"""

Desafio 095
- Aprimore o DESAFIOA 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
de aproveitamento de cada jogador.

"""

# eu fiz
"""
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    partidas.clear()

    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for i in range(0, total):
        partidas.append(int(input(f'>> Quantos gols na partida {i+1}: ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)

    time.append(jogador.copy())

    while True:
        op = str(input('Quer continuar? [S/N] ')).upper()[0]
        if op in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')

    if op == 'N':
        break

# print(time)

print('=='*30)
print(f'{"cod":3} {"nome":15} {"gols":15} {"total":15}')
print('--'*30)
for i, jo in enumerate(time):
    print(f'{str(i):>3} {str(jo["nome"]):15} {str(jo["gols"]):15} {str(jo["total:15"])}')

print('--'*30)
while True:

    op = int(input('Mostrar dados de qual jogador? (999 para parar)) '))
    if op == 999:
        break
    else:
        print(f'DADOS DE {time[op]["nome"]}:')
        #for i, g in time[op]['gols']:
        #    print(f'No jogo {i+1} fez {g} gols.')



print('-='*30)
"""

# ele fez
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    partidas.clear()

    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for i in range(0, total):
        partidas.append(int(input(f'>> Quantos gols na partida {i + 1}: ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)

    time.append(jogador.copy())

    while True:
        op = str(input('Quer continuar? [S/N] ')).upper()[0]
        if op in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')

    if op == 'N':
        break

# print(time)

print('==' * 30)
print(f'{"cod":3}', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')

print('')
print('--' * 30)
for i, jo in enumerate(time):
    print(f'{str(i):>3}', end=' ')
    for d in jo.values():
        print(f'{str(d):<15}', end='')
    print('')
print('--' * 30)
while True:

    op = int(input('Mostrar dados de qual jogador? (999 para parar)) '))
    if op == 999:
        break
    if op >= len(time):
        print('ERRO! Não existe jogados com codigo ', op)
    else:
        print(f'DADOS DE {time[op]["nome"]}:')
        for i, g in enumerate(time[op]['gols']):
            print(f'No jogo {i+1} fez {g} gols.')
    print('--'*30)

print('-=' * 30)
print('<< VOLTE SEMPRE >>')
