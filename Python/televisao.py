class Televisao:
    """
    Classe que representa uma televisão com status (ligada/desligada),
    volume, e canal.
    """

    def __init__(self):
        """
        Construtor da classe Televisao. Inicializa os atributos padrão.
        """
        self.status = False  # False indica que a TV está desligada
        self.volume = 10  # Volume inicial (escala de 0 a 100)
        self.canal = 1  # Canal inicial (começa no canal 1)

    def ligar(self):
        """
        Liga a televisão.
        """
        if not self.status:
            self.status = True
            print("A televisão foi ligada.")
        else:
            print("A televisão já está ligada.")

    def desligar(self):
        """
        Desliga a televisão.
        """
        if self.status:
            self.status = False
            print("A televisão foi desligada.")
        else:
            print("A televisão já está desligada.")

    def aumentar_volume(self):
        """
        Aumenta o volume da televisão em 1 unidade, até o máximo de 100.
        """
        if self.status:
            if self.volume < 100:
                self.volume += 1
                print(f"Volume aumentado para {self.volume}.")
            else:
                print("O volume já está no máximo.")
        else:
            print("A televisão está desligada. Não é possível ajustar o volume.")

    def diminuir_volume(self):
        """
        Diminui o volume da televisão em 1 unidade, até o mínimo de 0.
        """
        if self.status:
            if self.volume > 0:
                self.volume -= 1
                print(f"Volume diminuído para {self.volume}.")
            else:
                print("O volume já está no mínimo.")
        else:
            print("A televisão está desligada. Não é possível ajustar o volume.")

    def aumentar_canal(self):
        """
        Aumenta o canal da televisão em 1 unidade.
        """
        if self.status:
            self.canal += 1
            print(f"Canal alterado para {self.canal}.")
        else:
            print("A televisão está desligada. Não é possível mudar de canal.")

    def diminuir_canal(self):
        """
        Diminui o canal da televisão em 1 unidade, com o limite mínimo no canal 1.
        """
        if self.status:
            if self.canal > 1:
                self.canal -= 1
                print(f"Canal alterado para {self.canal}.")
            else:
                print("O canal já está no mínimo (1).")
        else:
            print("A televisão está desligada. Não é possível mudar de canal.")

    def trocar_canal(self, canal: int):
        """
        Troca o canal da televisão para um canal específico.

        Args:
            canal (int): O número do canal desejado.
        """
        if self.status:
            if canal > 0:
                self.canal = canal
                print(f"Canal alterado para {self.canal}.")
            else:
                print("O número do canal deve ser maior que zero.")
        else:
            print("A televisão está desligada. Não é possível mudar de canal.")


class ControleRemoto:
    """
    Classe que representa um controle remoto vinculado a uma televisão.
    """

    def __init__(self, televisao: Televisao):
        """
        Construtor da classe ControleRemoto.

        Args:
            televisao (Televisao): A televisão que será controlada.
        """
        self.televisao = televisao

    def ligar(self):
        """
        Liga a televisão via controle remoto.
        """
        self.televisao.ligar()

    def desligar(self):
        """
        Desliga a televisão via controle remoto.
        """
        self.televisao.desligar()

    def aumentar_volume(self):
        """
        Aumenta o volume da televisão via controle remoto.
        """
        self.televisao.aumentar_volume()

    def diminuir_volume(self):
        """
        Diminui o volume da televisão via controle remoto.
        """
        self.televisao.diminuir_volume()

    def aumentar_canal(self):
        """
        Aumenta o canal da televisão via controle remoto.
        """
        self.televisao.aumentar_canal()

    def diminuir_canal(self):
        """
        Diminui o canal da televisão via controle remoto.
        """
        self.televisao.diminuir_canal()

    def trocar_canal(self, canal: int):
        """
        Troca o canal da televisão para um canal específico via controle remoto.

        Args:
            canal (int): O número do canal desejado.
        """
        self.televisao.trocar_canal(canal)


# Programa principal para demonstrar as funcionalidades
if __name__ == "__main__":
    # Criando uma televisão
    tv = Televisao()

    # Criando um controle remoto vinculado à televisão
    controle = ControleRemoto(tv)

    # Exemplo de uso
    print("\n--- Controle da Televisão ---")
    controle.ligar()
    controle.aumentar_volume()
    controle.diminuir_volume()
    controle.aumentar_canal()
    controle.trocar_canal(5)
    controle.diminuir_canal()
    controle.desligar()
    controle.trocar_canal(3)  # Tentando trocar de canal com a TV desligada
