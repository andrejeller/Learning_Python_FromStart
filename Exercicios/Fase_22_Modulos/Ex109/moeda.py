# -- Exercicio 109

def metade(preco=0, format=True):
    res = preco / 2
    if format:
        return moeda(valor=res)
    return res


def dobro(preco=0, format=True):
    res = preco * 2
    return res if format is False else moeda(valor=res)
    # retorne res SE format for Falso, SE NÃO retorne moeda(res)


def aumentar(preco=0, porcentagem=0, format=True):
    res = preco + (preco * porcentagem/100)
    return res if not format else moeda(valor=res)


def diminuir(preco=0, porcentagem=0, format=True):
    res = preco - (preco * porcentagem/100)
    if format:
        return moeda(valor=res)
    return res


def moeda(valor=0.0, moeda='R$'):
    str = f'{moeda}{valor:.2f}'.replace('.', ',')
    return str
