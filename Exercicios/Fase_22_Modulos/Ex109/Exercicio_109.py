"""

Desafio 109
- Modifique as funções que foram criadas no desaifio 107 para que elas aceitem um parâmetro a mais, informando se
o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

"""

from Exercicios.Fase_22_Modulos.Ex109 import moeda

num = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'O dobro de {moeda.moeda(num)} é  {moeda.dobro(num, False)}')
print(f'Aumentando 10% temos  {moeda.aumentar(num, 10, True)}')
print(f'Diminuindo 80% temos  {moeda.diminuir(num, 80, False)}')
