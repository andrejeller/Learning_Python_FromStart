"""

Desafio 112
- Dentro do pacote utilizadesCeV que criamos no desafio 111, temos um módulo cjamado dado. Crie uma função chamada
leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas
valores que sejam monetarios.

"""

from Exercicios.Fase_22_Modulos.Ex112.utilidadescev import moeda
from Exercicios.Fase_22_Modulos.Ex112.utilidadescev import dado

# import Exercicios.Fase_22_Modulos.Ex111.utils
# Dentro do __init__.py do utilizadesCeV já temos os outros dois imports


#num = float(input('Digite o preço: R$ '))
num = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(num, 20, 12)
