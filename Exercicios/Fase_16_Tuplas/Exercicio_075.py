"""
Desafio 075
- Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
'A) Quantas vezes apareceu o valor 9.
'B) Em que posição foi digitado o primeiro valor 3.
'C) Quais foram os números pares.
"""

"""
a = int(input('Digite um numero: '))
b = int(input('Digite um numero: '))
c = int(input('Digite um numero: '))
d = int(input('Digite um numero: '))
tupla = (a, b, c, d)


for i in range(0, len(tupla)):
    if tupla[i] == 9:
        cont_num9 += 1

print(f'Voce digitou {cont_num9} numeros 9.')

if 3 in tupla:
    pos_num3 = tupla.index(3)
    print(f'O primeiro numero 3 está na pos {pos_num3}')
else:
    print('Voce não digitou nenhum numero 3.')


print('E os numeros pares são - ', end='')
for num in tupla:
    if num % 2 == 0:
        print(str(num) + ' ', end='')

"""
cont_num9 = 0
pos_num3 = 0

tupla = (int(input('Digite um numero: ')),
        int(input('Digite um numero: ')),
        int(input('Digite um numero: ')),
        int(input('Digite um numero: ')))

print(f'Voce digitou os valores {tupla}.')
print(f'O valor 9 aparece {tupla.count(9)} vezes.')

if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posicao.')
else:
    print('O valor 3 não foi digitado em nenhuma posicao.')

print('Os valores pares digitados foram ', end='')

for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')


