"""
Desafio 039
- Faça um progama que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
'Se ele ainda vai se alistar ao serviço militar.
'Se é a hora de se alistar.
'Se já passou do tempo do alistamento.
Seu programa também severá mostrar o tempo que falta ou que passou do prazo de alistamento.


"""
from datetime import date

ano = int(input('Digite o ano de seu nascimento: '))
atual = date.today().year
idade =  atual - ano

print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
if idade > 18:
    al = atual - (idade - 18)
    print('Você deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em ', al)
elif idade < 18:
    al = atual + (idade - 18)
    print('Você deverá se alistar em {} anos.'.format(18 - idade))
    print('Seu alistamento será em ', al)
else:
    print('Está na época de se alistar!')

