"""
Desafio 049
- Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço FOR.

"""

n = int(input('Digite um numero inteiro: '))

print('-'*13)

for i in range(0, 11):
    print('{} x {:2} = {:2}'.format(n, i, n * i))
print('-'*13)
