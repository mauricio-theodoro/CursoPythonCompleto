"""
Métodos de Data e Hora

import datetime

#Com o now() podemos especificar um timezone (Fuso Horário)
agora = datetime.datetime.now()

print(agora)

print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today()

print(hoje)

print(type(hoje))
print(repr(hoje))
-------


# Mudanças ocorrendo à meia-noite

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao)
print(type(manutencao))
print(repr(manutencao))

------------


# Encontrar o dia da semana, weekday()

# Os dias da semana do método weekday() começa em 0

# 0 - Segunda-feira (Mondey)
# 1 - Terça-Feira (Tuesday)
# 2 - Quarta-Feira (Wednesday)
# 3 - Quinta-Feira (Thursday)
# 4 - Sexta-Feira (Friday)
# 5 - Sabado (Sartuday)
# 6 - Domingo (Sunday)

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao.weekday())

------------
import datetime

aniversario = input('Qual é a data do seu nascimento? (dd/mm/yyy): ')

aniversario = aniversario.split('/')

aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Você nasceu em uma Segunda-feira')
elif aniversario.weekday() == 1:
    print('Você nasceu em uma Terça-feira')
elif aniversario.weekday() == 2:
    print('Você nasceu em uma Quarta-feira')
elif aniversario.weekday() == 3:
    print('Você nasceu em uma Quinta-feira')
elif aniversario.weekday() == 4:
    print('Você nasceu em uma Sexta-Feira')
elif aniversario.weekday() == 5:
    print('Você nasceu em uma Sabado')
elif aniversario.weekday() == 6:
    print('Você nasceu em um Domingo')

    -------------

import datetime

# Formatando datas/horas com strtime() (String Format Time)
# dd/mm/yyyy hora:minuto

hoje = datetime.datetime.today()

print(hoje)

# hoje_formatado = hoje.strftime('%d/%m/%Y')
hoje_formatado = hoje.strftime('%d/%b/%Y')

print(hoje_formatado)
---------

def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Março de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    elif data.month == 12:
        return f'{data.day} de Dezembro de {data.year}'
    else:
        return f'Opção inválida'
----------------------------

import datetime
from googletrans import Translator

def formata_data(data):
    translator = Translator()
    mes_em_ingles = data.strftime('%B')  # Nome do mês em inglês
    mes_em_portugues = translator.translate(mes_em_ingles, src='en', dest='pt').text  # Tradução para português
    return f"{data.day} de {mes_em_portugues} de {data.year}"

# Data/hora atual
hoje = datetime.datetime.today()

print(formata_data(hoje))

----------------

import datetime



nascimento = datetime.datetime.strptime('11/03/1994', '%d/%m/%Y')

print(nascimento)

nascimento = input('Qual é sua data de nasicmento? (dd/mm/yyyy): ')

nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')

print(nascimento)
--------------------------

import datetime

#Somente a hora

almoco = datetime.time(12,30, 0)

print(almoco)

------------------------
import timeit

# Marcando tempo de execução do nosso código com timeit

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

#List Comphension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)
"""
import timeit, functools

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma

print(timeit.timeit(functools.partial(teste, 2), number=10000))
