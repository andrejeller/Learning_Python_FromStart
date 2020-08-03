"""
Desafio 035
- Desenvolva um programa que leia o comprimento de três retas e dia ao usuário se elas podem ou não formar um triângulo.

Nota: Cada uma das retas precisa ser menor que a soma das outras duas.

"""
print('-=-'*20)
print('Analizador de Triângulos')
print('-=-'*20)

r1 = float(input('Reta 01: '))
r2 = float(input('Reta 02: '))
r3 = float(input('Reta 03: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas a cima PODEM formar um triângulo')
else:
    print('As retas a cima NÃO PODEM formar um triângulo')