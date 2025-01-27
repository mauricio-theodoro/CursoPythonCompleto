from datetime import datetime


def formatacao(data_str):
    """
    Quando se usa o import date, ele retorna com a data: YYYY/mm/dd.
    para modificar bastar utilizar o self.data_nascimento.strftime('%d/%m/%Y)

    Converte uma data no formato DD/MM/AAAA para uma string no formato por extenso.

    Args:
        data_str (str): A data no formato DD/MM/AAAA.

    Returns:
        str: A data formatada no estilo: '12 de Janeiro de 1991'.
    """
    # Dicionário para mapear os números dos meses para seus nomes
    meses = {
        1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril", 5: "maio", 6: "junho",
        7: "julho", 8: "agosto", 9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
    }
    try:
        # Divide a data em dia, mês e ano
        dia, mes, ano = map(int, data_str.split('/'))
        # Retorna a data formatada por extenso
        return f"{dia} de {meses[mes].title()} de {ano}"
    except (ValueError, KeyError):
        # Trata erros de formato ou valores inválidos
        raise ValueError("Data inválida. Por favor, use o formato DD/MM/AAAA.")


class Pessoa:
    """
    Classe que representa uma pessoa com nome, data de nascimento e email.
    """

    def __init__(self, nome: str, data_nascimento: str, email: str) -> None:
        """
        Construtor da classe Pessoa.

        Args:
            nome (str): O nome da pessoa.
            data_nascimento (str): A data de nascimento no formato DD/MM/AAAA.
            email (str): O email da pessoa.
        """
        # Atributos privados da classe
        self._nome = nome.title()  # Nome com a primeira letra maiúscula
        self._data_nascimento = formatacao(data_nascimento)  # Data formatada por extenso
        self._email = email  # Email

    @property
    def nome(self) -> str:
        """
        Retorna o nome da pessoa.
        """
        return self._nome

    @property
    def data_nascimento(self) -> str:
        """
        Retorna a data de nascimento da pessoa, formatada por extenso.
        """
        return self._data_nascimento

    @property
    def email(self) -> str:
        """
        Retorna o email da pessoa.
        """
        return self._email

    def imprimir_dados(self) -> None:
        """
        Imprime os dados da pessoa de forma formatada no console.
        """
        print("\n--- Dados da Pessoa ---")
        print(f"Nome: {self.nome}")
        print(f"Data de Nascimento: {self.data_nascimento}")
        print(f"Email: {self.email}")


if __name__ == "__main__":
    print("Cadastro de Pessoa\n")
    try:
        # Solicita os dados do usuário
        nome = input("Digite seu nome: ").strip()
        data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ").strip()
        email = input("Digite seu email: ").strip()

        # Cria um objeto da classe Pessoa
        pessoa = Pessoa(nome, data_nascimento, email)

        # Exibe os dados formatados no console
        pessoa.imprimir_dados()

    except ValueError as e:
        # Trata erros e exibe uma mensagem amigável
        print(f"\nErro: {e}")
    finally:
        # Mensagem final exibida sempre
        print("\nObrigado por utilizar nosso sistema!")
