"""
Loop while

Forma geral

while expressão_booleana:
    //execução do loop

O bloco do while será repitida enquanto a expressão booleana for verdadeira.

Expressão Booleana é toda expressão onde o resultado é verdadeiro ou falso.

Exemplo:

num = 5

num <= 5

Exemplo 1:
num = 1
while num < 10:
    print(num)
    num += 1

    # Exemplo 2

reposta = ''
while reposta != "sim":
    reposta = input("Já acabou ?")

OBS: Em um loop while, é importante que cuidemos do critério de parada para não causar um loop infinito.

# C OU JAVA
while(expressão){
    //execução
}
# Do while não existe no Python.
"""
# Exemplo 2

reposta = ''
while reposta != "sim":
    reposta = input("Já acabou ?")