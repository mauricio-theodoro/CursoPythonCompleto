"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

Toda Entrada do usuário, deve ser tratada!

# Else -> É executado somente se não ocorrer erro.
try:
    num = int(input('Infome um número: '))
except ValueError:
    print('Valor incorreto!')
else:
    print(f'Você digitou o {num}')

# Finally

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o finally')

# OBS: O bloco finally é sempre executado. Independente se houve exceção ou não.

# O finally, geralmente, é utilizado para fechar ou desalocar recursos.
"""
"""
# Exemplo mais complexo ERRADO!

def dividir(a, b):
    return a / b

num1 = float(input('Informe um número: '))
try:
    num2 = float(input('Informe outro número: '))
except ValueError:
    print('O valor precisa ser numerico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')
"""
"""
# Exemplo mais complexo Correto!

# OBS: A pessoa que criou a função é responsavel pelas entradas, então é preciso tratá-las!

def dividir(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        return "Erro: divisão por zero"
    except ValueError:
        return "Erro: valor incorreto"

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

resultado = dividir(num1, num2)

if isinstance(resultado, float):
    print(f"O resultado é: {round(resultado, 2)}")  # Usando round() para 2 casas decimais
else:
    print(resultado)
"""

def dividir( a, b):
    try:
        return float(a) / float(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um proble: {err}'

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

print(dividir(num1, num2))