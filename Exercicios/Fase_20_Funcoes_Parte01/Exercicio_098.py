"""

Desafio 098
- Faça um programa que tenha uma função chamada contador(), que receba três parametros: inicio, fim e passo e realize
a contagem.
Seu programa tem que realizar três contagens através da função criada:
'A. De 1 até 10, de 1 em 1
'B. De 10 até 0, de 2 em 2
'C. Uma contagem personalizada.

"""

from time import sleep


def contador(inicio, fim, passo):
    print('-='*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')

    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1

    i = inicio
    if inicio < fim:
        while i <= fim:
            print(i, end=' ')
            sleep(0.2)
            i += passo
    else:
        while i >= fim:
            print(i, end=' ')  # Parece ter um bug que se precisa disso -> print(i, end=' ', flush=True)
            sleep(0.2)
            i -= passo

    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*30)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
