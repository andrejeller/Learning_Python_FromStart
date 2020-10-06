# eu fiz
"""
def leiaDinheiro(pergunta):
    while True:
        valor = str(input(pergunta)).strip().replace(',', '.')
        decimal = '0'

        if '.' in valor:
            decimal = '0' + valor[valor.find('.'):]
            valor = valor[:valor.find('.')]
            #print(valor)

        if valor.isnumeric():
            res = float(valor) + float(decimal)
            print(res)
            break
        else:
            print(f'ERRO: {valor} é um preço invalido!')

    return valor

"""

# ele fez
def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()

        if entrada.isalpha() or entrada == '' or entrada.isalnum():
            print(f'\033[0:31m ERRO: \"{entrada}\" é um preço invalido. \033[m')
        else:
            valido = True
            return float(entrada)



