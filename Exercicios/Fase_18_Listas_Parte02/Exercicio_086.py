"""
Desafio 086
- Faça um programa que crie uma matriz de dimenção 3x3 e preencha com valores lidos pelo teclado.
No final mostre a matriz na tela com a formatação correta.
0 |_|_|_| [1][2][3]
1 |_|_|_| [4][5][6]
2 |_|_|_| [7][8][9]
   0 1 2
"""
"""
coluna = [0, 0, 0]
linhas = [coluna[:], coluna[:], coluna[:]]


for i in range(3):
    for j in range(3):
        linhas[i][j] = int(input('Digite um valor para [{}][{}]: '.format(i, j)))


print('Sua matriz...')
for i in range(3):
    for j in range(3):
        print(f'[{linhas[i][j]:^5}]', end=' ')

    print('')
"""

# ele fez
linhas = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(3):
    for c in range(3):
        linhas[l][c] = int(input(f'Digite um valor para [{l}][{c}]: '))


print('Sua matriz...')
for i in range(3):
    for j in range(3):
        print(f'[{linhas[i][j]:^5}]', end=' ')

    print('')