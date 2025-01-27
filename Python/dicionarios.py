"""
Dicionários

OBS: em algumas linguagens de programação, os dicionários Python são conhecidos
por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor'
    - Tanto chave quanto valor podem ter qualquer tipo de dado:
    - Podemos misturar tipos de dads;

    # Criação de dicionários

# Forma 1 (Mais comum)

print(type({}))

paises = {'br': 'Brasil','eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# FORMA 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')

print(paises)
print(type(paises))


"""

"""
paises = {'br': 'Brasil','eua': 'Estados Unidos', 'py': 'Paraguai'}

#Acessando os elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
print(paises['py'])
# print(paises('ru')) Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

#Forma 2 - Acessando via get - Recomendada
print(paises.get('br'))
print(paises.get('ru')) # Quando não houver, retornarar 'None'



# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado KeyError

paises = {'br': 'Brasil','eua': 'Estados Unidos', 'py': 'Paraguai'}
pais = paises.get('ru', 'Não encontrado')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print("Não encontrei o país")
    
    #Podemos fazer dessa maneira sem utilizar o if else
#Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
paises = {'br': 'Brasil','eua': 'Estados Unidos', 'py': 'Paraguai'}

pais = paises.get('py', 'Não encontrado')

print(f"País {pais}")

------------------

paises = {'br': 'Brasil','eua': 'Estados Unidos', 'py': 'Paraguai'}

# Podemos verificar se determinada chave se encontra em um dicionário.

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises) # Ele não busca pelo valor e sim pela chave

if 'ru' in paises:
    russia = paises['ru']
    

"""

"""
# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tuplas dicionário, como
# chaves de dicionário.

#Tuplas por exemplo são bastante interesantes de serem utilizadas como chaves de dicionários, pois as mesmas
# são imutáveis.
localidade = {
    (54.6544, 34.5644): 'Escritorio em Tókio',
    (40.7128, 74.6988): 'Escritorio em Nova York',
    (35.7749, 122.3419): "Escritorio em São Paulo"
}
print(localidade)
print(type(localidade))


# Adicionando elementos em um dicionário.

receita = {'jan': 100, 'fev': 123, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 - Forma mais comun

receita['abr'] = 350

print(receita)

# Forma 2

novodado = {'mai': 500}

receita.update(novodado)

print(receita)

receita.update({'jun': 600})

print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 550

print(receita)

# Forma 2

receita.update({'mai': 700})

print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# CONCLUSÃO 2: Em dicionários, não podemos ter chaves repetidas.

# Removendo dados de um dicionário

# Forma 1
ret = receita.pop('mar')
# OBS: Precisamos sempre informar a chave, e caso não encontre o elemento, um KeyErro é retornado
print(receita)
print(ret)
#OBS 2: Ao removermos um objeto, o valor deste pbjeto é sempre retornado.

# Forma 2

del receita['fev']

print(receita)

# Se a chave não existir será gerado um KeyError.
# OBS: O valor removido não é retornado.

# Imaginamos que possuimos um comércio eletrônico, onde temos um carrinho de compra na qual adicionamos produtos.

----
Carrinho de Compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;
----

# 1 - Poderíamos utilizar uma Lista para isso? Sim
carrinho = []

produto1 = ['Playstation 3', 1, 250.00]
produto2 = ['The Last of Us', 1, 300.00]
produto3 = ['GTA 5', 1, 500.00]

carrinho.append(produto1)
carrinho.append(produto2)
carrinho.append(produto3)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# 2 - Poderíamos utilizar uma Tupla para isso? Sim

produto = ('Playstation 5', 1, 2400.00)
produto4 = ('Playstation 3', 1, 1000.00)
produto5 = ('Playstation 2', 1, 400.00)

carrinho = {produto, produto4, produto5}

print(carrinho)

# 3 - Poderíamos utilizar um Dicionário para isso? Sim

carrinho2 = []

produto6 = {'nome': 'Plastation 4', 'quantidade': 1, 'preco':1230.00}
produto7 = {'nome': 'XBOX X', 'quantidade': 1, 'preco':2300.00}
produto8 = {'nome': 'PC GAMER', 'quantidade': 1, 'preco':3000.00}

carrinho2.append(produto6)
carrinho2.append(produto7)
carrinho2.append(produto8)

print(carrinho2)

# Métodos de dicionários.

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar o dicionário (Zerar dados)

print(d)

# Copiando um dicionário para outro

# Forma 1

novo = d.copy() # Deep Copy

print(novo)

novo['d'] = 4

print(d)
print(novo)


print(d)

# Forma 2 Shallow Copy

novo = d

print(novo)

novo['d'] = 5

print(d)
print(novo)

"""

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parâmetros: um interável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11),'Info')
print(veja)