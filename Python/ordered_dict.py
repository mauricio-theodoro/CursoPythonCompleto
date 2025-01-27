"""
Módulo Collection: Ordered Dict

"""
from collections import OrderedDict

"""
#Em um dicionário, a ordem de inserção dos elementos não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')
print(dicionario)
"""
"""
#Fazendo o import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor{valor}')
"""

#Entendnedo a diferença entre Dict e Ordered Dict

#Dicionário comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict2 == dict1) # True -> Já que a ordem dos elementos não importa para o diionário.

#Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2) # False -> Já que a ordem dos elementos importa para o OrderedDict