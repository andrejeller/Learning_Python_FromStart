"""
Desafio 062
- Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
encerra quando ele disser que quer mostrar '0 ZERO' termos.

"""

print('Gerador de PA')
print('-='*10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1

mais = 10
total = 0

while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end=' -> ')
        termo += razao
        cont += 1

    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?: '))
print('Progressão finalizada com {} termos mostrados.'.format(total))



# eu fiz
op = 1
while op != 0:
    n1 = int(input('Digite o primeiro numero da PA: '))
    r = int(input('Digita a razão desta PA: '))
    contador = n1

    while contador < (n1 + (10*r)):
        print(contador, end=' -> ')
        contador += r

    print('ACABOU')

