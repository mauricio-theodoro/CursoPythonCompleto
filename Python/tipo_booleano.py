"""
Tipo Boleano

Algebra Boleana, criada por George Boole

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a incial maiuscula

Errado:

true, false

Certo:

True, False
"""

ativo = True
print (ativo)

"""
Operações básicas:
"""

# Negação (not):

"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso,
se for falso o resultado será verdadeiro. Ou seja, sempre o contrário.
"""
# print(not ativo)

logado = False

# Ou (or):
"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro devem ser verdadeiros.
True or True -> True
True or False -> True
False or True - True
False or Faslse -> False
"""
print(ativo or logado)

# E (and):
"""
Também é uma operação binária, ou seja, depende de dois valores. Ambos os alores devem ser verdadeiro.

True and True -> True
True and False -> False
False and True -> False
False and False -> True
"""
