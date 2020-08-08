"""
Desafio 061
- Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while.


-- Desafio 051
---- Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
----- dessa progressão.

"""

print('Gerador de PA')
print('-='*10)

# 01
n1 = int(input('Digite o primeiro numero da PA: '))
r = int(input('Digita a razão desta PA: '))
contador = n1

while contador < (n1 + (10*r)):
    print(contador, end=' -> ')
    contador += r

print('ACABOU')


# 02

n1 = int(input('Digite o primeiro numero da PA: '))
r = int(input('Digita a razão desta PA: '))
contador = 1
termo = n1

while contador <= 10:
    print(termo, end=' -> ')
    termo += r
    contador += 1

print('ACABOU')
