"""
Desafio 013
- Faça um algorítimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

a = float(input('Salario: '))
aumento = a * 1.15
print('O novo valor do se salario com 15 de aumento é de R${:.2}.'.format(aumento))
