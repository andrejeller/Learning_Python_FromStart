"""
Desafio 060
- Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex. 5! = 5x4x3x2x1 = 120

"""
# 01
num = int(input('Digite um número: '))
soma = num
while num > 1:
    num -= 1
    soma = soma * num

print(num, '! é ', soma)

#02
print('-'*15)
num = int(input('Digite um número: '))
fat = num
print('Calculando {}!'.format(num))
while num > 1:
    #print('{} x '.format(num), end='')
    print('{}'.format(num), end='')
    print(' x ' if num > 1 else ' = ', end='')

    num -= 1
    fat = fat * num

print(fat)
