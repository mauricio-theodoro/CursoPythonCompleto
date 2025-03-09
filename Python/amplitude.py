def amplitude(lista):
    """
    Calcula e imprime a amplitude de uma lista de números.
    A amplitude é a diferença entre o maior e o menor valor da lista.
    """
    if not lista:
        print("A lista está vazia.")
        return

    maior = max(lista)
    menor = min(lista)
    amp = maior - menor

    print(f"Amplitude: {amp}")


# Testando a função
if __name__ == "__main__":
    dados = [10, 5, 8, 3, 12, 7]
    amplitude(dados)
