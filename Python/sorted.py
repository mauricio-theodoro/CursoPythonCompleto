"""
Sorted

OBS: Não confunda com sort(), apesar do nome serem parecidos. Já foi mostrado em Listas

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar.

OBS: O sorted, sempre retorna uma lista com os elementos do iterável ordenados.
"""
"""
#Exemplo de sort()
lista = [12, 21, 34, 42, 51, 1, 2, 4]

lista.sort()
print(lista)
# Faz ordenação da lista.
"""
"""
numeros = (3, 4, 2, 1)
print(numeros)

print(sorted(numeros)) # Ordenar do menor para o maior. 

print(numeros)
"""
"""
numeros = [5, 3, 4, 7, 8, 2, 1, 35, 10]

print(numeros)
# Adicionando parâmetros ao sorted()

print(set(sorted(numeros)))

print(sorted(numeros, reverse=True)) # Ordena do maior para o menor
"""
"""
# Podemos utilizar o sorted() para coisas mais complexas.

usuario = [
    {"username": 'samuel', "tweets": ["Eu adoro bolos",  "Eu adoro pizza"]},
{"username": 'carla', "tweets": ["eu u adoro gatos"]},
{"username": 'bruno', "tweets": []},
{"username": 'rafaela', "tweets": [], "cor": "amarelo"},
{"username": 'ana', "tweets": ["Onde está o meu gato?",  "Tenho que ir!"]},
{"username": 'cassio', "tweets": ["Te vejo lá",  "nunca gostei do X"]},
{"username": 'beatriz', "tweets": ['Eu adoro bolos,  Eu adoro pizza'], "cor": "preto", "musica": "rock"},
{"username": 'helena', "tweets": []}
]

print(usuario)

# Ordenando por username - Ordem Alfabética
print(sorted(usuario, key=lambda usuarios: usuarios['username']))

# Ordenando por tweets
print(sorted(usuario, key=lambda usuarios: len(usuarios['tweets']), reverse=True))
"""

# Último exemplo

musicas = [
    {"título": "Thunderstruck", "tocou": 3},
    {"título": "Black in Black", "tocou": 2},
    {"título": "Hello", "tocou": 6},
    {"título": "Dead Skin Mask", "tocou": 4},
    {"título": "Continuação", "tocou": 9},
    {"título": "Too old to rock 'in'roll, too young to die", "tocou": 5}
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))