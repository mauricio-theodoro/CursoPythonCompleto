"""
Modo tradicional:
valor1, valor2 = map(int, input('Digite dois números inteiros separados por espaço: ').split())

if valor1 > valor2:
    print(f"O número maior é:{valor1}")
else:
    print(f"O número maior é: {valor2}")

explicando o : print(f"O maior número é: {max(map(int, input('Digite dois números inteiros separados por espaço: ').split()))}")
input('Digite dois números inteiros separados por espaço: ') O que faz: Exibe a mensagem no terminal pedindo que o usuário insira dois números inteiros separados por espaço.
.split() O que faz: Divide a string retornada por input() em uma lista de substrings, separando-as com base no espaço.

map(int, ...) O que faz: Converte cada elemento da lista retornada por .split() de string para inteiro. ou seja, vai criar não só 2 variaveis, mas a quantidade que o usuário for digitando, é uma lista! então não tem necessidade de criar variaveis. o map é um loop explícito
max(...) O que faz: Determina o maior valor na sequência de inteiros retornada pelo map. essa função simplesmente busca o maior valor na lista, já fazendo a comparação entre eles.

f"O maior número é: { max(..) }" O que faz: Formata a mensagem de saída usando uma f-string.

"""
from math import sqrt

# 1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior
print(f"O maior número é: {max(map(int, input('Digite dois números inteiros separados por espaço: ').split()))}")

# Exemplo 2
valor1, valor2 = map(int, input('Digite dois números inteiros separados por espaço: ').split())


if valor1 > valor2:
    print(f"O número maior é:{valor1}")
elif valor1 == valor2:
    print(f"Os números {valor1} e {valor2} são iguais.")
else:
    print(f"O número maior é: {valor2}")

# 2. Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
# a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
# número é inválido.

n = int(input("Digite um número inteiro: "))
print(f"A raiz quadrada é: {sqrt(n)}" if n >= 0 else "Número inválido")

# 3. Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.
print("Par" if (n := int(input("Digite um número inteiro: "))) % 2 == 0 else "Ímpar")

# Soma de 2 números ou +
print("Resultado:", (sum(map(int, input('Digite dois números inteiros separados por espaço para serem somados: ').split()))))