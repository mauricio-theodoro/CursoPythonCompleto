"""
O operador Walrus permite fazer a atribuição e retorno de valor em uma única expressão.

variavel := expressão
"""
"""
nome = 'Geek University'
print(nome)

print(nome := 'Geek University')
"""
"""
cesta = []
fruta = input('Informe a fruta: ')
while fruta != 'manga':
    cesta.append(fruta)
    fruta = input('Informe a fruta: ')
"""
    # Python 3.8

cesta = []
while(fruta := input('Informe a fruta: ')) != 'manga':
    cesta.append(fruta)

print(cesta)