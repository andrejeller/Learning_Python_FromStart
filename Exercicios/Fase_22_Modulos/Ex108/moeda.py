# -- Exercicio 108

def metade(preco=0):
    res = preco / 2
    return res


def dobro(preco=0):
    res = preco * 2
    return res


def aumentar(preco=0, porcentagem=0):
    res = preco + (preco * porcentagem/100)
    return res


def diminuir(preco=0, porcentagem=0):
    res = preco - (preco * porcentagem/100)
    return res


def moeda(valor=0, moeda='R$'):
    str = f'{moeda}{valor:>8.2f}'.replace('.', ',')
    return str
