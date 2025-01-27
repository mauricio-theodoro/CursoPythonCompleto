"""
Debuggando com PDB

PDB -> Python Debugger

Bug -> Inseto

# OBS: A utilizção do print() para debugar código é uma prática ruim.

def dividir( a, b):
    print(f'a = {a}, b={b}')
    try:
        return float(a) / float(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um proble: {err}'

print(dividir(4, 7).__round__(2))

# Existem formas mais profissionais de realizar, utilizando o debugger
#Em Python, podemos fazer isso em diferentes IDEs como o PyCharm ou utilizando
# o PDB - Python Debugger

#Exemplo com o PyCharm
"""
"""
def dividir( a, b):
    print(f'a = {a}, b={b}')
    try:
        return float(a) / float(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um proble: {err}'

print(dividir(4, 0))


# Exemplo com o PDB - Python Debugger

# Para utilizar o Python Debugger, precisamos importa a biblioteca pdb e então poderemos utilizar a função set_trace()

# * A partir do Python 3.7, não é mais necessário importa a biblioteca pdb, pois o comando deug foi
# incorporada como função built-in (integrada) chamada breakpoint()

# Comandos básicos do PDB
# l (listar onde estamos no código
# n (próxima linha
# p (imprime variável)
# c (continua a execução - finaliza o debugger)

"""
"""
import pdb

nome = 'Harry'
sobrenome = 'Potter'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + ' faz o curso ' + curso
print(final)
"""
"""
nome = 'Harry'
sobrenome = 'Potter'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por que utilizar esse formato?
# O debug é utilizado durante o desenvolvimento. Costumamos realizar os improts de bibliotecas
# no inicio do arquivo. Por isso, ao invés de colocarmos o import do pdb no incio do arquivo,
# Nos colocamos somente onde vamos debuggar, e ao finalizar ja fazemos a remoção.
"""
"""
nome = 'Harry'
sobrenome = 'Potter'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python'
final = nome_completo + ' faz o curso ' + curso
print(final)
"""
# OBS: Cuidado com conflitos entre nomes de variáveis e os comandos do pdb

def soma(l, n, p, d, c):
    breakpoint()
    return l + n + p + d + c

print(soma(1, 2, 3, 4, 5))

# Como os nomes das variáveis são os mesmos dos comandos do pdb, devemos utilizar o comando p para imprimir
# As variáveis. Ou seja: p nome_da_variavel

# Nada de colocar nomes não representativos em variáveis. Sempre por nomes significativos.
