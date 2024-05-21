

class HoraErrorExcepcion(Exception):
    """Excepción personalizada para errores relacionados con la clase Hora."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)