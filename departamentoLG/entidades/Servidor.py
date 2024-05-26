import json
import os
import random
from departamentoLG.entidades.DatosHistoricos import TablaDatosHistoricos
from departamentoLG.entidades.Persona import Persona
from departamentoLG.entidades.Hora import Hora

class Servidor:
    numero_servidor = 1

    def __init__(self, horario_inicio: str, horario_fin: str):
        self.contador_dias = 1
        self.horario_inicio = Hora(horario_inicio)
        self.horario_fin = Hora(horario_fin)
        self.hora_finalizacion = Hora(horario_inicio)  # Última hora en la que finalizó un servicio

        self.cola_espera = []  # Cola de espera de personas que se ingresan al servidor
        self.estado_servidor = True  # True: Libre, False: Ocupado o bien cerrado
        self.numero_servidor = Servidor.numero_servidor  # El número de servidor se asigna automáticamente
        Servidor.numero_servidor += 1

        # Variables de monitoreo de rendimiento
        self.personas_en_espera = 0
        self.numero_personas_maximo_espera = 0
        self.tiempo_promedio_servicio = 0
        self.numero_total_personas_atendidas = 0
        self.tiempo_ocio_servidor = 0

        self.registro_total = {
            "Numero de servidor": self.numero_servidor,
            "Hora inicio": self.horario_inicio.get_hora(),
            "Hora fin": self.horario_fin.get_hora(),
            "dias": {}
        }

    def mostrar_estado_servidor(self):
        print(f"Servidor {self.numero_servidor} - Estado: {'Libre' if self.estado_servidor else 'Ocupado'} - Hora finalización: {self.hora_finalizacion} - Personas en espera: {self.personas_en_espera}")

    def limpiar_servidor(self):
        self.cola_espera = []
        self.estado_servidor = True
        self.hora_finalizacion = self.horario_inicio.copiar()
        self.personas_en_espera = 0
        self.numero_personas_maximo_espera = 0
        self.tiempo_promedio_servicio = 0
        self.numero_total_personas_atendidas = 0
        self.tiempo_ocio_servidor = 0

    def agregar_persona(self, persona: Persona, tiempo_servicio: int):
        if self.puede_atender(tiempo_servicio, persona.get_hora_llegada()):
            if self.servidor_vacio():
                persona.set_hora_atencion(persona.get_hora_llegada())
                self.calcular_hora_finalizacion_servidor_vacio(tiempo_servicio, persona.get_hora_llegada())
            else:
                persona.set_hora_atencion(self.hora_finalizacion)
                self.calcular_hora_finalizacion(tiempo_servicio)

            persona.set_servidor_asignado(self.numero_servidor)
            persona.set_hora_salida(self.hora_finalizacion)
            persona.set_tiempo_servicio(int(tiempo_servicio))

            self.cola_espera.append(persona)
            self.personas_en_espera += 1
            self.numero_total_personas_atendidas += 1

            return True  # Se agregó la persona al servidor

        return False  # No se agregó la persona al servidor

    def puede_atender(self, tiempo, hora_llegada=None):
        hora_finalizacion = self.hora_finalizacion.copiar()

        if hora_llegada:
            hora_finalizacion = hora_llegada.copiar()
            hora_finalizacion.sumar_minutos(int(tiempo))
            if hora_finalizacion > self.horario_fin:
                return False
        else:
            hora_finalizacion.sumar_minutos(int(tiempo))
            if hora_finalizacion > self.horario_fin:
                return False

        return True  # El servidor puede atender a la persona

    def calcular_hora_finalizacion_servidor_vacio(self, tiempo: int, hora_llegada: Hora):
        self.hora_finalizacion = hora_llegada.copiar()
        self.hora_finalizacion.sumar_minutos(int(tiempo))

    def calcular_hora_finalizacion(self, tiempo):
        self.hora_finalizacion.sumar_minutos(int(tiempo))

    def mostrar_cola_servidor(self):
        for persona in self.cola_espera:
            persona.mostrar_informacion()

    def guardar_informacion_diaria(self):
        self.registro_total["dias"][f"Dia {self.contador_dias}"] = {
            "Numero de personas atendidas": self.numero_total_personas_atendidas,
            "Numero de personas maximo en espera": self.numero_personas_maximo_espera,
            "Tiempo ocio servidor": self.tiempo_ocio_servidor
        }
        self.contador_dias += 1

    def eliminar_persona(self):
        if self.cola_espera:
            self.cola_espera.pop(0)
            self.personas_en_espera -= 1
            if self.servidor_vacio():
                self.estado_servidor = True  # Servidor ahora está libre

    def servidor_vacio(self):
        return not self.cola_espera

    # Métodos get de la clase
    def get_numero_servidor(self):
        return self.numero_servidor

    def get_persona_frente(self):
        if self.cola_espera:
            return self.cola_espera[0]
        return None

    def get_persona_atras(self):
        if self.cola_espera:
            return self.cola_espera[-1]
        return None

    def get_hora_finalizacion(self):
        return self.hora_finalizacion

    def get_estado_servidor(self):
        return self.estado_servidor

    def get_personas_en_espera(self):
        return len(self.cola_espera)

    # Métodos set de la clase
    def set_estado_servidor(self, estado):
        self.estado_servidor = estado

class AdministrarServidores:
    def __init__(self, servidores: list, tabla_datos: TablaDatosHistoricos):
        self.servidores = servidores
        self.tabla_datos = tabla_datos

        self.registro_total = {
            "Servidores": {}
        }
        self.ordenar_servidores_prioridad()

    def ordenar_servidores_prioridad(self):
        self.servidores.sort(key=lambda servidor: servidor.hora_finalizacion)

    def mostrar_servidores(self):
        for servidor in self.servidores:
            servidor.mostrar_estado_servidor()

    def agregar_servidor(self, servidor: Servidor):
        self.servidores.append(servidor)
        self.ordenar_servidores_prioridad()

    def asignar_persona_servidor(self, persona: Persona):
        """
        Asigna una persona al servidor menos ocupado o libre que pueda atender.

        Args:
            persona (Persona): La persona que se desea asignar a un servidor.

        Returns:
            bool: True si la persona fue asignada, False de lo contrario.
        """
        tiempo_servicio = self.tabla_datos.obtener_valor(random.random())
        servidor_seleccionado = None
        for servidor in self.servidores:
            if servidor.get_estado_servidor():
                if servidor.puede_atender(tiempo_servicio, persona.get_hora_llegada()):
                    servidor_seleccionado = servidor
                    break
                elif servidor_seleccionado is None or len(servidor.cola_espera) < len(servidor_seleccionado.cola_espera):
                    if servidor.puede_atender(tiempo_servicio, persona.get_hora_llegada()):
                        servidor_seleccionado = servidor

        if servidor_seleccionado:
            servidor_seleccionado.agregar_persona(persona, tiempo_servicio)
            self.ordenar_servidores_prioridad()
            return True

        return False

    def registro_total_servidores(self):
        for servidor in self.servidores:
            servidor.guardar_informacion_diaria()
            self.registro_total["Servidores"][f"Servidor {servidor.get_numero_servidor()}"] = servidor.registro_total

    def guardar_informacion_json(self):
        self.registro_total_servidores()
        with open("registro_servidores.json", "w") as archivo:
            json.dump(self.registro_total, archivo, indent=4)  # Indentación para legibilidad

        self.limpiar_servidores()

    def eliminar_servidor(self):
        if self.servidores:
            self.servidores.pop(0)

    def limpiar_servidores(self):
        for servidor in self.servidores:
            servidor.limpiar_servidor()
