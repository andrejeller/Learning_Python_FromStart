"""

Desafio 108
- Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores
como um valor monetáreo formatado.

"""

from Exercicios.Fase_22_Modulos.Ex108 import moeda

num = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é  {moeda.moeda(moeda.dobro(num))}')
print(f'Aumentando 10% temos  {moeda.moeda(moeda.aumentar(num, 10))}')
print(f'Diminuindo 80% temos  {moeda.moeda(moeda.diminuir(num, 80))}')
