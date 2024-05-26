
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


class Simular:

    def __init__(self, cantidad_dias):
        self.cantidad_dias = cantidad_dias


        ruta_clase = os.path.dirname(os.path.realpath(__file__))

        #Obtenemos los datos de los archivos y los convertimos en objetos de tipo TablaDatosHistoricos

        #Lineas de espera
        self.tabla_tiempo_llegada_cliente = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\lineas de espera\Tiempo de llegada clientes"))
        self.tabla_tiempo_realizacion_servicio_en_caja = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\lineas de espera\Tiempo de realizacion de servicio en caja"))
        self.tabla_tiempo_realizacion_servicio_tecnico = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\lineas de espera\Tiempo de realizacion de servicio tecnico"))
        self.tabla_tiempo_entrega_proveedor =  TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\lineas de espera\Tiempo de entrega proveedor"))

        #Precios
        self.tabla_costos_mantenimiento_caja = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\precios\Costo de mantenimiento de caja"))
        self.tabla_costos_de_mantenimiento_area_servicio_tecnico = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\precios\Costos de mantenimiento de area servicio tecnico"))
        self.descuentos_por_promocion_productos = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\precios\Descuentos por promocion productos"))
        self.tabla_descuentos_por_promocion_servicio_tecnico = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\precios\Descuentos por promocion servicio tecnico"))
        self.dias_de_promocion = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\precios\Dias de promocion"))


        #Objetos de inventario
        self.tabla_productos_caja_en_tienda = TablaInventario(os.path.join(ruta_clase, r"..\datos\precios\Productos de caja en tienda"))
        self.tabla_materiales_servicio_tecnico = TablaInventario(os.path.join(ruta_clase, r"..\datos\precios\Costo de materiales servicio tecnico"))


        #Probabilidades
        self.tabla_cantidad_materiales_servicio_tecnico = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\probabilidades\Cantidad materiales servicio tecnico"))
        self.tabla_cantidad_productos_comprar = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\probabilidades\Cantidad productos a comprar"))
        self.tabla_temporadas_de_afluencia = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\probabilidades\Temporadas de afluencia"))
        self.tabla_tipo_visita = TablaDatosHistoricos(os.path.join(ruta_clase, r"..\datos\probabilidades\Tipo de visita"))




        #Creamos los objetos que nos ayudaaran a dar seguimineto a la simulacion

        self.ventas_tabla_servicio_tecnico = Ventas(self.tabla_materiales_servicio_tecnico)
        self.ventas_productos = Ventas(self.tabla_productos_caja_en_tienda)

        self.tabla_pedidos_servicio_tecnico = Pedidos(self.tabla_tiempo_entrega_proveedor)
        self.tabla_pedidos_ventas_productos = Pedidos(self.tabla_tiempo_entrega_proveedor)

        #-----Hata aqui funciona bien-----#

        self.mostrar_tablas()

    def inicializar_servidores(self):
        pass



    def mostrar_tablas(self):

        # #Lineas de espera
        # self.tabla_tiempo_llegada_cliente.mostrar_tabla()
        # self.tabla_tiempo_realizacion_servicio_en_caja.mostrar_tabla()
        # self.tabla_tiempo_realizacion_servicio_tecnico.mostrar_tabla()
        # self.tabla_tiempo_entrega_proveedor.mostrar_tabla()
        #
        # #Precios
        # self.tabla_costos_mantenimiento_caja.mostrar_tabla()
        # self.tabla_costos_de_mantenimiento_area_servicio_tecnico.mostrar_tabla()
        # self.descuentos_por_promocion_productos.mostrar_tabla()
        # self.tabla_descuentos_por_promocion_servicio_tecnico.mostrar_tabla()
        # self.dias_de_promocion.mostrar_tabla()


        #Objetos de inventario
        self.tabla_productos_caja_en_tienda.mostrar_tabla()
        self.tabla_materiales_servicio_tecnico.mostrar_tabla()


        # #Probabilidades
        # self.tabla_cantidad_materiales_servicio_tecnico.mostrar_tabla()
        # self.tabla_cantidad_productos_comprar.mostrar_tabla()
        # self.tabla_temporadas_de_afluencia.mostrar_tabla()
        # self.tabla_tipo_visita.mostrar_tabla()


Simular(1)