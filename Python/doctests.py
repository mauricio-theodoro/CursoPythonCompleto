"""
Doctests

Doctests são testes que colocamos na docstring das funções/métodos Python.

Para rodar um test do doctest:

python -m doctest -v nome_do_modulo.py

def soma(a, b):
   #  Soma os numeros a e b
  #  >>> soma(1, 2) # < -- isso é um doctest
  #  3
  #  >>> soma(12, 2)
 #   14
 #
 #  return a + b

#print(soma(4,3))
"""
"""
# Outro exemplo, Aplicando o TDD

def duplicar(valores):
    #duplique os valores em uma lista
   # >>> duplicar([1, 2, 3, 4])
   # [2, 4, 6, 8]

   # >>> duplicar([])
   # []

  #  >>> duplicar(['a', 'b', 'c'])
   # ['aa', 'bb', 'cc']

   # >>> duplicar([True, None])
   # Traceback (most recent call last):
   #     ...
    #TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    return [2 * elemento for elemento in valores]
    """

"""
# Erro inesperado...
OBS: Dentro do doctest, o Python não reconhece string com aspas duplas. Precisa ser aspas simples.
def fala_oi():
#    Fala oi
#    >>> fala_oi()
    'oi'
    """
#    return "oi"

# Um último caso estranho...

def verdade():
    """Retorna verdade
    >>> verdade()
    True
    """
    return True