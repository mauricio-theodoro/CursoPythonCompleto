"""
Preservando metadatas com wraps

Metadados -> São dados intrísecos em arquivos.

wraps -> funções que envolvem elementos com diversas finalidades.


def ver_log(funcao):
    def logar(*args, **kwargs):
        ""Eu sou função (logar) de outra""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    ""Soma dois números.""
    return a + b


print(soma(10, 30))

print(soma.__name__) # soma
print(soma.__doc__) # soma dois números.
"""

# Resolução do Problema

from functools import wraps

def ver_log(funcao):
    @wraps(funcao) # Preservar o meta dados das nossas funções
    def logar(*args, **kwargs):
        """Eu sou função (logar) de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois números."""
    return a + b


# print(soma(10, 30))

print(soma.__name__) # soma
print(soma.__doc__) # soma dois números.

print(help(soma))