"""
Desafio 043
- Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre o status, de acordo
com a tabela abaixo:
'Abaixo de 18.5: Abaixo do peso.
'Entre 18.5 e 25: Peso ideal
'Entre 25 e 30: Sobrepeso
'Entre 30 e 40: Obesidade
'Acima de 40: Obesidade mórbida

"""

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

print('Seu imc é de {:.2f} e você está: '.format(imc), end='')

if imc < 18.5:
    print('Abaixo do peso.')
if 18.5 <= imc < 25:
    print('No peso ideal.')
if 25 <= imc < 30:
    print('Com sobrepeso.')
if 30 <= imc < 40:
    print('Com obesidade.')
else:
    print('Obesidade mórbita.')
