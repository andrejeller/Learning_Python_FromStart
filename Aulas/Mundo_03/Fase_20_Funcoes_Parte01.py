"""
O que foi visto na aula 20.
- Funções Parte 01

"""

# Somando dois numeros
"""
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)


def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)
soma(8, 9)
soma(2, 1)

soma(a=4, b=5)  # Forma explicita
soma(b=4, a=5)  # Pode alterar a ordem
"""

# Varios parametros, uma variavel (vira uma Tupla)
"""
# ele cria uma tupla
def contador(*num):
    # print(num)
    for v in num:
        print(v, end=' - ')
    print()

    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
"""

# Usando listas como parametros
# Obs. Toda passagem de parametro é por referencia
"""
def dobrarValores(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobrarValores(valores)
print(valores)
"""


# Somando varios valores em uma funcao
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.')


soma(5, 2)
soma(2, 9, 4)
