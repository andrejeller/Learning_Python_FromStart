"""
Desafio 051
- Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão.

"""

n1 = int(input('Digite o primeiro numero da PA: '))
r = int(input('Digita a razão desta PA: '))

# Calculo do N° termo -- N = primeiro + (N-1) * razão
for i in range(n1, n1 + (10 * r), r):
    print(i, end=' -> ')
print('ACABOU')
