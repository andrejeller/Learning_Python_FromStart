"""
Desafio 007
- Desenvolva um programa que leia as duas notas de um aluno, e calcule e mostre a sua média.
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2
print('Tendo as notas {} e {}, sua média é de {:.2}.'.format(n1, n2, media))
