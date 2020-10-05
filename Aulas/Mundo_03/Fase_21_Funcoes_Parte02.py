"""
O que foi visto na aula 21.
- Funções Parte 02


# Ajuda interativa
help()
help(print)

print(input.__doc__)
help(input)

# DOCSTRING
Para criar um pequeno manual que aparece ao utilizar o comando help()

# Parametros Opcionais

def somar(a, b, c):
    s = a + b + c

def somar(a, b, c=0):
    s = a + b + c
>> 'c=0' faz com que automaticamente, caso a variavel C não seja informada, ela vire 0

def somar(a=0, b=0, c=0):
>> Assim tambpem funcionaria, caso se chamasse a função sem passar nada. Sem mostrar erro algum.

somar(3, 2, 5)
somar(8, 4) '+ 0'

# Escopo de variaveis
>> Variavel Global x Local

# Retorno de Valores (return)
def somar(a, b, c):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2}, {r3}')

"""

# DOCSTRING
"""
def contador(inicio, fim, passo=1):
    "/""
    -> Faz uma contagem e mostra na tela.
    :param inicio:inicio da contagem
    :param fim: fim da contagem
    :param passo: passo da contagem
    :return: sem retorno
    Função criada por bla bla blalbla!
    "/""
    i = inicio
    if inicio < fim:
        while i <= fim:
            print(i, end=' ')
            i += passo

    print('FIM!')


# help(contador)
# contador(2, 10, 2)

"""

# RETURN
def fatorial(num=1):
    f = 1
    for i in range(num, 0, -1):
        f *= i
    return f


n=1
print(f'O fatorial e {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}.')


def par(n=0):
    if n % 2 ==0:
        return True
    else:
        return False


n = int(input('Digite um número: '))
#print(par(n))
if par(n):
    print('É par!')
else:
    print('Não é par!')

