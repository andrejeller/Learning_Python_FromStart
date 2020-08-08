"""
Desafio 065
- Crie um programa que leia vários números pelo teclado. No final da execução, mostre a média entre todos
os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou
não continuar a digitar valores.

"""

cont = soma = media = maior = menor = 0
continua = ''

while continua != 'N':
    num = int(input('Digite um numero: '))
    if cont == 0:
        menor = maior = num
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num

    soma += num
    cont += 1
    continua = str(input('Quer continuar: [S/N] ').upper().strip()[0])


media = soma / cont
print('Voce somou {} numeros, sendo {} o maior e {} o menor.'.format(cont, maior, menor))
print('E a média entre eles é {}.'.format(media))
