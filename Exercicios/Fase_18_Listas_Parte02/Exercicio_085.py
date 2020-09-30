"""

Desafio 085
- Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
mantenha separados os valores pares e ímpares. No final, mostre os valores pares e impares em ordem crescente.

"""
"""
pares = list()
impares = list()
numeros = list()

for i in range(7):
    num = int(input('Digite um número: '))

    if num % 2:
        impares.append(num)
    else:
        pares.append(num)


numeros.append(pares)
numeros.append(impares)
print(numeros)
"""
# ele fez
numeros = [[], []]

for i in range(7):
    num = int(input('Digite um número: '))

    if num % 2:
        numeros[0].append(num)
    else:
        numeros[1].append(num)


print(numeros[0])
print(numeros[1])
