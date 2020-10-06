"""
Desafio 059
- Crie um programa que leia dois valores e mostre um interface na tela:
'[1] Somar
'[2] Multiplicar
'[3] Maior
'[4] Novos números
'[5] Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.

"""


op = 4
n1 = n2 = 0
while op != 5:
    if op == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))

    print("""O que você quer fazer?
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa """)

    op = int(input('>>>> Opção: '))

    if op == 1:
        print('A soma é: ', n1 + n2)
    elif op == 2:
        print('A multiplicação é: ', n1 * n2)
    elif op == 3:
        if n1 > n2:
            print('O maior numero é ', n1)
        else:
            print('O maior numero é ', n2)

    print('=-*15')
