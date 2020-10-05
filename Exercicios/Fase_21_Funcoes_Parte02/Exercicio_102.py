"""

Desafio 102
- Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
processo de cálculo do fatorial.

"""

# eu fiz
"""
def fatorial(num=0, show=False):
    f = 1
    for i in range(num, 0, -1):
        f *= i
        if show:
            print(i, end=' * ')
    print('FIM')
    return f
"""


# ele fez
def fatorial(num=0, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser clculado.
    :param show: (opicional) Mostrar ou não a conta.
    :return: O valor do Fatorial de NUM
    """
    f = 1
    for i in range(num, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')

        f *= i

    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n, show=True)}.')
print(f'O fatorial de {n} é {fatorial(n, show=False)}.')
print(f'O fatorial de {n} é {fatorial(n)}.')

help(fatorial)
