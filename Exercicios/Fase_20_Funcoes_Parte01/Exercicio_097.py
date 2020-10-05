"""

Desafio 097
- Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parametro e mostre uma
mensagem com tamanho adaptável.
Ex. escreva('Ola, Mundo!')
Saída.
'~~~~~~~~~~~'
'Ola, Mundo!'
'~~~~~~~~~~~'

"""


def escreva(txt):
    lens = len(txt) + 2
    print('~' * lens)
    print(f' {txt} ')
    print('~' * lens)


escreva('Ola, mundo!')
escreva('IHHAAAAAAAAA QUE TOP VAMOS LÁ')
escreva('oi')
