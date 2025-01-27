"""
Leitura de Arquivos

Para o conteudo de um arquivo em Python, utilizamos a função integrada open(),
que significa 'abrir'

open() -> Na forma mais simples de utlização nós passamos apenas um parâmetro
de entrada, que neste caso é o caminho para o arquivo a ser lido. Essa função
retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

http://docs.python.org/3/library/functions.html#open

# OBS: Por padrão, a função open() abre o aruqivo para leitura. Este arquivo deve
existir, ou então teremos o erro FileNotFoundError

mode r -> Modo de Leitura. r -> read() -> ler
"""

#Exemplo

arquivo = open('texto.txt')

print(arquivo)

print(type(arquivo))

# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()

print(arquivo.read())

# OBS: O Python, utiliza um recurso para trabalhar com arquivo chamado cursor. Esse cursor,
# Funciona como o cursor quando estamos escrevendo.


# OBS: A função read() lê todo o conteúdo do arquivo.

ret = arquivo.read()

print(type(ret))
print(ret)
