"""
Desafio 069
- Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntra
de o usuário quer ou não continuar. No final, mostre:
'A Quantas pessoas tem mais de 18 anos.
'B Quantos homens foram cadastrados.
'C Quantas mulheres tem menos de 20 anos.

"""

cont_maior18 = cont_homens = cont_mulheres20 = 0
coon_total = 0

print('=' * 30)
print('{CADASTRO SIMPLES')

while True:

    print('-' * 30)

    nome = str(input('Digite o nome: ')).strip()

    sexo = ''
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]

    idade = int(input('Digite a idade: '))

    if idade > 18:
        cont_maior18 += 1

    if sexo in 'Mm':
        cont_homens += 1

    if sexo in 'Ff' and idade < 20:
        cont_mulheres20 += 1

    op = ''
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]

    if op in 'Nn':
        break

print(f'Voce cadastrou {cont_maior18} pessoas maiores de 18 anos, ', end='')
print(f'{cont_homens} homens, e {cont_mulheres20} mulheres menor de 20 anos')
