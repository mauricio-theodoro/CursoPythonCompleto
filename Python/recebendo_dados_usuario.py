"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String
Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplo:
- Aspas simples -> 'Rihanna'
- Aspas duplas -> "Rihanna"
- Aspas simples triplas -> '''Rihanna'''
"""
# - Aspas duplas triplas -> """Rihanna"""

# print("Qual é o seu nome? ")
# nome = input() # Input -> Entrada
nome = input("Qual é o seu nome: ")
# print("Qual é a sua idade:")
idade = int(input("Qual é a sua idade:"))
print(idade)

# Exemplos de print

print(f"Seja bem-vindo(a) {nome.title()}")
print(f"{nome.title()} tem {idade} anos")

print(f'{nome.title()} nasceu em {2024 - idade}')

# print("Seja bem-vindo(a) {0}, você tem {1} anos".format(nome.title(), idade))

# Processamento

# Saída de dados
# print("Seja bem vindo(a) %s" % nome.title())
# print("A %s tem %s anos" % (nome.title(), idade))