"""
Desafio 025
- Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""

nome = str(input('Digite sem nome: '))

print('O nome tem SILVA? {}'.format('SILVA' in nome.upper()))
