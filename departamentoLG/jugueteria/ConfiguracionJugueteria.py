from customtkinter import *
from tkinter import messagebox

from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine
from componentes_graficos.LtkEntry import LtkEntryLine, LtkEntryFill
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkComboBox import LtkComboBoxLine
from componentes_graficos.LtkTreeView import LtkFileInputTreeView


class Configuracion_jugueteria:

    def __init__(self):

        self.nombre_datos_historicos_probabilidades = ["Atraccion de clientes", "Compra de juguetes", "Dias de promocion", "Tipo de visita"]
        self.nombre_datos_historicos_espera = ["Espera por pagar"]
        self.nombre_datos_precio = ["Precio de juguetes", "Descuentos promocion"]

        self.ruta_ventana = os.path.dirname(os.path.abspath(__file__))


        self.ventana = CTkToplevel()
        self.ventana.title("Configuración de la juguetería")


        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(1, weight=1)
        self.ventana.grid_columnconfigure(2, weight=1)
        self.ventana.grid_columnconfigure(3, weight=1)

        self.ventana.grid_rowconfigure(0, weight=1)
        self.ventana.grid_rowconfigure(1, weight=1)
        self.ventana.grid_rowconfigure(2, weight=1)


        # self.ventana.resizable(False, False)
        # self.ventana.configure(fg_color="#FFFFFF")

        self.crear_componentes()


        self.ventana.mainloop()


    def crear_componentes(self):

        self.etiqueta_titulo_principal = LtkLabel(self.ventana, texto="Configuracion de la jugueteria")
        self.etiqueta_titulo_principal.configure(font=('Poppins', 20, "bold"))
        self.etiqueta_titulo_principal.grid(row=0, column=0, pady=(20, 20), sticky="nsew")

        self.caracteristicas_jugueteria()
        self.crear_componentes_edificio_caja()
        self.crear_componentes_datos_historicos()

        self.boton_guardar = LtkButtonFill(self.ventana,funcion=lambda: self.guardar_informacion(), nombre_boton="Guardar")
        self.boton_guardar.grid(row=4, column=0, columnspan=4, padx=(10,10), pady=(10, 20), sticky="nsew")


    def caracteristicas_jugueteria(self):

        #Frame caracteristicas jugueteria
        self.frame_caracteristicas_jugueteria = CTkFrame(self.ventana)
        self.frame_caracteristicas_jugueteria.grid(row=1, column=0, columnspan=2,padx = (10,10), pady=(10, 20), sticky="nsew")

        self.frame_caracteristicas_jugueteria.columnconfigure(1, weight=1)

        self.etiqueta_titulo_caracteristicas_jugueteria = LtkLabel(self.frame_caracteristicas_jugueteria, texto="Caracteristicas de la jugueteria")
        self.etiqueta_titulo_caracteristicas_jugueteria.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas_jugueteria.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.etiqueta_cantidad_empleados = LtkLabel(self.frame_caracteristicas_jugueteria, texto="Cantidad de empleados:")
        self.etiqueta_cantidad_empleados.grid(row=2, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_empleados = LtkEntryLine(self.frame_caracteristicas_jugueteria)
        self.entry_cantidad_empleados.grid(row=2, column=1,padx=(5,10),pady=(5, 5),sticky="nsew",columnspan=2)

        self.etiqueta_cantidad_maxima_personas = LtkLabel(self.frame_caracteristicas_jugueteria, texto="Cantidad maxima de personas:")
        self.etiqueta_cantidad_maxima_personas.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_maxima_personas = LtkEntryLine(self.frame_caracteristicas_jugueteria)
        self.entry_cantidad_maxima_personas.grid(row=3, column=1,padx=(5,10),pady=(5, 5),sticky="nsew",columnspan=2)

        self.etiqueta_horario = LtkLabel(self.frame_caracteristicas_jugueteria, texto="Horario:")
        self.etiqueta_horario.grid(row=4, column=0,padx=(10,10), pady=(5, 10), sticky="w")

        self.entry_horario_inicio = LtkEntryLine(self.frame_caracteristicas_jugueteria, "Hora inicio")
        self.entry_horario_inicio.grid(row=4, column=1, padx=(5,10), pady=(5, 15), sticky="nsew")
        self.entry_horario_cierre = LtkEntryLine(self.frame_caracteristicas_jugueteria, "Hora cierre")
        self.entry_horario_cierre.grid(row=4, column=2, padx=(5,10), pady=(5, 15), sticky="nsew")

    def crear_componentes_edificio_caja(self):

        #Frame edificio caja
        self.frame_edificio_caja = CTkFrame(self.ventana)
        self.frame_edificio_caja.grid(row=2, column=0, columnspan=2,padx = (10,10), pady=(10, 20), sticky="nsew")

        self.frame_edificio_caja.columnconfigure(1, weight=1)

        self.etiqueta_titulo_edificio_caja = LtkLabel(self.frame_edificio_caja, texto="Edificio caja")
        self.etiqueta_titulo_edificio_caja.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_edificio_caja.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.etiqueta_cantidad_cajas = LtkLabel(self.frame_edificio_caja, texto="Cantidad de cajas:")
        self.etiqueta_cantidad_cajas.grid(row=1, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_cajas = LtkEntryLine(self.frame_edificio_caja)
        self.entry_cantidad_cajas.grid(row=1, column=1,padx=(5,10),pady=(5, 5),sticky="nsew",columnspan=2)

        self.etiqueta_cantidad_empleados_caja = LtkLabel(self.frame_edificio_caja, texto="Cantidad de empleados por caja:")
        self.etiqueta_cantidad_empleados_caja.grid(row=2, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_empleados_caja = LtkEntryLine(self.frame_edificio_caja)
        self.entry_cantidad_empleados_caja.grid(row=2, column=1,padx=(5,10),pady=(5, 5),sticky="nsew",columnspan=2)



    def guardar_informacion(self):

        datos = {



        }

    def crear_componentes_datos_historicos(self):

        #Frame datos
        self.frame_datos_historicos = CTkFrame(self.ventana)
        self.frame_datos_historicos.grid(row=1, column=2, columnspan=2,padx = (10,10), pady=(10, 20), sticky="nsew")

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



    def cargar_datos_historicos_espera(self):

        if self.opcion_datos_historicos_espera.get() == "Espera por pagar":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Espera para pagar")
            self.crear_ventana_emergente("Espera por pagar", path)

    def cargar_datos_precios(self):

        if self.opcion_datos_precio.get() == "Precio de juguetes":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Precio juguetes")
            self.crear_ventana_emergente("Precio de juguetes", path)

        elif self.opcion_datos_precio.get() == "Descuentos promocion":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Descuentos promocion")
            self.crear_ventana_emergente("Descuentos promocion", path)

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


