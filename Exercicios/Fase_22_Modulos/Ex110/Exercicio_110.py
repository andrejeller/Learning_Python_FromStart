"""

Desafio 110
- Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algmas
informações geradas pelas fuções que já temos no módulo criado até aqui.

"""

from Exercicios.Fase_22_Modulos.Ex110 import moeda

num = float(input('Digite o preço: R$ '))
moeda.resumo(num, 20, 12)
