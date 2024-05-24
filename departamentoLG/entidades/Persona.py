from departamentoLG.entidades.Hora import Hora
class Persona:

    def __init__(self, numero: int, hora_llegada: str):
        self.numero_persona = numero
        self.hora_llegada = Hora(hora_llegada)

        self.hora_atencion = None
        self.hora_salida = None
        self.tiempo_espera_servidor = None
        self.servidor_asignado = None



    def __str__(self):
        return f"Persona {self.numero_persona} - {self.hora_llegada} - {self.hora_atencion} - {self.hora_salida}"

    def mostrar_informacion(self):
        print(f"Persona {self.numero_persona} - Hora de llegada: {self.hora_llegada} - Hora de atención: {self.hora_atencion} - Hora de salida: {self.hora_salida} - Tiempo de espera en el servidor: {self.tiempo_espera_servidor} minutos")

    def set_tipo_visita(self, tipo_visita : str):
        self.tipo_visita = tipo_visita

    def set_hora_atencion(self, hora_atencion : Hora):
        self.hora_atencion = hora_atencion

    def set_hora_salida(self, hora_salida : Hora):
        self.hora_salida = hora_salida

    def set_tiempo_espera_servidor(self, tiempo_espera_servidor : int):
        self.tiempo_espera_servidor = tiempo_espera_servidor  

    def get_hora_llegada(self):
        return self.hora_llegada
