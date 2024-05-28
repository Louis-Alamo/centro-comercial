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


class SimularLibreria:

    def __init__(self, dias_simulacion: int):
        self.dias_simulacion = dias_simulacion
        self.lista_servidores_cajas = []

        ruta_clase = os.path.dirname(os.path.realpath(__file__))

        # Tablas de líneas de espera
        self.tabla_tiempo_llegada_cliente = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\lineas de espera\Tiempo de llegada cliente"))
        self.tabla_tiempo_realizacion_servicio_en_caja = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\lineas de espera\Tiempo de realizacion servicio"))
        self.tabla_tiempo_entrega_proveedor = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\lineas de espera\Tiempo de entrega proveedor"))

        # Tablas de precios e inventario
        self.tabla_costos_mantenimiento_caja = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\precios\Costo de mantenimiento de libreria"))
        self.tabla_descuentos_promocion_productos = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\precios\Descuentos por promocion"))
        self.tabla_productos_caja_en_tienda = TablaInventario(os.path.join(ruta_clase, r"..\datos\precios\Productos"))

        # Tablas de probabilidades
        self.tabla_cantidad_productos_comprar = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\probabilidades\Cantidad libros a comprar"))

        # Tablas que no retornan numeros si no que cadenas de texto
        self.tabla_temporadas_afluencia = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\probabilidades\Temporadas de afluencia"))
        self.tabla_dias_promocion = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\precios\Dias de promocion"))

        # Obtener datos del JSON de configuración
        with open(os.path.join(ruta_clase, r"..\datos\configuraciones_libreria.json"), 'r') as f:
            self.datos_json = json.load(f)

        # Variables y objetos necesarios
        self.ventas_productos = Ventas(self.tabla_productos_caja_en_tienda)
        self.pedidos_productos = Pedidos(self.tabla_tiempo_entrega_proveedor)

        # Iniciar simulación
        self.iniciar_simulacion()

    def inicializar_servidores(self):
        cantidad_servidores_caja = self.datos_json["Caja"]["Cantidad de cajas"]
        horario_inicio_caja = self.datos_json["General"]["horario_inicio"]
        horario_cierre_caja = self.datos_json["General"]["horario_cierre"]

        for i in range(cantidad_servidores_caja):
            self.lista_servidores_cajas.append(Servidor(horario_inicio_caja, horario_cierre_caja))

        self.administrar_servidores_caja = AdministrarServidores(self.lista_servidores_cajas, self.tabla_tiempo_realizacion_servicio_en_caja)

    def iniciar_simulacion(self):
        self.inicializar_servidores()
        self.contador_dias = 1

        while self.contador_dias <= self.dias_simulacion:
            self.simular_dia(self.contador_dias)
            self.contador_dias += 1

            for servidor in self.lista_servidores_cajas:
                servidor.guardar_informacion_diaria()

        self.guardar_datos()

    def simular_dia(self, numero_dia: int):
        lista_personas_caja = self.generar_cantidad_personas(numero_dia)
        lista_personas_asignadas_caja = self.asignar_servidores_caja(lista_personas_caja)
        self.realizar_compras(lista_personas_asignadas_caja)

    def generar_cantidad_personas(self, dia: int):
        multiplicador_de_afluencia = 2 / 100  # Porcentaje
        cantidad_personas = random.randint(1, self.datos_json["General"]["capacidad_maxima_personas"])
        cantidad_personas += int(cantidad_personas * multiplicador_de_afluencia)

        lista_personas_compra = []

        # Listas de aleatorios
        lista_aleatorios = generar_numeros_aleatorios(cantidad_personas + 10)
        lista_aleatorios_tiempo_llegada = generar_numeros_aleatorios(cantidad_personas + 10)

        hora_llegada_caja = Hora(self.datos_json["General"]["horario_inicio"])

        for i in range(cantidad_personas):
            tiempo_llegada = int(self.tabla_tiempo_llegada_cliente.obtener_valor(lista_aleatorios_tiempo_llegada[i]))
            hora_llegada_caja.sumar_minutos(tiempo_llegada)
            lista_personas_compra.append(Persona(i, hora_llegada_caja.get_hora()))

        return lista_personas_compra

    def asignar_servidores_caja(self, lista_personas):
        lista_personas_asignadas = []
        lista_personas_no_asignadas = []

        for persona in lista_personas:
            if self.administrar_servidores_caja.asignar_persona_servidor(persona):
                lista_personas_asignadas.append(persona)
            else:
                lista_personas_no_asignadas.append(persona)

        return lista_personas_asignadas

    def realizar_compras(self, lista_personas):
        # Comprobar si llegó pedido
        lista_pedidos = self.pedidos_productos.pedido_por_entregar(self.contador_dias)
        for pedido in lista_pedidos:
            self.tabla_productos_caja_en_tienda.registrar_pedido(pedido[2], pedido[1])  # Actualizar inventario

        for persona in lista_personas:
            cantidad_productos_comprar = int(self.tabla_cantidad_productos_comprar.obtener_valor(random.random()))
            lista_aleatorios_compra = generar_numeros_aleatorios(cantidad_productos_comprar + 10)

            lista_productos_comprados = []
            for i in range(cantidad_productos_comprar):
                lista_productos_comprados.append(self.tabla_productos_caja_en_tienda.obtener_producto(lista_aleatorios_compra[i]))

            for producto in lista_productos_comprados:
                if self.tabla_productos_caja_en_tienda.comprobar_stock(producto):
                    self.ventas_productos.registrar_venta(persona.get_numero_persona(), producto)
                    self.tabla_productos_caja_en_tienda.registrar_compra_venta(producto)

                    if self.tabla_productos_caja_en_tienda.comprobar_stock_minimo(producto):
                        self.realizar_pedido_producto(producto)
                else:
                    self.realizar_pedido_producto(producto)

        self.ventas_productos.cierre_dia()

    def realizar_pedido_producto(self, producto: str):
        self.pedidos_productos.realizar_pedido(
            self.contador_dias,
            producto,
            self.tabla_productos_caja_en_tienda.obtener_cantidad_reorden(producto),
            self.tabla_productos_caja_en_tienda.obtener_precio_producto(producto)
        )

    def guardar_datos(self):
        self.ventas_productos.guardar_informacion_json("ventas_productos")
        self.pedidos_productos.guardar_datos_json("pedidos_productos")
        self.administrar_servidores_caja.guardar_informacion_json("informacion_servidores_caja")


# Ejecutar simulación
SimularLibreria(1)
