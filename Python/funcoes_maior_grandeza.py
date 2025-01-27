"""
Funções de Maior Grandeza - Higher Order Functions - HOF

O que isso significa?

- Quando uma linguagem de programação suporte HOF, indica que podemos ter funções
que retornam outras funções como resultado ou mesmo que podemos passar funções
como argumentos para outras funções, e até mesmo criar variáveis do tipo funções
nos nossos programas.

OBS: Na seção de funções, utilizamos isso.

Em Python, as funções são Cidadões de Primeira Classe, First Class Citizen


"""
"""
# Exemplo - Definindo as funções

def soma(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def mutiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando as funções

print(calcular(4, 3, soma))

print(calcular(4, 3, diminuir))

print(calcular(4, 3, mutiplicar))

print(round(calcular(4, 3, dividir), 2))
"""

# Nested Functions - Funções Aninhadas

"""
Em Python podemos também ter funções dentro de funções, que são conhecidas por Nested Functions
ou também Inner Functions (Funções Internas).
"""
"""
# Exemplo:

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa

# Testando:

print(cumprimento('Angelica'))
print(cumprimento('Solange'))
"""
"""
# Retornando funções de outras funções

from random import choice

def faz_me_rir():
    def rir():
        return choice(('hahahahaha ', 'kkkkkkkkkkkk ', 'rsrsrsrs '))
    return rir

# Testando

rindo = faz_me_rir()

print(rindo())
"""

# Inner Functions (Funções Internas / Nested Functions) podem acessar o escopo de funções mais externas.

from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        riso = choice(('kkkkkkkkkkkk ', 'hahahahahaha ', 'rsrsrsrsrsrs '))
        return f'{riso} {pessoa}'
    return dando_risada

# Testando
rindo = faz_me_rir_novamente('Fernanda')

print(rindo())
print(rindo())
print(rindo())