"""
Desafio 063
- Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de
uma Sequência de Fibonacci.
Ex: 0 -> 1 -> 1-> 2 -> 3 -> 5 -> 8


"""

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)

n = int(input('Quantos termos vocÊ quer mostar: '))

t1 = 0
t2 = 1
cont = 0
print('~'*30)
print(' {} -> {} -> '.format(t1, t2), end='')
while cont < n:
    t3 = t1 + t2
    print(' {} -> '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1

print('FIM')
print('~'*30)

# 02
n = int(input('Quantos termos vocÊ quer mostar: '))
contador = 0

atual = 0
anterior = 1

while contador < n:
    contador += 1
    print(atual, end=' -> ')
    aux = atual
    atual = atual + anterior
    anterior = aux

print('ACABOU')