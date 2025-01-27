"""
Erros mais comuns em Python

é importante prestar atenção e aprender a ler as saídas de erros geradas pela execução
do nosso código.

Os erros mais comuns:

SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o Python
não reconhece como parte da linguagem.
"""
"""
# Exemplos SyntaxError

def funcao:
    print('Harry Potter')
"""
"""
# Exemplos SyntaxError

None = 1
"""
"""
# Exemplos SyntaxError

return  # <-  deve sempre coloca dentro de uma função
"""

"""
2 - NameError -> Ocorre quando uma variável ou função não foi definida.
Exemplos NameError

a) 
print(harry)

b)

harry()

a = 18

if a < 10:
    msg = 'É maior que 10'

print(msg)

"""
"""
# TypeError - > Ocorre quando uma função/operação/ação é aplicada a um tipo errado.
# Exemplos TypeError

print(len(5))

b)

print('Harry' + [])
"""
"""
# 4 - IndexError -> Ocorre quando tentanmos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando
# um índice inváido.

# Exemplos IndexError

lista = ['Harry']
print(lista[2])

lista = ['Harry']
print(lista[0][5])

tupla = ('Harry',)
print(lista[0][5])

5 - Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto, mas 
valor inapropriado (incorreto)

a) 
#Exemplos ValueError


print(int('potter'))
"""
"""
6 - KeyError - > Ocorre quando tentamos acessar um dicionário com uma chave que não existe
#Exemplos KeyError


print(int('potter'))

#Exemplos KeyError

dic = {'python': 'potter'}
print(dic['harry'])
"""
"""
7 AttributeError -> Ocorre quando uma variável não tem um atributo/função.

Exemplos AttributeError

a)
tupla = (1, 2, 3, 4, 62, 53, 12, 11)
tupla.sort()
print(tupla)

8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

Exemplos IndentationError

a)
def nova():
print('harry')

b)
for i in range(10):
i+1
"""
i = 0

for i in range(10):
    print(i + 1)

print(i + 1)

# OBS: Exception e Erros são sinônimos na programação.
# OBS: Importante ler e prestar atenção na saída de erro.