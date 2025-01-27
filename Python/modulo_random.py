"""
Módulo Random e o que são módulos?

- Em Python, módulos nada mais são do que outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatório.


# OBS: Existem duas formas de se utilizar um módulo ou função deste

# Forma 1 - Importando todo o módulo ( Não recomendado).

import random

# random() -> Gera um número pseudo-aleatório entre 0 e 1.

# OBS: Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem
# dentro do módulo ficarão disponíveis. ( Ficarão em Memória). Caso você saiba quais funções você precisa utilizar
# deste módulo, então essa não seria a forma ideal de utilização. Nós veremos uma forma melhor na Forma 2.

print(random.random())

#  Veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função ]
#  separado por ponto.

# OBS: Não confuda função random() com o pacote random. Pode parecer confuso , mas a função random() é
# apenas uma função dentro do módulo random.
"""

"""
# Forma 2 - Importando uma função especifica do módulo.

from random import random
# No import  acima, estamos falando: Do módulo random, importe a função random

for i in range(1, 10):
    print(random())
"""
"""
# uniform() -> Gera um número pseudo-aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7).__round__(1)) # 7 Não é incluido. mas se utilizar round inclui OBS <---
"""
"""
# randint() -> Gera valores pseudo-aleatório entre os valores estabelecidos.

# Gerador de apostas para lotofacil

from random import randint

for i in range(15):
    print(randint(1, 25), end=', ')
    

# choice() -> Mostra um valor aleatório entre um iterável
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))
"""

# choice() -> Mostra um valor aleatório entre um iterável
from random import choice

print(choice('Harry Potter'))

# shuffle() -> Tem a função de embaralhar dados
from random import shuffle
cartas = ['K', 'J', 'Q', 'A', '2', '4','5', '6', '7']

print(cartas)

shuffle(cartas)

print(cartas.pop())