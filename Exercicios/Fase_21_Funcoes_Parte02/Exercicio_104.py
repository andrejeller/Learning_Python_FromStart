"""

Desafio 104
- Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só
que fazendo a validação para aceitar apenas um valor numérico.
Ex. n = leiaInt('Digite um numero: ')

"""


def leiaInt(str):
    while True:
        n = input(str)
        if n.isnumeric():
            n = int(n)
            return n  # f'{n} é um numero.'

        else:
            print(f'\033[0;31mERRO! --{n}-- não é um número.\033[m')


n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o número {n}.')

