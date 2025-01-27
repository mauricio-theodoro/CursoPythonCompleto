"""
Escopo de variáveis

Dois casos de espoco:

1 - Variáveis globais;
    - Variáveis globais são reconhecidas, ou seja, seu escopo comoreende, todo o programa.
2 - Variáveis locais
    - Váriaveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu espoco
    está limitado ao bloco onde foi declarado.

Para declarar variáveis em Python fazemos:

nome_da_variavel = valore_da_variavel
Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero =42;
"""

numero = 42
print(numero)
print(type(numero))

numero = "harry"
print(numero)
print(type(numero))

numero = 534
if numero > 40:
    novo = numero + 10 # A variável 'novo' está declarada localmente dentro do bloco do if. Portanto, é local
    print(novo)
