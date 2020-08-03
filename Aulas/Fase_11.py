"""
O que foi visto na aula 11.
- Cores no Terminal

módulo: colorized

Padrão ANSI
escape sequence

Um código que funciona bem no python é '\033[ aqui vao os codigos m'
\033[ style; text; back m

códigos para estilo: (que funcionam melhor para o python)
0 - Normal
1 - Negrito
4 - Sublinhado
7 - Negativo

códigos para texto: (30 -> 37)
30 - Branco
31 - Vermelho
32 - Verde
33 - Amarelo
34 - Azul
35 - Magenta
36 - Ciano
37 - Cinza

códigos para o fundo: (40 -> 47)
40 - Branco
41 - Vermelho
42 - Verde
43 - Amarelo
44 - Azul
45 - Magenta
46 - Ciano
47 - Cinza


"""

print('\033[4;30;45m Olá, Mundo!\033[m')
print('\033[33;44m Olá, Mundo!\033[m')

a = 3
b = 5

print('O valores são \033[32m{}\033[m e \033[31m{}\033[m.'.format(a, b))

nome = 'andre'
print('Olá! Muito prazer em te conhecer, {}{}!!!{}'.format('\033[7m', nome, '\033[m'))


cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'PB': '\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}!!!{}'.format(cores['amarelo'], nome, cores['limpa']))

