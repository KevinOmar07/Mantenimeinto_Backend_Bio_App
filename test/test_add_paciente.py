import unittest
from validacion_datos import Validacion_datos

class TestAddPaciente(unittest.TestCase):

    validar = Validacion_datos()

    def test_validar_entradas_string(self):
        nombre = "Kevin Omar"
        self.assertEqual(self.validar.validar_string_add_paciente(nombre), True)

    def test_validar_entradas_int(self):
        nombre = "K000"
        self.assertEqual(self.validar.validar_string_add_paciente(nombre), False)

    def test_validar_edad(self):
        numero = "22"
        self.assertEqual(self.validar.validar_edad_y_numero(numero), True)

    def test_validar_edad_decimal(self):
        numero = "22.3"
        self.assertEqual(self.validar.validar_edad_y_numero(numero), False)

    def test_validar_peso(self):
        numero = "22.2"
        self.assertEqual(self.validar.validar_peso(numero), True)

    def test_validar_numero(self):
        numero = "9612458874"
        self.assertEqual(self.validar.validar_edad_y_numero(numero), True)

    def test_validar_numero_decimal(self):
        numero = "9612458874.03"
        self.assertEqual(self.validar.validar_edad_y_numero(numero), False)