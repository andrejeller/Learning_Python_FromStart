"""
- Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
Considere: US$1,00 = R$3,27
"""

a = float(input('Digite um valor em R$: '))
real = a / 3.27
print('Com R${:.2} voce pode comprar US${:.2}'.format(real, a))
