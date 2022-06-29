import re

class Validacion_datos:

    def validar_nombre(self, name):
        expresion = re.compile(r'^[a-zA-Z][a-zA-Z]*$')
        if expresion.match(name):
            return ['Nombre valido', True]
        return ['Nombre incorrecto', False]