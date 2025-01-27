
def funcao1():
    print('Curso de Python - primeiro.py')


if __name__ == '__main__':
    funcao1()
    print('primeiro.py está sendo executado diretamente')
else:# geralmente o else não existe aqui!
    print(f'primeiro.py foi importado. {__name__}')