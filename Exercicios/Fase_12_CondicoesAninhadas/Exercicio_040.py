"""
Desafio 040
- Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
com a média atingida:
'Média abaixo de 5.0: REPROVADO
'Média entre 5.0 e 6.9: RECUPERAÇÃO
'Média superior a 7.0: APROVADO


"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media > 7.0:
    print('APROVADO')
elif 5.0 <= media < 7.0:
    print('RECUPERAÇÃO')
elif media >= 7.0:
    print('REPROVADO')

