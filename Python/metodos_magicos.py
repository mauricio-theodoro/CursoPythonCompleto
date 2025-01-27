"""
POO - Métodos Mágicos

Métodos Mágicos, são todos os métodos que utilizam dunder.

# dunder init -> __init__()
    def __init__(self, titulo, autor, pagina):
        self.titulo = titulo
        self.autor = autor
        self.pagina = pagina

Dunder > Double Underscore

# dunder repr -> Representação do objeto
    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'
"""

class Livro:

    def __init__(self, titulo, autor, pagina):
        self.titulo = titulo
        self.autor = autor
        self.pagina = pagina

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.pagina

    def __del__(self):
        print('Um objeto do tipo Livro foi deletado da memória')

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'


livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Inteligência Artifical com Python', 'Geek University', 350)

print(str(livro1))

print(str(livro2))
print(len(livro2))

print(livro1 * 3)