from Persona import Persona
from Hora import Hora
import os
from DatosHistoricos import TablaDatoshistoricos
import random
from departamentoLG.entidades.DatosHistoricos import TablaDatoshistoricos

class Servidor:
    numero_servidor = 1

    def __init__(self, horario_inicio: str, horario_fin: str):
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


        #Mostrar datos inciales
        print(f"Servidor {self.numero_servidor} - Hora inicio: {self.horario_inicio} - Hora fin: {self.horario_fin}")

    def agregar_persona(self, persona: Persona, tiempo_servicio: int):
        if self.puede_atender(tiempo_servicio, persona.get_hora_llegada()) or self.puede_atender(tiempo_servicio):
            if self.servidor_vacio():
                self.calcular_hora_finalizacion_servidor_vacio(tiempo_servicio, persona.get_hora_llegada())
            else:
                self.calcular_hora_finalizacion(tiempo_servicio)

            self.cola_espera.append(persona)
            self.personas_en_espera += 1
            print(f"Se actualizo la hora de finalizacion con una suma de tiempo de {tiempo_servicio} paso a ser {self.hora_finalizacion}")

            return True  # Se agregó la persona al servidor

        return False  # No se agregó la persona al servidor


    def puede_atender(self, tiempo, hora_llegada=None):
        hora_finalizacion = Hora(self.hora_finalizacion.get_hora())

        if hora_llegada:
            hora_finalizacion = hora_llegada
            hora_finalizacion.sumar_minutos(tiempo)
            if hora_finalizacion > self.horario_fin:
                self.estado_servidor = False # se apaga el servidor porque ya no puede atender a mas
                return False
        else:
            hora_finalizacion.sumar_minutos(tiempo)
            if hora_finalizacion > self.horario_fin:
                self.estado_servidor = False #Se apaga el servidor porque ya no puede atender a mas
                return False

        return True  # El servidor puede atender a la persona

    def calcular_hora_finalizacion_servidor_vacio(self, tiempo: int, hora_llegada: Hora):
        self.hora_finalizacion = hora_llegada
        self.hora_finalizacion.sumar_minutos(tiempo)

    def calcular_hora_finalizacion(self, tiempo):
        self.hora_finalizacion.sumar_minutos(tiempo)

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
    def __init__(self, servidores: list, tabla_datos: TablaDatoshistoricos):
        self.servidores = servidores
        self.tabla_datos = tabla_datos

        self.ordenar_servidores_prioridad()

    def ordenar_servidores_prioridad(self):
        self.servidores.sort(key=lambda servidor: servidor.hora_finalizacion)
    def mostrar_servidores(self):
        for servidor in self.servidores:
            print(f"Servidor {servidor.get_numero_servidor()} - Estado: {'Libre' if servidor.get_estado_servidor() else 'Ocupado'} - Hora finalización: {servidor.get_hora_finalizacion()} - Personas en espera: {servidor.get_personas_en_espera()}")
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
                if servidor.get_estado_servidor() and servidor.puede_atender(tiempo_servicio, persona.get_hora_llegada()):
                    servidor_seleccionado = servidor
                    break
                elif servidor_seleccionado is None or len(servidor.cola_espera) < len(servidor_seleccionado.cola_espera):
                    if servidor.puede_atender(tiempo_servicio, persona.get_hora_llegada()):
                        servidor_seleccionado = servidor

        if servidor_seleccionado:
            servidor_seleccionado.agregar_persona(persona, tiempo_servicio)
            print(
                f"Persona {persona.numero_persona} asignada al servidor {servidor_seleccionado.get_numero_servidor()}")

            self.ordenar_servidores_prioridad()
            return True

        print(f"Persona {persona.numero_persona} no pudo ser asignada a ningún servidor.")
        return False





    def eliminar_servidor(self):
        if self.servidores:
            self.servidores.pop(0)




# #Pruebas de la clase servidor
#
# dir_path = os.path.dirname(os.path.realpath(__file__))
# path = os.path.join(dir_path,  r'..\jugueteria\datos\lineas de espera\Tiempo de espera por caja')
# tabla_datos = TablaDatoshistoricos(path)
#
#
# servidor1 = Servidor("08:00 AM", "06:30 PM")
# servidor2 = Servidor("08:00 AM", "06:30 PM")
#
# persona1 = Persona(1, "08:00 AM", "08:00 AM")
# persona2 = Persona(2, "08:00 AM", "09:00 AM")
# persona3 = Persona(3, "08:00 AM", "10:30 AM")
# persona4 = Persona(4, "08:00 AM", "10:30 AM")
# persona5 = Persona(5, "08:00 AM", "10:40 AM")
# persona6 = Persona(6, "08:00 AM", "10:50 AM")
#
#
#
# admin = AdministrarServidores([servidor1,servidor2], tabla_datos)
# admin.asignar_persona_servidor(persona1)
# #servidor2.set_estado_servidor(False)
#
# admin.asignar_persona_servidor(persona2)
# admin.asignar_persona_servidor(persona3)
# admin.asignar_persona_servidor(persona4)
# admin.asignar_persona_servidor(persona5)
# admin.asignar_persona_servidor(persona6)
#



#admin.mostrar_servidores()

#4
#4
#10
#6