"""
Ranges
- Precisamos conhecer o loops for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequ~encia numericas, não de forma aleatória,
mas sim de forma especificada.

Formas gerais:

#Forma 1

range(valor_de_parada)

for num in range(11):
    print(num)
OBS: valor_de_parada não inclusiva (início padrão 0, e passo de 1 em 1)

# Forma 2
range(valor_de_inicio, valor_de_parada)

for num in range(4, 11):
    print(num)

OBS: valor_de_parada não inclusiva (início especificado pelo usuário, e passa de 1 em 1)

# Forma 3
range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusiva (início especificado pelo utilizador, e passo especificado pelo utilizador)

#Forma 4: Inversa

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusiva (início especificado pelo utilizador, e passo especificado pelo utilizador)
"""

# Exemplo de Forma 3: a soma do primeiro número com o último.
for num in range(5, 50, 5):
    print(num)

#Exemplo Forma 4:
for num in range(10, 0, -1):
    print(num)

