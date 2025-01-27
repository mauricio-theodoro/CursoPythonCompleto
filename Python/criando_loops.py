"""
Criando sua própria versão de loop

for num in [1, 2, 3, 4, 5]:
    print(num, '\n')

for letra in 'Geek University':
    print(letra)

iter([1, 2, 3, 4, 5])

iter('Geek University')
"""

def forpy(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

numeros = [1, 2, 3, 4, 5]

forpy(numeros)
