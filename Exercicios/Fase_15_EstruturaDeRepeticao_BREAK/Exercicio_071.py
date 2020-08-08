"""
Desafio 071
- Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado(numero inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs. considere que o caixa possui cédulsa de R$50, R$20, R$10 e R$1.

"""


print('='*30)
print('{:=^30}'.format('BANCO SUPER'))
print('='*30)

valor = int(input('Quanto voce vai sacar? R$ '))
total = valor

valor_cedula = 50
total_cedula = 0
while True:
    if total >= valor_cedula:
        total -= valor_cedula
        total_cedula += 1

    else:

        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R${valor_cedula}.')

        if valor_cedula == 50:
            valor_cedula = 20

        elif valor_cedula == 20:
            valor_cedula = 10

        elif valor_cedula == 10:
            valor_cedula = 1

        total_cedula = 0
        if total == 0:
            break

print('=' * 30)
print('Volte sempre ao BANCO SUPER! Tenha um bom dia!')
