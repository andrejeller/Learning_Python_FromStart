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
from time import sleep

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
op = 0

while op != 5:

    print("""O que você quer fazer?
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa """)

    op = int(input('>>>>> Qual a sua opção? '))

    if op == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif op == 2:
        produto = n1 * n2
        print('A resultado de {} x {} é {}'.format(n1, n2, produto))

    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {}, o maior valor é {}.'.format(n1, n2, maior))

    elif op == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))

    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente.')

    print('-='*15)
    sleep(2)
print('Fim do programa! Volte sempre!')
