import unittest
import main

class TestLogin(unittest.TestCase):

    def test_validarEntradasString(self):
        nombre = "Kevin"
        self.assertEqual(main.validarNombre(nombre), ['Nombre valido', True])

    def test_validarEntradasInt(self):
        nombre = "K000"
        self.assertEqual(main.validarNombre(nombre), ['Nombre incorrecto', False])