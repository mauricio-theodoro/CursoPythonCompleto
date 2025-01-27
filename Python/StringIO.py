"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional o softeware precisa
ter permissão:
    - Permissão de Leitura -> Para ler o arquivo.
    - Permissão de Escrita -> Para escrever no arquivo.

StringIO -> Utilizado para ler e criar arquivos em memória.

"""

# rimeiro fazemos o import
from io import StringIO

mensagem = 'Essa é uma mensagem de uma string normal'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto depois

arquivo = StringIO(mensagem)
# Arquivo = open('arquivo.txt', 'w')

# Agora tendo o arquivo, podemos utilizar o que já sabemos
print(arquivo.read())

# Escrevendo outros tetos
arquivo.write("mais um teste")

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())