"""

Desafio 092
- Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionario
se por acaso a CTPS for diferente de ZERO, o dicionario receberá também o ano de contratação e o salario. Calcule
e acresente, além da idade, com quantos anos a pessoa vai se aposentar. (dps de 35 anos trabalhados)

"""

# eu fiz
"""
pessoa = {'nome': str(input('Nome: ')),
          'ano': int(input('Ano de nascimento: ')),
          'ct': int(input('Carteira de trabalho: (se não tiver digite 0) '))
          }

if pessoa['ct'] != 0:
    pessoa['idade'] = 2020 - pessoa["ano"]
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = int(input('Salário R$ '))
    pessoa['aposentadoria'] = (pessoa['contratacao'] + 35) - pessoa['ano']

print('-'*30)
for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}.')
"""

#ele fez
from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
ano =  int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - ano
dados['ct'] =  int(input('Carteira de trabalho: (se não tiver digite 0) '))


if dados['ct'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = int(input('Salário R$ '))
    dados['aposentadoria'] = ((dados['contratacao'] + 35) - datetime.now().year) + dados['idade']

print('-'*30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}.')
