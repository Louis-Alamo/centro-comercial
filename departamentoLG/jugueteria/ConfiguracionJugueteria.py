import json

from customtkinter import *
from tkinter import messagebox

from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine
from componentes_graficos.LtkEntry import LtkEntryLine, LtkEntryFill
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkComboBox import LtkComboBoxLine
from componentes_graficos.LtkTreeView import LtkFileInputTreeView


class ConfiguracionJugeteria:

    def __init__(self):



        self.ruta_ventana = os.path.dirname(os.path.abspath(__file__))


        self.ventana = CTkToplevel()
        self.ventana.title("Configuración de la juguetería")


        self.ventana.grid_columnconfigure(1, weight=1)
        self.ventana.grid_rowconfigure(1, weight=1)



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
        self.etiqueta_titulo_principal = LtkLabel(self.ventana, texto="Configuracion de la jugueteria")
        self.etiqueta_titulo_principal.configure(font=('Poppins', 20, "bold"))
        self.etiqueta_titulo_principal.grid(row=0, column=0, pady=(10, 20), sticky="ew", columnspan=2)
        self.etiqueta_titulo_principal.columnconfigure(0,weight=1)  # Para que la etiqueta se expanda solo horizontalmente y esté centrada


        self.inicializar_componentes()


        self.boton_cerrar = LtkButtonFill(self.ventana,funcion=lambda: self.ventana.destroy(), nombre_boton="Cerrar")
        self.boton_cerrar.grid(row=2, column=0, columnspan=4, padx=(10,10), pady=(10, 20), sticky="w")

        self.boton_guardar = LtkButtonFill(self.ventana,funcion=lambda: self.guardar_informacion(), nombre_boton="Guardar")
        self.boton_guardar.grid(row=2, column=1, columnspan=4, padx=(10,10), pady=(10, 20), sticky="nsew")

    def crear_botones_clasificacion_caracteristicas_cine(self):

        self.boton_caracteristicas_principales = LtkButtonLine(self.frame_clasificacion_configuracion, funcion=lambda: self.caracteristicas_jugueteria(), nombre_boton="Opciones generales")
        self.boton_caracteristicas_principales.grid(row=0, column=0, padx=(5,5), pady=(5, 5), sticky="nsew")

        self.boton_crear_componentes_edificio_caja = LtkButtonLine(self.frame_clasificacion_configuracion, funcion=lambda: self.crear_componentes_edificio_caja(), nombre_boton="Opciones de caja")
        self.boton_crear_componentes_edificio_caja.grid(row=1, column=0, padx=(5,5), pady=(5, 5), sticky="nsew")

    def resetear_frame_caracteristicas(self):
        for widget in self.frame_caracteristicas.winfo_children():
            widget.grid_remove()

    def inicializar_componentes(self):

        self.crear_componentes_edificio_caja()
        self.caracteristicas_jugueteria()

        self.configuracion_caja = {
            "Cantidad de cajas": int(2 if self.entry_cantidad_cajas.get() == "" else self.entry_cantidad_cajas.get()),
            "Pago por empleado": 1000 if self.entry_sueldo_empleado.get() == "" else self.entry_sueldo_empleado.get(),
            "Rendimiento por empleado": 10 if self.entry_rendimiento_empleado.get() == "" else self.entry_rendimiento_empleado.get()
        }

        self.datos_generales = {

            "capacidad_maxima_personas": int(50 if self.entry_cantidad_maxima_personas.get() == "" else self.entry_cantidad_maxima_personas.get()),
            "horario_inicio": "08:00" if self.entry_horario_inicio.get() == "" else self.entry_horario_inicio.get(),
            "horario_cierre": "20:00" if self.entry_horario_cierre.get() == "" else self.entry_horario_cierre.get()

        }


    def caracteristicas_jugueteria(self):

        self.lista_opciones_probabilidad_general = ["Atraccion de clientes", "Compra de juguetes", "Dias de promocion", "Tipo de visita", "Eventos especiales",  "Temporadas de alfuencia"]
        self.lista_opciones_precio_general = ["Costo de mantenimiento de jugueteria", "Descuentos por promocion"]


        self.resetear_frame_caracteristicas()

        self.frame_caracteristicas.columnconfigure(1, weight=1)

        self.etiqueta_titulo_caracteristicas_jugueteria = LtkLabel(self.frame_caracteristicas, texto="Caracteristicas de la jugueteria")
        self.etiqueta_titulo_caracteristicas_jugueteria.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas_jugueteria.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.etiqueta_cantidad_maxima_personas = LtkLabel(self.frame_caracteristicas, texto="Cantidad maxima de personas:")
        self.etiqueta_cantidad_maxima_personas.grid(row=1, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_maxima_personas = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_maxima_personas.grid(row=1, column=1,padx=(5,10),pady=(5, 5),sticky="nsew",columnspan=2)

        self.etiqueta_horario = LtkLabel(self.frame_caracteristicas, texto="Horario:")
        self.etiqueta_horario.grid(row=3, column=0,padx=(10,10), pady=(5, 10), sticky="w")

        self.entry_horario_inicio = LtkEntryLine(self.frame_caracteristicas, "Hora inicio")
        self.entry_horario_inicio.grid(row=3, column=1, padx=(5,10), pady=(5, 15), sticky="nsew")
        self.entry_horario_cierre = LtkEntryLine(self.frame_caracteristicas, "Hora cierre")
        self.entry_horario_cierre.grid(row=3, column=2, padx=(5,10), pady=(5, 15), sticky="nsew")


        #Datos historicos

        #Probabilidades
        self.etiqueta_opcion_probabilidades_general = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de probabilidades:")
        self.etiqueta_opcion_probabilidades_general.grid(row=5, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_probabilidades_general = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_probabilidad_general)
        self.opcion_probabilidades_general.grid(row=5, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_probabilidades_general = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_probabilidad_general(), nombre_boton="Cargar datos")
        self.boton_cargar_probabilidades_general.grid(row=5, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")

        #Precio
        self.etiqueta_opcion_precio_general = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de precio:")
        self.etiqueta_opcion_precio_general.grid(row=6, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_precio_general = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_precio_general)
        self.opcion_precio_general.grid(row=6, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_precio_general = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_precios_general(), nombre_boton="Cargar datos")
        self.boton_cargar_precio_general.grid(row=6, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")


        self.boton_guardar_datos_general_local = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.guardar_datos_generales(), nombre_boton="Guardar datos")
        self.boton_guardar_datos_general_local.grid(row=7, column=0, padx=(20,20), pady=(50, 20), sticky="nsew", columnspan=4)


    def crear_componentes_edificio_caja(self):

        self.lista_opciones_espera_caja = ["Tiempo de espera por caja"]
        self.lista_opciones_productos = ["Productos"]
        self.lista_opciones_costos = ["Descuentos por promocion"]

        self.resetear_frame_caracteristicas()

        self.frame_caracteristicas.columnconfigure(1, weight=1)

        self.etiqueta_titulo_edificio_caja = LtkLabel(self.frame_caracteristicas, texto="Edificio caja")
        self.etiqueta_titulo_edificio_caja.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_edificio_caja.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.etiqueta_cantidad_cajas = LtkLabel(self.frame_caracteristicas, texto="Cantidad de cajas(empleado por caja):")
        self.etiqueta_cantidad_cajas.grid(row=1, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_cajas = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_cajas.grid(row=1, column=1,padx=(5,10),pady=(5, 5),sticky="nsew",columnspan=2)

        self.etiquteta_sueldo_empleado = LtkLabel(self.frame_caracteristicas, texto="Sueldo de empleado por hora:")
        self.etiquteta_sueldo_empleado.grid(row=2, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_sueldo_empleado = LtkEntryLine(self.frame_caracteristicas)
        self.entry_sueldo_empleado.grid(row=2, column=1,padx=(5,10),pady=(5, 5),sticky="nsew",columnspan=2)

        self.etiqueta_rendimiento_empleado = LtkLabel(self.frame_caracteristicas, texto="Rendimiento de empleado por hora:")
        self.etiqueta_rendimiento_empleado.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_rendimiento_empleado = LtkEntryLine(self.frame_caracteristicas)
        self.entry_rendimiento_empleado.grid(row=3, column=1,padx=(5,10),pady=(5, 5),sticky="nsew",columnspan=2)

        #Datos historicos

        #Probabilidades
        self.etiqueta_opcion_espera_caja = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de espera por caja:")
        self.etiqueta_opcion_espera_caja.grid(row=5, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_espera_caja = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_espera_caja)
        self.opcion_espera_caja.grid(row=5, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_espera_caja = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_espera_caja(), nombre_boton="Cargar datos")
        self.boton_cargar_espera_caja.grid(row=5, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")

        #Productos
        self.etiqueta_opcion_productos = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de productos:")
        self.etiqueta_opcion_productos.grid(row=6, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_productos = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_productos)
        self.opcion_productos.grid(row=6, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_productos = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_productos(), nombre_boton="Cargar datos")
        self.boton_cargar_productos.grid(row=6, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")


        self.boton_guardar_datos_caja = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.guardar_datos_caja(), nombre_boton="Guardar datos")
        self.boton_guardar_datos_caja.grid(row=7, column=0, padx=(20,20), pady=(50, 20), sticky="nsew", columnspan=4)

    def guardar_datos_generales(self):
        self.datos_generales = {

            "capacidad_maxima_personas": int(50 if self.entry_cantidad_maxima_personas.get() == "" else self.entry_cantidad_maxima_personas.get()),
            "horario_inicio": "08:00" if self.entry_horario_inicio.get() == "" else self.entry_horario_inicio.get(),
            "horario_cierre": "20:00" if self.entry_horario_cierre.get() == "" else self.entry_horario_cierre.get()

        }
        messagebox.showinfo("Información", "Datos guardados localmente")

    def guardar_datos_caja(self):

        self.configuracion_caja = {
            "Cantidad de cajas": int(2 if self.entry_cantidad_cajas.get() == "" else self.entry_cantidad_cajas.get()),
            "Pago por empleado": 1000 if self.entry_sueldo_empleado.get() == "" else self.entry_sueldo_empleado.get(),
            "Rendimiento por empleado": 10 if self.entry_rendimiento_empleado.get() == "" else self.entry_rendimiento_empleado.get()
        }
        messagebox.showinfo("Información", "Datos guardados localmente")



    def guardar_informacion(self):

        datos = {
            "General": self.datos_generales,
            "Caja": self.configuracion_caja
        }

        informacion =  json.dumps(datos, indent=4)

        with open(os.path.join(self.ruta_ventana, "datos\\configuraciones_jugueteria.json"), "w") as file:
            file.write(informacion)


    def cargar_datos_historicos_probabilidades(self):

        if self.opcion_datos_historicos_probabilidades.get() == "Atraccion de clientes":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Atraccion de clientes")
            self.crear_ventana_emergente("Atraccion de clientes", path)

        elif self.opcion_datos_historicos_probabilidades.get() == "Compra de juguetes":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Compra de juguetes")
            self.crear_ventana_emergente("Compra de juguetes", path)

        elif self.opcion_datos_historicos_probabilidades.get() == "Dias de promocion":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Dias de promocion")
            self.crear_ventana_emergente("Dias de promocion", path)

        elif self.opcion_datos_historicos_probabilidades.get() == "Tipo de visita":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Tipo de visita")
            self.crear_ventana_emergente("Tipo de visita", path)

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


    def cargar_datos_probabilidad_general(self):

        if self.opcion_probabilidades_general.get() == "Atraccion de clientes":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Atraccion de clientes")
            self.crear_ventana_emergente("Atraccion de clientes", path)

        elif self.opcion_probabilidades_general.get() == "Compra de juguetes":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Compra de juguetes")
            self.crear_ventana_emergente("Compra de juguetes", path)

        elif self.opcion_probabilidades_general.get() == "Dias de promocion":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Dias de promocion")
            self.crear_ventana_emergente("Dias de promocion", path)

        elif self.opcion_probabilidades_general.get() == "Tipo de visita":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Tipo de visita")
            self.crear_ventana_emergente("Tipo de visita", path)

        elif self.opcion_probabilidades_general.get() == "Eventos especiales":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Eventos especiales")
            self.crear_ventana_emergente("Eventos especiales", path)

        elif self.opcion_probabilidades_general.get() == "Temporadas de alfuencia":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Temporadas de afluencia")
            self.crear_ventana_emergente("Temporadas de alfuencia", path)



    def cargar_datos_precios_general(self):

        if self.opcion_precio_general.get() == "Costo de mantenimiento de jugueteria":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Costo de mantenimiento de jugueteria")
            self.crear_ventana_emergente("Costo de mantenimiento de jugueteria", path)

        elif self.opcion_precio_general.get() == "Descuentos por promocion":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Descuento por promocion")
            self.crear_ventana_emergente("Descuentos por promocion", path)

    def cargar_datos_espera_caja(self):

        if self.opcion_espera_caja.get() == "Tiempo de espera por caja":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Tiempo de espera por caja")
            self.crear_ventana_emergente("Tiempo de espera por caja", path)

    def cargar_datos_productos(self):

        if self.opcion_productos.get() == "Productos":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Productos")
            self.crear_ventana_emergente("Productos", path)



