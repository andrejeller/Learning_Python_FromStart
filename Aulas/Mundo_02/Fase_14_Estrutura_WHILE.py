"""
O que foi visto na aula 13.
- Estrutura de repetição WHILE

"""

# antes
for i in range(1, 10):
    print(i)
print('FIM')

# agora
i = 1
while i < 10:
    print(i)
    i += 1
print('FIM')

# exemplo
n = 1

for i in range(1, 5):
    n = input('Digite um número: ')
print('FIM')

while n != 0:
    n = int(input('Digite um número: '))
print('FIM')

r = ''
while r != 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ').upper())
print('FIM')


n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1

print('Acabou \n Voce digitou {} numeros pares e {} impares {}.'.format(par, impar))
