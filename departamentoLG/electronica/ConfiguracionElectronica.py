from customtkinter import *
from tkinter import messagebox

from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine
from componentes_graficos.LtkEntry import LtkEntryLine, LtkEntryFill
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkComboBox import LtkComboBoxLine
from componentes_graficos.LtkTreeView import LtkFileInputTreeView


class ConfiguracionElectronica:

    def __init__(self):
        self.nombre_datos_historicos_probabilidades = ["Atraccion de clientes", "Compra de alimentos y bebidas",
                                                       "Dias de promocion", "Duracion de peliculas",
                                                       "Eventos especiales", "Fallos en el sistema",
                                                       "Tiempo de limpieza entre peliculas", "Tipo de visita",
                                                       "Uso de baño", "Clasificacion de peliculas"]
        self.nombre_datos_historicos_espera = ["Espera baño", "Espera en la dulceria", "Espera en sala de cine",
                                               "Espera en la taquilla"]
        self.ruta_ventana = os.path.dirname(os.path.abspath(__file__))

        self.ventana = CTkToplevel()
        self.ventana.title("Configuración de tienda electronica")

        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(1, weight=1)
        self.ventana.grid_columnconfigure(2, weight=1)
        self.ventana.grid_columnconfigure(3, weight=1)

        self.ventana.resizable(False, False)
        self.ventana.configure(fd_color="#FFFFFF")

        self.crear_componentes()

        self.ventana.mainloop()

    def crear_componentes(self):
        self.etiqueta_titulo_principal = LtkLabel(self.ventana, texto="Configuracion tienda electronica")
        self.etiqueta_titulo_principal.configure(font=('Poppins', 20, "bold"))
        self.etiqueta_titulo_principal.grid(row=0, column=0, pady=(20, 20), sticky="nsew")

        self.boton_guardar = LtkButtonFill(self.ventana, funcion=lambda: self.guardar_informacion(),
                                           nombre_boton="Guardar")
        self.boton_guardar.grid(row=4, column=0, columnspan=4, padx=(10, 10), pady=(10, 20), sticky="nsew")

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
        self.etiqueta_opcion_datos_historicos_probabilidades = LtkLabel(self.frame_datos_historicos,
                                                                        texto="Seleccionar datos de probabilidades:")
        self.etiqueta_opcion_datos_historicos_probabilidades.grid(row=1, column=0, padx=(10, 10), pady=(5, 2),
                                                                  sticky="w")

        self.opcion_datos_historicos_probabilidades = LtkComboBoxLine(self.frame_datos_historicos,
                                                                      self.nombre_datos_historicos_probabilidades)
        self.opcion_datos_historicos_probabilidades.grid(row=1, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew",
                                                         columnspan=2)

        self.boton_cargar_datos_historicos_probabilidades = LtkButtonFill(self.frame_datos_historicos,
                                                                          funcion=lambda: self.cargar_datos_historicos_probabilidades(),
                                                                          nombre_boton="Cargar datos")
        self.boton_cargar_datos_historicos_probabilidades.grid(row=1, column=3, padx=(5, 10), pady=(5, 5),
                                                               sticky="nsew")

        # Espera
        self.etiqueta_opcion_datos_historicos_espera = LtkLabel(self.frame_datos_historicos,
                                                                texto="Seleccionar datos de espera:")
        self.etiqueta_opcion_datos_historicos_espera.grid(row=2, column=0, padx=(10, 10), pady=(5, 2), sticky="w")

        self.opcion_datos_historicos_espera = LtkComboBoxLine(self.frame_datos_historicos,
                                                              self.nombre_datos_historicos_espera)
        self.opcion_datos_historicos_espera.grid(row=2, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew",
                                                 columnspan=2)

        self.boton_cargar_datos_historicos_espera = LtkButtonFill(self.frame_datos_historicos,
                                                                  funcion=lambda: self.cargar_datos_historicos_espera(),
                                                                  nombre_boton="Cargar datos")
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