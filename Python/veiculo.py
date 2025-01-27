"""
1. Crie a classe Veiculo, contendo marca e modelo. Crie as propriedades getters e setters
para os atributos e um método para imprimir os dados de um veículo.
Crie também o construtor da classe.

2. Crie a classe Carro que herda a classe Veiculo e possui o atributo portas.
Crie as propriedades getters e
setters para o atributo. Crie também o construtor da classe.
Sobrescreva o método de imprimir os dados do
veículo de forma a apresentar também a quantidade de portas do carro.

3. Crie um programa, instancie um objeto da classe Carro e teste o seu médodo.
"""


class Veiculo:
    """
    Classe que representa um veículo genérico com marca e modelo.
    """

    def __init__(self, marca: str, modelo: str) -> None:
        """
        Construtor da classe Veiculo.
        Inicializa o veículo com uma marca e modelo.

        Args:
            marca (str): A marca do veículo.
            modelo (str): O modelo do veículo.
        """
        self._marca = marca  # Atributo privado para a marca do veículo.
        self._modelo = modelo  # Atributo privado para o modelo do veículo.

    @property
    def marca(self) -> str:
        """
        Getter para o atributo 'marca'.
        Permite acessar o valor da marca do veículo.

        Returns:
            str: A marca do veículo.
        """
        return self._marca

    @marca.setter
    def marca(self, nova_marca: str) -> None:
        """
        Setter para o atributo 'marca'.
        Permite alterar o valor da marca do veículo.

        Args:
            nova_marca (str): A nova marca do veículo.
        """
        self._marca = nova_marca

    @property
    def modelo(self) -> str:
        """
        Getter para o atributo 'modelo'.
        Permite acessar o valor do modelo do veículo.

        Returns:
            str: O modelo do veículo.
        """
        return self._modelo

    @modelo.setter
    def modelo(self, novo_modelo: str):
        """
        Setter para o atributo 'modelo'.
        Permite alterar o valor do modelo do veículo.

        Args:
            novo_modelo (str): O novo modelo do veículo.
        """
        self._modelo = novo_modelo

    def imprimir_dados(self) -> None:
        """
        Método que imprime os dados do veículo.
        Exibe a marca e o modelo.
        """
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")

# from nomedoarquivo import Classe(Veiculo) <- Exemplo de importação
class Carro(Veiculo):
    """
    Classe que representa um carro, herdando de Veiculo.
    Adiciona o atributo específico 'portas', que representa a quantidade de portas do carro.
    """

    def __init__(self, marca: str, modelo: str, portas: int):
        """
        Construtor da classe Carro.
        Inicializa um carro com marca, modelo e quantidade de portas.

        Args:
            marca (str): A marca do veículo.
            modelo (str): O modelo do veículo.
            portas (int): A quantidade de portas do carro.
        """
        super().__init__(marca, modelo)  # Chama o construtor da classe base Veiculo.
        self._portas = portas  # Atributo privado para a quantidade de portas do carro.

    @property
    def portas(self) -> int:
        """
        Getter para o atributo 'portas'.
        Permite acessar o valor da quantidade de portas do carro.

        Returns:
            int: A quantidade de portas.
        """
        return self._portas

    @portas.setter
    def portas(self, quantidade_portas: int) -> None:
        """
        Setter para o atributo 'portas'.
        Permite alterar o valor da quantidade de portas do carro.

        Args:
            quantidade_portas (int): A nova quantidade de portas.

        Raises:
            ValueError: Se o número de portas for menor que 1.
        """
        if quantidade_portas < 1:
            raise ValueError("O número de portas deve ser pelo menos 1.")
        self._portas = quantidade_portas

    def imprimir_dados(self):
        """
        Método sobrescrito para imprimir os dados do carro.
        Além da marca e modelo, exibe também a quantidade de portas.
        """
        super().imprimir_dados()  # Chama o método imprimir_dados da classe base Veiculo.
        print(f"Portas: {self.portas}")


# Programa principal para testar a classe Carro
if __name__ == "__main__":
    try:
        # Instancia um objeto da classe Carro.
        carro = Carro("Toyota", "Corolla", 4)

        # Exibe os dados iniciais do carro.
        print("Dados do carro (inicial):")
        carro.imprimir_dados()

        # Testa os setters para alterar os atributos.
        carro.marca = "Honda"
        carro.modelo = "Civic"
        carro.portas = 5

        # Exibe os dados atualizados do carro.
        print("\nDados do carro (após modificações):")
        carro.imprimir_dados()

        # Testa a validação no setter de portas.
        print("\nTestando a validação:")
        carro.portas = 0  # Esta linha deve gerar um erro.
    except ValueError as e:
        # Trata erros gerados por valores inválidos.
        print(f"Erro: {e}")
