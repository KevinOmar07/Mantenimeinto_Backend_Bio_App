import unittest

from validacion_datos import Validacion_datos

class MyTestCase(unittest.TestCase):
    validar = Validacion_datos()

    def test_validar_nombre_letras(self):
        nombre = "Kevin"
        self.assertEqual(self.validar.validar_nombre(nombre), ['Nombre valido', True])

    def test_validar_nombre_numeros(self):
        nombre = "123"
        self.assertEqual(self.validar.validar_nombre(nombre), ['Nombre incorrecto', False])

    def test_validar_nombre_numeros_y_letras(self):
        nombre = "K3v1n"
        self.assertEqual(self.validar.validar_nombre(nombre), ['Nombre incorrecto', False])

