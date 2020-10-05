"""

Desafio 105
- Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionario
com as seguntes informações.
' Quantidade de notas
' A maior nota
' A menor nota
' A média da turma
' A situação (opcional)

Adicione também as docstrings da função

"""

# eu fiz
"""
def notas(*nots, sit=False):
    # print(nots, sit)

    maior = menor = soma = 0
    for i, no in enumerate(nots):
        soma += no
        if i == 0:
            maior = no
            menor = no
        else:
            if no > maior:
                maior = no
            if no < menor:
                menor = no
    media = soma / len(nots)

    if sit:
        if media < 6:
            situacao = 'RUIM'
        elif 6 <= media < 7:
            situacao = 'BOA'
        else:
            situacao = 'MUITO BOA'

        return {'quantidade': len(nots), 'maior': maior, 'menor': menor, 'media': media, 'situacao': situacao}
    else:
        return {'quantidade': len(nots), 'maior': maior, 'menor': menor, 'media': media}


print(notas(2, 5, 1, 5.1, 10, 10, 10, 10, 10, sit=True))
print(notas(2, 5, 1, 5.1, 10, 10, sit=True))
print(notas(2, 5, 1, 5.1, 10, sit=True))
print(notas(2, 5, 1, 5.1, sit=True))
"""


# ele fez
def notas(*nots, sit=False):
    """
    -> Função para analizar notas e situações de vários alunos.
    :param nots: uma ou mais notas de alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return:dicionário com várias informações sobre a situação da turma
    """

    r = dict()
    r['total'] = len(nots)
    r['maior'] = max(nots)
    r['menor'] = min(nots)
    r['media'] = sum(nots) / len(nots)

    if sit:
        if r['media'] < 6:
            r['situacao'] = 'RUIM'
        elif 6 <= r['media'] < 7:
            r['situacao'] = 'BOA'
        else:
            r['situacao'] = 'MUITO BOA'

    return r


print(notas(2, 5, 1, 5.1, 10, 10, 10, 10, 10, sit=True))
print(notas(2, 5, 1, 5.1, 10, 10, sit=True))
print(notas(2, 5, 1, 5.1, 10))
print(notas(2, 5, 1, 5.1, sit=False))

help(notas)
