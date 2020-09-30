"""

Desafio 087
- Aprimore o exercicio anterior, mostrando no final:
'A. A soma de todos os valores pares digitados.
'B. A soma dos valores da terceira coluna.
'C. O maior valor da segunda linha.

"""
# eu fiz
"""
coluna = [0, 0, 0]
linhas = [coluna[:], coluna[:], coluna[:]]


for i in range(3):
    for j in range(3):
        linhas[i][j] = int(input('Digite um valor para [{}][{}]: '.format(i, j)))


somaPares = 0
somaColuna3 = 0
maiorValor2Linha = 0

print('Sua matriz...')
for i in range(3):
    for j in range(3):
        n = linhas[i][j]
        print(f'[{n:^5}]', end=' ')

        if not n % 2:
            somaPares += n

        if i == 1:
            if j == 0:
                maiorValor2Linha = n
            else:
                if n > maiorValor2Linha:
                    maiorValor2Linha = n

        if j == 2:
            somaColuna3 += n

    print('')



print('A soma dos numeros pares é ', somaPares)
print('A soma da terceira coluna é ', somaColuna3)
print('O maior valor da segunda linha é', maiorValor2Linha)
"""

# ele fez

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}][{c}]: '))

somaPares = somaColuna3 = maiorValor2Linha = 0

for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end=' ')

        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]

    print('')

print(f'A soma dos valores pares é {somaPares}.')

for l in range(0, 3):
    somaColuna3 += matriz[l][2]

print(f'A soma do svalores da terceira coluna é {somaColuna3}')

maior = 0
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print(f'O maior valor na segunda linha é {maior}.')
