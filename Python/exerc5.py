#1. Crie um programa que tenha uma função que recebe um parâmetro inteiro e devolve o seu dobro.

def inteiro(numero_int):
    return numero_int * 2


numero = int(input('Digite um número para receber o dobro do valor: '))
print(f'O dobro de {numero} é {inteiro(numero_int=numero)}')

# 2. Faça um programa que tenha uma função que recebe uma data no formato string exemplo “01/01/2024” e
# imprima ela por extenso como “1 de janeiro de 2024”.


def formatacao(data_str):
    # Dicionário para mapear os números dos meses para seus nomes
    meses = {
        1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril", 5: "maio", 6: "junho",
        7: "julho", 8: "agosto", 9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
    }
    # Divide a data em dia, mês e ano
    dia, mes, ano = map(int, data_str.split('/'))
    # Retorna a data formatada por extenso
    return f"{dia} de {meses[mes].title()} de {ano}"
# Entrada do usuário


data = input("Digite a data no formato DD/MM/AAAA: ")
try:
    resultado = formatacao(data)  # Tenta formatar a data
except (ValueError, KeyError):  # Captura erros específicos
    print("Por favor, insira uma data válida no formato DD/MM/AAAA.")
else:
    # Se não houver nenhum erro, exibe a data formatada
    print(f"Data formatada: {resultado}")
finally:
    # Código que será executado sempre, independentemente de erros
    print("Obrigado por usar o programa!")

# 3. Faça um programa que tenha uma função que receba uma lista de inteiros e retorne o maior valor.

# Função para encontrar o maior valor em uma lista


# Função para encontrar o maior valor em uma lista
def encontrar_maior(lista_inteiros):
    if not lista_inteiros:  # Verifica se a lista está vazia
        return "A lista está vazia. Não é possível determinar o maior valor."
    return max(lista_inteiros)  # Retorna o maior valor usando a função embutida `max`

# Lista para armazenar os números inteiros
inteiros = []

# Loop para coletar os números
while True:
    try:
        numero = int(input("Digite um número inteiro (ou 0 para sair): "))
        if numero == 0:  # Condição para encerrar o loop
            break
        inteiros.append(numero)  # Adiciona o número à lista
    except ValueError:
        print("Por favor, insira apenas números inteiros.")

# Processa a lista de inteiros e exibe o maior valor
if inteiros:  # Verifica se a lista não está vazia
    maior_valor = encontrar_maior(inteiros)
    print(f"O maior valor da lista é: {maior_valor}")
else:
    print("Nenhum número foi inserido. Encerrando o programa.")



