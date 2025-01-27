"""
Funções com Parametro Padrão - Defaul Paramters)

- Funções onde a passagem de parâmetro seja opcional;

#Exemplo de função onde a passagem de parâmetro seja opcional
print("Harry Potter')

print()

#Exemplo de função a passagem de prâmetro seja obrigatória
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado()) <-- TypeError

"""

"""
def exponecional(numero, potencia=2):
    return numero ** potencia

print(exponecional(2, 3))  # 2 * 2 = 8
print(exponecional(3, 2)) # 3 * 3 = 9

print(exponecional(3)) # Por padrão eleva ao quadrado
print(exponecional(3,5)) # Eleva á potência informada pelo usuário.

#OBS
# Se o usuário passar somente 1 argumento, este atribuído ao parâmetro numero, e será calculado o quadrad deste número;
# Se o usuário passar 2 argumentos, o primeiro será atribuído ao parâmetro número e o segundo ao parâmetro potencial.
# Então será calculada esta potência

print(exponecional())
"""


#OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração
"""
#ERRO
def teste(potencia, num=2):
    return num ** potencia


print(teste(6))
"""
"""
# Outros exemplos

def soma(num1=5, num2=4):
    return num1 + num2

print(soma(4, 3))
print(soma(4)) 
print(soma())
"""
"""
# Exemplo mais complexo

def mostra_informacao(nome='Harry', bruxo=False):
    if nome == 'Harry' and bruxo:
        return f"Bem-vindo Bruxo {nome}"
    elif nome == 'Harry':
        return 'Eu pensei que você fosse o Bruxo!'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(bruxo=True))
print(mostra_informacao(True))
print(mostra_informacao('Potter'))
print(mostra_informacao(nome='Harry'))

"""

# Por que utilizar parâmetros com valor default?

"""
- Nos permite ser mais flexíveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplo mais legíveis de código;

"""

# Quais tipos de dados podemos utilizar como valores default para parâmetros?
"""
- Qualquer tipo de dado:
    - Números, String, floats, booleanos, listas, tuplas, dicionários, funções e etc..;
    
"""

"""
# Exemplos

def soma(num1, num2):
    return num1 + num2

def mat (num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))
"""
"""
# Escopo - Evitar problemas e confusões

# Variáveis globais
# Variáveis locais

instrutor = 'Harry' # Variável global

def diz_oi():
    instrutor = 'Python'
    return f'Oi {instrutor}'

print(diz_oi())

#OBS: SE TIVERMOS UMA VARIAVEL LOCAL COM O MESMO NOME DE UMA VARIALVEL GLOBAL, A LOCAL TERÁ PREFERENCIA

total = 0

def diz_oi():
    prof = 'Python'
    return f'Olá {prof}'

print(diz_oi())

print(prof) # NameError


def incrementa():
    total = total + 1 # UnboundLocalError ( A variável local está sendo utilizada para processamento sem ter sido inicializada.
    return total

print(incrementa())

"""
"""
# Atenção com variáveis globais (Se puder evitar, evite!)

total = 0

def incrementa():
    global total
    total += 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())
"""

# Podemos ter funções que são declaradas dentro de funções, e também possuimos uma forma especial de escopo de variável


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador += 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())

print(dentro()) # NameError