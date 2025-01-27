"""
Pacotes

Módulo -> É apenas um arquivo Python que pode ter diversas funções para utilizarmos;

Pacote -> É um diretório contendo uma coleção de módulos;

OBS: Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um arquivo chamado __init__.py

Nas versões do Python 3.x não é mais obrigatória a utilização deste arquivo, mas normalmente ainda é
utilizado para amnter compatibilidade

# A pasta aula e todos os arquivo lá pertence a esse aula.
"""

"""

from aula import aula1, aula2

from aula.subpacote import aula3, aula4

print(aula1.pi)

print(aula1.funcao1(3,6))

print(aula2.curso)

print(aula2.funcao2())

print(aula3.funcao3())

print(aula4.funcao4())
"""

from aula.aula1 import funcao1


from aula.subpacote.aula4 import funcao4


print(funcao1(4,7))

print(funcao4())