"""

Desafio 111
- Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando

"""
from Exercicios.Fase_22_Modulos.Ex111.utilidadescev import moeda
from Exercicios.Fase_22_Modulos.Ex111.utilidadescev import dado

# import Exercicios.Fase_22_Modulos.Ex111.utils
# Dentro do __init__.py do utilizadesCeV já temos os outros dois imports

num = float(input('Digite o preço: R$ '))
moeda.resumo(num, 20, 12)

