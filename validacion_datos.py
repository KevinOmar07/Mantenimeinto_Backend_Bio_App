import re

class Validacion_datos:

    def validar_nombre(self, name):
        expresion = re.compile(r'^[a-zA-Z][a-zA-Z]*$')
        if expresion.match(name):
            return ['Nombre valido', True]
        return ['Nombre incorrecto', False]

    def validar_string_add_paciente(self, name):
        expresion = re.compile(r'^[a-zA-Z -\']+$')
        if expresion.match(name):
            return True
        return False

    def validar_peso(self, dato):
        expresion = re.compile(r'^[1-9]+([.])?([0-9]+)?$')
        if expresion.match(dato):
            return True
        return False

    def validar_edad_y_numero(self, dato):
        expresion = re.compile(r'^[1-9][0-9]+$')
        if expresion.match(dato):
            return True
        return False