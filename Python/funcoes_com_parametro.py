"""
Funções com parâmetro ( de entrada)

-Funções que recebem dados para serem processados dentro da mesma;
Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processsamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada, mas não possuem saída;
- Não possuem entrada, mas possuem saída;
- Possuem entrada e saída;

"""

# Refatoruando uma função

def quadrado(numero):
    return numero * numero

"""
print(quadrado(6))
print(quadrado(2))
print(quadrado(7))

ret = quadrado(5)
print(ret)

print(quadrado()) # TypeError
"""

"""
aniversariante = str(input('Digite um nome:'))

def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data queriada')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o/a {aniversariante}!!')


cantar_parabens(aniversariante.title())

# Funções podem ter n parâmetros de entrada, ou seja, podemos receber como entrada
# em uma função quantos parâmentros forem necessários, ele são separados por vírgula.

#Exemplo

def soma(a, b):
    return a + b

print(soma(a= 5, b=6))

def mutiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5))
print(soma(5, 20))

print(mutiplica(5, 5))
print(mutiplica(2, 5))

print(outra(5, 5, "Curso "))

# OBS: Se a gente informar um número errado de parâmetro ou argumentos, teremos TypeError.

# print(soma(2, 3, 4)) # <-  TypeError - Passando argumentos a mais.
# print(soma(4)) # <- TyperError - Passando argumentos a menos

# Nomeando parâmentros

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Harry', 'Potter'))

# A diferença entre parâmentros e argumentos

# Parâmetros são variáveis declaradas na definição de uma função;
# Argumenos são dados passados durante a execução de uma função;

# A ordem dos parâmetros importa!

nome = 'Felicia'
sobrenome = 'Marrone'

print(nome_completo(nome, sobrenome))

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos
# utilizar qualquer ordem.

print(nome_completo(nome='Angelica', sobrenome="Theodoro"))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcio'))
"""

# Erro comum na utilização do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))
    print(type(soma_impares(lista)))

    tupla =  (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(tupla))
    print(type(soma_impares))