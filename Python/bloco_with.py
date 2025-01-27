"""
O bloco with

Passo para se trabalhar com arquivos

# 1 - Abrimos o arquivo
# 2 - Mnipulamos o arquivo
# 3 - Fechamos o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados
são fechados após o bloco with.

"""

# O bloco with - Forma PythOnica de manipular os arquivos

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

# print(arquivo.read())
print(arquivo.closed)