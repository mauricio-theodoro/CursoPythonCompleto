import unittest

from atividades import comer, dormir

class AtividadesTestes(unittest.TestCase):

    def test_comer(self):
        """Testando o retorno com comida saudavel."""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )
    def test_comer_gostosa(self):
        """Testando o retorno com comida gostosa."""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque a gente so vive uma vez.'
        )

    def test_dormir_pouco(self):
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas.'
        )

    def dormir_muito(self):
        self.assertEqual(
            dormir(10),
            'Ptz! Dormi muito! Estou atrasado para o trabalho!'
        )

if __name__ == '__main__':
    unittest.main()
