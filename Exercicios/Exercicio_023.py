"""
Desafio 023
- Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
Ex. Digite um número: 1834
Print: Unidade: 4, Dezena: 3, Centena: 8, Milhar: 1;
"""

num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analizando o número... ')
print('Unidade: {}'.format(u))
print('Centena: {}'.format(d))
print('Dezena:  {}'.format(c))
print('Milhar:  {}'.format(m))

