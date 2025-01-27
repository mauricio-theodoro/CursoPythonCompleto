def main():
    """
    Programa para manipulação de arquivo texto "arq.txt":
    a) Cria ou abre o arquivo.
    b) Permite que o usuário grave caracteres até digitar '0'.
    c) Fecha o arquivo.
    d) Lê e exibe o conteúdo do arquivo.
    """
    import os

    # a) Cria ou abre o arquivo texto
    filename = "arq.txt"
    with open(filename, "w", encoding="utf-8") as file:
        print("Digite os caracteres para gravar no arquivo (digite '0' para encerrar):")
        while True:
            char = input("Digite um caractere: ").strip()
            if char == "0":
                break
            file.write(char + "\n")

    # c) Fecha o arquivo - feito automaticamente pelo gerenciador de contexto 'with'.

    # d) Abre, lê e exibe o conteúdo do arquivo
    if os.path.exists(filename):
        print("\nConteúdo do arquivo 'arq.txt':")
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                print(line.strip())
    else:
        print(f"Erro: O arquivo {filename} não foi encontrado.")

if __name__ == "__main__":
    main()


