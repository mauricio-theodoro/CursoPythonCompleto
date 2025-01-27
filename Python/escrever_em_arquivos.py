"""
Escrevendo em arquivos


# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacioal.

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Esta função recebe uma string como parâmetro.

Abrindo um arquivo para escrita com o modo 'w' se o arquivo não existir será criado,
caso ele já exista, o antérior será apagado e um novo será criado. Dessa forma, todo o contéudo no arquivo
anterior é perdido.
"""
"""
# Exemplo de escrita - modo 'w' - write (escrita)

# Forma Pythônica
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito fácil. \n')
    arquivo.write('Podemos colocar quantas linhas quisermos\n')
    arquivo.write('Essa é a última linha.')
"""
"""
# Forma tradicional de escrita em arquivo (Não Pythônica)
arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer\n')
arquivo.write('Mais um texto.')

arquivo.close()
"""
"""
with open('harry.txt', 'w') as arquivo:
    arquivo.write('Harry\n' * 1000)
"""

with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input("Informe uma fruta ou digitie 'sair': ")
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
