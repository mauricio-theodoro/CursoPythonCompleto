"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Cojuntos
da Matemática.

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:

- Sets (Conjuntos não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não sçao indexados;
Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não importamos com a ordenação deles. Quanado não precisamos se preocupar
com chaves, valores e itens duplicados.

Os conjuntos (sets) são referênciados em Python com chaves {}

Diferença entre Conjuntos (Set) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

"""

"""
# Definindo um conjunto:

# Forma 1

s = set({1, 2, 6, 3, 4, 5, 6, 7, 4, 8}) # Repare que possuimos valores repetidos.
print(s)
print(type(s))

#OBS: Ao criar um conjunto, caso seja adicionado um valor já existnete, o mesmo
#será ignorado sem gerar error, e não fará parte do conjunto.

# FORMA 2 = Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto
if 3 in s:
    print('Tem o 3')
else:
    print(f'não tem o 3')

"""
"""
# Importante lembrar que, além de não termos valores duplicados, não temos ordem.

dados = '44, 23, 12, 64, 564, 34, 32, 32'

# Listas aceitam valores duplicados, então temos 8 elementos.
lista = [44, 23, 12, 64, 564, 34, 32, 32]
print(f'Lista: {lista} com {len(lista)} elementos')

#Tuplas aceitam valores duplicados, então temos 8 elementos.
tupla = (44, 23, 12, 64, 564, 34, 32, 32)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

#Dicionários não aceitam chaves duplicadas, então temos 7 elementos.
dicionario = {}.fromkeys([44, 23, 12, 64, 564, 34, 32, 32], 'dirct')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

#Conjunto não aceitam valores duplicados, então temos 7 elementos.
conjunto = {44, 23, 12, 64, 564, 34, 32, 32}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

"""
"""
# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 54.23, 34}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)
"""
"""
# Usos interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
#Informaram manualmente a cidade de onde vieram.

# Nós adiconamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição.

cidades = ['Belo Horizonte', 'Rio de Janeiro', 'Cuiaba', 'São Paulo', 'Campo Grande', 'Rio de Janeiro', 'São Paulo', 'Campo Grande']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.

# O que vocÊ faria? Faria um loop na lista? e remover as repetições?

#Podemos utilizar o set para isso:

print('Cidades: ',set(cidades))

"""
"""
# Adicionando elementos em um conjunto
s = {1, 2, 3, 4, 5, 6}

s.add(7)
s.add(7) #Duplicidade não gera erro. Simplesmente é ignorado e não é adicionado.
print(s)
"""
"""
#Removendo elementos em um conjunto.
s = {1, 2, 3}
print(s)
# Forma 1

s.remove(3) # Não é índice! Informamos o valor a ser removido.
print(s)

# OBS: Caso o valor não seja encontrado, será gerado um erro: KeyError. Nenhum valor é retornado.

# Forma 2

s.discard(2)
print(s)

# OBS: Se o valor não for encontrado, nennhum erro é gerado.
"""
"""
# Copiando um conjunto para outro.
s = {1, 2, 3, 4, 5}
print(s)

# Copiando um conjunto para outro

# Forma 1 - Deep Copy
novo = s.copy()
print(novo)
novo.add(6)

print(novo)
print(s)
"""
"""
# Forma 2 - Shallow Copy
s = {1, 2, 3, 4, 5}
print(s)

novo = s
novo.add(6)

print(novo)
print(s)
"""
"""
#Podemos remover todos os itens de um conjunto

s = {1, 2, 43, 5}
print(s)
s.clear()
print(s)
"""

#Metodos matemáticos de Conjuntos

# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e um
# contendo estudando do curso de Java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia','Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}
"""
# Veja que alguns alunos que estudam Python também estudam Java.

# Precisamos gerar um conjunto com nomes de estudantes únicos.

# Forma 1 - Utilizando union - Recomendado essa utilização para os leigos.
# unicos1 = estudantes_java.union(estudantes_python)
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utilizando o caractere pipe '|' <- que é essa barra
unicos2 = estudantes_python | estudantes_java
print(unicos2)
"""

"""
# Gerar um conjunto de estudantes que estão em ambos os cursos.

# Forma 1 - Utilizando intersection

ambos1 = estudantes_python.intersection((estudantes_java))
print(ambos1)

# Forma 2 - Utilizando o &

ambos2 = estudantes_java & estudantes_python
print(ambos2)
"""
"""
# Gerar um conjunto de estudantes que não estão no mesmo curso.

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)
"""

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

s = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))

