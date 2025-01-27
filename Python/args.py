"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá
chamar de qualquer coisa, desde que comece com asterisco.

Exemplo:
*xis

Mas por convenção, utilizamos *args para definí-lo

Mas o que é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada
em uma tupla. Então desde já lembre-se que tuplas são imutáveis.
"""


"""
# Exemplo

def soma_todos_numeros(num1=1, num2=6, num3=2, num4=4):
    return num1 + num2 + num3 + num4

print(soma_todos_numeros(5,5,7,5 ))

print(soma_todos_numeros(3, 6))

print(soma_todos_numeros(1,2,5, 7)) 
"""

# Entendendo o args
"""
def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(32, 34))
print(soma_todos_numeros(23,45,76,12,22))

print(type(soma_todos_numeros()))
"""
"""
def soma_todos_numeros(nome, email, *args):
    return sum(args)

print(soma_todos_numeros('Anete', 'teste@gmail.com'))
print(soma_todos_numeros('Teste', 'teste1@gmail.com', 1))
print(soma_todos_numeros('Teste', 'teste1@gmail.com', 12, 231))
print(soma_todos_numeros('Teste', 'teste1@gmail.com', 3,231,123,1))
"""

# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Harry' in args and 'Universidade' in args:
        return 'Bem-vindo Harry!'
    return 'Eu não tenho certeza quem você é ...'


print(verifica_info())
print(verifica_info(1, True, 'Universidade', 'Harry'))
print(verifica_info(1, 'Universidade', 3.145))


def soma_todos_numeros(*args):
    return sum(args)

#print(soma_todos_numeros())
#print(soma_todos_numeros(1,24,67,21))

numeros : [1, 2, 4, 5, 6, 7, 8]

numeros = map(int, input("Digite três números inteiros separados por espaço: ").split())

# Desempacotador

print(soma_todos_numeros(*numeros))
print(type(numeros))

# OBS: O asterisco serve para que seja informado ao Python que está passando um argumento
# uma coleção de dados. Desta forma, ele saberá
# que precisará antes desempacotar estes dados.