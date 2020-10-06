"""
O que foi visto na aula 22.
- Tratamento de Erros e Exceções

Erro sintatico
primt() != print()

Erro semantico

-- Exceção

NameError:
print(x) - variavel não inicializada


ValueErro: estava esperando INT recebou STRING
n = int(input('Numero: '))
print(f'Voce digitou o numero {n}')


ZeroDivisionError: Ao tentar fazer uma divisão por ZERO. (r = 8 / 0)
a = int(input('Numerador: '))
b = int(input('Denominador: '))

r = a/b
print(f'O resultado é {r}')

TypeError:
r = 2 / '2'


IndexError: Indice 3 não existe.
lst = [3, 6, 4]
print(lst[3])

ModuleNotFoundError: Quando o arquivo UTEIS não for encontrado
import uteis

**
try:
    o que geralmente pode dar problema
except:
    o que fazer caso o try falhe
else:
    se deu tudo certo, faça isso
finally:
    independente se deu certo ou falha FAÇA ISSO
**

"""
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))

    r = a/b

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')

except ZeroDivisionError:
    print('Não é possivel dividir um número por zero.')

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')

except Exception as erro:
    print('Infelizmente tivemos um problema :(')
    print('O erro encontrado foi', erro.__class__, erro.__cause__)

else:
    print(f'O resultado é {r}')

finally:
    print(f'Volte sempre! Muito Obrigado!')


