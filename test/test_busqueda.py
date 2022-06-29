import unittest
from validacion_datos import Validacion_datos

class TestLogin(unittest.TestCase):

    validar = Validacion_datos()

    def test_validar_palabra(self):
        nombre = "PalabraPrueba"
        self.assertEqual(self.validar.validar_palabra(nombre), True)

    def test_validar_no_palabra(self):
        nombre = "841"
        self.assertEqual(self.validar.validar_palabra(nombre), False)