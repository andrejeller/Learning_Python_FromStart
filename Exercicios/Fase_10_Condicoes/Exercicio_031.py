"""
Desafio 031
- Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando
R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.


"""

dist = float(input('Qual a distância desta viagem? '))
print('O passagem irá custar ', end='')
valor = 0.0

if dist <= 300.0:
    valor = dist * 0.50
else:
    valor = dist * 0.45
print('R${:.2f}.'.format(valor))
