

class Persona:

    def __init__(self, numero, tiempo_llegada):
        self.numero_persona = numero
        self.tiempo_llegada = tiempo_llegada

    def __str__(self):
        return f'Persona {self.numero_persona} llega a las {self.tiempo_llegada}'