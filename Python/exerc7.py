def contar_vogais_e_consoantes(nome_arquivo):
    try:
        # Abre o arquivo no modo de leitura
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()

        # Define os conjuntos de vogais e consoantes
        vogais = set("aeiouáéíóúâêîôûãõ")  # Inclui acentos comuns em português
        consoantes = set("bcdfghjklmnpqrstvwxyz")

        # Inicializa os contadores
        contador_vogais = 0
        contador_consoantes = 0

        # Conta as vogais e consoantes no conteúdo
        for char in conteudo.lower():
            if char in vogais:
                contador_vogais += 1
            elif char in consoantes:
                contador_consoantes += 1

        # Retorna os resultados
        return contador_vogais, contador_consoantes

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    # Solicita ao usuário o nome do arquivo
    nome_arquivo = input('Digite o nome do arquivo texto: ').strip()

    # Chama a função para contar vogais e consoantes
    resultado = contar_vogais_e_consoantes(nome_arquivo)

    if resultado:
        vogais, consoantes = resultado
        print(f"O arquivo contém {vogais} vogais e {consoantes} consoantes.")
