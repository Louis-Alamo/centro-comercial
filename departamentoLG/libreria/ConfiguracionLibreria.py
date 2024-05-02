from customtkinter import *
from tkinter import messagebox

from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine
from componentes_graficos.LtkEntry import LtkEntryLine, LtkEntryFill
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkComboBox import LtkComboBoxLine
from componentes_graficos.LtkTreeView import LtkFileInputTreeView


class ConfiguracionLibreria:

    def __init__(self):
        self.nombre_datos_historicos_probabilidades = ["Eventos literarios", "Tendencias de venta", "Compra de libros", "Costo por libro", "Tipo de visita"]
        self.nombre_datos_historicos_espera = ["Espera en caja", "Espera en eventos", "Espera en lectura", "Espera en exhibicion",]
        self.ruta_ventana = os.path.dirname(os.path.abspath(__file__))

        self.ventana = CTkToplevel()
        self.ventana.title("Configuración de la juguetería")

        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(1, weight=1)
        self.ventana.grid_columnconfigure(2, weight=1)
        self.ventana.grid_columnconfigure(3, weight=1)

        self.ventana.resizable(False, False)
        self.ventana.configure(fg_color="#FFFFFF")

        self.crear_componentes()

        self.ventana.mainloop()

    def crear_componentes(self):
        self.etiqueta_titulo_principal = LtkLabel(self.ventana, texto="Configuracion libreria")
        self.etiqueta_titulo_principal.configure(font=('Poppins', 20, "bold"))
        self.etiqueta_titulo_principal.grid(row=0, column=0, pady=(20, 20), sticky="nsew")

        self.crear_componentes_caracteristicas_libreria()
        self.crear_componentes_areas_exhibicion()
        self.crear_componentes_areas_caja()
        self.crear_componentes_espacios_para_eventos()
        self.crear_componentes_espacios_para_lectura()
        self.crear_componentes_datos_historicos()

        self.boton_guardar = LtkButtonFill(self.ventana, funcion=lambda: self.guardar_informacion(),nombre_boton="Guardar")
        self.boton_guardar.grid(row=4, column=0, columnspan=4, padx=(10, 10), pady=(10, 20), sticky="nsew")


    def crear_componentes_caracteristicas_libreria(self):

        #Frame caracteristicas
        self.frame_caracteristicas = CTkFrame(self.ventana)
        self.frame_caracteristicas.grid(row=1, column=0, columnspan=2,padx = (10,10), pady=(10, 20), sticky="nsew")

        self.frame_caracteristicas.columnconfigure(1, weight=1)

        self.etiqueta_titulo_caracteristicas = LtkLabel(self.frame_caracteristicas, texto="Caracteristicas de la libreria")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.etiqueta_capacidad_libreria = LtkLabel(self.frame_caracteristicas, texto="Capacidad de la libreria:")
        self.etiqueta_capacidad_libreria.grid(row=1, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_capacidad_libreria = LtkEntryLine(self.frame_caracteristicas)
        self.entry_capacidad_libreria.grid(row=1, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")

        self.etiqueta_cantidad_empleados = LtkLabel(self.frame_caracteristicas, texto="Cantidad de empleados:")
        self.etiqueta_cantidad_empleados.grid(row=2, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_cantidad_empleados = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_empleados.grid(row=2, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")

        self.etiqueta_horario = LtkLabel(self.frame_caracteristicas, texto="Horario:")
        self.etiqueta_horario.grid(row=4, column=0,padx=(10,10), pady=(5, 10), sticky="w")

        self.entry_horario_inicio = LtkEntryLine(self.frame_caracteristicas, "Hora inicio")
        self.entry_horario_inicio.grid(row=4, column=1, padx=(5,10), pady=(5, 15), sticky="nsew")
        self.entry_horario_cierre = LtkEntryLine(self.frame_caracteristicas, "Hora cierre")
        self.entry_horario_cierre.grid(row=4, column=2, padx=(5,10), pady=(5, 15), sticky="nsew")

    def crear_componentes_areas_exhibicion(self):

        #Frame areas de exhibicion
        self.frame_areas_exhibicion = CTkFrame(self.ventana)
        self.frame_areas_exhibicion.grid(row=2, column=0, columnspan=2, padx=(10, 10), pady=(10, 20), sticky="nsew")

        self.frame_areas_exhibicion.columnconfigure(1, weight=1)

        self.etiqueta_titulo_areas_exhibicion = LtkLabel(self.frame_areas_exhibicion, texto="Areas de exhibicion")
        self.etiqueta_titulo_areas_exhibicion.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_areas_exhibicion.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.etiqueta_cantidad_areas = LtkLabel(self.frame_areas_exhibicion, texto="Cantidad de areas:")
        self.etiqueta_cantidad_areas.grid(row=1, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_cantidad_areas = LtkEntryLine(self.frame_areas_exhibicion)
        self.entry_cantidad_areas.grid(row=1, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")

        self.etiqueta_capacidad_areas = LtkLabel(self.frame_areas_exhibicion, texto="Capacidad de las areas:")
        self.etiqueta_capacidad_areas.grid(row=2, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_capacidad_areas = LtkEntryLine(self.frame_areas_exhibicion)
        self.entry_capacidad_areas.grid(row=2, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")


    def crear_componentes_areas_caja(self):

        #Frame areas de caja
        self.frame_areas_caja = CTkFrame(self.ventana)
        self.frame_areas_caja.grid(row=3, column=0, columnspan=2, padx=(10, 10), pady=(10, 20), sticky="nsew")

        self.frame_areas_caja.columnconfigure(1, weight=1)

        self.etiqueta_titulo_areas_caja = LtkLabel(self.frame_areas_caja, texto="Areas de caja")
        self.etiqueta_titulo_areas_caja.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_areas_caja.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.etiqueta_cantidad_cajas = LtkLabel(self.frame_areas_caja, texto="Cantidad de cajas:")
        self.etiqueta_cantidad_cajas.grid(row=1, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_cantidad_cajas = LtkEntryLine(self.frame_areas_caja)
        self.entry_cantidad_cajas.grid(row=1, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")

        self.etiqueta_cantidad_de_empleados_caja = LtkLabel(self.frame_areas_caja, texto="Cantidad de empleados por caja:")
        self.etiqueta_cantidad_de_empleados_caja.grid(row=2, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_cantidad_de_empleados_caja = LtkEntryLine(self.frame_areas_caja)
        self.entry_cantidad_de_empleados_caja.grid(row=2, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")


    def crear_componentes_espacios_para_eventos(self):

        #Frame espacios para eventos
        self.frame_espacios_para_eventos = CTkFrame(self.ventana)
        self.frame_espacios_para_eventos.grid(row=1, column=2, columnspan=2, padx=(10, 10), pady=(10, 20), sticky="nsew")

        self.frame_espacios_para_eventos.columnconfigure(1, weight=1)

        self.etiqueta_titulo_espacios_para_eventos = LtkLabel(self.frame_espacios_para_eventos, texto="Espacios para eventos")
        self.etiqueta_titulo_espacios_para_eventos.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_espacios_para_eventos.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.etiqueta_cantidad_espacios = LtkLabel(self.frame_espacios_para_eventos, texto="Cantidad de espacios:")
        self.etiqueta_cantidad_espacios.grid(row=1, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_cantidad_espacios = LtkEntryLine(self.frame_espacios_para_eventos)
        self.entry_cantidad_espacios.grid(row=1, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")

        self.etiqueta_capacidad_espacios = LtkLabel(self.frame_espacios_para_eventos, texto="Capacidad de los espacios:")
        self.etiqueta_capacidad_espacios.grid(row=2, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_capacidad_espacios = LtkEntryLine(self.frame_espacios_para_eventos)
        self.entry_capacidad_espacios.grid(row=2, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")

    def crear_componentes_espacios_para_lectura(self):

        #Frame espacios para lectura
        self.frame_espacios_para_lectura = CTkFrame(self.ventana)
        self.frame_espacios_para_lectura.grid(row=2, column=2, columnspan=2, padx=(10, 10), pady=(10, 20), sticky="nsew")

        self.frame_espacios_para_lectura.columnconfigure(1, weight=1)

        self.etiqueta_titulo_espacios_para_lectura = LtkLabel(self.frame_espacios_para_lectura, texto="Espacios para lectura")
        self.etiqueta_titulo_espacios_para_lectura.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_espacios_para_lectura.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.etiqueta_cantidad_espacios_lectura = LtkLabel(self.frame_espacios_para_lectura, texto="Cantidad de espacios:")
        self.etiqueta_cantidad_espacios_lectura.grid(row=1, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_cantidad_espacios_lectura = LtkEntryLine(self.frame_espacios_para_lectura)
        self.entry_cantidad_espacios_lectura.grid(row=1, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")

        self.etiqueta_capacidad_espacios_lectura = LtkLabel(self.frame_espacios_para_lectura, texto="Capacidad de los espacios:")
        self.etiqueta_capacidad_espacios_lectura.grid(row=2, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_capacidad_espacios_lectura = LtkEntryLine(self.frame_espacios_para_lectura)
        self.entry_capacidad_espacios_lectura.grid(row=2, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")

    def guardar_informacion(self):
        pass

    def crear_componentes_datos_historicos(self):
        # Frame datos
        self.frame_datos_historicos = CTkFrame(self.ventana)
        self.frame_datos_historicos.grid(row=3, column=2, columnspan=2, padx=(10, 10), pady=(10, 20), sticky="nsew")

        self.frame_datos_historicos.columnconfigure(1, weight=1)

        self.etiqueta_titulo_datos_historicos = LtkLabel(self.frame_datos_historicos, texto="Datos historicos")
        self.etiqueta_titulo_datos_historicos.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_datos_historicos.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        # Probabilidades
        self.etiqueta_opcion_datos_historicos_probabilidades = LtkLabel(self.frame_datos_historicos,texto="Seleccionar datos de probabilidades:")
        self.etiqueta_opcion_datos_historicos_probabilidades.grid(row=1, column=0, padx=(10, 10), pady=(5, 2),sticky="w")

        self.opcion_datos_historicos_probabilidades = LtkComboBoxLine(self.frame_datos_historicos,self.nombre_datos_historicos_probabilidades)
        self.opcion_datos_historicos_probabilidades.grid(row=1, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_datos_historicos_probabilidades = LtkButtonFill(self.frame_datos_historicos,funcion=lambda: self.cargar_datos_historicos_probabilidades(),nombre_boton="Cargar datos")
        self.boton_cargar_datos_historicos_probabilidades.grid(row=1, column=3, padx=(5, 10), pady=(5, 5),sticky="nsew")

        # Espera
        self.etiqueta_opcion_datos_historicos_espera = LtkLabel(self.frame_datos_historicos,texto="Seleccionar datos de espera:")
        self.etiqueta_opcion_datos_historicos_espera.grid(row=2, column=0, padx=(10, 10), pady=(5, 2), sticky="w")

        self.opcion_datos_historicos_espera = LtkComboBoxLine(self.frame_datos_historicos,self.nombre_datos_historicos_espera)
        self.opcion_datos_historicos_espera.grid(row=2, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_datos_historicos_espera = LtkButtonFill(self.frame_datos_historicos,funcion=lambda: self.cargar_datos_historicos_espera(),nombre_boton="Cargar datos")
        self.boton_cargar_datos_historicos_espera.grid(row=2, column=3, padx=(5, 10), pady=(5, 5), sticky="nsew")

    def cargar_datos_historicos_probabilidades(self):
        pass

    def cargar_datos_historicos_espera(self):
        pass

    def crear_ventana_emergente(self, titulo, ruta_archivo):
        self.ventana_emergente = CTkToplevel()
        self.ventana_emergente.title(titulo)

        # Establecer la ventana como modal
        self.ventana_emergente.grab_set()
        self.ventana_emergente.focus_set()
        self.ventana_emergente.transient(self.ventana)
        self.ventana_emergente.attributes('-topmost', True)

        self.tabla = LtkFileInputTreeView(self.ventana_emergente, ruta_archivo)
        self.tabla.grid(row=0, column=0, padx=(10, 10), pady=(10, 20), sticky="nsew")

        self.boton_guardar = LtkButtonFill(self.ventana_emergente,
                                           funcion=lambda: self.tabla.guardar_informacion(self.ventana_emergente),
                                           nombre_boton="Guardar")
        self.boton_guardar.grid(row=1, column=0, padx=(10, 10), pady=(10, 20), sticky="nsew")

        self.ventana_emergente.mainloop()


