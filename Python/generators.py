"""
Generators

Em aulas anteriores nós estudamos:
- List COmprehension;
- Dictionary Comprehension;
- Set Comprehension;

Não vimos:
- Tuple Comprehension... porque elas se chamam Generators

nomes = ['Celio', 'Camila', 'Carla', 'Cassiano', 'Carine', 'Catia', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))
"""
from sys import getsizeof

"""
# Poderiamos ter realizado o código acima utilizando o Generators

nomes = ['Celio', 'Camila', 'Carla', 'Cassiano', 'Carine', 'Catia', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))

# Generator
res = (nome[0] == 'C' for nome in nomes) # melhor performace, o que vai gastar menos recursos da maquina
print(type(res))
# escolha sempre o Generator que possível, fazem a mesma coisas, mas ele tem melhor performace.
"""
"""
# Qual é a utilidade de getsizeof() -> Retorna a quantidade de bytes em memória do elemento passado como parâmetro.
from sys import getsizeof

# Mostra quantos bytes a string 'Harry' está ocupando em memória. Quanto maior a sring, mas espaço ocupa.
print(getsizeof('Harry'))

print(getsizeof('Potter'))

print(getsizeof(9))

print(getsizeof(9234528234))

print(getsizeof(True))
"""

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')

print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dic_comp} bytes')
print(f'Generator Expression: {gen} bytes')

# Eu posso iterar no Generator Expression? Sim!

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)