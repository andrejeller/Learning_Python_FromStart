"""
O que foi visto na aula 07.
- Operações Aritiméticas

+ .. Soma
- .. Subtração
* .. Multiplicação
/ .. Divisão
** . Potência
// . Divisão Inteira
%  . Módulo (Resto da divisão)

Ordem de Precedência
1. ()
2. **
3. * .. / .. // .. %
4. + .. -

"""

nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome))  # para ter 20 caracteres
print('Prazer em te conhecer {:>20}!'.format(nome))  # alinhado a direita
print('Prazer em te conhecer {:<20}!'.format(nome))  # alinhado a esquerda
print('Prazer em te conhecer {:^20}!'.format(nome))  # centrallizado
print('Prazer em te conhecer {:=^20}!'.format(nome))  # centralizado preenchendo o resto com '='
print('Prazer em te conhecer {:@>20}!'.format(nome))  # alinhado a direita preenchendo oo resto com '@'

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d))
print('Divisão inteira {}, o potência {}'.format(di, e))

print('Divisão com 3 casas decimais {:.3}'.format(d), end=' ')
print('Para dar outro print na mesma linha, e \n quebrendo uma linha no meio.', end=' ----- ')
print('e agora a continuacao da linha')
