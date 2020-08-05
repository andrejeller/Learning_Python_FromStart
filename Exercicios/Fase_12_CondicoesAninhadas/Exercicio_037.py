"""
Desafio 037
- Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
Print: 1. para binário; 2. para octal; 3. para hexadecimal.

Obs. Foi colocado [2:] nas strings de saída para 'recortar' os dois primeiros caracteres
"""

num = int(input('Digite um número: '))
print("""Escolha uma base de conversão:
1. Binário
2. Octal
3. Hexadecimal
""")
base = int(input('Sua opção: '))

if base == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida.')
