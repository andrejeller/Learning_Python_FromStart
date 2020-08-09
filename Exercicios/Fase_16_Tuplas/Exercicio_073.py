"""
Desafio 073
- Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem
de colocação. Depois mostre:
'A) Apenas os 5 primeiros colocados
'B) Os útimos 4 colocados da tabela.
'C) Uma lista com os times em ordem alfabética.
'D) Em que posição na tabela está o time da Chapecoense.
"""

colocados = ('UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ',
            'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')


print(f'As primeira CINCO colocados são: {colocados[0:5]}')
print(f'Os ultimos QUATRO colocados são: {colocados[-4:]}')
print(f'Times em ordem alfabetica: {sorted(colocados)}')
index = colocados.index('ONZE') + 1
print(f'Tipo chapecoense está na pocisão: {index}')

#OU

print(f'Tipo chapecoense está na pocisão: {colocados.index("ONZE") + 1}') # ELE ENTENDE AS ASPAS DUPLAS
