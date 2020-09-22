"""
Desafio 080
- Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já
na posição correta de inserção(sem usar o sort()).

"""
""" # Eu Fiz
lista = list()
num = int(input('Insira um numero na lista: '))
lista.append(num)

for i in range(5):
    print('---- Lista atual: ', lista)
    num = int(input('Insira um numero na lista: '))

    inserido = False
    for j, n in enumerate(lista):
        if num <= n:
            lista.insert(j, num)
            inserido = True
            break
        else:
            continue

    if not inserido:
        lista.append(num)
"""

# Ele fez
lista = []
for i in range(0, 5):
    n = int(input('Insira um numero na lista: '))

    if i == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1

print('-'*30)
print(f'Os valores digitados em ordem foram {lista}.')