"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre àspas simples -> 'uma string', '234', 'e', 'True', '42.3'
- Sempre que estiver entre àspas duplas -> "uma string", "234", "e", "True", "42.3"
- Sempre que estiver àspas simples triplas -> '''uma string''', '''234''', '''e''', '''True''', '''42.3'''
"""
# Estiver entre àspas duplas triplas -> """uma string""", """234""", """a""", """True""", """43.5"""

nome = 'Hello World'
print(nome)
print(type(nome))

nome = "Gina's \nBar"
print(nome)
nome = 'High School'
print(nome.upper())
print(nome.split()) # Transforma em uma lista de string

# Se estiver entre àspas triplas -> """um string"""",  """423""", """t""", """False""", """95434.9"""

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ['W', 'Z', 'z', 'o', 'T', 'D', 'k', 'h', 'm', 'z']

nome = "harry potter"
print(nome[0:5]) # Slice de string

print(nome[10])
"""
[:: - 1] -> Comce do primeiro elemento, e vá até o útilmo elemento e inverta-los
"""
print(nome[::-1]) # Inversão da String Pythônico
print(nome)

print(nome.replace('h', 'y'))
print(nome.replace('r', 'k'))

texto ="socorram me subino onibus em marrocos" # Palíndromo
print(texto)

print(texto[:: - 1]) # Palíndromo