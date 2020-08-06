"""
Desafio 048
- Faça um programa que faça a soma de todos os números ímpares que são multiplos de três e que se encontram no
intervalo de 1 até 500.

"""

# Maneira 01
soma = 0
qtd = 0
for i in range(0, 501):
    if i % 2 == 1 and i % 3 == 0:
        # print(i, end=' ')
        soma += i
        qtd += 1
print('A soma de todos os {} valores solicitados é {}.'.format(qtd, soma))

# Maneira 02
soma = 0
qtd = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        # print(i, end=' ')
        soma += i
        qtd += 1
print('A soma de todos os {} valores solicitados é {}.'.format(qtd, soma))
