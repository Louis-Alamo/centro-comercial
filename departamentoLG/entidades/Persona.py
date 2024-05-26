from departamentoLG.entidades.Hora import Hora
class Persona:

    def __init__(self, numero: int, hora_llegada: str):
        self.numero_persona = numero
        self.hora_llegada = Hora(hora_llegada)

        self.hora_atencion = None #Hora en la que inicia el servicio en el servidor
        self.hora_salida = None #Hora de finalizacion de servicio en el servidor
        self.tiempo_espera_servidor = None #Tiempo que estuvo esperando en el servidor para ser atendido
        self.servidor_asignado = None #Servidor al que se le asigno a la persona
        self.tiempo_servicio = None


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

    def set_servidor_asignado(self, servidor_asignado: str):
        self.servidor_asignado = servidor_asignado

    def set_tiempo_servicio(self, tiempo_servicio: int):
        self.tiempo_servicio = tiempo_servicio

    def get_hora_llegada(self):
        return self.hora_llegada

    def get_numero_persona(self):
        return self.numero_persona

    def get_informacion_completa(self):
        return [
            self.numero_persona,
            self.hora_llegada.get_hora(),
            self.hora_atencion.get_hora() if self.hora_atencion else "No atendido",
            self.hora_salida if self.hora_salida else "No atendido",
            self.tiempo_espera_servidor if self.tiempo_espera_servidor else "No atendido",
            self.servidor_asignado if self.servidor_asignado else "No asignado",
            self.tiempo_servicio if self.tiempo_servicio else "No atendido"
        ]