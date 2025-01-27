"""
Len, Abs Sum, Round

# Len

len() -> Retorna o tamanho (ou seja, o número de itens) de um iterável.

"""
"""
# Só para revisar

print(len("Harry Potter"))
print(len([1,2,3,4,5]))
print(len((1,2,3,4,5)))
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))
print(len(range(0, 10)))

# Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte:

# Dunder len
print('Harry Potter'.__len__())

# Abs

abs() -> Retorna o valor absoluto de um número inteiro ou real, De forma básica, seria o seu valor real sem o sinal.
"""
"""
# Exemplos Abs

print(abs(-5))
print(abs(5))
print(abs(3.15))
print(abs(-65.23))

#   Não existe ABS de string

# Sum

sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos,
incluindo o valor inicial.

OBS: O valor incial default = 0
"""
"""
#Exemplo Sum

print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))

print(sum([1.574, 2.535, 3.976, 4.756, 5.684]))

print(sum((1, 2, 3, 4, 5)))
print(sum({1, 2, 3, 4, 5}))
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))
"""
"""
# Round
round() -> Retorna um número arredondado para n digito de precisão após a casa decimal, Se a precisão não for
infornada retorna o inteiro mais proximo da entrada.
"""

# Exemplos Round

print(round(14.1))

print(round(1.7))

print(round(5.123142, 3))

print(round(2.23253, 2))