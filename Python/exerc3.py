# 1. Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números
# maiores que 0.

print(f"Lista múltiplo de 3: {[3 * i for i in range(1, 6)]}")

#Exemplo 2
# Inicializamos o contador e o valor do múltiplo
contador = 1
# Loop para mostrar os cinco primeiros múltiplos de 3
while contador <= 5:
    print(contador * 3)  # Calcula e exibe o múltiplo de 3
    contador += 1  # Incrementa o contador

#2. Faça um programa que utilize o comando while para mostrar na tela uma contagem regressiva, iniciando
# em 10 e terminando em 0. Mostre também uma mensagem “FIM!” após a contagem.
# Início da contagem regressiva
num = 10

# Loop para a contagem regressiva
while num >= 0:  # Continua enquanto num for maior ou igual a 0
    print(num)  # Mostra o valor atual de num
    num -= 1  # Decrementa 1 a cada iteração
# Mensagem final
print("FIM!")

#3. Faça um programa que declare um inteiro, inicialize-o com 0, incremente-o de 1000 em 1000, imprimindo
# seu valor na tela, até que seu valor seja 100000 (cem mil).

numero = 0
while numero <= 100000:
    print(numero)
    numero += 1000
# Exemplo 2
for n in range(0, 100001, 1000):
    print(n)