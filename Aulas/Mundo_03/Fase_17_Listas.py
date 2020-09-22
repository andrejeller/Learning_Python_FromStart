"""
O que foi visto na aula 17.
- Listas


Tuplas = ()
Listas = []

lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
lanche[3] = 'b'  # Agora sim funciona

lanche.append('cookie')
lanche.insert(0, 'Cachorro Quente')
del lanche[3]
lanche.pop(3)
lanche.remove('pizza')

if 'pizza' in lanche:
    lanche.remove('pizza')

valores = list(range(4, 11))
valores = [4, 5, 6, 7, 8, 9, 10]

valores = list(range(4, 11, 2))
valores = [4, 6, 8, 10]

valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()
valores = [0, 2, 3, 4, 5, 8, 9]
valores.sort(reverse=True)
valoers = [9, 8, 5, 4, 3, 2]
len(valores) = 7

"""



num = [2, 5, 9, 1]
num[2] = 3
# num[4] = 7 # Vai dar erro
num.append(7)
num.sort(reverse=True)
print(num)
num.insert(2, 0)
print(f'Essa lista tem {len(num)} elementos.')
num.pop()
print(num)
num.pop(2)
print(num)
num.insert(2, 2)
print(num)
num.remove(2)  # Vai remover o primeiro valor 2 que ele encontrar
print(num)

if 4 in num:
    num.remove(4)
else:
    print('Não encontrei o numero 4.')

print('-'*10)
# valores = []
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for i, v in enumerate(valores):
    #print(f' {v}...', end=''))
    print(f'Na posicao {i} encontrei o valor {v}.')
print('Cheguei ao final do programa')


# for cont in range(0, 5):
#    valores.append(int(input('Digite um valor: ')))

a = [2, 3, 4, 7]
b = a
b[2] = 8  # OPAAAA olha o ponteiro aí
print(f'Lista A: {a}.')
print(f'Lista B: {b}.')
a[2] = 4  # Voltando ao normal

b = a[:] # B recebe todos os valores de a, criando uma copia
b[2] = 8  # Olha o ponteiro aí
print(f'Lista A: {a}.')
print(f'Lista B: {b}.')

