"""
Exercicio 03
- Crie um programa que leia dois numeros e mostre a soma entre eles.
"""

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
print('A soma entre {} e {} vale {} '.format(n1, n2, n1 + n2))
print('A soma entre {0} e {1} vale {2} '.format(n1, n2, n1 + n2))
print('A soma entre {1} e {0} vale {2} '.format(n1, n2, n1 + n2))