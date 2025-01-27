"""
Any e All

all() - > Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.
"""
"""
# Exemplo all()

print(all([0, 1, 2, 3, 4, 5, 6])) # Todos os números são veridadeiros? <- False, o '0' é False.
print(all([ 1, 2, 3, 4, 5, 6])) # Todos os números são veridadeiros? True

print(all([]))

print(all(( 1, 2, 3, 4, 5, 6)))
print(all({ 1, 2, 3, 4, 5, 6}))
print(all('Harry'))

nomes = ['Celio', 'Camila', 'Carla', 'Cassiano', 'Carine', 'Catia']

print(all(nome[0] == 'C' for nome in nomes))

#OBS: Um iterável vazio convertidio em boolean é False mas o all() entende como True
print(all([letra for letra in 'eio' if letra in 'aeiou']))

print(all([num for num in [4, 3, 2, 1, 6, 7, 8, 9] if num % 2 == 0]))
"""
"""
any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False
"""

print(any([0, 1, 2, 3, 4, 5, 6])) # True

print(any([0, False, {}, (), []])) # False

nomes = ['Celio', 'Camila', 'Carla', 'Cassiano', 'Carine', 'Catia', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

print(any([num for num in [ 4, 2, 10, 6, 8, 5] if num % 2 == 0]))