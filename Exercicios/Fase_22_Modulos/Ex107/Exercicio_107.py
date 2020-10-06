"""

Desafio 107
- Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro(), metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.

"""

from Exercicios.Fase_22_Modulos.Ex107 import moeda

num = float(input('Digite o preço: R$ '))
print(f'A metade de R${num} é R${moeda.metade(num)}')
print(f'O dobro de R${num} é  R${moeda.dobro(num)}')
print(f'Aumentando 10% temos  R${moeda.aumentar(num, 10)}')
print(f'Diminuindo 80% temos  R${moeda.diminuir(num, 80)}')
