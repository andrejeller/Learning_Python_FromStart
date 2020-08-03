"""
Desafio 029
- Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.


"""

vel = float(input('Qual a velocidade do carro? '))

if vel > 80.0:
    print('Ele está muito rápido, foi multado!', end=' ')
    multa = (vel - 80.0) * 7
    print('Sua multa será de R${:.2f}.'.format(multa))
else:
    print('Tudo certo por aqui!')

