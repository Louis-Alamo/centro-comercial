
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
        self.lista_servidores_cajas = []
        self.lista_servidores_servicio = []


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

        self.ventas_servicio_tecnico = Ventas(self.tabla_materiales_servicio_tecnico)
        self.ventas_productos = Ventas(self.tabla_productos_caja_en_tienda)

        self.pedidos_servicio_tecnico = Pedidos(self.tabla_tiempo_entrega_proveedor)
        self.pedidos_ventas_productos = Pedidos(self.tabla_tiempo_entrega_proveedor)


        #Leemos la configuracion del json de configuraciones
        with open(os.path.join(ruta_clase, r"..\datos\configuracion_electronica.json"), 'r') as f:
            self.datos_json = json.load(f)







        #-----Hata aqui funciona bien-----#

        self.iniciar_simulacion()

    #Ya quedo
    def inicializar_servidores(self):


        #Inicializamos los servidores de caja
        cantidad_servidores_caja = self.datos_json["Caja"]["Cantidad de cajas"]
        horario_inicio_caja = self.datos_json["Generales"]["horario_inicio"]
        horario_cierre_caja = self.datos_json["Generales"]["horario_cierre"]

        for i in range(cantidad_servidores_caja):
            self.lista_servidores_cajas.append(Servidor(horario_inicio_caja, horario_cierre_caja))

        self.administrar_servidores_caja = AdministrarServidores(self.lista_servidores_cajas,self.tabla_tiempo_realizacion_servicio_en_caja)


        #Incializamos los servidores de servicio tecnico
        cantidad_servidores_servicio = self.datos_json["Servicio tecnico"]["Cantidad de empleados"]
        horario_inicio_servicio = self.datos_json["Servicio tecnico"]["Horario inicio"]
        horario_cierre_servicio = self.datos_json["Servicio tecnico"]["Horario cierre"]

        for i in range(cantidad_servidores_servicio):
            self.lista_servidores_servicio.append(Servidor(horario_inicio_servicio, horario_cierre_servicio))

        self.administrar_servidores_servicios = AdministrarServidores(self.lista_servidores_servicio, self.tabla_tiempo_realizacion_servicio_tecnico)


    def iniciar_simulacion(self):
        self.inicializar_servidores()
        self.contador_dias = 1

        while self.contador_dias <= self.cantidad_dias:
            self.simular_dias()
            self.contador_dias += 1


            for servidor in self.lista_servidores_cajas:
                servidor.guardar_informacion_diaria()

            for servidor in self.lista_servidores_servicio:
                servidor.guardar_informacion_diaria()




        self.guardar_informacion()
    def simular_dias(self):
        personas_caja, persoans_servidor = self.generar_cantidad_personas()
        lista_personas_caja, lista_personas_servicio = self.asignar_servidores(personas_caja, persoans_servidor)
        #Realizamos compras y servicios
        self.comrpa_productos(lista_personas_caja)
        self.utilizacion_servicios(lista_personas_servicio)


    #Ya quedo
    def generar_cantidad_personas(self):
        multiplicador_de_afluencia = 2 / 100 #Porcentaje
        cantidad_personas = random.randint(1, self.datos_json["Generales"]["capacidad_maxima_personas"])
        cantidad_personas += int(cantidad_personas * multiplicador_de_afluencia)


        lista_personas_servicio = []
        lista_personas_compra = []

        #Listas de aleatorios (se generan 10 mas por si la cantidad de persoans es emnor a 10 ya que el metodo necesita al menos 10 numeros para funcionar, solo se usan los necesarios no todos)
        lista_aleatorios = generar_numeros_aleatorios(cantidad_personas + 10)
        lista_aleatorios_tiempo_llegada = generar_numeros_aleatorios(cantidad_personas + 10)

        hora_llegada_caja = Hora(self.datos_json["Generales"]["horario_inicio"])
        hora_llegada_servicio = Hora(self.datos_json["Servicio tecnico"]["Horario inicio"])


        for i in range(cantidad_personas):
            tipo_visita = self.tabla_tipo_visita.obtener_valor(lista_aleatorios[i])
            tiempo_llegada = int(self.tabla_tiempo_llegada_cliente.obtener_valor(lista_aleatorios_tiempo_llegada[i]))

            if tipo_visita == "Compra":
                hora_llegada_caja.sumar_minutos(tiempo_llegada)
                lista_personas_compra.append(Persona(i, hora_llegada_caja.get_hora()))


            elif tipo_visita == "Servicio":
                hora_llegada_servicio.sumar_minutos(tiempo_llegada)
                lista_personas_servicio.append(Persona(i, hora_llegada_servicio.get_hora()))



        return lista_personas_compra, lista_personas_servicio

    #Metodos relacionados con los servidores
    def asignar_servidores(self, lista_personas_caja, lista_personas_servicio):

        lista_personas_asignadas_caja = self.asignar_servidores_caja(lista_personas_caja)
        lista_personas_asignadas_servicio = self.asignar_servidores_servicio(lista_personas_servicio)
        return lista_personas_asignadas_caja, lista_personas_asignadas_servicio

    def asignar_servidores_caja(self, lista_personas):


        lista_personas_asignadas = []
        lista_personas_no_asignadas = []

        for i in range (len(lista_personas)):
            if self.administrar_servidores_caja.asignar_persona_servidor(lista_personas[i]):
                lista_personas_asignadas.append(lista_personas_asignadas)
            else:
                lista_personas_no_asignadas.append(lista_personas[i])

        return lista_personas_asignadas

    def asignar_servidores_servicio(self, lista_personas):

        lista_personas_asignadas = []
        lista_personas_no_asignadas = []

        for i in range (len(lista_personas)):
            if self.administrar_servidores_servicios.asignar_persona_servidor(lista_personas[i]):
                lista_personas_asignadas.append(lista_personas_asignadas)
            else:
                lista_personas_no_asignadas.append(lista_personas[i])

        return lista_personas_asignadas
    #Metodos relacionados con las ventas y pedidos

    def comrpa_productos(self, lista_personas):

        #Comprobamos si llego productos
        lista_pedidos = self.pedidos_ventas_productos.pedido_por_entregar(self.contador_dias)
        for lista in lista_pedidos:
            self.tabla_productos_caja_en_tienda.registrar_pedido(lista[2], lista[1])


        cantidad_personas_comprar = len(lista_personas)
        lista_productos = self.tabla_productos_caja_en_tienda.get_nombres_productos()

        for i in range(cantidad_personas_comprar):
            cantidad_productos_comprar = int(self.tabla_cantidad_productos_comprar.obtener_valor(random.random()))
            lista_aleatorios_compra = generar_numeros_aleatorios(cantidad_productos_comprar + 10)

            lista_productos_comprados = []
            for i in range(cantidad_productos_comprar):
                lista_productos_comprados.append(self.tabla_productos_caja_en_tienda.obtener_producto(lista_aleatorios_compra[i]))
            contador_productos = [0] * len(lista_productos)

            for i in range(len(lista_productos_comprados)):
                producto = lista_productos_comprados[i]
                indice = lista_productos.index(producto)
                contador_productos[indice] += 1



            for i in range(len(lista_productos)):

                if contador_productos[i] != 0:
                    if self.tabla_productos_caja_en_tienda.registrar_compra_venta(lista_productos[i], contador_productos[i]):
                        self.ventas_productos.registrar_venta("Persona anonima", lista_productos[i], contador_productos[i])


        for i in range(len(lista_productos)):
            if self.tabla_productos_caja_en_tienda.comprobar_stock_minimo(lista_productos[i]):
                self.pedidos_ventas_productos.realizar_pedido(self.contador_dias, lista_productos[i], self.tabla_productos_caja_en_tienda.obtener_cantidad_reorden(lista_productos[i]), self.tabla_productos_caja_en_tienda.obtener_precio_producto(lista_productos[i]))



        self.ventas_productos.cierre_dia()

    def utilizacion_servicios(self, lista_personas):

        #Comprobamos si llego productos
        lista_pedidos = self.pedidos_servicio_tecnico.pedido_por_entregar(self.contador_dias)
        for lista in lista_pedidos:
            self.tabla_materiales_servicio_tecnico.registrar_pedido(lista[2], lista[1])


        cantidad_personas_comprar = len(lista_personas)
        lista_productos = self.tabla_materiales_servicio_tecnico.get_nombres_productos()

        for i in range(cantidad_personas_comprar):
            cantidad_productos_comprar = int(self.tabla_cantidad_materiales_servicio_tecnico.obtener_valor(random.random()))
            lista_aleatorios_compra = generar_numeros_aleatorios(cantidad_productos_comprar + 10)

            lista_productos_comprados = []
            for i in range(cantidad_productos_comprar):
                lista_productos_comprados.append(self.tabla_materiales_servicio_tecnico.obtener_producto(lista_aleatorios_compra[i]))
            contador_productos = [0] * len(lista_productos)

            for i in range(len(lista_productos_comprados)):
                producto = lista_productos_comprados[i]
                indice = lista_productos.index(producto)
                contador_productos[indice] += 1



            for i in range(len(lista_productos)):

                if contador_productos[i] != 0:
                    if self.tabla_materiales_servicio_tecnico.registrar_compra_venta(lista_productos[i], contador_productos[i]):
                        self.ventas_servicio_tecnico.registrar_venta("Persona anonima", lista_productos[i], contador_productos[i])


        for i in range(len(lista_productos)):
            if self.tabla_materiales_servicio_tecnico.comprobar_stock_minimo(lista_productos[i]):
                self.pedidos_servicio_tecnico.realizar_pedido(self.contador_dias, lista_productos[i], self.tabla_materiales_servicio_tecnico.obtener_cantidad_reorden(lista_productos[i]), self.tabla_materiales_servicio_tecnico.obtener_precio_producto(lista_productos[i]))



        self.ventas_servicio_tecnico.cierre_dia()

    def realizar_pedido(self, producto):
        self.pedidos_ventas_productos.realizar_pedido(self.contador_dias, producto, self.tabla_productos_caja_en_tienda.obtener_cantidad_reorden(producto), self.tabla_productos_caja_en_tienda.obtener_precio_producto(producto))

    #Mostrar e guardar informacion
    def mostrar_tablas(self):


        print("Lineas de espera")
        #Lineas de espera
        self.tabla_tiempo_llegada_cliente.mostrar_tabla()
        self.tabla_tiempo_realizacion_servicio_en_caja.mostrar_tabla()
        self.tabla_tiempo_realizacion_servicio_tecnico.mostrar_tabla()
        #self.tabla_tiempo_entrega_proveedor.mostrar_tabla()


        print("\nPrecios")
        #Precios
        self.tabla_costos_mantenimiento_caja.mostrar_tabla()
        self.tabla_costos_de_mantenimiento_area_servicio_tecnico.mostrar_tabla()
        self.descuentos_por_promocion_productos.mostrar_tabla()
        self.tabla_descuentos_por_promocion_servicio_tecnico.mostrar_tabla()
        self.dias_de_promocion.mostrar_tabla()


        print("\nInventario")
        #Objetos de inventario
        self.tabla_productos_caja_en_tienda.mostrar_tabla()
        self.tabla_materiales_servicio_tecnico.mostrar_tabla()

        print("\nProbabilidades")
        #Probabilidades
        self.tabla_cantidad_materiales_servicio_tecnico.mostrar_tabla()
        self.tabla_cantidad_productos_comprar.mostrar_tabla()
        self.tabla_temporadas_de_afluencia.mostrar_tabla()
        self.tabla_tipo_visita.mostrar_tabla()

    def guardar_informacion(self):
        self.administrar_servidores_caja.guardar_informacion_json("Informacion servidores caja")
        self.administrar_servidores_servicios.guardar_informacion_json("Informacion servidores servicio")

        self.ventas_productos.guardar_informacion_json("ventas productos caja")
        self.ventas_servicio_tecnico.guardar_informacion_json("Ventas de servicio tecnico")

        self.pedidos_ventas_productos.guardar_datos_json("Pedidos de productos caja")
        self.pedidos_servicio_tecnico.guardar_datos_json("Pedidos de productos servicio")

Simular(365)