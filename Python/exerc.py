

# 1. Faça um programa que leia um número inteiro e imprima-o
numero: int = int(input("Digite um número inteiro: "))

print(f"O número digitado foi {numero}")

# 2. Faça um programa que peça para o usuário digitar três valores inteiro e imprima a soma deles.
val1, val2, val3 = map(int, input("Digite três números inteiros separados por espaço: ").split())
print(type(val1))

soma = val1 + val2 + val3

print(f"A soma dos valores digitados são: {soma}")

# 3. Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos.

valor1, valor2, valor3 = map(int, input('Digite três números inteiros separados por espaço: ').split())

somaQuadrado = valor1**2 + valor2**2 + valor3**2

print(f'A soma dos quadrados dos valores lidos são: {somaQuadrado}')