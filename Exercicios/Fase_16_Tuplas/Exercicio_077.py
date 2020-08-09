"""
Desafio 077
- Crie um programa que tenha uma tupla com várias palavras(não usar acentos). Depois disso, você deve mostrar,
para cada palavra, quais são as vogais.
"""


contagem = ('UM', 'DOIS', 'TRES', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ',
            'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')

for palavra in contagem:
    print(f'Para palavra {palavra.upper()} tem - ', end='')
    for vogal in 'AEIOU':
        if vogal.upper() in palavra.upper():
            print(vogal, end=' ')
    print('')
