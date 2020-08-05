"""
Desafio 044
- Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:
' À vista dinheiro/cheque: 10% de desconto
' À vista no cartão: 5% de desconto
' Em até 2x no cartão: preço normal
' 3x ou mais no cartão: 20% de juros


"""

preco = float(input('Qual o valor do protudo? R$ '))
print("""Escolha a forma de pagamento:
1. À vista dinheiro/cheque: 10% de desconto
2. À vista no cartão: 5% de desconto
3. Em até 2x no cartão: preço normal
4. 3x ou mais no cartão: 20% de juros """)
forma = int(input('Forma de pagamento: ', ))
novo_valor = preco

if forma == 1:
    novo_valor = preco * 0.90
    #novo_valor = preco - (preco * 10 /100)
elif forma == 2:
    novo_valor = preco * 0.95
    # novo_valor = preco - (preco * 5 /100)
elif forma == 3:
    novo_valor = preco
    parcela = novo_valor / 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros.'.format(parcela))
else:
    novo_valor = preco + (preco * 0.20)
    # novo_valor = preco + (preco * 20 /100)
    parcela = novo_valor / 10
    print('Sua compra será parcelada em até 10x de R${:.2f} com 20% de Juros.'.format(parcela))


print('Valor a ser pago: R$ {}.'.format(novo_valor))
