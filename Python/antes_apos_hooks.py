"""
Unittest - Antes e após hooks
-----
hooks - são os testes em si. Ou seja, a execução dos testes.
-----

setup() -> é executado antes de cada método de teste. É útil para criarmos instaância de objetoss e outros dados;

tearDown() -> é executado ao final de cada método de teste. É útil para excluir dados ou fehcar conexões com
bancos de dados.


"""

import unittest
from unittest import TestCase


class ModuloTest(unittest, TestCase):

    def setUp(self):
        # Configurações do setup()
        pass

    def test_primeiro(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar após o teste.
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass