"""
Desafio 083
- Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.


"""

"""
# eu fiz - obs. sem a parte de ordem correta
expressao = str(input('Digite uma expressão: '))
abertos = expressao.count('(')
fechados = expressao.count(')')

if abertos == fechados:
    print('A expressão está correta!')
else:
    print('A expressão está incorreta!')
"""

# ele fez
expressao = str(input('Digite a expressão: '))
pilha = []

for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão é valida..')
else:
    print('A expressão está invalida...')
