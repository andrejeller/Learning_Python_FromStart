"""
Desafio 024
- Crie um programa que leia um nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""

nome = str(input('Digite o nome de uma cidade: '))
nome2 = nome

nome = nome.upper().split()
print('Comeca com "SANTO"? {}'.format('SANTO' in nome[0]))
#print(nome)

# OU
print(nome2[:5].upper() == 'SANTO')
# SANTO sempre vai ter 5 letras, então sendo a primeira palavra é facil de comparar
