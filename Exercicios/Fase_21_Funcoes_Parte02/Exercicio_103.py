"""

Desafio 103
- Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

"""

# eu fiz
"""
def ficha(nome='<sem nome>', gols=0):
    return f'O jogador {nome} fez {gols} gols.'


nome = input('Digite o nome do jogador: ')
gols = input('Quantos gols ele fez? ')

if len(nome) == 0 and len(gols) == 0:
    print(ficha())

elif len(nome) == 0:
    print(ficha(gols=int(gols)))

elif len(gols) == 0:
    print(ficha(nome=nome))
"""


# ele fez
def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome = str(input('Digite o nome do jogador: '))
g = str(input('Quantos gols ele fez? '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if nome.strip() == '':
    ficha(gols=g)
else:
    ficha(nome, g)
