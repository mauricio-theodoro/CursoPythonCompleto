"""
Módulo Externo

Utilizamos o gerenciador de pacotes Python, chamado Pip - Python Installer Package

Podemos conhecer todos os pacotes externos oficiais em: https://pypi.org

colorama -> É utilizado para permitir impressão de textos coloridos no terminal.

Instalando um módulo Pip
"""

"""
# Utilizando o pacote colorama

from colorama import init, Fore, Back

init()

print(Fore.MAGENTA + 'Mauricio Theodoro')
print(Fore.BLUE + 'Harry Potter')
print(Back.RED + 'Harry Potter')
"""

# houve erro no meu terminal.. Vou arrumar e comento o que fiz para resolver o problema para exportação de pdf
import pydf
pdf = pydf.generate_pdf('<h1>this is html</h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)