"""
O que foi visto na aula 10.
- Condições (Parte 01)

-----
tempo = int(input('Quantos anos tem seu carro?'))
if tempo<=3:
    print('carro novo')
else:
    print('carro velho')

print('--FIM--')

-----
tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo' if tempo<=3 else 'carro velho')
print('--FIM--')

"""


nome = str(input('Qual é seu nome? '))
if nome == 'Andre':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')

print('Bom dia, {}!'.format(nome))

n1 = float(input('Digita a primeira nota: '))
n2 = float(input('Digita a segunda nota: '))
m = (n1 + n2)/2
print('A média foi {:.1f}'.format(m))

if m >= 6.0:
    print('Sua média é boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

print('PARABÉNS' if m>= 6.0 else 'ESTUDE MAIS')