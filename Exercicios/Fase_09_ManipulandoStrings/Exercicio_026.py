"""
Desafio 026
- Faça um programa que leia uma frase pelo teclado e mostre:

Quantas vezes aparece a letra "A".
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a última vez.
"""

frase = str(input('Digite uma pequena frase: ')).lower().strip()
print('A letra ~A~ aparece {} vezes.'.format(frase.count('a')))
print('A primeira letra ~A~ aparece no {}° caractere.'.format(frase.find('a') + 1))
print('A última letra ~A~ aparece no {}° caractere'.format(frase.rfind('a')+1))  # RFIND .. começa a contagem da DIREITA É GENIAL
