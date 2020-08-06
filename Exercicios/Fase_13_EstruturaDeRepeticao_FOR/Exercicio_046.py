"""
Desafio 046
- Faça um programa que mostre na tela uma contagem regressiva para estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.

"""
from time import sleep
#import emoj

print('-='*50)

print('... ', end='')
for i in range(10, -1, -1):
    print('{} ... '.format(i), end='')
    sleep(1)

print('')
print('-='*50)
print('------    FELIZ ANO NOVOOO!!!!!   ---------')
