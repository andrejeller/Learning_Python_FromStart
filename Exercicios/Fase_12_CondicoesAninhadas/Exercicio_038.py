"""
Desafio 038
- Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
Print: 'O primeiro valor é maior'; 'O segundo valor é maior'; 'Não existe valor maior, os dois são iguais'


"""

n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha outro número: '))

if n1 > n2:
    print('O primeiro número é maior!')
elif n2 > n1:
    print('O segundo número é maior!')
else:
    print('Os números são iguais!')
