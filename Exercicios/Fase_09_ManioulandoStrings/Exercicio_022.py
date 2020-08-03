"""
Desafio 022
- Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiusculas;
O nome com todas as letras minusculas;
Quantas letras ao todo(sem considerar os espaços);
Quantas letras tem o primeiro nome;
"""

nome = str(input('Escreva seu nome completo: '))
print('Analizando nome...')

print(nome.upper())
print(nome.lower())

print('Seu nome tem {} letras.'.format(len(nome)))
nome2 = nome.strip()
nome2 = nome.replace(' ', '')
print('Seu nome tem {} letras.'.format(len(nome2)))

res = nome.split()
print('O primeiro nome tem {} letras e o ultimo tem {} letras'.format(len(res[0]), len(res[len(res)-1])))
print('{}, {}'.format(res[0], res[len(res)-1]))


# Como o guanabara fez...
nome80 = str(input('Escreva seu nome completo: ')).strip()  # já removendo todos os espços antes e depois
print('Seu nome em maiusculas é ', nome80.upper())
print('Seu nome em minusculas é ', nome80.lower())
print('Seu nome ao todo tem {} letras.'.format(len(nome80) - nome80.count(' ')))
print('Seu primeito nome tem {} letras.'.format(nome80.find(' ')))  # pois o primeiro espaco já divide o primeiro nome
