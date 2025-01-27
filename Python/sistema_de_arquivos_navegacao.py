
"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do módulo
os.

os -> Operating System - Sistema Operacional

Exemplo de caminhos: C:\\Users\\Mauricio\\PycharmProjects\\FirstClass
"""
"""
import os

# Exibe o diretório de trabalho atual
print(os.getcwd())  # Exibe o caminho absoluto do diretório corrente

# Alterando o diretório atual para o nível acima
os.chdir('..')
print(os.getcwd())

# Alterando novamente para o nível acima
os.chdir('..')
print(os.getcwd())

# Verificando se o caminho é absoluto
print(os.path.isabs(r'C:\\Users\Mauricio\PycharmProjects\FirstClass'))  # True
"""
import os



# Podemos listar os arquivos e diretórios com mais detalhes com scandir()


scanner = os.scandir()
print(list(scanner))

arquivos = list(scanner)
#print(arquivos)

print(arquivos[0].inode()) #
print(arquivos[0].is_dir()) # É um diretório ? False
print(arquivos[0].is_file()) # É um arquivo? True
print(arquivos[0].is_symlink()) # É um link simbólico? False
print(arquivos[0].path) # caminho até o arquivo
print(arquivos[0].name) # Nome do arquivo
print(arquivos[0].stat()) # Estatísticas...

# OBS: Quando utilizamos a função scandir() nós precisamos fecha-la, assim quando abrimos um arquivo.

scanner.close()