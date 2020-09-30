"""

Desafio 089
- Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar todas as notas de cada
aluno individualmente.

"""

#eu fiz
"""
notas = [0, 0]
aluno = ['', notas[:]]
turma = list()

while True:

    novoA = aluno[:]
    novoA[0] = str(input('Nome: '))
    novoA[1][0] = int(input('Nota 01: '))
    novoA[1][1] = int(input('Nota 02: '))

    turma.append(novoA[:])
    novoA.clear()

    op = str(input('Deseja continuar? [S/N] '))
    if op in 'nN':
        break

print('-'*30)
print('Médias Gerais')
for al in turma:
    media = (al[1][0] + al[1][1]) / 2
    print(f'Nome: {al[0]}, Média: {media}')

print('-'*30)
print('Notas detalhadas')

for al in turma:
    print(f'Nome: {al[0]}, Nota 01: {al[1][0]}, Nota 02: {al[1][1]}')

print('-'*30)
print(turma)
"""

# ele fez

ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'nN':
        break

print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-'*30)
    op = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if op == 999:
        print('FINALIZANDO...')
        break

    if op <= len(ficha) - 1:
        print(f'Notas de ficha {ficha[op][0]} são {ficha[op][1]}')

print('<<< VOLTE SEMPRE >>>')
