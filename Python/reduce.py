"""
Reduce

OBS: A partir do Python3+ a função reduce() não é mais uma função integrada (built-in).Agora tem que importa e utilizar
esta função a partir do módulo 'functools'

Guido van Russum: utilize a função reduce() se você realmente precisa dela. Em todo caso,
99% das vezes um loop for é mais legível.


Para entender o reduce()

# Imagine que você possua uma coleção de dados:

dados = [a1, a2, a3 ..., an]

# E você tem uma função que recebe dois parâmetros:

def funcao(x, y):
    return x * y

Assim como map() e filter(), a função reduce() recebe dois parâmetros: a função e o iterável.

reduce(funcao, dados)

A função reduce(), funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
    Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo1 mais o terceiro elemento e quarda o resultado.

    Isso é repetido até o final.
    Passo 3: res3 = f(res2, a4)
    .
    .
    .
    Passo n: resn = f(resn, an)

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No final,
reduce() irá retornar o resultado final.

Alternativamente, poderiamos ver a função reduce() como:

funcao(funcao(funcao(a1, a2), a3), a4), ...), an) executa até chegar ao final

"""

# Como funciona na prática?

# Vamos utilizar a função reduce() para multiplicar todos os números de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 6, 10]

# Para utilizar o reduce() nós precisamos de uma função que retorna dois parâmetros.
multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# Utilizando um loop normal

res = 1
for n in dados:
    res = res * n

print(res)