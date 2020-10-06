"""

Desafio 114
- Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
pudim.com.br

"""

import requests

try:
    response = requests.get('http://www.pudim.com.br/')

except:
    print('Não consegui acessar. :(')

else:
    # print(response.status_code)
    if response.status_code == 200:
        print('Consegui acessar!. :)')
    else:
        print('O site está fora do ar. :/')
