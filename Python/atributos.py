"""
POO - Atributos

Atributos - Representam as características do objeto. Ou seja, pelos atributos
conseguimos representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância;
    - Atributos de Classe;
    - Atributos Dinâmicos;

# Atributo de instância: São atributos declarados dentro do método construtor.

# OBS: Método construtor: É um método especial utilizado para a construção do objeto.

# Em Java, uma classe Lâmpada, incluindo seus atributos, ficaria mais ou menos:

public class Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor,){
        this. voltagem = voltagem;
        this.cor = cor;
    }
}

Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é público.
Ou seja, pode ser acessado em todo o projeto.
Caso queira demonstrar que determinado atributo deve ser tratado como privado, ou seja,
que deve ser acessado/utilizado somente dentro do própria classe onde está declarado,
utiliza-se __ duplo underscore no inicio de seu nome.

Isso é conhecido também como Nome MangLing

"""

"""

class Lampada:
    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False

class ContaCorrente:
    def __init__(self, numero, limite, saldo, investimento):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo
        self.investimento = investimento

class Produto:
    def __init__(self, nome, descricao, tamanho, valor):
        self.nome = nome
        self.descricao = descricao
        self.tamanho = tamanho
        self.valor = valor

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        
class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
"""
# Atributos Públicos e Atributos Privados

class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    # Duplo underline deixa-o privado

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)
# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não
# vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe.

# Exemplos

user = Acesso('user@gmail.com', '1123456')

print(user.email)
# print(user.__senha) < ERRADO

print(user._Acesso__senha) # Correto. Temo acesso, mas não deveriamos fazer esse acesso. (Name Mangling)


user.mostra_senha()
user.mostra_email()

"""
# O que significa atributos de instância?
# Significa que, ao criarmos instâncias/ objetos de uma classe, todas as instâncias terão estes atributos.

user1 = Acesso('user1@gmail.com', '1234567')
user2 = Acesso('user2@gmail.com', '0923911')

user1.mostra_email()
user2.mostra_email()
"""

# Atributos de Classe

#p1 = Produto('Carro', 'Automovel', 30000)
#p2 = Produto('PlayStation 4', 'Video Game', 2400)
#p3 = Produto('XBX S', 'Video Game', 4000)

# Atributos de classe, são atributos, que são declarados diretamente na classe, ou seja,
# Fora do construtor, Geralmente já inicializamos um valor, e esse valor é compartilhado entre
# Todas as instâncias da classe. Ou seja, ao invés de cada instância da classe teram os seus próprios
# valores como os caso dos atributos de instância, com os atributos de classe todas as instâncias
#terão o mesmo valor

# Refatorando a classe produto:
class Produto:
    imposto = 1.05 # 1.05% de imposto
    contador = 0
    def __init__(self, nome, descricao, valor, peso):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        self.peso = peso
        Produto.contador = self.id
"""
p1 = Produto('Carro', 'Automovel', 30000)
p2 = Produto('PlayStation 4', 'Video Game', 2400)
p3 = Produto('XBX S', 'Video Game', 4000)
"""
"""
print(p1.imposto) # Acesso possível, mas incorreto de um atributo de classe
print(p2.imposto)# Acesso possível, mas incorreto de um atributo de classe
print(p3.imposto)# Acesso possível, mas incorreto de um atributo de classe
print(p3.valor)# Acesso possível, mas incorreto de um atributo de classe
print(p1.valor)# Acesso possível, mas incorreto de um atributo de classe

# Não precisamos criar uma instância de classe para fazer acesso a um atributo de classe

print(Produto.imposto) # Acesso correto de um atributo de classe

Produto.imposto = 2.05

print(Produto.imposto) # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)
print(p3.id)

# OBS: Em liguagens como o Java, os atributos conhecidos como atributos de classe aqui em Python
# São chamado de atributos estáticos;
"""

# Atributo Dinâmicos -> Um atributo de instância que pode ser criado em tempo de execução.

# OBS: O atributo dinâmico será exclusivo da instância que o criou.

p1 = Produto('Carro', 'Automovel', 30000, 10000)
p2 = Produto('PlayStation 4', 'Video Game', 2400, 3.5)
p3 = Produto('XBX S', 'Video Game', 4000, 4.5)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5' # Note que na classe Produto não existe o atributo peso

print(f'Produto: {p1.nome}, Valor: {p1.valor}, Peso: {p1.peso}Kg')

print(f'Produto: {p2.nome}, Valor: {p2.valor}, Peso: {p2.peso}Kg')

print(f'Produto: {p3.nome}, Valor: {p3.valor}, Peso: {p3.peso}Kg')

print(p1.__dict__)
print(p2.__dict__)

print(Produto.__dict__)

del p2.peso

print(p2.__dict__)