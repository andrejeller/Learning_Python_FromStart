"""
Desafio 033
- Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


"""
#n1, n2, n3 = 0

# GUANABARA 01 ------------------------------------
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))

if a < b and a < c:
    menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c

if a > b and a > c:
    maior = a
if b > c and b > a:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor digitado foi, ', menor)
print('O maior valor digitado foi, ', maior)
print('-'*50)
# GUANABARA 02 ------------------------------------
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c


maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c


print('O menor valor digitado foi, ', menor)
print('O maior valor digitado foi, ', maior)
print('-'*50)

# MEU ------------------------------------
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

lista = [n1, n2, n3]

lista.sort()
# print(lista)

print('O menor número da lista é ', lista[0])
print('O maior número da lista é ', lista[len(lista) - 1])
print('-'*50)

