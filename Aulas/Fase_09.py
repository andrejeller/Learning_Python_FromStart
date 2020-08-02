"""
O que foi visto na aula 07.
- Manipulando Cadeias de Texto


Fatiamento de String
- frase[9]    ... apenas o caractere 9
- frase[9:13] ... do caractere 9 até o 12
- frase[9:21:2] . do caractere 9 até o 21 pulando de 2 em 2 .. 9, 11, 13, 15, 17, 19
- frase[:5]   ... do caractere 0 até o 4
- frase[15:]  ... do caractere 15 até o final
- frase[9::3] ... do caractere 9 até o final pulando de 3 em 3 .. 9, 12, 15, 18

Analise de String
- len(frase)              ... quantos caracteres tem a frase
- frase.count('o')        ... contar quantas vezes aparecem a letra 'o'
- frase.count('o', 0, 13) ... contar quantas vezes aparece a letra 'o' entre o caractere 0 e 12
- frase.find('deo')        ... contar quantas vezes aparece a string 'deo' .. vai retornar o primeiro caracter da frase
- frase.find('algo')      ... se não existir ele vai retornar -1
- 'Curso' in frase        ... retorna uma Bool caso a string exista dentro da outra

Transformação de String
- frase.replace('Python', Android) ... onde tiver 'Python' ele substitui por 'Android'
- frase.upper()                    ... deixa todas as letras maiusculas "OLHA QUE LEGAL"
- frase.lower()                    ... deixa todas as letras minusculas "olha que legal"
- frase.captalize()                ... deixa tudo minusculo, e a primeira letra maiuscula "Olha que legal"
- frase.title()                    ... deixa as primeiras letras das frases maiusculas "Olha Que Legal Isso Aqui"

- frase.strip()                    ... remove todos os primeiros e utimos espaçoes inuteis "__Olha que legal___" fica "Olha que legal"
- frase.rstrip()                   ... remove somente os ultimos espaços  "__Olha que legal___" fica "__Olha que legal"
- frase.lstrip()                   ... remove somente os primeiros espaços  "__Olha que legal___" fica "Olha que legal__"
Obs. Serve para remover os espaços nas extremidades

Divisão de String
- frase.split()                    ... separa a string em todos os espços "Olha que legal" vira ["Olha", "que", "legal"]

Junção de String
- '-'.join(frase)                  ... junta mais de uma string com o caractere escolhido '-' ["Olha", "que", "legal"] vira "Olha-que-legal"


"""

frase = "Curso em Video Python"
print(frase[1::2])

# Imprimir texto longo -- muito bom para MENUs
print("""
-- AOGRA SIM 
EU CONSIGO DAR PTINT
EM UM TEXTO GRANDE
ISSO É MASSAAAAA.....
""")

print(frase.count('o'))
print(frase.upper().count('o'))

frase = "Curso em Video Python"
print(len(frase))

frase = "   Curso em Video Python   "
print(len(frase))
frase = frase.strip()

print(len(frase))
frase = frase.replace('Python', 'Android')

print(frase)
print('Curso' in frase)
print(frase.find('Video'))
print(frase.lower().find('video'))

print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[0][3])  # pegue da primeira frase a letra 3
