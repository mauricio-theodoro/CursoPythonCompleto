"""
Teste de Memória com Generetors

# Sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13....

# Testando Fibo - 449MB
for n in fibo_lista(10000):
    print(n)
"""

# Função utilizando LISTA
def fibo_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums



# Função usando geradores - Consome menos memória

def fibo_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador += 1

# Teste 2 Geradores 3 MB
for n in fibo_gen(10000):
    print(n)