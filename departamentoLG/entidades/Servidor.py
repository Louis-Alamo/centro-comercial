from departamentoLG.entidades.Persona import Persona


class Servidor:

    def __init__(self, horario_inicio, horario_fin):
        self.horario_inicio = horario_inicio
        self.horario_fin = horario_fin

        self.cola_espera = []

        self.hora_finalizacion = None

    
    def agregar_persona(self, persona: Persona):
        self.cola_espera.append(persona)

    def calcular_hora_finalizacion(self):
        pass



from datetime import datetime, timedelta

class Hora:
    def __init__(self, hora_str):
        self.formato_12h = "%I:%M %p"
        self.hora = datetime.strptime(hora_str, self.formato_12h)

    def __str__(self):
        return self.hora.strftime(self.formato_12h)

    def sumar_segundos(self, segundos):
        self.hora += timedelta(seconds=segundos)

    def sumar_minutos(self, minutos):
        self.hora += timedelta(minutes=minutos)

    def sumar_hora(self, otra_hora_str):
        otra_hora = datetime.strptime(otra_hora_str, self.formato_12h)
        delta = otra_hora - datetime.combine(otra_hora.date(), datetime.min.time())
        self.hora += delta

# Ejemplo de uso
hora = Hora("08:00 AM")
print("Hora inicial:", hora)

hora.sumar_minutos(30)
print("Después de sumar 30 minutos:", hora)

hora.sumar_segundos(3600)  # Sumar una hora en segundos
print("Después de sumar 3600 segundos:", hora)

hora.sumar_hora("01:15 PM")  # Sumar otra hora en formato 12 horas
print("Después de sumar 01:15 PM:", hora)
