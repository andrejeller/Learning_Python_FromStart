"""
O que foi visto na aula 13.
- Estrutura de repetição FOR

"""

print('Oi')
print('Oi')
print('Oi')
print('--'*10)


for i in range(1, 6):
    print('Oi')
    # print('FIM')
print('FIM')

for i in range(1, 6):
    print(i)

# 'Contagem Regressiva'
for i in range(6, 0, -1):
    print(i)

# Pulando de 2 em 2
for i in range(2, 6, 2):
    print(i)


print('--'*10)

n = int(input('Digite um número: '))
for i in range(0, n):
    print(i)

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for i in range(inicio, fim, passo):
    print(i)

soma = 0
for i in range(0, 4):
    n = int(input('Digite um número: '))
    soma = soma + n  # soma += n
