"""
O que foi visto na aula 07.
- Trabalhando com Módulos

import bebida  # vai importar todas as bebidas
from doce import pudum  # vai importar apenas o pudim dentro dos doces


import math
from math import sqrt
from math import sqrt, ceil  # para importar mais de uma funcionalidade sem importar tudo
"""
import math
#from math import sqrt  # Ctrl + Espaco mostra as opcoes

num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))

