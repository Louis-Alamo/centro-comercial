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
        print(f"Servidor {self.numero_servidor} - Estado: {'Libre' if self.estado_servidor else 'Ocupado'} -Hora de inicio: {self.horario_inicio} - Hora de cierre: {self.horario_fin}- Hora finalización: {self.hora_finalizacion} - Personas en espera: {self.personas_en_espera}")

    def limpiar_servidor(self):
        self.cola_espera = []
        self.estado_servidor = True
        self.hora_finalizacion = self.horario_inicio.copiar()
        self.personas_en_espera = 0
        self.numero_personas_maximo_espera = 0
        self.tiempo_promedio_servicio = 0
        self.numero_total_personas_atendidas = 0
        self.tiempo_ocio_servidor = 0

    def agregar_persona(self, persona: Persona):



        if self.servidor_vacio() or self.hora_finalizacion < persona.get_hora_llegada():
            persona.set_hora_atencion(persona.get_hora_llegada())
            persona.set_servidor_asignado(self.numero_servidor)


            nueva_hora_finalizacion = persona.get_hora_llegada().copiar()
            nueva_hora_finalizacion.sumar_minutos(persona.get_tiempo_servicio())
            self.hora_finalizacion = nueva_hora_finalizacion.copiar()

            persona.set_hora_salida(self.hora_finalizacion.copiar())

        else:
            persona.set_hora_atencion(self.hora_finalizacion.copiar())
            persona.set_servidor_asignado(self.numero_servidor)

            self.hora_finalizacion.sumar_minutos(persona.get_tiempo_servicio())
            persona.set_hora_salida(self.hora_finalizacion.copiar())

            self.numero_personas_maximo_espera = max(self.numero_personas_maximo_espera, len(self.cola_espera))

        self.cola_espera.append(persona)


    def servidor_vacio(self):
        return len(self.cola_espera) == 0


    def puede_atender(self, persona: Persona):
        if self.hora_finalizacion > self.horario_fin:
            self.estado_servidor = False

        if self.estado_servidor:
            #Creamos copias de variables locales
            hora_finalizacion_persona  = self.hora_finalizacion.copiar()
            hora_finalizacion_persona.sumar_minutos(int(persona.get_tiempo_servicio()))

            if hora_finalizacion_persona < self.horario_fin:
                return True

        return False


    def mostrar_cola_servidor(self):
        for persona in self.cola_espera:
            persona.mostrar_informacion()

    def guardar_informacion_diaria(self):
        self.numero_total_personas_atendidas = len(self.cola_espera)

        self.registro_total["dias"][f"Dia {self.contador_dias}"] = {
            "Numero de personas atendidas": self.numero_total_personas_atendidas,
            "Numero de personas maximo en espera": self.numero_personas_maximo_espera,
            "Tiempo ocio servidor": self.tiempo_ocio_servidor
        }
        self.contador_dias += 1
        self.limpiar_servidor()

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
        self.personas_no_atendidas = 0



        self.registro_total = {
            "Servidores": {},
            "Personas no atendidas": self.personas_no_atendidas
        }
        #self.ordenar_servidores_prioridad()

    def ordenar_servidores_prioridad(self):
        n = len(self.servidores)

        for i in range(n-1):
            for j in range(n-1-i):
                if self.servidores[j].get_hora_finalizacion() > self.servidores[j+1].get_hora_finalizacion():
                    self.servidores[j], self.servidores[j + 1] = self.servidores[j + 1], self.servidores[j]



    def mostrar_servidores(self):
        for servidor in self.servidores:
            servidor.mostrar_estado_servidor()

    def agregar_servidor(self, servidor: Servidor):
        self.servidores.append(servidor)
        self.ordenar_servidores_prioridad()

    def asignar_persona_servidor(self, persona: Persona):

        tiempo_llegada = self.tabla_datos.obtener_valor(random.random())
        persona.set_tiempo_servicio(tiempo_llegada)
        for servidor in self.servidores:
            if servidor.puede_atender(persona):
                if persona.hora_llegada > servidor.hora_finalizacion:
                    servidor.agregar_persona(persona)
                    self.ordenar_servidores_prioridad()
                    return True

        servidor = self.servidores[0]
        if servidor.puede_atender(persona):
            servidor.agregar_persona(persona)
            self.ordenar_servidores_prioridad()

        return False #Ya de plano nigun servidor quiere a la persona




    def registro_total_servidores(self):
        for servidor in self.servidores:
            servidor.guardar_informacion_diaria()
            self.registro_total["Servidores"][f"Servidor {servidor.get_numero_servidor()}"] = servidor.registro_total

    def guardar_informacion_json(self, nombre_archivo = "registro_servidore"):
        self.registro_total_servidores()
        with open(f"{nombre_archivo}.json", "w") as archivo:
            json.dump(self.registro_total, archivo, indent=4)  # Indentación para legibilidad

        self.limpiar_servidores()

    def eliminar_servidor(self):
        if self.servidores:
            self.servidores.pop(0)

    def limpiar_servidores(self):
        for servidor in self.servidores:
            servidor.limpiar_servidor()

    def set_personas_no_atendidas(self, cantidad):
        self.personas_no_atendidas = cantidad




# #
# #
# #
# #
# servidor1 = Servidor("09:00 AM", "03:00 PM")
# servidor2 = Servidor("09:00 AM", "03:00 PM")
#
# ruta_clase = os.path.dirname(os.path.realpath(__file__))
#
# tabla_tiempo_realizacion_servicio_en_caja = TablaDatosHistoricos(
#     os.path.join(ruta_clase, r"..\electronica\datos\lineas de espera\Tiempo de realizacion de servicio en caja"))
#
# administrar_servidores = AdministrarServidores([servidor1, servidor2], tabla_tiempo_realizacion_servicio_en_caja)
#
#
# persona1 = Persona(1, "09:00 AM")
# persona2 = Persona(2, "09:10 AM")
# persona3 = Persona(3, "09:20 AM")
# persona4 = Persona(4, "09:30 AM")
# persona5 = Persona(5, "09:35 AM")
# persona6 = Persona(6, "09:40 AM")
#
#
# administrar_servidores.asignar_persona_servidor(persona1)
# administrar_servidores.asignar_persona_servidor(persona2)
# administrar_servidores.asignar_persona_servidor(persona3)
# administrar_servidores.asignar_persona_servidor(persona4)
# administrar_servidores.asignar_persona_servidor(persona5)
# administrar_servidores.asignar_persona_servidor(persona6)
#
#
# # # # #Administra y agregar
# # # # print("\nPrimera parte")
# # # # administrar_servidores.asignar_persona_servidor(persona1)
# # # # administrar_servidores.mostrar_servidores()
# # # #
# # # # print("\nSegunda parte")
# # # # administrar_servidores.asignar_persona_servidor(persona2)
# # # # administrar_servidores.mostrar_servidores()
# # # #
# # # # print("\nTercera parte")
# # # # administrar_servidores.asignar_persona_servidor(persona3)
# # # # administrar_servidores.mostrar_servidores()
# # #
# print("\n----------------Informacion personas -------------------")
# #Mostramos las personas
# persona1.mostrar_informacion()
# persona2.mostrar_informacion()
# persona3.mostrar_informacion()
# persona4.mostrar_informacion()
# persona5.mostrar_informacion()
# persona6.mostrar_informacion()
#
#
# print("\n----------------Colas de servidor-----------------")
# #Mostrmos las colas
# print("\n")
#
# print("Servidor 1")
# servidor1.mostrar_cola_servidor()
#
#
# print("\n")
# print("Servidor 2")
# servidor2.mostrar_cola_servidor()