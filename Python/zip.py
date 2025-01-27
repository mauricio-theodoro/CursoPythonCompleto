"""
Zip

zip() -> Cria um iterável (Zip Object) que agrega elemento de cada um dos iteráveis passados como entrada em pares.
"""
from typing import final

"""
# Exemplos

lista1 = [1, 2, 4]
lista2 = [3, 6, 7]

zip1 = zip(lista1, lista2, 'abc')

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma lista, Tupla, ou Dicionário.

print(list(zip1))

zip1 = zip(lista1, lista2, 'abc')
print(tuple(zip1))

zip1 = zip(lista1, lista2, 'abc')
print(set(zip1))

zip1 = zip(lista1, lista2)
print(dict(zip1))

#OBS: o zip() utiliza como parâmetro o menor tamanho em iterável. Isso significa que se estiver
# Trabalahando com iteráveis de tamanhos diferentes, irá parar os elementos do menor
# iterável acabar.
lista3 = [1, 2, 3, 4, 23]

zip1 = zip(lista3, lista2, lista1)
print(list(zip1))
"""
"""
 # Podemos utilizar diferentes iteráveis com zip

tupla = 1, 2,3, 6, 4, 5
lista = [1, 2,3, 6, 4, 5]

dicionario = {'a': 11, 'b':12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Lista de tuplas
dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))
"""

# Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 67, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)

# Podemos utilizar o map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))