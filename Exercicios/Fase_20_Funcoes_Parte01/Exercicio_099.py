"""

Desafio 099
- Faça um programa que tenha uma função chamada maior(), que receba vários parametros com valores inteiros.
Seu programa tem que analizar os valores e dizer qual deles é o maior.

"""

from random import randint

def maior(*valores):
    print('-='*30)
    print(f'{valores} Foram informados {len(valores)} valores ao todo.')
    maior = 0
    for i, v in enumerate(valores):
        if i == 0:
            maior = v
        if v > maior:
            maior = v
    print(f'O maior valor informado foi {maior}.')



maior(12, 8, 3, 8, 9, 2, 60)
maior(3, 8, 10, 7)
maior(3, 90)
maior(4, 2)
maior()