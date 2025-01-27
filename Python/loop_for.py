"""
Loop for

Loop -> Estrutura de repetição.
For -> É uma dessas estruturas.
C ou JAVA

for(int i =0; i < 10; i++){
//execução do loop
}

Python
for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequência ou sobre valores interáveis.

Exemplos de iteráveis:
- String
    nome = "Harry Potter"
- Lista
    lista = [1, 4, 6, 7, 8, 9]
- Range
    numeros = range(1, 10)
"""
nome = "Harry Potter"
lista = [1, 2, 3, 4, 5, 6]
numeros = range(1, 10) # É preciso transformar em uma lista
#Exemplo de for 1 (Iterando em um string)
for letra in nome:
    print(letra)

#Exemplo de for 2 (Iterando sobre um lista)
for numero in lista:
    print(numero)

#Exemplo de for 3 (Iterando sobe um range)
"""
range(valor_inicial, valor_final):
OBS: O valor final não é incluido
"""
for numero in range(1, 11):
    print(numero)

"""
Enumerate:

for i, v in enumerate(nome):
    print(nome[i])
    
OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)


for valor in enumerate(nome):
    print(valor[1])
"""
for _, l in enumerate(nome):
    print(l)

for valor in enumerate(nome):
    print(valor)

"""
qtd = int(input("Quantas vezes esse loop deve rodar? "))
for n in range(1, qtd + 1):
    print(f"Imprindo {n}")

qtd = int(input("Quantas vezes esse loop deve rodar? "))
soma = 0
for n in range(1, qtd + 1):
    num = int(input(f"Informe o {n}/{qtd} valor: "))
    soma += num
print(f"A soma é: {soma}")


#For sem pular linhas
nome = 'Harry Potter'
for letra in nome:
    print(letra.lower(), end='')
"""



"""
Tabela de Emoji
https://apps.timwhitlock.info/emoji/tables/unicode
"""
#Original: U+1F63C
#Modificado: U0001F63C
pisciano =  '\U00002653'

for _ in range(3):
    for num in range(1, 11):
        print(pisciano * num)