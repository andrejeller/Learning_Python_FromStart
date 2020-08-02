"""
Desafio 013
- Faça um algorítimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

salario = float(input('Salario: '))
aumento = salario * 1.15  # jeito 1
aumento2 = salario + (salario * 15 / 100)  # jeito 2
print('O novo valor do se salario com 15% de aumento é de R${:.2f}.'.format(aumento))
