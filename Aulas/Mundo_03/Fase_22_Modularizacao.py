"""
O que foi visto na aula 22.
- Modularização e Pacotes


T.odo arquivo .py poder ser um módulo.
Um pacote é um diretório com vários módulos e um arquivo __init__.py
Um pacote pode ter outros pacotes dentro.

"""
#import Aulas.Mundo_03.Fase_22_Modulos.uteis
#from Aulas.Mundo_03.Fase_22_Modulos.uteis import dobro, triplo
from Aulas.Mundo_03.Fase_22_Modulos.uteis import numeros

num = int(input('Digite um valor: '))
#fat = Aulas.Mundo_03.Fase_22_Modulos.uteis.fatorial(num)
fat = numeros.fatorial(num)


print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {numeros.dobro(num)}.')
print(f'O triplo de {num} é {numeros.triplo(num)}.')
