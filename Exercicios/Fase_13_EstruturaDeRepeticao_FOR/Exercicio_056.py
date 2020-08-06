"""
Desafio 056
- Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
'A média de idade do grupo.
'Qual é o nome do homem mais velho.
'Quantas mulheres têm menos de 20 anos.

"""


# Maneira 01
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
count_mulher_20 = 0
for i in range(0, 4):
    print('------ {}ª PESSOA -------'.format(i))
    n = str(input('Digite um nome: ')).strip()
    ida = int(input('Digite uma idade: '))
    s = str(input('Sexo [M/F]: ')).upper()
    soma_idade += ida
    if i == 1 and s in 'Mm':
        maior_idade_homem = ida
        nome_mais_velho = n
    elif s in 'Mm' and ida > maior_idade_homem:
        maior_idade_homem = ida
        nome_mais_velho = n

    if s in 'Ff' and ida < 20:
        count_mulher_20 += 1


media_idade = soma_idade / 4
print('A média de idade do grupo é de {} anos.'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, nome_mais_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(count_mulher_20))



# Maneira 02
nomes = ['']
idades = []
sexos = ['']

soma = 0
id_mais_velho = 0
qnt_mulheres_kids = 0

for i in range(0, 4):
    print('-'*10)
    n = str(input('Digite um nome: '))
    ida = int(input('Digite uma idade: '))
    s = str(input('Sexo [M/F]: ')).upper()
    nomes.append(n)
    idades.append(ida)
    sexos.append(s)


for i in range(0, 4):
    soma += idades[i]
    if sexos[i] == 'M' and idades[i] > idades[id_mais_velho]:
        id_mais_velho = i
    if sexos[i] == 'F' and idades[i] < 20:
        qnt_mulheres_kids += 1

soma = soma / 4

print('='*15)
print('A média de idades é: {}.'.format(soma))
print('O homem mais velho tem {} anos, sendo o {}.'.format(idades[id_mais_velho], nomes[id_mais_velho]))
print('A quantidade de mulheres menores de 20 é {}.'.format(qnt_mulheres_kids))
