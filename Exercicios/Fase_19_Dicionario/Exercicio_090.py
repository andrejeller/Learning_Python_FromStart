"""

Desafio 090
- Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionario. No final,
mostre o conteúdo da estrutura na tela.

"""

# eu fiz
"""
nome = str(input('Nome: '))
media = float(input('Média: '))


situacao = ''
if media >= 7:
    situacao = 'aprovado'
else:
    situacao = 'reprovado'

aluno = {'nome': nome, 'media': media, 'situacao': situacao}
print(f'O aluno {aluno["nome"]} foi {aluno["situacao"]} com média {aluno["media"]}.')
"""

#ele fez
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média do aluno {aluno["nome"]}:'))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperacao'
else:
    aluno['situacao'] = 'Reprovado'

print('-='*30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')

