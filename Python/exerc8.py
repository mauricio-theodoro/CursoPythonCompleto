def contar_linhas(nome_arquivo):
    try:
        # Abre o arquivo no modo de leitura
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            # Conta o número de linhas no arquivo
            numero_linhas = sum(1 for _ in arquivo)

        # Retorna o número de linhas
        return numero_linhas

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    # Solicita ao usuário o nome do arquivo
    nome_arquivo = input("Digite o nome do arquivo texto: ").strip()

    # Chama a função para contar linhas
    resultado = contar_linhas(nome_arquivo)

    if resultado is not None:
        print(f"O arquivo contém {resultado} linhas.")
