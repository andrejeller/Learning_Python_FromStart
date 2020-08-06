"""
Desafio 027
- Faça um programa que leia o nome completo completo de uma pessoa, postrando em seguida o primeiro
e o último nome separadamente.

Ex. Aa Maria de Souza
Print: Primeiro: Ana, Ultimo: Souza
"""

nome = str(input('Escreva seu nome completo: ')).strip()

nome = nome.split()
print('Primeiro nome: {}'.format(nome[0]))
print('Ultimo nome: {}'.format(nome[len(nome)-1]))
