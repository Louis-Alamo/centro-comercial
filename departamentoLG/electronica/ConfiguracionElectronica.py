from customtkinter import *
from tkinter import messagebox

from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine
from componentes_graficos.LtkEntry import LtkEntryLine, LtkEntryFill
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkComboBox import LtkComboBoxLine
from componentes_graficos.LtkTreeView import LtkFileInputTreeView
import json
import os

class ConfiguracionElectronica:

    def __init__(self):


        self.nombre_datos_historicos_probabilidades = ["Atraccion clientes", "Clasificacion de los productos", "Dias de promocion", "Eventos especiales", "Tipo de servicio", "Tipo de visita"]
        self.nombre_datos_historicos_espera = ["Tiempo de espera de servicio", "Tiempo de espera en caja", "Tiempo de realizacion de servicio"]
        self.nombre_datos_precio = ["Costos de productos", "Costos de servicios", "Descuentos promocion servicios", "Descuentos por promocion productos productos"]

        self.ruta_ventana = os.path.dirname(os.path.abspath(__file__))


        self.ventana = CTkToplevel()
        self.ventana.title("Configuración de la tienda de electronica")


        self.ventana.grid_columnconfigure(1, weight=1)


        self.ventana.grid_rowconfigure(1, weight=1)


        #self.ventana.resizable(False, False)
        #self.ventana.configure(fg_color="#FFFFFF")

        self.crear_componentes()


        self.ventana.mainloop()


    def crear_componentes(self):

        self.frame_clasificacion_configuracion = CTkFrame(self.ventana)
        self.frame_clasificacion_configuracion.grid(row=1, column=0,padx=(10,5),pady=(10,10), sticky="ns")

        self.frame_clasificacion_configuracion.columnconfigure(0, weight=1)

        self.crear_botones_clasificacion_caracteristicas_cine()

        # Frame de características
        self.frame_caracteristicas = CTkFrame(self.ventana)
        self.frame_caracteristicas.grid(row=1, column=1,padx=(5,10),pady=(10,10),  sticky="nsew")

        self.frame_caracteristicas.columnconfigure(0, weight=1)
        self.frame_caracteristicas.columnconfigure(1, weight=1)

        # Etiqueta de título principal
        self.etiqueta_titulo_principal = LtkLabel(self.ventana, texto="Configuracion tienda electronica")
        self.etiqueta_titulo_principal.configure(font=('Poppins', 20, "bold"))
        self.etiqueta_titulo_principal.grid(row=0, column=0, pady=(10, 20), sticky="ew", columnspan=2)
        self.etiqueta_titulo_principal.columnconfigure(0,weight=1)  # Para que la etiqueta se expanda solo horizontalmente y esté centrada


        self.inicializar_componentes()


        self.boton_cerrar = LtkButtonFill(self.ventana,funcion=lambda: self.ventana.destroy(), nombre_boton="Cerrar")
        self.boton_cerrar.grid(row=2, column=0, columnspan=4, padx=(10,10), pady=(10, 20), sticky="w")

        self.boton_guardar = LtkButtonFill(self.ventana,funcion=lambda: self.guardar_informacion(), nombre_boton="Guardar")
        self.boton_guardar.grid(row=2, column=1, columnspan=4, padx=(10,10), pady=(10, 20), sticky="nsew")

    def resetear_frame_caracteristicas(self):
        for widget in self.frame_caracteristicas.winfo_children():
            widget.grid_remove()

    def crear_botones_clasificacion_caracteristicas_cine(self):

        self.boton_caracteristicas_principales = LtkButtonLine(self.frame_clasificacion_configuracion, funcion=lambda: self.crear_caracteristicas_electronica(), nombre_boton="Opciones generales")
        self.boton_caracteristicas_principales.grid(row=0, column=0, padx=(5,5), pady=(5, 5), sticky="nsew")

        self.boton_crear_componentes_edificio_caja = LtkButtonLine(self.frame_clasificacion_configuracion, funcion=lambda: self.crear_componentes_edificio_caja(), nombre_boton="Opciones de caja")
        self.boton_crear_componentes_edificio_caja.grid(row=1, column=0, padx=(5,5), pady=(5, 5), sticky="nsew")

        self.boton_crear_componentes_area_servicio = LtkButtonLine(self.frame_clasificacion_configuracion, funcion=lambda: self.crear_componetes_area_de_servicio_tecnico(), nombre_boton="Opciones de servicio tecnico")
        self.boton_crear_componentes_area_servicio.grid(row=2, column=0, padx=(5,5), pady=(5, 5), sticky="nsew")

    def inicializar_componentes(self):
        self.crear_componentes_edificio_caja()
        self.crear_componetes_area_de_servicio_tecnico()
        self.crear_caracteristicas_electronica()



        self.datos_generales = {

            "capacidad_maxima_personas": int(50 if self.entry_cantidad_maxima_personas.get() == "" else self.entry_cantidad_maxima_personas.get()),
            "horario_inicio": "08:00" if self.entry_horario_inicio.get() == "" else self.entry_horario_inicio.get(),
            "horario_cierre": "20:00" if self.entry_horario_cierre.get() == "" else self.entry_horario_cierre.get()

        }

        self.configuracion_caja = {

            "Cantidad de cajas": int(2 if self.entry_cantidad_cajas.get() == "" else self.entry_cantidad_cajas.get()),
            "Pago por empleado": 1000 if self.entry_paga_empleado_caja.get() == "" else self.entry_paga_empleado_caja.get(),
            "Rendimiento por empleado": 10 if self.entry_rendimiento_por_empleado_caja.get() == "" else self.entry_rendimiento_por_empleado_caja.get()
        }

        self.datos_servicio_tecnico = {
            "Cantidad de empleados": int(2 if self.entry_cantidad_empleados_servicio_tecnico.get() == "" else self.entry_cantidad_empleados_servicio_tecnico.get()),
            "Pago por empleado": 1000 if self.entry_paga_empleado_servicio_tecnico.get() == "" else self.entry_paga_empleado_servicio_tecnico.get(),
            "Rendimiento por empleado": 10 if self.entry_rendimiento_por_empleado_servicio_tecnico.get() == "" else self.entry_rendimiento_por_empleado_servicio_tecnico.get(),
            "Horario inicio": "08:00" if self.entry_horario_inicio_servicio.get() == "" else self.entry_horario_inicio_servicio.get(),
            "Horario cierre": "20:00" if self.entry_horario_cierre_servicio.get() == "" else self.entry_horario_cierre_servicio.get()
        }

    def crear_caracteristicas_electronica(self):

        self.lista_opciones_probabilidades_electronica = ["Atraccion de clientes", "Dias de promocion", "Eventos especiales", "Tipo de visita", "Temporadas de afluencia"]
        self.lista_opciones_precio_electronica = ["Precio de mantenimiento de la tienda", "Descuentos por promocion productos"]


        self.resetear_frame_caracteristicas()

        self.frame_caracteristicas.columnconfigure(1, weight=1)

        self.etiqueta_titulo_caracteristicas_jugueteria = LtkLabel(self.frame_caracteristicas, texto="Caracteristicas de la tienda de electronica")
        self.etiqueta_titulo_caracteristicas_jugueteria.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas_jugueteria.grid(row=0, column=0, columnspan=2, pady=(5, 10))


        self.etiqueta_cantidad_maxima_personas = LtkLabel(self.frame_caracteristicas, texto="Capacidad maxima de personas:")
        self.etiqueta_cantidad_maxima_personas.grid(row=1, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_maxima_personas = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_maxima_personas.grid(row=1, column=1,padx=(5,10),pady=(5, 5),sticky="nsew",columnspan=2)

        self.etiqueta_horario = LtkLabel(self.frame_caracteristicas, texto="Horario:")
        self.etiqueta_horario.grid(row=2, column=0,padx=(10,10), pady=(5, 10), sticky="w")

        self.entry_horario_inicio = LtkEntryLine(self.frame_caracteristicas, "Hora inicio")
        self.entry_horario_inicio.grid(row=2, column=1, padx=(5,10), pady=(5, 15), sticky="nsew")
        self.entry_horario_cierre = LtkEntryLine(self.frame_caracteristicas, "Hora cierre")
        self.entry_horario_cierre.grid(row=2, column=2, padx=(5,10), pady=(5, 15), sticky="nsew")

        #Probabilidades
        self.etiqueta_opcion_probabilidades = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de probabilidades:")
        self.etiqueta_opcion_probabilidades.grid(row=3, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_probabilidades = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_probabilidades_electronica)
        self.opcion_probabilidades.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_probabilidades = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_probabilidades_electronica(), nombre_boton="Cargar datos")
        self.boton_cargar_probabilidades.grid(row=3, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")

        #Precio
        self.etiqueta_opcion_precio = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de precio:")
        self.etiqueta_opcion_precio.grid(row=4, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_precio = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_precio_electronica)
        self.opcion_precio.grid(row=4, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_precio = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_precios_electronica(), nombre_boton="Cargar datos")
        self.boton_cargar_precio.grid(row=4, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")

        self.boton_guardar_datos_generales = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.guardar_datos_generales(), nombre_boton="Guardar datos")
        self.boton_guardar_datos_generales.grid(row=5, column=0, padx=(20,20), pady=(50, 20), sticky="nsew", columnspan=4)


    def crear_componentes_edificio_caja(self):

        self.lista_opciones_probabilidades_caja = ["Dias de promocion caja", "Fallos en el sistema de caja", "Tiempo de reparacion de fallo"]
        self.lista_costos_caja = ["Costos de mantenimiento de caja", "Costos de reparacion de caja"]
        self.lista_opciones_tiempo_espera_caja = ["Tiempo de espera en caja", "Tiempo de realizacion de servicio en caja", "Tiempo de espera en fila caja"]
        self.lista_opciones_productos_caja = ["Clasificacion de productos", "Descuentos por promocion productos"]

        self.resetear_frame_caracteristicas()

        self.frame_caracteristicas.columnconfigure(1, weight=1)

        self.etiqueta_titulo_edificio_caja = LtkLabel(self.frame_caracteristicas, texto="Edificio caja")
        self.etiqueta_titulo_edificio_caja.configure(font=('Poppins', 24, "bold"))
        self.etiqueta_titulo_edificio_caja.grid(row=0, column=0, columnspan=3, pady=(5, 10))

        self.etiqueta_cantidad_cajas = LtkLabel(self.frame_caracteristicas, texto="Cantidad de cajas(empleado por caja):")
        self.etiqueta_cantidad_cajas.grid(row=1, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_cajas = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_cajas.grid(row=1, column=1,padx=(5,10),pady=(5, 5),sticky="nsew",columnspan=2)


        self.etiqueta_paga_empleado_caja = LtkLabel(self.frame_caracteristicas, texto="Sueldo por empleado:")
        self.etiqueta_paga_empleado_caja.grid(row=2, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_paga_empleado_caja = LtkEntryLine(self.frame_caracteristicas)
        self.entry_paga_empleado_caja.grid(row=2, column=1,padx=(5,10),pady=(5, 5),sticky="nsew",columnspan=2)

        self.etiqueta_rendimiento_por_empleado_caja = LtkLabel(self.frame_caracteristicas, texto="Rendimiento por empleado:")
        self.etiqueta_rendimiento_por_empleado_caja.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_rendimiento_por_empleado_caja = LtkEntryLine(self.frame_caracteristicas)
        self.entry_rendimiento_por_empleado_caja.grid(row=3, column=1,padx=(5,10),pady=(5, 5),sticky="nsew",columnspan=2)

        #Probabilidades
        self.etiqueta_opcion_probabilidades_caja = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de probabilidades:")
        self.etiqueta_opcion_probabilidades_caja.grid(row=4, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_probabilidades_caja = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_probabilidades_caja)
        self.opcion_probabilidades_caja.grid(row=4, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_probabilidades_caja = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_probabilidades_caja(), nombre_boton="Cargar datos")
        self.boton_cargar_probabilidades_caja.grid(row=4, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")

        #Costos
        self.etiqueta_opcion_costos_caja = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de costos:")
        self.etiqueta_opcion_costos_caja.grid(row=5, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_costos_caja = LtkComboBoxLine(self.frame_caracteristicas, self.lista_costos_caja)
        self.opcion_costos_caja.grid(row=5, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_costos_caja = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_costos_caja(), nombre_boton="Cargar datos")
        self.boton_cargar_costos_caja.grid(row=5, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")

        #Tiempo de espera
        self.etiqueta_opcion_tiempo_espera_caja = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de tiempo de espera:")
        self.etiqueta_opcion_tiempo_espera_caja.grid(row=6, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_tiempo_espera_caja = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_tiempo_espera_caja)
        self.opcion_tiempo_espera_caja.grid(row=6, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_tiempo_espera_caja = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_tiempo_espera_caja(), nombre_boton="Cargar datos")
        self.boton_cargar_tiempo_espera_caja.grid(row=6, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")

        #Productos
        self.etiqueta_opcion_productos_caja = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de productos:")
        self.etiqueta_opcion_productos_caja.grid(row=7, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_productos_caja = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_productos_caja)
        self.opcion_productos_caja.grid(row=7, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_productos_caja = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_productos_caja(), nombre_boton="Cargar datos")
        self.boton_cargar_productos_caja.grid(row=7, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")

        self.boton_guardar_datos_caja = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.guardar_datos_caja(), nombre_boton="Guardar datos")
        self.boton_guardar_datos_caja.grid(row=8, column=0, padx=(20,20), pady=(50, 20), sticky="nsew", columnspan=4)

    def crear_componetes_area_de_servicio_tecnico(self):

        self.lista_opciones_probabilidad_servicio_tecnico = ["Fallos en el sistema de servicio tecnico","Tipo de servicio"]
        self.lista_opciones_precio_servicio_tecnico = ["Costos de materiales", "Descuentos por promocion servicio tecnico", "Costos de mantenimiento de area servicio tecnico", "Costo de servicio tecnico"]
        self.lista_opciones_tiempo_espera_servicio_tecnico = ["Tiempo de espera en fila servicio tecnico", "Tiempo de realizacion de servicio tecnico"]

        #Frame area de servicio tecnico
        self.resetear_frame_caracteristicas()

        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)

        self.etiqueta_titulo_area_servicio_tecnico = LtkLabel(self.frame_caracteristicas, texto="Area de servicio tecnico")
        self.etiqueta_titulo_area_servicio_tecnico.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_area_servicio_tecnico.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.etiqueta_cantidad_empleados_servicio_tecnico = LtkLabel(self.frame_caracteristicas, texto="Cantidad de empleados:")
        self.etiqueta_cantidad_empleados_servicio_tecnico.grid(row=1, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_empleados_servicio_tecnico = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_empleados_servicio_tecnico.grid(row=1, column=1,padx=(5,10),pady=(5, 5),sticky="nsew",columnspan=2)

        self.etiqueta_paga_empleado_servicio_tecnico = LtkLabel(self.frame_caracteristicas, texto="Pago por empleado:")
        self.etiqueta_paga_empleado_servicio_tecnico.grid(row=2, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_paga_empleado_servicio_tecnico = LtkEntryLine(self.frame_caracteristicas)
        self.entry_paga_empleado_servicio_tecnico.grid(row=2, column=1,padx=(5,10),pady=(5, 5),sticky="nsew",columnspan=2)

        self.etiqueta_rendimiento_por_empleado_servicio_tecnico = LtkLabel(self.frame_caracteristicas, texto="Rendimiento por empleado:")
        self.etiqueta_rendimiento_por_empleado_servicio_tecnico.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_rendimiento_por_empleado_servicio_tecnico = LtkEntryLine(self.frame_caracteristicas)
        self.entry_rendimiento_por_empleado_servicio_tecnico.grid(row=3, column=1,padx=(5,10),pady=(5, 5),sticky="nsew",columnspan=2)

        self.etiqueta_horario_servicio = LtkLabel(self.frame_caracteristicas, texto="Horario de servicio:")
        self.etiqueta_horario_servicio.grid(row=4, column=0,padx=(10,10), pady=(5, 10), sticky="w")

        self.entry_horario_inicio_servicio = LtkEntryLine(self.frame_caracteristicas, "Hora inicio")
        self.entry_horario_inicio_servicio.grid(row=4, column=1, padx=(5,10), pady=(5, 15), sticky="nsew")
        self.entry_horario_cierre_servicio = LtkEntryLine(self.frame_caracteristicas, "Hora cierre")
        self.entry_horario_cierre_servicio.grid(row=4, column=2, padx=(5,10), pady=(5, 15), sticky="nsew")

        #Probabilidades
        self.etiqueta_opcion_probabilidades_servicio_tecnico = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de probabilidades:")
        self.etiqueta_opcion_probabilidades_servicio_tecnico.grid(row=5, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_probabilidades_servicio_tecnico = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_probabilidad_servicio_tecnico)
        self.opcion_probabilidades_servicio_tecnico.grid(row=5, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_probabilidades_servicio_tecnico = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_probabilidades_servicio_tecnico(), nombre_boton="Cargar datos")
        self.boton_cargar_probabilidades_servicio_tecnico.grid(row=5, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")

        #Precio
        self.etiqueta_opcion_precio_servicio_tecnico = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de precio:")
        self.etiqueta_opcion_precio_servicio_tecnico.grid(row=6, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_precio_servicio_tecnico = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_precio_servicio_tecnico)
        self.opcion_precio_servicio_tecnico.grid(row=6, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_precio_servicio_tecnico = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_precio_servicio_tecnico(), nombre_boton="Cargar datos")
        self.boton_cargar_precio_servicio_tecnico.grid(row=6, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")

        #Tiempo de espera
        self.etiqueta_opcion_tiempo_espera_servicio_tecnico = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de tiempo de espera:")
        self.etiqueta_opcion_tiempo_espera_servicio_tecnico.grid(row=7, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_tiempo_espera_servicio_tecnico = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_tiempo_espera_servicio_tecnico)
        self.opcion_tiempo_espera_servicio_tecnico.grid(row=7, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_tiempo_espera_servicio_tecnico = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_tiempo_espera_servicio_tecnico(), nombre_boton="Cargar datos")
        self.boton_cargar_tiempo_espera_servicio_tecnico.grid(row=7, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")

        self.boton_guardar_datos_servicio_tecnico = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.guardar_datos_servicio_tecnico(), nombre_boton="Guardar datos")
        self.boton_guardar_datos_servicio_tecnico.grid(row=8, column=0, padx=(20,20), pady=(50, 20), sticky="nsew", columnspan=4)

    def guardar_informacion(self):

        configuracion_electronica = {
            "Generales": self.datos_generales,
            "Caja": self.configuracion_caja,
            "Servicio tecnico": self.datos_servicio_tecnico
        }

        informacion_json = json.dumps(configuracion_electronica, indent=4)


        with open(os.path.join(self.ruta_ventana, "datos\\configuracion_electronica.json"), "w") as file:
            file.write(informacion_json)


    def crear_ventana_emergente(self,titulo, ruta_archivo):

        self.ventana_emergente = CTkToplevel()
        self.ventana_emergente.title(titulo)

        # Establecer la ventana como modal
        self.ventana_emergente.grab_set()
        self.ventana_emergente.focus_set()
        self.ventana_emergente.transient(self.ventana)
        self.ventana_emergente.attributes('-topmost', True)

        self.tabla =  LtkFileInputTreeView(self.ventana_emergente, ruta_archivo)
        self.tabla.grid(row=0, column=0, padx=(10,10), pady=(10, 20), sticky="nsew")

        self.boton_guardar = LtkButtonFill(self.ventana_emergente, funcion=lambda: self.tabla.guardar_informacion(self.ventana_emergente), nombre_boton="Guardar")
        self.boton_guardar.grid(row=1, column=0, padx=(10,10), pady=(10, 20), sticky="nsew")

        self.ventana_emergente.mainloop()




    #Carga de datos

    #General
    def cargar_datos_probabilidades_electronica(self):

        if self.opcion_probabilidades.get() == "Atraccion de clientes":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Atraccion de clientes")
            self.crear_ventana_emergente("Costos de productos", path)

        elif self.opcion_probabilidades.get() == "Dias de promocion":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Dias de promocion")
            self.crear_ventana_emergente("Dias de promocion", path)

        elif self.opcion_probabilidades.get() == "Eventos especiales":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Eventos especiales")
            self.crear_ventana_emergente("Eventos especiales", path)

        elif self.opcion_probabilidades.get() == "Tipo de visita":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Tipo de visita")
            self.crear_ventana_emergente("Tipo de visita", path)

        elif self.opcion_probabilidades.get() == "Temporadas de afluencia":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Temporadas de afluencia")
            self.crear_ventana_emergente("Temporadas de afluencia", path)



    def cargar_datos_precios_electronica(self):

        if self.opcion_precio.get() == "Precio de mantenimiento de la tienda":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Precio de mantenimiento de la tienda")
            self.crear_ventana_emergente("Precio de mantenimiento de la tienda", path)

        elif self.opcion_precio.get() == "Descuentos por promocion productos":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Descuentos por promocion productos")
            self.crear_ventana_emergente("Descuentos por promocion productos", path)


    #Caja
    def cargar_datos_probabilidades_caja(self):

        if self.opcion_probabilidades_caja.get() == "Dias de promocion caja":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Dias de promocion en caja")
            self.crear_ventana_emergente("Dias de promocion caja", path)

        elif self.opcion_probabilidades_caja.get() == "Fallos en el sistema de caja":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Fallos en el sistema de caja")
            self.crear_ventana_emergente("Fallos en el sistema de caja", path)

        elif self.opcion_probabilidades_caja.get() == "Tiempo de reparacion de fallo":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Tiempo de reparacion de fallo")
            self.crear_ventana_emergente("Tiempo de reparacion de fallo", path)

    def cargar_datos_costos_caja(self):

            if self.opcion_costos_caja.get() == "Costos de mantenimiento de caja":
                path = os.path.join(self.ruta_ventana, "datos\\precios\\Costo de mantenimiento de caja")
                self.crear_ventana_emergente("Costos de mantenimiento de caja", path)

            elif self.opcion_costos_caja.get() == "Costos de reparacion de caja":
                path = os.path.join(self.ruta_ventana, "datos\\precios\\Costo de reparacion de caja")
                self.crear_ventana_emergente("Costos de reparacion de caja", path)

    def cargar_datos_tiempo_espera_caja(self):

        if self.opcion_tiempo_espera_caja.get() == "Tiempo de espera en caja":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Tiempo de espera en caja")
            self.crear_ventana_emergente("Tiempo de espera en caja", path)

        elif self.opcion_tiempo_espera_caja.get() == "Tiempo de realizacion de servicio en caja":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Tiempo de realizacion de servicio en caja")
            self.crear_ventana_emergente("Tiempo de realizacion de servicio en caja", path)

        elif self.opcion_tiempo_espera_caja.get() == "Tiempo de espera en fila caja":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Tiempo de espera en fila caja")
            self.crear_ventana_emergente("Tiempo de espera en fila caja", path)

    def cargar_datos_productos_caja(self):

        if self.opcion_productos_caja.get() == "Clasificacion de productos":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Clasificacion de productos")
            self.crear_ventana_emergente("Clasificacion de productos", path)

        elif self.opcion_productos_caja.get() == "Descuentos por promocion productos":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Descuentos por promocion productos")
            self.crear_ventana_emergente("Descuentos por promocion", path)

    #Servicio tecnico
    def cargar_datos_probabilidades_servicio_tecnico(self):

        if self.opcion_probabilidades_servicio_tecnico.get() == "Fallos en el sistema de servicio tecnico":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Fallos en el sistema de servicio tecnico")
            self.crear_ventana_emergente("Fallos en el sistema de servicio tecnico", path)

        elif self.opcion_probabilidades_servicio_tecnico.get() == "Tipo de servicio":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Tipo de servicio")
            self.crear_ventana_emergente("Tipo de servicio", path)


    def cargar_datos_precio_servicio_tecnico(self):

        if self.opcion_precio_servicio_tecnico.get() == "Costos de materiales":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Costo de materiales")
            self.crear_ventana_emergente("Costos de materiales", path)

        elif self.opcion_precio_servicio_tecnico.get() == "Descuentos por promocion servicio tecnico":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Descuentos por promocion servicio tecnico")
            self.crear_ventana_emergente("Descuentos por promocion servicio tecnico", path)

        elif self.opcion_precio_servicio_tecnico.get() == "Costos de mantenimiento de area servicio tecnico":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Costos de mantenimiento de area servicio tecnico")
            self.crear_ventana_emergente("Costos de mantenimiento de area servicio tecnico", path)

        elif self.opcion_precio_servicio_tecnico.get() == "Costo de servicio tecnico":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Costo de servicio tecnico")
            self.crear_ventana_emergente("Costo de servicio tecnico", path)


    def cargar_datos_tiempo_espera_servicio_tecnico(self):

        if self.opcion_tiempo_espera_servicio_tecnico.get() == "Tiempo de espera en fila servicio tecnico":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Tiempo de espera en fila servicio tecnico")
            self.crear_ventana_emergente("Tiempo de espera en fila servicio tecnico", path)

        elif self.opcion_tiempo_espera_servicio_tecnico.get() == "Tiempo de realizacion de servicio tecnico":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Tiempo de realizacion de servicio tecnico")
            self.crear_ventana_emergente("Tiempo de realizacion de servicio tecnico", path)


    #Guardar datos

    def guardar_datos_generales(self):
        self.datos_generales = {

            "capacidad_maxima_personas": int(50 if self.entry_cantidad_maxima_personas.get() == "" else self.entry_cantidad_maxima_personas.get()),
            "horario_inicio": "08:00" if self.entry_horario_inicio.get() == "" else self.entry_horario_inicio.get(),
            "horario_cierre": "20:00" if self.entry_horario_cierre.get() == "" else self.entry_horario_cierre.get()

        }

        messagebox.showinfo("Guardado", "Datos guardados localmente")

    def guardar_datos_caja(self):
        self.configuracion_caja = {
            "Cantidad de cajas": int(2 if self.entry_cantidad_cajas.get() == "" else self.entry_cantidad_cajas.get()),
            "Pago por empleado": 1000 if self.entry_paga_empleado_caja.get() == "" else self.entry_paga_empleado_caja.get(),
            "Rendimiento por empleado": 10 if self.entry_rendimiento_por_empleado_caja.get() == "" else self.entry_rendimiento_por_empleado_caja.get()
        }

        messagebox.showinfo("Guardado", "Datos guardados localmente")


    def guardar_datos_servicio_tecnico(self):

        self.datos_servicio_tecnico = {
            "Cantidad de empleados": int(2 if self.entry_cantidad_empleados_servicio_tecnico.get() == "" else self.entry_cantidad_empleados_servicio_tecnico.get()),
            "Pago por empleado": 1000 if self.entry_paga_empleado_servicio_tecnico.get() == "" else self.entry_paga_empleado_servicio_tecnico.get(),
            "Rendimiento por empleado": 10 if self.entry_rendimiento_por_empleado_servicio_tecnico.get() == "" else self.entry_rendimiento_por_empleado_servicio_tecnico.get(),
            "Horario inicio": "08:00" if self.entry_horario_inicio_servicio.get() == "" else self.entry_horario_inicio_servicio.get(),
            "Horario cierre": "20:00" if self.entry_horario_cierre_servicio.get() == "" else self.entry_horario_cierre_servicio.get()
        }

        messagebox.showinfo("Guardado", "Datos guardados localmente")

