"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.
"""
"""
valores = 1, 2, 3, 4, 5, 6

media = (sum(valores) / len(valores))

print(media)
"""
"""
# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.5, 0.9, 4.1, 4.3, -0.1]

# Calculando a media dos dados utilizando a função mean() mean signficica media

media = statistics.mean(dados)
print(media)

#OBS: Asssim como a função map(), a filter() recebe dois parâmetros, sendo uma função e um iterável.

res = filter(lambda  x: x > media, dados)
print(list(res))

print(f'Novamente:{list(res)}')

# OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são excluidos da memória.
"""
"""
paises = ['', 'Argentina', '', 'Brasil', 'Chile','', 'Canadá', '', 'Equador', 'Uruguai', '', 'Colombia','']

res = filter(None, paises)
#res = filter(lambda pais: len(pais) > 0, paises)
# res = filter(lambda pais: pais != '', paises)

print(list(res))
"""
"""
# A diferença entre map() e filter() é:

# map() -> Recebe dois parâmetro, uma função e um iterável e retorna um objeto mapeando a função oara cada elemento do iterável

# filter() -> Recebe dois parâmetros, uma função é um iterável e rotorna um objetodo filtando apenas os elementos de acordo com a função.

"""
"""
# Exemplo mais complexo

usuario = [
    {"username": 'samuel', "tweets": ["Eu adoro bolos",  "Eu adoro pizza"]},
{"username": 'carla', "tweets": ["eu u adoro gatos"]},
{"username": 'bruno', "tweets": []},
{"username": 'rafaela', "tweets": []},
{"username": 'ana', "tweets": ["Onde está o meu gato?",  "Tenho que ir!"]},
{"username": 'cassio', "tweets": ["Te vejo lá",  "nunca gostei do X"]},
{"username": 'beatriz', "tweets": ['Eu adoro bolos,  Eu adoro pizza']}
]

print(usuario)

# Filtrar os usuários que estão inativos no Twitter
# Forma 1
# invativos = list(filter(lambda u: len(u['tweets']) == 0, usuario))

# Forma 2
invativos = list(filter(lambda usuario: not usuario['tweets'], usuario))

print(invativos)

"""

# Combinando filter() e mao()

nomes = ['vanessa', 'ana', 'Paula']


# Devemos criar uma lista contendo 'Sua instrutura é' + nome, desde que cada nome tenha menos de 5 caracteres.

lista = list(map(lambda nome: f'Sua instrutora é: {nome.title()}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)
