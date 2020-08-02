"""
Desafio 014
- Escreve um programa que converta uma temperatura digitada em °C para °F.
"""

c = float(input('Qual a temperatuda em °C?: '))
f = ((9 * c) / 5) + 32.0
print('A temperatuda de {}°C corresponde a {}°F'.format(c, f))
