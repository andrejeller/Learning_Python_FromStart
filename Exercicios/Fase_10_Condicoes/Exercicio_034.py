"""
Desafio 034
- Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
superiores a R$1.200,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento será de 15%.


"""


salario = float(input('Qual o seu salário? '))

if salario > 1200.0:
    aumento = salario * 0.10
    print('Por ter um salario alto, seu aumento será de 10%. Ficando: R${:0.2f}'.format(salario + aumento))
else:
    aumento = salario * 0.15
    print('Por ter um salario baixo, seu aumento será de 15%. Ficando: R${:0.2f}'.format(salario + aumento))


