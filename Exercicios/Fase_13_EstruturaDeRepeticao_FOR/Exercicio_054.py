"""
Desafio 054
- Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas já
atingiram a maioridade e quantas já são maiores. (20+)

"""
from datetime import date
atual = date.today().year


# O que ele queria
cont_menor = 0
cont_maior = 0
for i in range(0, 7):
    ano = int(input('{}. Digite um ano de nascimento: '.format(i+1)))
    idade = atual - ano
    if idade >= 21:
        cont_maior += 1
    else:
        cont_menor += 1

print('Ao todo tivemos {} pessoas maiores de idade.'.format(cont_maior))
print('E também tivemos {} pessoas menores de idade.'.format(cont_menor))



# O que eu fiz kkk 300 mil vezes mais dificil
lista = []
for i in range(0, 7):
    ano = int(input('{}. Digite um ano de nascimento: '.format(i+1)))
    lista.append(ano)

print(lista)

for i in range(0, 7):
    if atual - lista[i] > 20:
        print('Maior de idade (20+). {}'.format(lista[i]))
    else:
        print('Menor de idade (20-). {}'.format(lista[i]))



