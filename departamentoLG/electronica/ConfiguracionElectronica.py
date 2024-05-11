from customtkinter import *
from tkinter import messagebox

from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine
from componentes_graficos.LtkEntry import LtkEntryLine, LtkEntryFill
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkComboBox import LtkComboBoxLine
from componentes_graficos.LtkTreeView import LtkFileInputTreeView


class ConfiguracionElectronica:

    def __init__(self):

        self.nombre_datos_historicos_probabilidades = ["Atraccion clientes", "Clasificacion de los productos", "Eventos de promocion", "Eventos especiales", "Tipo de servicio", "Tipo de visita"]
        self.nombre_datos_historicos_espera = ["Tiempo de espera de servicio", "Tiempo de espera en caja", "Tiempo de realizacion de servicio"]
        self.nombre_datos_precio = ["Costos de productos", "Costos de servicios", "Descuentos promocion servicios", "Descuentos de promocion productos"]

        self.ruta_ventana = os.path.dirname(os.path.abspath(__file__))


        self.ventana = CTkToplevel()
        self.ventana.title("Configuración de la tienda de electronica")


        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(1, weight=1)
        self.ventana.grid_columnconfigure(2, weight=1)
        self.ventana.grid_columnconfigure(3, weight=1)

        self.ventana.grid_rowconfigure(0, weight=1)
        self.ventana.grid_rowconfigure(1, weight=1)
        self.ventana.grid_rowconfigure(2, weight=1)


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
        self.etiqueta_titulo_principal = LtkLabel(self.ventana, texto="Configuracion tiendo electronica")
        self.etiqueta_titulo_principal.configure(font=('Poppins', 20, "bold"))
        self.etiqueta_titulo_principal.grid(row=0, column=0, pady=(10, 20), sticky="ew", columnspan=2)
        self.etiqueta_titulo_principal.columnconfigure(0,weight=1)  # Para que la etiqueta se expanda solo horizontalmente y esté centrada


        #self.inicializar_componentes()


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

        self.boton_crear_componentes_edificio_caja = LtkButtonLine(self.frame_clasificacion_configuracion, funcion=lambda: self.crear_componentes_edificio_caja(), nombre_boton="Opciones generales")
        self.boton_crear_componentes_edificio_caja.grid(row=1, column=0, padx=(5,5), pady=(5, 5), sticky="nsew")

        self.boton_crear_componentes_area_servicio = LtkButtonLine(self.frame_clasificacion_configuracion, funcion=lambda: self.crear_componetes_area_de_servicio_tecnico(), nombre_boton="Opciones generales")
        self.boton_crear_componentes_area_servicio.grid(row=2, column=0, padx=(5,5), pady=(5, 5), sticky="nsew")

    def inicializar_componentes(self):
        self.crear_componentes_edificio_caja()
        self.crear_componetes_area_de_servicio_tecnico()
        self.crear_caracteristicas_electronica()


    def crear_caracteristicas_electronica(self):


        self.resetear_frame_caracteristicas()

        self.frame_caracteristicas.columnconfigure(1, weight=1)

        self.etiqueta_titulo_caracteristicas_jugueteria = LtkLabel(self.frame_caracteristicas, texto="Caracteristicas de la tienda de electronica")
        self.etiqueta_titulo_caracteristicas_jugueteria.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas_jugueteria.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.etiqueta_cantidad_empleados = LtkLabel(self.frame_caracteristicas, texto="Cantidad de empleados:")
        self.etiqueta_cantidad_empleados.grid(row=2, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_empleados = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_empleados.grid(row=2, column=1,padx=(5,10),pady=(5, 5),sticky="nsew",columnspan=2)

        self.etiqueta_cantidad_maxima_personas = LtkLabel(self.frame_caracteristicas, texto="Cantidad maxima de personas:")
        self.etiqueta_cantidad_maxima_personas.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_maxima_personas = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_maxima_personas.grid(row=3, column=1,padx=(5,10),pady=(5, 5),sticky="nsew",columnspan=2)

        self.etiqueta_horario = LtkLabel(self.frame_caracteristicas, texto="Horario:")
        self.etiqueta_horario.grid(row=4, column=0,padx=(10,10), pady=(5, 10), sticky="w")

        self.entry_horario_inicio = LtkEntryLine(self.frame_caracteristicas, "Hora inicio")
        self.entry_horario_inicio.grid(row=4, column=1, padx=(5,10), pady=(5, 15), sticky="nsew")
        self.entry_horario_cierre = LtkEntryLine(self.frame_caracteristicas, "Hora cierre")
        self.entry_horario_cierre.grid(row=4, column=2, padx=(5,10), pady=(5, 15), sticky="nsew")

    def crear_componentes_edificio_caja(self):

        self.resetear_frame_caracteristicas()

        self.frame_caracteristicas.columnconfigure(1, weight=1)

        self.etiqueta_titulo_edificio_caja = LtkLabel(self.frame_caracteristicas, texto="Edificio caja")
        self.etiqueta_titulo_edificio_caja.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_edificio_caja.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.etiqueta_cantidad_cajas = LtkLabel(self.frame_caracteristicas, texto="Cantidad de cajas:")
        self.etiqueta_cantidad_cajas.grid(row=1, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_cajas = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_cajas.grid(row=1, column=1,padx=(5,10),pady=(5, 5),sticky="nsew",columnspan=2)

        self.etiqueta_cantidad_empleados_caja = LtkLabel(self.frame_caracteristicas, texto="Cantidad de empleados por caja:")
        self.etiqueta_cantidad_empleados_caja.grid(row=2, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_empleados_caja = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_empleados_caja.grid(row=2, column=1,padx=(5,10),pady=(5, 5),sticky="nsew",columnspan=2)

        self.etiqueta_paga_empleado_caja = LtkLabel(self.frame_caracteristicas, texto="Pago por empleado:")
        self.etiqueta_paga_empleado_caja.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_paga_empleado_caja = LtkEntryLine(self.frame_caracteristicas)
        self.entry_paga_empleado_caja.grid(row=3, column=1,padx=(5,10),pady=(5, 5),sticky="nsew",columnspan=2)

    def crear_componetes_area_de_servicio_tecnico(self):

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

        self.etiqueta_horario_servicio = LtkLabel(self.frame_caracteristicas, texto="Horario de servicio:")
        self.etiqueta_horario_servicio.grid(row=3, column=0,padx=(10,10), pady=(5, 10), sticky="w")

        self.entry_horario_inicio_servicio = LtkEntryLine(self.frame_caracteristicas, "Hora inicio")
        self.entry_horario_inicio_servicio.grid(row=3, column=1, padx=(5,10), pady=(5, 15), sticky="nsew")
        self.entry_horario_cierre_servicio = LtkEntryLine(self.frame_caracteristicas, "Hora cierre")
        self.entry_horario_cierre_servicio.grid(row=3, column=2, padx=(5,10), pady=(5, 15), sticky="nsew")



    def guardar_informacion(self):

        datos = {



        }

    def crear_componentes_datos_historicos(self):

        #Frame datos
        self.frame_datos_historicos = CTkFrame(self.ventana)
        self.frame_datos_historicos.grid(row=2, column=2, columnspan=2,padx = (10,10), pady=(10, 20), sticky="nsew")

        self.frame_datos_historicos.columnconfigure(1, weight=1)

        self.etiqueta_titulo_datos_historicos = LtkLabel(self.frame_datos_historicos, texto="Datos historicos")
        self.etiqueta_titulo_datos_historicos.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_datos_historicos.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        #Probabilidades
        self.etiqueta_opcion_datos_historicos_probabilidades = LtkLabel(self.frame_datos_historicos, texto="Seleccionar datos de probabilidades:")
        self.etiqueta_opcion_datos_historicos_probabilidades.grid(row=1, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_datos_historicos_probabilidades = LtkComboBoxLine(self.frame_datos_historicos, self.nombre_datos_historicos_probabilidades)
        self.opcion_datos_historicos_probabilidades.grid(row=1, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_datos_historicos_probabilidades = LtkButtonFill(self.frame_datos_historicos,funcion=lambda: self.cargar_datos_historicos_probabilidades(), nombre_boton="Cargar datos")
        self.boton_cargar_datos_historicos_probabilidades.grid(row=1, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")



        #Espera
        self.etiqueta_opcion_datos_historicos_espera = LtkLabel(self.frame_datos_historicos, texto="Seleccionar datos de espera:")
        self.etiqueta_opcion_datos_historicos_espera.grid(row=2, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_datos_historicos_espera = LtkComboBoxLine(self.frame_datos_historicos, self.nombre_datos_historicos_espera)
        self.opcion_datos_historicos_espera.grid(row=2, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_datos_historicos_espera = LtkButtonFill(self.frame_datos_historicos,funcion=lambda: self.cargar_datos_historicos_espera(), nombre_boton="Cargar datos")
        self.boton_cargar_datos_historicos_espera.grid(row=2, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")

        #Precio
        self.etiqueta_opcion_datos_precio = LtkLabel(self.frame_datos_historicos, texto="Seleccionar datos de precio:")
        self.etiqueta_opcion_datos_precio.grid(row=3, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_datos_precio = LtkComboBoxLine(self.frame_datos_historicos, self.nombre_datos_precio)
        self.opcion_datos_precio.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_datos_precio = LtkButtonFill(self.frame_datos_historicos,funcion=lambda: self.cargar_datos_precios(), nombre_boton="Cargar datos")
        self.boton_cargar_datos_precio.grid(row=3, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")


    def cargar_datos_historicos_probabilidades(self):

        if self.opcion_datos_historicos_probabilidades.get() == "Atraccion clientes":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Atraccion clientes")
            self.crear_ventana_emergente("Atraccion clientes", path)

        elif self.opcion_datos_historicos_probabilidades.get() == "Clasificacion de los productos":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Clasificacion de los productos")
            self.crear_ventana_emergente("Clasificacion de los productos", path)

        elif self.opcion_datos_historicos_probabilidades.get() == "Eventos de promocion":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Eventos de promocion")
            self.crear_ventana_emergente("Eventos de promocion", path)

        elif self.opcion_datos_historicos_probabilidades.get() == "Eventos especiales":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Eventos especiales")
            self.crear_ventana_emergente("Eventos especiales", path)

        elif self.opcion_datos_historicos_probabilidades.get() == "Tipo de servicio":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Tipo de servicio")
            self.crear_ventana_emergente("Tipo de servicio", path)

        elif self.opcion_datos_historicos_probabilidades.get() == "Tipo de visita":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Tipo de visita")
            self.crear_ventana_emergente("Tipo de visita", path)

    def cargar_datos_historicos_espera(self):

        if self.opcion_datos_historicos_espera.get() == "Tiempo de espera de servicio":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Tiempo de espera de servicio")
            self.crear_ventana_emergente("Tiempo de espera de servicio", path)

        elif self.opcion_datos_historicos_espera.get() == "Tiempo de espera en caja":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Tiempo de espera en caja")
            self.crear_ventana_emergente("Tiempo de espera en caja", path)

        elif self.opcion_datos_historicos_espera.get() == "Tiempo de realizacion de servicio":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Tiempo de realizacion de servicio")
            self.crear_ventana_emergente("Tiempo de realizacion de servicio", path)

    def cargar_datos_precios(self):

        if self.opcion_datos_precio.get() == "Costos de productos":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Costos de productos")
            self.crear_ventana_emergente("Costos de productos", path)

        elif self.opcion_datos_precio.get() == "Costos de servicios":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Costos de servicios")
            self.crear_ventana_emergente("Costos de servicios", path)

        elif self.opcion_datos_precio.get() == "Descuentos promocion servicios":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Descuentos promocion servicios")
            self.crear_ventana_emergente("Descuentos promocion servicios", path)


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


