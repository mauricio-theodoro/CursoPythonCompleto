from traceback import print_tb

#1. Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores
# lidos.

#Loop para ler 6 valores inteiros

lista = []
print('Digite 6 valores inteiros:')
while len(lista) < 6:
    valor = int(input(f'Digite o valor {len(lista) + 1}/6: ')) # Solicitando ao usuário um valor inteiro
    lista.append(valor) # Adiciona o valor à lista

for valor in lista:
    print(valor)

# Fazendo o mesmo em uma linha:

lista = [int(input(f'Digite o valor {i + 1}/6: ')) for i in range(6)]
print(f'Os valores da lista são: {lista}')

# 2. Faça um programa que possua uma lista denominada A que armazene 6 números inteiros. O programa
# deve executar os seguintes passos:

# Passo a: Criar a lista A com os valores especificados
A: list[int] = [1, 0, 5, -2, -5, 7]

# Passo b: Calcular a soma dos valores das posições A[0], A[1] e A[5]
soma: int = A[0] + A[1] + A[5]
print(f"Soma dos valores nas posições A[0], A[1] e A[5]: {soma}")

# Passo c: Modificar a lista na posição 5, atribuindo o valor 100
A[5] = 100

# Passo d: Mostrar cada valor da lista A, um por linha
print("\nValores da lista A:")
for valor1 in A:
    print(valor1)

A = [1, 0, 5, -2, -5, 7];

print("Soma:", A[0] + A[1] + A[5]); A[5] = 100; print(*A, sep="\n")

# 3. Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele
# possui.

listagem: list[int] = []
contador_pares: int = 0

while len(listagem) < 10:
    valor3: int = int(input(f'Informe o valor {len(listagem) + 1}/10: '))
    listagem.append(valor3)

    if valor3 % 2 == 0:
        contador_pares += 1

if contador_pares > 0:
    print(f'A lista {listagem} possi {contador_pares} pares.')
else:
    print(f'A lista {listagem} não possui valores pares.')