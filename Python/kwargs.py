"""
**kwargs

Poderiamos chamar esse parâmetro de **xis, ou qualquer outro nome desde que tenha os '**', mas por
convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras
em uma tupla, o **kargs exige que utilizemos parâmetros nomeados, e transforma esses parâmetro
extras em um dicionário.
"""
"""
# Exemplo:

def cores_favorita(**kargs):
    for pessoa, cor in kargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor.title()}')

cores_favorita(ana='Roxo', julia='amarelo', maria='Branco', caio='Verde')

#OBS: Os parâmetros *args e **kwargs não são obrigatórios.

cores_favorita()

cores_favorita(harry='teste')
"""
"""

#Exemplo mais complexo:

def cumprimento_especial(**kwargs):
    if 'harry' in kwargs and kwargs['harry'] == 'Python':
        return 'Você recebeu um cumprimento Pythonico'
    elif 'harry' in kwargs:
        return f'{kwargs['harry']} Harry'
    return 'Não tenho certeza de quem é você ...'


print(cumprimento_especial())
print(cumprimento_especial(harry='Python'))
print(cumprimento_especial(harry='Oi'))
print(cumprimento_especial(harry='Especial'))

"""
"""

# Nas nossas funções, podemos ter (NESSA ORDEM):
# - Parâmetros obrigatórios;
# - *args;
# - Parâmetros default (não obrigatórios);
# - **kwargs

def minha_funcao(idade, nome, *args, solteiro=True, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Roberta')
minha_funcao(30, 'Mauricio')
minha_funcao(27, 'Maira', 3, 5, 3, solteiro=False)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(122, 'Carla', 9, 4, 2, java=False, python=True)
"""
"""

#Entendendo porque é importante manter a ordem dos parâmetros na declaração:

# Função com a ordem correta de parâmetros
#def mostra_indo(a, b, *args, instrutor='Harry', **kwargs):
#    return [a, b, args, instrutor, kwargs]

# Função com a ordem incorreta de parâmetros
def mostra_indo(a, b, instrutor='Harry', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_indo(1, 2, 3, sobrenome='Faculdade', cargo='Instrutor'))
"""

# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f'{kwargs['nome']} {kwargs['sobrenome']}'

nomes = {'nome': 'Fernada', 'sobrenome': 'Montenegro'}

print(mostra_nomes(**nomes))


def soma_mutiplos_numeros(a, b, c, **kwargs):
    print(a + b + c)

lista = [1, 2, 4]
tupla = (1, 2, 4)
conjunto = {1, 2, 4}

soma_mutiplos_numeros(*lista)
soma_mutiplos_numeros(*tupla)
soma_mutiplos_numeros(*conjunto)

dicionarios = dict(a=1, b=2, c=3)
soma_mutiplos_numeros(**dicionarios)

#OBS: Os nomes da chave em um dicionário devem ser os mesmos dos parâmetros da função

#dicionarios = dict(d=1, e=2, f=3) # <-- Erro - TypeError
#soma_mutiplos_numeros(**dicionarios)
dicionarios = dict(a=1, b=2, c=3, nome='Harry')


print(dicionarios)