"""
CModulo Collections - Counter

Collection -> High-performance Container Datatypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quanidade
de ocorrências desse elemento.


"""

#Utilizando o Counter

from collections import Counter
"""
# Exemplo 1
#Criando uma lista - podemos utilizar qualquer iterável aqui
lista = [1, 1, 2, 4, 2, 5, 6, 6, 7, 8, 6, 0, 8, 0, 9, 8, 7, 5, 5, 6, 7, 8, 9, 4, 4, 3]

#Utilizando o Counter
res = Counter(lista)
print(res)
print(type(res))
 # Counter({6: 4, 8: 4, 4: 3, 5: 3, 7: 3, 1: 2, 2: 2, 0: 2, 9: 2, 3: 1})
 # veja que para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências.
 #Poderoa ser tuplas, dicionario etc..
 """

"""
#Exemplo 2
print(Counter("Harry Potter"))
# Counter({'r': 3, 't': 2, 'H': 1, 'a': 1, 'y': 1, ' ': 1, 'P': 1, 'o': 1, 'e': 1})
"""

#Exemplo 3

texto = """Gil Vicente (1465 — 1536) é geralmente considerado o primeiro grande dramaturgo português, 
além de poeta de renome. Há quem o identifique com o ourives, autor da Custódia de Belém, mestre da balança, 
e com o mestre de Retórica do rei Dom Manuel. Enquanto homem de teatro, parece ter também desempenhado as 
tarefas de músico, actor e encenador. É frequentemente considerado, de uma forma geral, o pai do teatro português, 
ou mesmo do teatro ibérico já que também escreveu em castelhano - partilhando a paternidade da dramaturgia 
espanhola com Juan del Encina.

A obra vicentina é tida como reflexo da mudança dos tempos e da passagem da Idade Média para o Renascimento, 
fazendo-se o balanço de uma época onde as hierarquias e a ordem social eram regidas por regras inflexíveis, 
para uma nova sociedade onde se começa a subverter a ordem instituída, ao questioná-la. Foi, o principal 
representante da literatura renascentista portuguesa, anterior a Camões, incorporando elementos populares 
na sua escrita que influenciou, por sua vez, a cultura popular portuguesa."""

palavras = texto.split()
#print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrências no texto
print(res.most_common(5))