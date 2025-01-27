"""
Definindo Funções

- Funções são pequenos trechos de código que realizam tarefas específicas:
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplificada.

Já utilizamos várias funções desde que iniciamos:
    - print()
    - len()
    - max()
    - min()
    - count()
    - e mais;
"""
"""
# Exemplo de utilização de funções:

cores = ['verde', 'amarelo', 'azul', 'branco']

#Utilizando uma função integrada do Python. (Built-in) do Python printo()

print(cores)

curso = "Programação em PYTHON"

for i in cores:
    print(i)

print(curso)
cores.append('roxo')
print(cores)

# curso.append('Mais dados...') # AttributeError
# print(curso)

cores.clear()
print(cores)

# print(help(print))

#DRY - Don't Repeat Yourself -  Não repita seu código.

# Como definir funções:
"""
"""
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
Onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome compostom separado por underline (Snake Case)
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
nesse bloco pode ter ou não retorno da função.

OBS: Veja que, para definir uma funçãom, utilizamos a palavra reservada 'def', informando ao Python que estamos
definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos : que é utilizado em Python para
para definir blocos.

"""

#Definindo a primeira função:

def diz_oi():
    print('oi!')

"""
OBS:

1 - Veja que, dentro da nossa função podemos utilizar outra função;
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que essa função não recebe nenhum parâmetro de entrada;
4 - Veja que esta função não retorna nada;
"""

#Utilizando funções

# Chamada de execução
# diz_oi()

"""
ATENÇÃO:

Nunca esqueça de utilizar o parênteses ao executar uma função.

Exemplo:

# Errado!
diz_oi

# Certo
diz_oi()

# Errado!
diz_oi ()


"""

# Exemplo 2

def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data queriada')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!!')

for i in range(5):
    cantar_parabens()

cantar = cantar_parabens

cantar()