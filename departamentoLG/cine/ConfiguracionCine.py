from customtkinter import *

from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine
from componentes_graficos.LtkEntry import LtkEntryLine, LtkEntryFill
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkComboBox import LtkComboBoxLine
from componentes_graficos.LtkTreeView import LtkFileInputTreeView

class ConfiguracionCine:

    def __init__(self):

        self.nombre_datos_historicos_probabilidades = ["Atraccion de clientes", "Compra de alimentos y bebidas", "Dias de promocion", "Duracion de peliculas", "Eventos especiales", "Fallos en el sistema", "Tiempo de limpieza entre peliculas", "Tipo de visita", "Uso de baño", "Clasificacion de peliculas"]
        self.nombre_datos_historicos_espera = ["Espera baño", "Espera en la dulceria", "Espera en sala de cine", "Espera en la taquilla"]

        self.ruta_ventana = os.path.dirname(os.path.abspath(__file__))

        self.ventana = CTk()
        self.ventana.title("Configuracion Cine")

        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(1, weight=1)
        self.ventana.grid_columnconfigure(2, weight=1)
        self.ventana.grid_columnconfigure(3, weight=1)


        #self.ventana.resizable(False, False)
        self.ventana.configure(fd_color="#FFFFFF")



        self.crear_componentes()

        self.ventana.mainloop()

    def crear_componentes(self):

        self.etiqueta_titulo_principal = LtkLabel(self.ventana, texto="Configuracion Cine")
        self.etiqueta_titulo_principal.configure(font=('Poppins', 20, "bold"))
        self.etiqueta_titulo_principal.grid(row=0, column=0, pady=(20, 20), sticky="nsew")

        self.crear_componentes_caracteristicas_cine()

        self.crear_componentes_edificios_internos()
        self.crear_componentes_datos_historicos()





    def crear_componentes_caracteristicas_cine(self):

        self.frame_caracteristicas = CTkFrame(self.ventana)
        self.frame_caracteristicas.grid(row=1, column=0, columnspan=2,padx = (10,10), pady=(10, 20), sticky="nsew")

        self.etiqueta_titulo_caracteristicas = LtkLabel(self.frame_caracteristicas, texto="Caracteristicas")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)


        #Cantidad de empleados
        self.etiqueta_cantidad_empleados = LtkLabel(self.frame_caracteristicas, texto="Cantidad de empleados:")
        self.etiqueta_cantidad_empleados.grid(row=2, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_empleados = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_empleados.grid(row=2, column=1,padx=(5,10),pady=(5, 5),sticky="nsew",columnspan=2)

        self.etiqueta_capacidad_cine = LtkLabel(self.frame_caracteristicas, texto="Capacidad del cine:")
        self.etiqueta_capacidad_cine.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_capacidad_cine = LtkEntryLine(self.frame_caracteristicas)
        self.entry_capacidad_cine.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.etiqueta_horario = LtkLabel(self.frame_caracteristicas, texto="Horario:")
        self.etiqueta_horario.grid(row=4, column=0,padx=(10,10), pady=(5, 10), sticky="w")

        self.entry_horario_inicio = LtkEntryLine(self.frame_caracteristicas, "Hora inicio")
        self.entry_horario_inicio.grid(row=4, column=1, padx=(5,10), pady=(5, 15), sticky="nsew")
        self.entry_horario_cierre = LtkEntryLine(self.frame_caracteristicas, "Hora cierre")
        self.entry_horario_cierre.grid(row=4, column=2, padx=(5,10), pady=(5, 15), sticky="nsew")



    def crear_componentes_edificios_internos(self):

        self.crear_componentes_salas_cine()
        self.crear_componentes_dulceria()
        self.crear_componentes_taquilla()
        self.crear_componentes_baños()

    def crear_componentes_salas_cine(self):
        #Frame salas de cine

        self.frame_salas_cine = CTkFrame(self.ventana)
        self.frame_salas_cine.grid(row=2, column=0, columnspan=2,padx = (10,10), pady=(10, 20), sticky="nsew")

        self.frame_salas_cine.columnconfigure(1, weight=1)

        self.etiqueta_titulo_salas_cine = LtkLabel(self.frame_salas_cine, texto="Salas de cine")
        self.etiqueta_titulo_salas_cine.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_salas_cine.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.etiqueta_cantidad_salas = LtkLabel(self.frame_salas_cine, texto="Cantidad de salas:")
        self.etiqueta_cantidad_salas.grid(row=1, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_salas = LtkEntryLine(self.frame_salas_cine)
        self.entry_cantidad_salas.grid(row=1, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)


        self.etiqueta_capacidad_salas = LtkLabel(self.frame_salas_cine, texto="Capacidad de las salas:")
        self.etiqueta_capacidad_salas.grid(row=2, column=0, padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_capacidad_salas = LtkEntryLine(self.frame_salas_cine)
        self.entry_capacidad_salas.grid(row=2, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.etiqueta_cantidad_empleados_sala = LtkLabel(self.frame_salas_cine, texto="Cantidad de empleados por sala:")
        self.etiqueta_cantidad_empleados_sala.grid(row=3, column=0, padx=(10,10), pady=(5, 10), sticky="w")
        self.entry_cantidad_empleados_sala = LtkEntryLine(self.frame_salas_cine)
        self.entry_cantidad_empleados_sala.grid(row=3, column=1, padx=(5,10), pady=(5, 15), sticky="nsew",columnspan=2)

    def crear_componentes_dulceria(self):
        #Frame dulceria

        self.frame_dulceria = CTkFrame(self.ventana)
        self.frame_dulceria.grid(row=3, column=0, columnspan=2,padx = (10,10), pady=(10, 20), sticky="nsew")

        self.frame_dulceria.columnconfigure(1, weight=1)

        self.etiqueta_titulo_dulceria = LtkLabel(self.frame_dulceria, texto="Dulceria")
        self.etiqueta_titulo_dulceria.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_dulceria.grid(row=0, column=0, columnspan=2, pady=(5, 10))


        self.etiqueta_cantidad_empleados_dulceria = LtkLabel(self.frame_dulceria, texto="Cantidad de empleados:")
        self.etiqueta_cantidad_empleados_dulceria.grid(row=1, column=0, padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_empleados_dulceria = LtkEntryLine(self.frame_dulceria)
        self.entry_cantidad_empleados_dulceria.grid(row=1, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.etiqueta_cantidad_cajas_dulceria = LtkLabel(self.frame_dulceria, texto="Cantidad de cajas:")
        self.etiqueta_cantidad_cajas_dulceria.grid(row=2, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_cajas_dulceria = LtkEntryLine(self.frame_dulceria)
        self.entry_cantidad_cajas_dulceria.grid(row=2, column=1, padx=(5,10), pady=(5, 15), sticky="nsew",columnspan=2)

    def crear_componentes_taquilla(self):
        #Frame taquilla

        self.frame_taquilla = CTkFrame(self.ventana)
        self.frame_taquilla.grid(row=1, column=2, columnspan=2,padx = (10,10), pady=(10, 20), sticky="nsew")

        self.frame_taquilla.columnconfigure(1, weight=1)

        self.etiqueta_titulo_taquilla = LtkLabel(self.frame_taquilla, texto="Taquilla")
        self.etiqueta_titulo_taquilla.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_taquilla.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.etiqueta_cantidad_empleados_taquilla = LtkLabel(self.frame_taquilla, texto="Cantidad de empleados:")
        self.etiqueta_cantidad_empleados_taquilla.grid(row=1, column=0, padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_empleados_taquilla = LtkEntryLine(self.frame_taquilla)
        self.entry_cantidad_empleados_taquilla.grid(row=1, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.etiqueta_cantidad_cajas_taquilla = LtkLabel(self.frame_taquilla, texto="Cantidad de cajas:")
        self.etiqueta_cantidad_cajas_taquilla.grid(row=2, column=0, padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_cajas_taquilla = LtkEntryLine(self.frame_taquilla)
        self.entry_cantidad_cajas_taquilla.grid(row=2, column=1, padx=(5,10), pady=(5, 15), sticky="nsew",columnspan=2)

    def crear_componentes_baños(self):
        #Frame baños

        self.frame_banos = CTkFrame(self.ventana)
        self.frame_banos.grid(row=2, column=2, columnspan=2,padx = (10,10), pady=(10, 20), sticky="nsew")

        self.frame_banos.columnconfigure(1, weight=1)

        self.etiqueta_titulo_banos = LtkLabel(self.frame_banos, texto="Baños")
        self.etiqueta_titulo_banos.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_banos.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.etiqueta_cantidad_baños = LtkLabel(self.frame_banos, texto="Cantidad de baños:")
        self.etiqueta_cantidad_baños.grid(row=1, column=0, padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_baños = LtkEntryLine(self.frame_banos)
        self.entry_cantidad_baños.grid(row=1, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.etiqueta_capacidad_baños = LtkLabel(self.frame_banos, texto="Capacidad de los baños:")
        self.etiqueta_capacidad_baños.grid(row=2, column=0, padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_capacidad_baños = LtkEntryLine(self.frame_banos)
        self.entry_capacidad_baños.grid(row=2, column=1, padx=(5,10), pady=(5, 15), sticky="nsew",columnspan=2)

    def crear_componentes_datos_historicos(self):

        #Frame datos
        self.frame_datos_historicos = CTkFrame(self.ventana)
        self.frame_datos_historicos.grid(row=3, column=2, columnspan=2,padx = (10,10), pady=(10, 20), sticky="nsew")

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

    def cargar_datos_historicos_probabilidades(self):


        if self.opcion_datos_historicos_probabilidades.get() == "Atraccion de clientes":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Atraccion de clientes")
            self.crear_ventana_emergente("Atraccion de clientes", path)

        elif self.opcion_datos_historicos_probabilidades.get() == "Compra de alimentos y bebidas":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Compra de alimentos y bebidas")
            self.crear_ventana_emergente("Compra de alimentos y bebidas", path)

        elif self.opcion_datos_historicos_probabilidades.get() == "Dias de promocion":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Dias de promocion")
            self.crear_ventana_emergente("Dias de promocion", path)

        elif self.opcion_datos_historicos_probabilidades.get() == "Duracion de peliculas":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Duracion de peliculas")
            self.crear_ventana_emergente("Duracion de peliculas", path)

        elif self.opcion_datos_historicos_probabilidades.get() == "Eventos especiales":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Eventos especiales")
            self.crear_ventana_emergente("Eventos especiales", path)

        elif self.opcion_datos_historicos_probabilidades.get() == "Fallos en el sistema":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Fallos en el sistema")
            self.crear_ventana_emergente("Fallos en el sistema", path)

        elif self.opcion_datos_historicos_probabilidades.get() == "Tiempo de limpieza entre peliculas":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Tiempo de limpieza entre peliculas")
            self.crear_ventana_emergente("Tiempo de limpieza entre peliculas", path)

        elif self.opcion_datos_historicos_probabilidades.get() == "Tipo de visita":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Tipo de visita")
            self.crear_ventana_emergente("Tipo de visita", path)

        elif self.opcion_datos_historicos_probabilidades.get() == "Uso de baño":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Uso de baño")
            self.crear_ventana_emergente("Uso de baño", path)

        elif self.opcion_datos_historicos_probabilidades.get() == "Clasificacion de peliculas":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Clasificacion de peliculas")
            self.crear_ventana_emergente("Clasificacion de peliculas", path)


    def cargar_datos_historicos_espera(self):

        if self.opcion_datos_historicos_espera.get() == "Espera baño":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Espera en el baño")
            self.crear_ventana_emergente("Espera baño", path)

        elif self.opcion_datos_historicos_espera.get() == "Espera en la dulceria":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Espera en la dulceria")
            self.crear_ventana_emergente("Espera en la dulceria", path)

        elif self.opcion_datos_historicos_espera.get() == "Espera en sala de cine":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Espera en sala de cine")
            self.crear_ventana_emergente("Espera en sala de cine", path)

        elif self.opcion_datos_historicos_espera.get() == "Espera en la taquilla":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Espera en la taquilla")
            self.crear_ventana_emergente("Espera en la taquilla", path)

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


