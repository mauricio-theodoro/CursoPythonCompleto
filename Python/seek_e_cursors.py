"""
Seek e Cursors

seek() -> é utilizado para movimentar o cursor pelo arquivo
"""
"""
arquivo = open('texto.txt')

print(arquivo.read())

# A função seek() server ou é utilizada para movimentação do curso pelo arquivo. Ela recebe um
# parâmetro que indica onde queremos colocar o cursor


# Movimentando o cursor pelo arquivo com a função seek() - > Procurar
arquivo.seek(0)

print(arquivo.read())

arquivo.seek(20)
"""

arquivo = open('texto.txt')

# readline() -> Função que lê o arquivo linha a linha
"""
ret = arquivo.readline()

##print(type(ret))
#print(ret.split(' '))
#print(arquivo.readline())
#print(arquivo.readline())

linhas = arquivo.readlines()

print(len(linhas))

OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco do sistema operacional
e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar
os trabalhos com o arquivo devemos fechar essa conexão. Para isso utilizamos a função close()

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo;

2 - Trabalhar o arquivo;

3 - Fechar o arquivo;
"""
"""
# 1 - Abrir o arquivo;
arquivo = open('texto.txt')

# 2 - Trabalhar o arquivo;
print(arquivo.read())
print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado.

# 3 - Fechar o arquivo;
arquivo.close()
print(arquivo.closed)

# OBS: Se tentarmos manupular o arquivo após o seu fechamento, teremos um ValueError
"""

print(arquivo.read(150))