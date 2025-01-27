"""
Listas Aninhadas

- Algumas linguagens de programação possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes);

Em Python nós temos as listas

numeros = [1, 'b', 3.865, True, 5]
"""

"""
from tipo_float import valor

# Exemplos

listas = [[1,  2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3x3

print(listas)
print(type(listas))

# Como fazemos para acessar os dados?

print(listas[0][1])
print(listas[0][2])
print(listas[1][0])
print(listas[2][2])

# Iterando com loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num)

# List Comprehension

[[print(valor) for valor in lista] for lista in listas]

"""

# Gerando um tabuleiro/matriz 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valor inicial

print([['*' for i in range(1, 4)] for j in range(1, 4)])