"""
POO - Objetos

Objetos -> São instância da classe. Ou seja, após o mapeamento do objeto do mundo real para sua
representação computacional, devemos poder criar quantos objetos forem necessários. Podemos
pensar nos objetos/instâncias de uma classe como variáveis do tipo definido na classe.


# Instâncias/Objeto (isso)
lamp1 = Lampada('branca', 110, 60)

lamp1.ligar_desligar() #<-- é um objeto/instância
print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

cc1 = ContaCorrente(5000, 30000)

user1 = Usuario('Maurício', 'Theodoro', 'mauricioantonionetinho@gmail.com','123456')

nome = 'Angel'
sobrenome = 'Jolie'
email = 'angelbff@gmail.com'
senha = '23412'

"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    #Metodo de ligar e desligar, se ela estiver ligada vai cair no primeiro if e desligar, se não ela vai para o else e Liga a lampada.
    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz oi')

class ContaCorrente:

    contador = 3999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


cli1 = Cliente('Jessica Monteiro', '213.233.123-11')

cc = ContaCorrente(6000, 10000, cli1)

cc.mostra_cliente()

