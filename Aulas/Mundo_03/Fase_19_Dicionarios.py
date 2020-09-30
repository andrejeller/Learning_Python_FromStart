"""
O que foi visto na aula 19.
- Dicionarios

"""

"""
pessoas = {'nome': 'gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

print(pessoas.keys())
print(pessoas.items())
print(pessoas.values())

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo']
print(pessoas)

pessoas['nome'] = 'Leandro'
pessoas['peso'] = 85.3
print(pessoas)
"""

"""
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigle': 'SP'}

brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[0]['sigla'])
"""

estado = dict()
brasil = list()

for i in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    # brasil.append(estado)  # Não consigo fazer fatiamento para criar uma copia -- brasil.append(estado[:])
    brasil.append(estado.copy())  # Agora sim ele vai adicionar uma copia

#print(brasil)

for e in brasil:
    # print(e)
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

    for v in e.values():
        print(v, end=' ')

    print('')

