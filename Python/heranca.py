"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Também extender nossas classe.
OBS: Com a herança, a partir de um classe existente, nós extendemos outra classe
que passa a herdar atributos e mpetodos da classe herdada.

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

Pergunta: Existe alguma entidade genérica o suficiente para encapsular os atributos
e métodos comuns a outras entidades?



class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Angelina', 'Jolie', '123.123.124-91', 23221)
funcionario1 = Funcionario('Roberta', 'Letter', '231.231.234-33', 2312)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

OBS: Quando uma classe herda de outra classse ela herda todos os atributos e métodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    [Pessoa]
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;

Quando uma classe herda de outra classe, ela é chamada:
    [Cliente, Funcionario]
    - Sub Classe;
    - Classe Filha;
    - Classe Específica;

Sobreescrita de Métodos, ocorre quando reescrevemos um método presente na super classe
 em classes filhas. (Overriding)
"""

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf) # Forma comum de acessar dados da super classe
        self.__renda = renda

class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        Pessoa.__init__(self, nome, sobrenome, cpf) # Forma não comum de acessar dados da super classe
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionário: {self.__matricula} \nNome: {self._Pessoa__nome}'



cliente1 = Cliente('Angelina', 'Jolie', '123.123.124-91', 23221)
funcionario1 = Funcionario('Roberta', 'Letter', '231.231.234-33', 2312)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)
print(funcionario1.__dict__)