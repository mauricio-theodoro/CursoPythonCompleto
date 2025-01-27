"""
Sistema de Arquivos - Manipulação

# Descobrindo se um arquivo ou diretório existe

print(os.path.exists('arquivo.txt')) # False
print(os.path.exists('frutas.txt')) # True



# Diretório
# Path relativo
print(os.path.exists('../FirstClass')) # True


#Path Absoluto
print(os.path.exists('/Users/Mauricio/PycharmProjects')) # True
print(os.path.exists('/Users/Mauricio/Estudos')) # False
print(os.path.exists('/Users/Mauricio/Links')) # True


# Criando arquivos

# Forma 1
open('arquivo-teste.txt', 'w').close()

# Forma 2
open('arquivo-teste2.txt', 'a').close()

# Forma 3

with open('arquivo-teste3.txt', 'w') as arquivo:
    pass

    # Criando arquivos

os.mknod('arquivo-teste4.txt')

# Se estiver utilizando no Mac OS, pode haver um erro de PermissionError

# OBS: Criando um arquivo via mknod(), se o arquivo existir teremos o erro FileExistsError


# OBS: A função mkdir() cria um diretório se este não existir. Caso exista, teremos FileExistsError

#Criando multi-diretorios (AVORES DE DIRETORIO)
os.makedirs('templates/geek/university')

# OBS: Se exsitir, teremos um FIleExistsError

os.makedirs('templates2/novo2/outro2', exist_ok=True)

# Renomear arquivos e diretórios
#Diretorios
os.rename('geek2/novo2', 'geek2')

# OBS: Se o diretório não existir teremos um FileNotFoundError

# OBS: Se o diretório que queremos renomear não estiver vazio teremos um OSError


# Renoameando nome do arquivo
# Arquivos
os.rename('geek2/novo2/outro2/texte.txt', 'geek2/novo2/outro2/geek2.txt')

#Deletando arquivos:

# ATENÇÃO Tome cuidado com os comandos de deletação. Ao deletar um arquivo ou diretorio, eles não
# Não vão para lixeira, eles somem.

os.remove('arquivo-teste3.txt')

#OBS: Se você estiver no Windows e o arquivo que você for deletar estiver em uso, você terá um erro.

# OBS: Caso o arquivo não exista, teremos o FileNotFoundError

# OBS: Se você informar um diretório ao invés de um arquivo, teremos um IsADirectoryError

# Removendo Diretórios

os.rmdir('templates')

# OBS: Se o diretório tiver qualquer conteúdo teremos um OSError

# OBS: Se o diretório não existir teremos um FileNotFoundError


# Removendo uma árvore de diretórios

for arquivo in os.scandir('geek2'):
    print(f'- {arquivo.name}')
    if arquivo.is_file():
        os.remove(arquivo.path)


# Podemos remover um árvore de diretórios vazios.

os.removedirs('geek2/novo1/teste2/onemore')

# Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para.

# ATENÇÃO: Ao remover os arquivos, eles não vão para a leixeira, eles são deletados permanentemente

# Se quiser que seja enviado para a lixeira é preciso installar um pacote: pip install send2trash

from send2trash import send2trash

os.remove('arquivo-teste.txt') # Não vai para a leixeira. E é deletado imediatamente

send2trash('arquivo-teste2.txt') # Vai para lixeira. Pode ser restaurado


# Importando a biblioteca send2trash (eneiva arquivos e diretórios para a leixeira)
from send2trash import send2trash

send2trash('templates')

# Trabalhando com arquivos e diretorios temporários


with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei um diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Teste no python para criar um diretorio e um arquivo\n')
        arquivo.write(input('Digite alguma coisa para ficar gravado no arquivo: '))
    input()

# Estamos criando um diretório temporario, abrindo o mesmo e dentro dele criando
# um arquivo para escrevermos um texto.No final, usamos um input() só para mantermos
# Os arquivos temporarios 'vivos' dentro dos blocos with

# OBS: Possivelmente o codigo acima não irá funcionar se você estiver utilizando o Windows
# Por conta desse sistema trabalhar de forma diferente com arquivos temporarios


# Criando um arquivo temporario

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Harry Potter\n')
    tmp.seek(0)
    print(tmp.read())


# Sem o bloco with

#OBS: Em arquivos temporarios só conseguimos escrever em bits. Por isso, utilizamos o b''
arquivo = tempfile.TemporaryFile()
arquivo.write(b'Harry Potter\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

"""

import os
import tempfile



arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Harry Potter\n')

print(arquivo.name)

print(arquivo.read())

input()