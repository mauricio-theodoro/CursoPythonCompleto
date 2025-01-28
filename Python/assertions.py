"""
Assertions (Afirmações/Questionamentos)

Em Python utilizamos a palavra reservada 'assert' para realizar simples afirmações
utilizadas nos testes.

Utilizamos o 'assert' em uma expressão que queremos checar se é válida ou não.
Se a expressão for verdadeira, o assert retorna None e caso seja falsa levanta um erro
do tipo AssertionError.

# OBS: Podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro
personalizada.

# OBS: A palavra 'assert' pode ser utilizada em qualquer função ou código nosso... não precisa
ser exclusivamente nos testes.

Se um programa Python for executado com o parâmetro -O, nenhum assertion será validado.

"""

def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a + b

ret = soma_numeros_positivos(5, 3) # 8
# ret = soma_numeros_positivos(-5, 3) # AssertionError
print(ret)

def comer_fast_food(comida):
    assert comida in[
        'pizza',
        'sorvete',
        'Batata',
        'Arroz',
        'Feijão',
        'cachorro quente'
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'


food = input('Informa a comida: ')

print(comer_fast_food(food))

# ALERTA: Cuidado ao usar Assertion, se for utilizado com -O o erro não vai notificar

def faca_algo_ruim(usuario):
    assert usuario.eh_admin, 'Somente administradores podem ter acesso!'
    destroi_todo_o_sistema() # <-- apenas um exemplo caso use o assert de maneira errado o usuario pode acessar.
    return 'Adeus'