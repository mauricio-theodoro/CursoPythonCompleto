"""
O block try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo
assim que o programa pare de funcionar e o usuário receba mensagens de erro inesperados.


try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema


# Exemplo 1 - Tratando um erro genérico

try:
    geek()
except:
    print('Deu algum problema')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.
#Exemplo 2 - Tratando um erro genérico

try:
    len(5)
except:
    print('Deu algum problema')

# Tente executar a função geek(), caso você não encontre erros, imprima a mensagem de erro.

OBS: Tratar erros de forma genérica não é a melhor forma de tratamento de erros. O ideal é sempre
tratar de forma específica.

# Exemplo 3 - Tratando um erro especifico

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')


# Exemplo 3 - Tratando um erro especifico

try:
    len(5)
except NameError:
    print('Você está utilizando uma função inexistente')
except TypeError:
    print('O objeto inteiro não é permitido.')


# Exemplo 5 - Tratando um erro específico com detalhes do erro:

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}'
"""

"""
try:
    #len(5)
    #geek()
    print('Geek' [9])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')
"""

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return print('TypeError')

dic = {'nome': 'Harry'}

print(pega_valor(dic, 8))