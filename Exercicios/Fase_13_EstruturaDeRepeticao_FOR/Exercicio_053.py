"""
Desafio 053
- Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

Obs. podemos usar frase.strip().replace(' ', '') OU
palavras = frase.split() -- separa em array
juntando = ''.join(palavras) -- junta o array

"""

frase = str(input('Digite uma frase: ').strip().replace(' ', '').upper())

ao_contrario = ''

# Maneira 01
for i in range(len(frase), 0, -1):
    ao_contrario += frase[i - 1]

# Maneira 02 - fatiamento do python
inverso = frase[::-1]


#print(frase)
#print(ao_contrario)

if frase == ao_contrario:
    print('É um palíndromo!')
else:
    print('NÃO é um palíndromo. :(')