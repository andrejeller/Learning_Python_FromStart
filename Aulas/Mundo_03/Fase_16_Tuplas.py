"""
O que foi visto na aula 16.
- Túplas

-- "AS TUPLSA SÃO IMUTAVEIS"
Obs. Só pode alterar os valores em 'tempo de editor', não após dar 'play'.

"""

lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')  # no python novo não precisa mais do parenteses
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[0:4:2])
print(sorted(lanche))  # mostrando a lista em ordem alfabetica

# lanche[1] = 'Refigerante' -- Não funciona pois as tuplas são imutaveis

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(len(lanche)):
    # print(f'Eu vou comer {cont}')
    # print(f'Eu vou comer {lanche[cont]}')
    print(f'Eu vou comer {lanche[cont]} na posicao {cont}')


for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')

a = (2, 5, 4)
b = (5, 8, 1, 2)
print(a)
print(b)
c = a + b
print(c)
print(len(c))
print(c.count(5))  # quantas vezes está aparecendo o numero 5 dentro de C
print(c.index(8))  # em que posicao está o 8 -- retorna o primeiro encontrado


pessoa = ('Gustavo', 39, 'M', 99.88)  # voce poe ter dados de tipos diferentes dentro das tuplas
del(pessoa)  # assim voce pode apagar a tupla.

