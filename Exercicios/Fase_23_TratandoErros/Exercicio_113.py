"""

Desafio 113
- Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um
número inválido. Aproveite e crie também uma função leiaFloar() com a mesma funcionalidade.

"""


def leiaInt(msg):
    while True:

        try:
            num = int(input(msg))

        except (ValueError, TypeError):
            print(f'\033[0;31mERRO! Número inválido.\033[m')

        else:
            return num  # f'{n} é um numero.'


def leiaFloat(msg):
    while True:

        try:
            num = float(input(msg))

        except:
            print(f'\033[0;31mERRO! Número inválido.\033[m')

        else:
            return num  # f'{n} é um numero.'


n = leiaInt('Digite um numero inteiro: ')
g = leiaFloat('Digite um real: ')
print(f'Voce acabou de digitar o número {n} e {g}.')
