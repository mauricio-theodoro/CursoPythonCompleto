def calcular_frete(peso):
    """
    Calcula o valor do frete com base no peso da carga.
    """
    if peso <= 10:
        print("O valor do frete é R$ 50,00.")
    elif 11 <= peso <= 20:
        print("O valor do frete é R$ 80,00.")
    else:
        print("Transporte não aceito para cargas acima de 20kg.")


# Testando as funções
if __name__ == "__main__":

    pesos_teste = [5, 10, 15, 20, 25]
    for peso in pesos_teste:
        print(f"Peso: {peso}kg -> ", end="")
        calcular_frete(peso)
