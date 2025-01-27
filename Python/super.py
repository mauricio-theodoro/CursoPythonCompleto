"""
POO - O método super()

O método super() se refere á super classe.


"""

class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} fala {som}')


class Gato(Animal):

    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie) <-- é possivel fazer dessa maneira
        super().__init__(nome, especie) # <-- recomandado
        super().faz_som('hahahahaha')
        self.__raca = raca

felix = Gato('Felix', 'Felino', 'Angorá')
felix.faz_som('miau')