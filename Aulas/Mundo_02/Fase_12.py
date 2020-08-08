"""
O que foi visto na aula 12.
- Condições Aninhadas (if, elif, else)

Obs. É aninhado pois parece um ninho, temos uma dentro da outra e dentro da outra, como aqueças bonecas...

Ele continua mostrando um bom exemplo com a movimentação de um carro.


"""

nome = str(input('Qual é o seu nome? '))

if nome == 'André':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Braisl.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome faminino.')
else:
    print('Seu nome é bem normal.')

print('Tenha um bom dia, {}.'.format(nome))
