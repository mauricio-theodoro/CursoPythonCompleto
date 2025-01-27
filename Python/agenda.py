import itertools


class Contato:
    """
    Classe que representa um contato com ID, nome, telefone e email.
    """

    def __init__(self, id_contato: int, nome: str, telefone: str, email: str):
        """
        Inicializa os atributos de um contato.

        Args:
            id_contato (int): Identificador único do contato.
            nome (str): Nome do contato.
            telefone (str): Número de telefone do contato.
            email (str): Endereço de email do contato.
        """
        self.id_contato = id_contato
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        """
        Retorna uma representação legível de um contato.

        Returns:
            str: Dados formatados do contato.
        """
        return f"ID: {self.id_contato}, Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"


class Agenda:
    """
    Classe que gerencia a lista de contatos armazenados.
    """

    def __init__(self):
        """
        Inicializa a agenda com uma lista de contatos e um gerador de IDs únicos.
        """
        self.contatos = []
        self.id_generator = itertools.count(1)  # Gerador de IDs únicos.

    def armazenar_contato(self, nome: str, telefone: str, email: str):
        """
        Armazena um novo contato na agenda.

        Args:
            nome (str): Nome do contato.
            telefone (str): Telefone do contato.
            email (str): Email do contato.
        """
        id_contato = next(self.id_generator)
        novo_contato = Contato(id_contato, nome.title(), telefone, email.lower())
        self.contatos.append(novo_contato)
        print(f"Contato '{novo_contato.nome}' armazenado com sucesso! (ID: {novo_contato.id_contato})")

    def remover_contato(self, id_contato: int):
        """
        Remove um contato pelo ID.

        Args:
            id_contato (int): Identificador do contato a ser removido.
        """
        for contato in self.contatos:
            if contato.id_contato == id_contato:
                self.contatos.remove(contato)
                print(f"Contato '{contato.nome}' removido com sucesso.")
                return
        print(f"Contato com ID {id_contato} não encontrado.")

    def buscar_contato(self, nome: str):
        """
        Busca contatos pelo nome fornecido.

        Args:
            nome (str): Nome a ser buscado.
        """
        encontrados = [contato for contato in self.contatos if nome.lower() in contato.nome.lower()]
        if encontrados:
            print(f"{len(encontrados)} contato(s) encontrado(s) com o nome '{nome}':")
            for contato in encontrados:
                print(contato)
        else:
            print(f"Nenhum contato encontrado com o nome '{nome}'.")

    def atualizar_contato(self, id_contato: int, nome=None, telefone=None, email=None):
        """
        Atualiza as informações de um contato existente.

        Args:
            id_contato (int): ID do contato a ser atualizado.
            nome (str): Novo nome (opcional).
            telefone (str): Novo telefone (opcional).
            email (str): Novo email (opcional).
        """
        for contato in self.contatos:
            if contato.id_contato == id_contato:
                if nome:
                    contato.nome = nome.title()
                if telefone:
                    contato.telefone = telefone
                if email:
                    contato.email = email.lower()
                print(f"Contato '{contato.nome}' atualizado com sucesso!")
                return
        print(f"Contato com ID {id_contato} não encontrado.")

    def imprimir_agenda(self):
        """
        Exibe todos os contatos armazenados na agenda.
        """
        if not self.contatos:
            print("A agenda está vazia.")
        else:
            print("\n--- Contatos na Agenda ---")
            for contato in self.contatos:
                print(contato)


def exibir_menu():
    """
    Exibe o menu principal de opções.
    """
    print("\n--- MENU ---")
    print("1. Armazenar novo contato")
    print("2. Remover contato")
    print("3. Buscar contato por nome")
    print("4. Imprimir todos os contatos")
    print("5. Editar contato")
    print("6. Sair")


def main():
    """
    Função principal para executar o programa da agenda.
    """
    agenda = Agenda()  # Instância da agenda.

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            # Armazenar um novo contato.
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o email do contato: ")
            agenda.armazenar_contato(nome, telefone, email)

        elif escolha == "2":
            # Remover contato pelo ID.
            try:
                id_contato = int(input("Digite o ID do contato a ser removido: "))
                agenda.remover_contato(id_contato)
            except ValueError:
                print("ID inválido. Por favor, insira um número.")

        elif escolha == "3":
            # Buscar contatos pelo nome.
            nome = input("Digite o nome do contato a ser buscado: ")
            agenda.buscar_contato(nome)

        elif escolha == "4":
            # Exibir todos os contatos.
            agenda.imprimir_agenda()

        elif escolha == "5":
            # Editar contato existente.
            try:
                id_contato = int(input("Digite o ID do contato a ser editado: "))
                nome = input("Digite o novo nome (ou pressione Enter para manter): ").strip() or None
                telefone = input("Digite o novo telefone (ou pressione Enter para manter): ").strip() or None
                email = input("Digite o novo email (ou pressione Enter para manter): ").strip() or None
                agenda.atualizar_contato(id_contato, nome, telefone, email)
            except ValueError:
                print("ID inválido. Por favor, insira um número.")

            else:
                # Opção inválida.
                print("Opção inválida. Por favor, escolha uma opção válida.")

        elif escolha == "6":
            # Sair do programa.
            print("Encerrando o programa. Até mais!")
            break


# Executa o programa.
if __name__ == "__main__":
    main()
