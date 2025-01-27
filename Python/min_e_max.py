"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elemento.
"""
"""
# Exemplos

lista = [1, 2, 3, 5, 57, 8, 121, 452, 2315]

print(max(lista))

tupla = (1, 2, 3, 5, 57, 8, 121, 452, 2315)

print(max(tupla))

conjunto = {1, 2, 3, 5, 57, 8, 121, 452, 2315}

print(max(conjunto))

dicionario = {'a':1,'b': 2,'c': 3,'d': 5,'e': 57,'f': 8,'g': 121,'h': 452,'i': 2315}

print(max(dicionario))

dicionario = {'a':1,'b': 2,'c': 3,'d': 5,'e': 57,'f': 8,'g': 121,'h': 452,'i': 2315}

print(max(dicionario.values()))

print(max((3, 99)))
"""
"""
# Faça um programa que receba dois valores do usuário e mostre o maior.

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(max(val1, val2))
"""
"""
print(max(4, 3, 56, 12, 44, 33))

print(max('a', 'ab', 'abc'))

print(max('a', 'b', 'c', 'g'))

print(max(4.354, 1.543))

print(max('Harry Potter'))
"""
# min() - Retorna o menor valor em um iterável ou o menor de dois ou mais elementos.
# Outros exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(max(nomes))
print(min(nomes))

print(max(nomes, key=lambda nome: len(nome))) # Ollivander
print(min(nomes, key=lambda nome: len(nome))) #Tim

musicas = [
    {"título": "Thunderstruck", "tocou": 3},
    {"título": "Black in Black", "tocou": 2},
    {"título": "Hello", "tocou": 6},
    {"título": "Dead Skin Mask", "tocou": 4},
    {"título": "Adele", "tocou": 9},
    {"título": "Too old to rock 'in'roll, too young to die", "tocou": 5}
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

print(max(musicas, key=lambda musica: musica['tocou'])['título'])
print(min(musicas, key=lambda musica: musica['tocou'])['título'])


# Como encontrar a musica mais tocada e a menos tocada sem usar max(), min() e lambda
max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['título'])

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['título'])

min = 999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['título'])
