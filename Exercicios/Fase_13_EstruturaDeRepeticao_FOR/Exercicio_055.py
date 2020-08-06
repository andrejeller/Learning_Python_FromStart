"""
Desafio 055
- Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

"""
# Maneira 01
peso = float(input('Digite seu peso (Kg): '))
maior = peso
menor = peso

for i in range(0, 4):
    peso = float(input('Digite seu peso (Kg): '))
    if peso < menor:
        menor = peso
    if peso > maior:
        maior = peso

# Maneira 02
for i in range(0, 4):
    peso = float(input('Digite seu peso (Kg): '))

    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso

print('O maior peso encontrado foi {}Kg. \nE o menor peso encontrado foi {}Kg.'.format(maior, menor))
