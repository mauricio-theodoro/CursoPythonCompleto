"""
utilizando Lambdas

Conhecidas por expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja, funções anônimas

# Função em Python

def soma(a, b):
    retun a + b

"""
"""
# Função em Python
def funcao(x):
    return 3 * x + 1

print(funcao(3))

# Expressão Lambda

lambda x: 3 * x + 1

# E como utilizar a expressão lambda?

calc = lambda x: 3 * x + 1

print(calc(3))
print(calc(2))
"""
"""
# Podemos ter expressões lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' harry ', '     potter     '))
print(nome_completo('MaRGARETY', ' bOLIVIA '))
"""
"""
# Em funções Python, podemos ter nenhuma ou várias entradas. Em Lambdas também

gostar = lambda  : 'Como não gostar de Python?!'

uma = lambda x: 3 * x + 2

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3/ (1 / x + 1 / y + 1 /z)

# n = lambda x1, x1, ..., xn: <expressão>

print(gostar())
print(uma(1))
print(duas(2, 4))
print(tres(1, 2, 3))

# OBS: Se passar mais argumentos do que parâmetro esperados teremos TyperError
"""
"""
# Outro exemplo

autores = ['Isaac Newton', 'Rubens Barreto', 'Roberto Amorim',
           'Fernanda F. Montenegro', 'Sandy  C. E. Fernendez', 'Olga Silva']


# Ordenação pelo sobrenome
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)
"""

# Função Quadrática
# f(x) = a * x ** 2 + b * x + c

#Definido a função
def geradora_funcao_quadratica(a, b, c):
    """ Retorna a função f(x) a*x**2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(3, 0, 1)(2))