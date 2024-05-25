import random

from departamentoLG.entidades.DatosHistoricos import TablaDatosHistoricos
from departamentoLG.entidades.Financiero import Ventas, Pedidos, TablaInventario
from departamentoLG.entidades.Servidor import Servidor,AdministrarServidores
from departamentoLG.entidades.Hora import Hora
from departamentoLG.entidades.Persona import Persona
from util.NumerosAleatorios import generar_numeros_aleatorios

import os
import json


class SimularJugueteria():

    def __init__(self, dias_simulacion: int):

        self.dias_simulacion = dias_simulacion

        ruta_clase = os.path.dirname(os.path.realpath(__file__))

        #Tablas de lineas de espera
        self.tabla_timepo_llegada_cliente = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\lineas de espera\Tiempo de llegada cliente"))
        self.tabla_tiempo_realizacion_servicio = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\lineas de espera\Tiempo de realizacion servicio"))


        #Tablas de precios e inventario
        self.costo_mantenimiento_jugueteria = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\precios\Costo de mantenimiento de jugueteria"))
        self.tabla_descuentos_promocion = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\precios\Descuentos por promocion"))
        self.tabla_inventario = TablaInventario(os.path.join(ruta_clase, r"..\datos\precios\Productos"))


        #Tablas de probabilidades
        self.cantidad_juguetes_comprar = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\probabilidades\Cantidad juguetes a comprar"))




        #Pusados porque necesitan una clase en especial
        self.tabla_temporadas_afluencia = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\probabilidades\Temporadas de afluencia"))
        self.tabla_dias_promocion = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\precios\Dias de promocion"))



        #Obtenemos los datos del json

        with open(os.path.join(ruta_clase, r"..\datos\configuraciones_jugueteria.json"), 'r') as f:
            self.datos = json.load(f)


        #Varibles y objetos necesarios

        self.servidores = []

        self.inicializar_servidores()
        self.administrar_servidores = AdministrarServidores(self.servidores, self.tabla_tiempo_realizacion_servicio)
        self.administrar_servidores.mostrar_servidores()



        #Por ultimo llamamos a la funcion que realizara la simulacion
        self.iniciar_simulacion()

    def inicializar_servidores(self):
        cantidad_servidores = self.datos["Caja"]["Cantidad de cajas"]
        horario_inicio = self.datos["General"]["horario_inicio"]
        horario_fin = self.datos["General"]["horario_cierre"]

        for i in range(cantidad_servidores):
            self.servidores.append(Servidor(horario_inicio, horario_fin))


    def generar_cantidad_personas(self, dia: int):
        temporada_afluencia = 2 #Sera el porecentaje de aumento por el dia
        cantidad_personas = random.randint(1, self.datos["General"]["capacidad_maxima_personas"])
        cantidad_personas = int(cantidad_personas + (cantidad_personas * temporada_afluencia))

        hora_actual = Hora(self.datos["General"]["horario_inicio"])

        lista_personas = []
        numeros_aleatorios = generar_numeros_aleatorios(cantidad_personas)

        for i in range(cantidad_personas):
            tiempo_llegada = self.tabla_timepo_llegada_cliente.obtener_valor(numeros_aleatorios[i])
            hora_actual.sumar_minutos(int(tiempo_llegada))
            persona = Persona(i+1, hora_actual.get_hora())
            lista_personas.append(persona)

        return lista_personas


    def iniciar_simulacion(self):

        for i in range(self.dias_simulacion):
            self.lista_personas = self.generar_cantidad_personas(i)


        for persona in self.lista_personas:
            persona.mostrar_informacion()


SimularJugueteria(10)


