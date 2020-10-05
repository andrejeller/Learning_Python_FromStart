"""

Desafio 101
- Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.


"""

# eu fiz
"""
from datetime import datetime


def voto(ano):
    idade = datetime.now().year - ano
    print(f'Voce tem {idade} anos e ', end='')
    if idade < 16:
        return 'Voce não pode votar.'
    if 16 <= idade < 18 or idade >= 65:
        return 'Seu voto é opcional!'
    else:
        return 'Seu voto é obrigatorio.'


print(voto(int(input('Digite seu ano de nascimento: '))))
"""

# ele fez


# importando a bib APENAS dentro do contexto/função que será utilizada
def voto(ano):
    from datetime import datetime

    atual = datetime.now().year
    idade = atual - ano
    print(f'Com {idade} anos: ', end='')

    if idade < 16:
        return 'NÃO VOTA.'
    if 16 <= idade < 18 or idade >= 65:
        return 'VOTO OPCIONAL.'
    else:
        return 'VOTO OBRIGATORIO.'


#Programa principal
nasc = int(input('Digite seu ano de nascimento: '))
print(voto(nasc))
