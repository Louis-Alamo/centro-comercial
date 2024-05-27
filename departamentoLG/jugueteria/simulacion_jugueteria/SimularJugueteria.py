import os
import json
import tabulate
import random

from departamentoLG.entidades.DatosHistoricos import TablaDatosHistoricos
from departamentoLG.entidades.Financiero import Ventas, Pedidos, TablaInventario
from departamentoLG.entidades.Servidor import Servidor, AdministrarServidores
from departamentoLG.entidades.Hora import Hora
from departamentoLG.entidades.Persona import Persona
from util.NumerosAleatorios import generar_numeros_aleatorios


class SimularJugueteria:

    def __init__(self, dias_simulacion: int):

        self.dias_simulacion = dias_simulacion
        ruta_clase = os.path.dirname(os.path.realpath(__file__))

        # Tablas de líneas de espera
        self.tabla_tiempo_llegada_cliente = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\lineas de espera\Tiempo de llegada cliente"))
        self.tabla_tiempo_realizacion_servicio = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\lineas de espera\Tiempo de realizacion servicio"))
        self.tabla_tiempo_entrega_proveedor = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\lineas de espera\Tiempo de entrega proveedor"))

        # Tablas de precios e inventario
        self.costo_mantenimiento_jugueteria = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\precios\Costo de mantenimiento de jugueteria"))
        self.tabla_descuentos_promocion = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\precios\Descuentos por promocion"))
        self.tabla_inventario = TablaInventario(os.path.join(ruta_clase, r"..\datos\precios\Productos"))

        # Tablas de probabilidades
        self.cantidad_juguetes_comprar = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\probabilidades\Cantidad juguetes a comprar"))

        # Tablas que no retornan numeros si no que cadenas de texto
        self.tabla_temporadas_afluencia = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\probabilidades\Temporadas de afluencia"))
        self.tabla_dias_promocion = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\precios\Dias de promocion"))

        # Obtener datos del JSON de configuración
        with open(os.path.join(ruta_clase, r"..\datos\configuraciones_jugueteria.json"), 'r') as f:
            self.datos = json.load(f)

        # Variables y objetos necesarios
        self.servidores = [] #Lista donde se almacenaran los servidores creados
        self.inicializar_servidores() #Inicalizamos los servidores
        self.administrar_servidores = AdministrarServidores(self.servidores, self.tabla_tiempo_realizacion_servicio)
        self.administrar_servidores.mostrar_servidores()

        # Objetos para el manejo de las ventas y pedidos
        self.ventas = Ventas(self.tabla_inventario)
        self.pedidos = Pedidos(self.tabla_tiempo_entrega_proveedor)

        # Iniciar simulación
        self.iniciar_simulacion()

    def inicializar_servidores(self):
        cantidad_servidores = self.datos["Caja"]["Cantidad de cajas"]
        horario_inicio = self.datos["General"]["horario_inicio"]
        horario_fin = self.datos["General"]["horario_cierre"]

        for _ in range(cantidad_servidores):
            self.servidores.append(Servidor(horario_inicio, horario_fin))

    def iniciar_simulacion(self):

        self.contador_dias = 0

        for _ in range(self.dias_simulacion):
            self.contador_dias += 1

            self.simular_dia(self.contador_dias)

            self.guardar_datos()


    def simular_dia(self, numero_dia: int):

        self.lista_personas = self.generar_cantidad_personas(numero_dia) #Generamos la cantidad de personas

        for persona in self.lista_personas:
            persona.mostrar_informacion()


        # Asignar a los servidores las personas
        lista_personas_no_asignadas = []
        lista_personas_si_asignadas = []

        for persona in self.lista_personas:
            if self.administrar_servidores.asignar_persona_servidor(persona):
                lista_personas_si_asignadas.append(persona)
            else:
                lista_personas_no_asignadas.append(persona)

        for servidor in self.servidores:
            print("Servidor", servidor.get_numero_servidor())
            servidor.mostrar_cola_servidor()


        # Realizar compras
        for persona in lista_personas_si_asignadas:
            cantidad_productos = int(self.cantidad_juguetes_comprar.obtener_valor(random.random()))
            self.realizar_compra_productos(cantidad_productos, persona)

        self.ventas.cierre_dia()




    #
    def generar_cantidad_personas(self, dia: int):

        temporada_afluencia = 2  # Será el porcentaje de aumento por el día
        cantidad_personas = random.randint(1, self.datos["General"]["capacidad_maxima_personas"])
        cantidad_personas = int(cantidad_personas + (cantidad_personas * (temporada_afluencia / 100)))

        hora_actual = Hora(self.datos["General"]["horario_inicio"])
        lista_personas = []
        numeros_aleatorios = generar_numeros_aleatorios(cantidad_personas)

        for i in range(cantidad_personas):
            tiempo_llegada = self.tabla_tiempo_llegada_cliente.obtener_valor(numeros_aleatorios[i])
            hora_actual.sumar_minutos(int(tiempo_llegada))
            persona = Persona(i + 1, hora_actual.get_hora())
            lista_personas.append(persona)

        return lista_personas




    def realizar_compra_productos(self, cantidad_productos: int, persona: Persona):
        lista_aleatorios = generar_numeros_aleatorios(cantidad_productos + 10)

        # Comprobar si llegó pedido
        lista_pedidos = self.pedidos.pedido_por_entregar(self.contador_dias)

        for pedido in lista_pedidos:
            self.tabla_inventario.registrar_pedido(pedido[2], pedido[1])  # Actualizar inventario

        for i in range(cantidad_productos):
            producto = self.tabla_inventario.obtener_producto(lista_aleatorios[i])

            if self.tabla_inventario.comprobar_stock(producto):
                self.ventas.registrar_venta(persona.get_numero_persona(), producto)
                self.tabla_inventario.registrar_compra_venta(producto)

                if self.tabla_inventario.comprobar_stock_minimo(producto):
                    self.realizar_pedido_producto(producto)
            else:
                self.realizar_pedido_producto(producto)

    def realizar_pedido_producto(self, producto: str):
        self.pedidos.realizar_pedido(
            self.contador_dias,
            producto,
            self.tabla_inventario.obtener_cantidad_reorden(producto),
            self.tabla_inventario.obtener_precio_producto(producto)
        )

    def guardar_datos(self):
        self.ventas.guardar_informacion_json()
        self.pedidos.guardar_datos_json()
        self.administrar_servidores.guardar_informacion_json()


# Ejecutar simulación
SimularJugueteria(50)
