"""
Desafio 050
- Desenvolva um programa que leia seis números inteiros e mostre a soma de apenas aqueles que forem pares.
Se o valor for ímpar, desconsidere-o.

"""

soma = 0
cont = 0
for i in range(0, 6):
    n = int(input('Digite o {}° numero: '.format(i+1)))
    if n % 2 == 0:
        soma += n
        cont += 1

print('Você informou {} números pares e a soma foi {}.'.format(cont, soma))
