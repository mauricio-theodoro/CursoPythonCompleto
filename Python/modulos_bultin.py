"""
Trabalhando com Módulos Builtin (módulo integrados, que já vem instalados no Python)
___________________________
| Python | Módulos builtin |
---------------------------

# Utilizando alias (apelidos para módulos/funções
import random as rdm

print(rdm.random())

"""
"""
# Podemos importar todas as funções de um módulo utilizando o *

# Importando todo o módulo

from random import *

print(random())
"""
"""
# fazendo duas importações na mesma linha
from random import randint as rdi, random as rdm

print(rdi(1,10))
print(rdm())
"""

# Costumamos a utilizar tuple para colocar multiplos imports de um mesmo módulo
from random import  (
    random,
    randint,
    shuffle,
    choice
)

lista = ['Harry', 'Potter', 'Shopping']

print(random())
print(randint(1, 50))
shuffle(lista)
print(lista)
print(choice('Shopping'))
