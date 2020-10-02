"""

Desafio 094
- Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
todos os dicionarios em uma lista. No final, mostre:
'A. Quantas pessoas foram cadastradas.
'B. A média de idade do grupo.
'C. Uma lista com todas as mulheres.
'D. Uma lista com todas as pessoas com idade acima da média.

"""

# eu fiz, quase tudo
"""
todos = list()
pessoa = dict()

while True:

    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: '))
    pessoa['idade'] = int(input('Idade: '))
    todos.append(pessoa.copy())
    pessoa.clear()

    op = str(input('Quer continuar? [S/N] '))
    if op in 'nN':
        break

print(f'Voce cadastrou {len(todos)} pessoas.')
print(f'A média de idade é {0}.')
print(f'')
print(f'')
"""

# ele fez
pessoa = dict()
galera = list()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        op = str(input('Quer continuar? [S/N] ')).upper()[0]
        if op in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')

    if op == 'N':
        break

print('--'*30)
print(galera)

print(f'A) Ao todo tamos {len(galera)} pessoas cadastradas.')

media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos')

print(f'C) As mulheres foram ', end='')
for p in galera:
    if p['sexo'] in 'fF':
        print(f'{p["nome"]}', end=', ')



print(f'\nD) Lista das pessoas que estão com a idade a cima da média:  ')
for p in galera:
    if p['idade'] > media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}', end='; ')
        print('')
print('<<< ENCERRADO >>>')