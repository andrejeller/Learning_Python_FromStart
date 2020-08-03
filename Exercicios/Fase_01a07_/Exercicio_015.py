"""
Desafio 015
- Escreve um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado. Calcula o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

dias = int(input('Quantos dias foi alugado?: '))
km = float(input('Quantos Km rodados?: '))

valor = (60 * dias) + (0.15 * km)
print('Por ter rodado {}Km em {} dias, você precisa pagar {:.2f}'.format(km, dias, valor))

