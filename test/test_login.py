import unittest
from validacion_datos import Validacion_datos

class TestLogin(unittest.TestCase):

    validar = Validacion_datos()

    def test_validarEntradasString(self):
        nombre = "Kevin"
        self.assertEqual(self.validar.validar_nombre(nombre), ['Nombre valido', True])

    def test_validarEntradasInt(self):
        nombre = "K000"
        self.assertEqual(self.validar.validar_nombre(nombre), ['Nombre incorrecto', False])