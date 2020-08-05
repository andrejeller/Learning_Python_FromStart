"""
Desafio 042
- Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
'EQUILÁTERO: todos os lados iguais
'ISÓCELES: dois lados iguais
'ESCALENO: todos os lados diferentes

Nota: Cada uma das retas precisa ser menor que a soma das outras duas.

"""
print('-=-'*20)
print('Analizador de Triângulos')
print('-=-'*20)

r1 = float(input('Reta 01: '))
r2 = float(input('Reta 02: '))
r3 = float(input('Reta 03: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas a cima PODEM formar um triângulo... ', end='')

    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓCELES')

else:
    print('As retas a cima NÃO PODEM formar um triângulo')