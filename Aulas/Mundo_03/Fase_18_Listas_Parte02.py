"""
O que foi visto na aula 18.
- Listas parte 02

"""

teste = list()
teste.append('André')
teste.append(22)
print(teste)

galera = list()
galera.append(teste[:])  # galera.append(teste) - Precisa ser feito uma copia
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])  # galera.append(teste) - Precisa ser feito uma copia
print(galera)

# --
print('-'*50)
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0])
print(galera[0][0])
print(galera[2][1])

for p in galera:
    # print(p)
    # print(p[0])
    print(f'{p[0]} tem {p[1]} anos de idade.')

# --
print('-'*50)
galera = list()
dado = list()

for i in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])  # passando uma cópia
    dado.clear()
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
    else:
        print(f'{p[0]} é menor de idade.')

# --
print('-'*50)
