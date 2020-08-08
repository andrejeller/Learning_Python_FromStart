"""
Desafio 064
- Crie um programa que leia vários numeros inteiros pelo teclado. O programa só vai parara quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a
soma entre eles(desconsiderando o flag '999').


"""

cont = -1
soma = 0
num = 0

while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um numero: '))

print('Voce digitou {} numeros e a soma deles é {}.'.format(cont, soma))
