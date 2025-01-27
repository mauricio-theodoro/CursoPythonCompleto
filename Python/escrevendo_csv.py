"""
Escrevendo em arquivos CSV

reader() (leitor), write() (escritor)

writerow() -> Escrever uma linha
"""
"""
# writer() -> Gera um objeto para que possamos escrever em um arquivo CSV. Utilizamos o método
# writerow() para escrever cada linha. Este método recebe uma lista.
from csv import writer

with open('filme.csv', 'w') as arquivo:
    escritor_csv =writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero:')
            duracao = input('Informe a duração (em minutos):')
            escritor_csv.writerow([filme, genero, duracao])
"""

# DictWriter

from csv import DictWriter

with open('filmes2.csv', 'w') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow({'Título': filme, 'Gênero': genero, 'Duração': duracao})