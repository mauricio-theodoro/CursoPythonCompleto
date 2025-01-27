"""
Listas

Listas em Python funciona como vetores/Matrizes (arrays) em outras linguagens, com a diferença
de serem dinamicos e também podemos colocar qualquer tipo de dados.

Linguagens C/JAVA ARRAYS:
    - Possuem tamanhos e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array será sempre
    do tipo inteiro e poderá ter sempre no máximo 5 valores.

Já em Python:

- Dinâmico: Não possui tamanho fixo; Podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: As listas não possuem tipo de dado fixo; Podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: []

Listas são mutáveis: Ou seja, elas podem mudar constantemente.
"""

"""
type([])

lista1 = [13, 22, 2,  35, 34, 15, 1, 2, 1, 86, 7, 8, 9, 23, 324, 123, 12, 1]

lista2 = ['a', 't', 'f', 'h', 'k', 'n', 'l', 'w', 'm']

lista3 = []

lista4 = list(range(11))

lista5 = list("Harry Potter")

# Podemos facilmente checar se determinado valor está contido na lista
num = 18
if num in lista4:
    print(f"Encontrei o número {num}")
else:
    print(f"Não encontrei o número {num}")

for i in enumerate(lista5):
    print(i)

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

lista5.sort()
print(lista5)

#Podemos facilmente contar o npumero de ocorrências de um valor em uma lista
print(lista1.count(2))
print(lista5.count('r'))

# Adicionar elementos em listas
"""
#OBS: Para adicionar elementos em listas, utilizamos a função append
#* Com append, só é possível adicionar um elemento por vez
"""
n = int(input(f'Digite o valor a ser adicionado na lista: '))
lista1.append(n)
print(lista1)

m = input(f'Digite uma letra a ser adicionado na lista: ')
lista2.append(m)
print(lista2)

lista1.append([8, 6, 4, 2])
print(lista1)

if [8, 6, 4, 2] in lista1:
    print("Encontrei a lista")
else:
    print("Não encontrei a lista")

# extend adiciona individualmente enquanto append separadamente, ou em um conjuto
lista1.extend([123, 44, 67]) # Coloca cada elemento da lista como valor adicional a lista
print(lista1)

lista7 = []
print("Info:", (n := int(input("Digite um número: "))) and lista7.append(n) or lista7)

print("Resultado:", (n := str(input("Digite um novo valor:"))) and lista1.append(n) or lista1 )

# Podemos inserir um novo elemento na lista informando a posição do indice
# OBS: Isso não substitui o valor inicial, o mesmo será deslocado para a direita da lista.
lista1.insert(2, 'novo valor'.title())
print(lista1)

print("Resultado:", (n := str(input("Digite um novo valor:"))) and lista1.insert(2, n) or lista1 )


#Podemos facilmente juntar duas listas
lista6 = [ lista1 + lista3]
print(lista6)
lista1.extend(lista2)
print(f'Junção da lista: {lista1}')

# Podemos facilmente inverte uma lista
#lista2.reverse()
#lista1.reverse()
print(lista2[:: - 1])
print(lista1[:: - 1])


# Copiar uma lista
lista8 = lista2.copy()
print(lista8)
print(len(lista8)) # quantos elementos tem na lista

# Podemos remover facilmente o último elemento de uma lista
# OBS: O pop não somente remove o útlimo elemento, mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# OBS: Os elementos á direita deste índice serão deslocados para a esquerda.
# OBS: Se não houver elemento no índice informado, retornará o erro IndexError.
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (eliminar toda a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 4]
print(nova)
nova *= 3
print(nova)

# Pdemos facilmente converter uma string para uma lista
#exemplo 1

curso = "Programação na web"
print(curso)
curso = curso.split()
print(curso)

#OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas.

#Exemplo 2
curso = "Programação,na,web,para,leigo"
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string

lista9 = ['PROGRAMAÇÃO', "eM", "python"]
print(lista9)

#Abaixo estamos falando: Pega a lista9, e coloca entre cada elemento um espaço e transforma em uma string
curso1 = ' '.join(lista9)
print(curso1.title())

#Abaixo estamos falando: Pega a lista9, coloca cifrão entre cada elemento e transforma em uma string
curso = '$'.join(lista9)
print(curso.title())

lista10 = [1, 34.8, True, "Harry", 'P', [1, 2, 4], 99999]
lista11 = [1, 4, 7, 9, 45, 34, 21]

# Interando sobre listas
#Exemplo 1 - utilizando for

soma = 0
for elemento in lista11:
    print(elemento)
    soma += elemento
print(soma)

#Exemplo 2 - utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair': ")
    produto = input()
    if produto != "sair":
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0]) #verde
print(cores[1]) #amarelo
print(cores[2]) #azul
print(cores[3]) #branco

#Fazer acesso aos elementos de froma indexada inversa
#Pense na lista como um circulo, onde o final de um elemento está ligado ao incio da lista.
print(cores[-1])#branco
print(cores[-2])#azul
print(cores[-3])#amarelo
print(cores[-4]) # verde

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

#Gerar indice em um for. # Numerando os elementos dos indices
for indice, cor in enumerate(cores, 1):
    print(indice, cor)

# Outros métodos não tão importantes, mas úteis para trabalhar com listas
#Encontrar o índice de um elemento na lista

lista12 = [4, 3, 6 , 4, 7, 10, 54, 33, 42, 4]

#Em qual índice está o valor 6?
print(lista12.index(6))

#Em qual índice está o valor 6?
print(lista12.index(10))

#OBS : Caso não tenha este elemento na lista, será apresentado um erro ValueError

print(lista12.index(4)) # Retorna o índice do primeiro elemento encontrado, quando houver o mesmo elemento na lista repetidas vezes

#Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar.
print(lista12.index(4,1))
print(lista12.index(4,5))

print(lista12.index(4,5,7))# Busca o indice do valor 4, entre os indice 5 a 7

#Revisão de slicing

# lista [inicio:fim:passo]
# range(inicio:fim:passo)
"""
"""
#Trabalhando com slice de lista com o parâmentro 'inicio'
lista13 = [1, 2, 3, 4, 5, 6, 7]

print(lista13[1:]) # Iniciando no indice 1 e pegando todos os elementos restantes.

# Trabalhando com slice de lista com o parâmetro 'fim'
print(lista13[:2]) # começa em 0, pega até o índice 2 - 1

print(lista13[:4]) # começa em 0, pega até o índice 4 - 1

print(lista13[1:3]) # começa em 1, pega até o índice 3

# Trabalhando com slice de lista com o parÂmetro "passo"
print(lista13[1::2]) # começa em 1, vai até o final, de 2 em 2

print(lista13[::2])# começa em 0, vai até o final, de 2 em 2

# Som*, Valor Maximo*, Valor Mínimo*, Tamnho

# * Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sum(lista)) #soma
print(max(lista))# maximo valor
print(min(lista))#minimo valor
print(len(lista))# tamanho da lista

# Transformar uma lista em tupla

lista2 = [1, 2, 3, 4, 5]
print(lista2)
print(type(lista2))

tupla = tuple(lista2)
print(tupla)
print(type(tupla))

# Desempacotamento de listas

lista3 = [1, 2, 3]

num1, num2, num3 = lista3

print(num1)
print(num2)
print(num3)

#OBS: Se tiver mais elementos para desempacotar do que variáveis para receber os valores, teremos ValueError;

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

#Forma 1

lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)
print(lista)
print(nova)

#Veja que ao utilizamos lista.copy() copiamos os dados da lista para uma nova lista, mas elas
#ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra. Isso em Pytho é chamado
#de Deep Copy (cópia profunda)
"""

#Forma 2 - Shallow Copy
lista = [1, 2, 3]
print(lista)

nova = lista # cópia

nova.append(4)

print(lista)
print(nova)

#Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas
#após realizar a modificação em uma das listas, essa modificação modificou ambas as listas.
#isso em Python é chamado de Shallow Copy.


