"""
Modos de Abertura de Arquivo

r ->  Abre para leitura - padrão
w -> Abre para escrita - sobreescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera FileExistError
a -> Abre para escrita, adicionando o conteúdo ao final do arquivo.
+ -> Abre para o modo de atualização: Leitura e Escrita. ( Temos o controle do cursor

# OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso exista, o novo conteúdo
sera adiconado SEMPRE ao final do arquivo. Com o modo 'a', não controlamos o cursor.
será adicionado ao final.

http://docs.python.org/3/library/functions.html#open
"""

"""
# Exemplo X
try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo\n')
except FileExistsError:
    print('Arquivo já existe')
"""
"""
with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input("Informe uma fruta ou digite 'sair': ")
        if fruta != 'sair':
            arquivo.write(fruta.title())
            arquivo.write('\n')
        else:
            break
"""
#Exemplo r+
with open('outro.txt', 'r+') as arquivo:

    arquivo.write('Adicionando\n')
    arquivo.seek(10)
    arquivo.write('Um novo de topo\n')
    arquivo.seek(12)
    arquivo.write('Nova linha\n')
    arquivo.write('Teste\n')