"""

Desafio 115
- Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um
arquivo de texto simples

O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

"""

from Exercicios.Fase_23_TratandoErros.Ex115.lib.interface import *
from Exercicios.Fase_23_TratandoErros.Ex115.lib.arquivo import *
from time import sleep

file = 'nomes.txt'

if not arquivoExiste(file):
    criarArquivo(file)

lerArquivo(file)

while True:
    op = menu(['Ver pessoas cadastradas.', 'Cadastrar nova pessoa.', 'Sair do Sistema.'])

    if op == 1:
        titulo('OPÇÃO 1')
        lerArquivo(file)

    elif op == 2:
        titulo('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = lerInt('Idade: ')
        cadastrar(file, nome, idade)

    elif op == 3:
        titulo('Saindo do sistema... Até logo!')
        break

    else:
        print('Opção inválida')

    sleep(2)
