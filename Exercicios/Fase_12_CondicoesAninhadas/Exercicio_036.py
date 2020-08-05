"""
Desafio 036
- Escreva um programa para aprovar um empréstimoo bancário para a compra de uma casa. O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.


"""
valor_casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = float(input('Em quantos anos gostaria de pagar? '))

parcela = valor_casa / (anos * 12)

if parcela > (salario * 0.3):
    print('Empréstimo negado, o valor da parcela (R${:.2f}) excede 30% de seu orçamento/salário.'.format(parcela))
else:
    print('Empréstimo aprovado! O valor da parcela (R${:.2f}) cabe em seu orçamento/salário!'.format(parcela))
