from customtkinter import *
from tkinter import messagebox

from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine, LtkButtonTransparentBackground
from componentes_graficos.LtkEntry import LtkEntryLine, LtkEntryFill
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkCheckBox import LtkCheckBoxFill
from componentes_graficos.LtkComboBox import LtkComboBoxLine
from componentes_graficos.LtkTreeView import LtkFileInputTreeView

import json
import os

class ConfiguracionCine:

    def __init__(self):

        self.nombre_datos_historicos_probabilidades = ["Atraccion de clientes", "Compra de alimentos y bebidas", "Dias de promocion", "Duracion de peliculas", "Eventos especiales",  "Tipo de visita", "Uso de baño", "Clasificacion de peliculas"]
        self.nombre_datos_historicos_espera = ["Espera baño", "Espera en la dulceria", "Espera en la taquilla"]
        self.nombre_datos_precios = [ "Precio peliculas", "Precios alimentos y bebidas", "Descuentos promocion", "Precio baño"]

        self.ruta_ventana = os.path.dirname(os.path.abspath(__file__))

        self.ventana = CTk()
        self.ventana.title("Configuracion Cine")


        self.ventana.grid_columnconfigure(1, weight=1)
        self.ventana.grid_rowconfigure(1, weight=1)



        # self.ventana.resizable(False, False)
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
        self.etiqueta_titulo_principal = LtkLabel(self.ventana, texto="Configuracion Cine")
        self.etiqueta_titulo_principal.configure(font=('Poppins', 20, "bold"))
        self.etiqueta_titulo_principal.grid(row=0, column=0, pady=(10, 20), sticky="ew", columnspan=2)
        self.etiqueta_titulo_principal.columnconfigure(0,weight=1)  # Para que la etiqueta se expanda solo horizontalmente y esté centrada


        
        # self.boton_guardar = LtkButtonFill(self.ventana,funcion=lambda: self.guardar_informacion(), nombre_boton="Guardar")
        # self.boton_guardar.grid(row=4, column=0, columnspan=4, padx=(10,10), pady=(10, 20), sticky="nsew")

    def guardar_informacion(self):
        informacion = {
            "cantidad_empleados": int(17 if self.entry_cantidad_empleados.get() == "" else self.entry_cantidad_empleados.get()),
            "capacidad_cine": int(100 if self.entry_capacidad_cine.get() == "" else self.entry_capacidad_cine.get()),
            "horario_inicio": str("08:00" if self.entry_horario_inicio.get() == "" else self.entry_horario_inicio.get()),
            "horario_cierre": str("22:00" if self.entry_horario_cierre.get() == "" else self.entry_horario_cierre.get()),
            "cantidad_salas": int(5 if self.entry_cantidad_salas.get() == "" else self.entry_cantidad_salas.get()),
            "capacidad_salas": int(50 if self.entry_capacidad_salas.get() == "" else self.entry_capacidad_salas.get()),
            "cantidad_empleados_sala": int(2 if self.entry_cantidad_empleados_sala.get() == "" else self.entry_cantidad_empleados_sala.get()),
            "cantidad_empleados_dulceria": int(3 if self.entry_cantidad_empleados_dulceria.get() == "" else self.entry_cantidad_empleados_dulceria.get()),
            "cantidad_cajas_dulceria": int(3 if self.entry_cantidad_cajas_dulceria.get() == "" else self.entry_cantidad_cajas_dulceria.get()),
            "cantidad_empleados_taquilla": int(1 if self.entry_cantidad_empleados_taquilla.get() == "" else self.entry_cantidad_empleados_taquilla.get()),
            "cantidad_cajas_taquilla": int(5 if self.entry_cantidad_cajas_taquilla.get() == "" else self.entry_cantidad_cajas_taquilla.get()),
            "cantidad_baños": int(2 if self.entry_cantidad_baños.get() == "" else self.entry_cantidad_baños.get()),
            "capacidad_baños": int(5 if self.entry_capacidad_baños.get() == "" else self.entry_capacidad_baños.get())
        }

        informacion_json = json.dumps(informacion, indent=4)

        dir_path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(dir_path, r'datos\configuracion_cine.json')

        # Escribe la cadena JSON en un archivo
        with open(config_path, 'w') as f:
            f.write(informacion_json)

        messagebox.showinfo("Informacion", "Informacion guardada correctamente")


    def resetear_frame_caracteristicas(self):
        for widget in self.frame_caracteristicas.winfo_children():
            widget.destroy()

    def crear_botones_clasificacion_caracteristicas_cine(self):

        self.boton_caracteristicas_principales = LtkButtonLine(self.frame_clasificacion_configuracion, funcion=lambda: self.crear_componentes_caracteristicas_cine(), nombre_boton="Opciones generales")
        self.boton_caracteristicas_principales.grid(row=0, column=0, padx=(5,5), pady=(5, 5), sticky="nsew")

        self.boton_caracteristicas_salas = LtkButtonLine(self.frame_clasificacion_configuracion, funcion=lambda: self.crear_componentes_salas_cine(), nombre_boton="Salas de cine")
        self.boton_caracteristicas_salas.grid(row=1, column=0, padx=(5,5), pady=(5, 5), sticky="nsew")

        self.boton_caracteristicas_dulceria = LtkButtonLine(self.frame_clasificacion_configuracion, funcion=lambda: self.crear_componentes_dulceria(), nombre_boton="Dulceria")
        self.boton_caracteristicas_dulceria.grid(row=2, column=0, padx=(5,5), pady=(5, 5), sticky="nsew")

        self.boton_caracteristicas_taquilla = LtkButtonLine(self.frame_clasificacion_configuracion, funcion=lambda: self.crear_componentes_taquilla(), nombre_boton="Taquilla")
        self.boton_caracteristicas_taquilla.grid(row=3, column=0, padx=(5,5), pady=(5, 5), sticky="nsew")

        self.boton_caracteristicas_baños = LtkButtonLine(self.frame_clasificacion_configuracion, funcion=lambda: self.crear_componentes_baños(), nombre_boton="Baños")
        self.boton_caracteristicas_baños.grid(row=4, column=0, padx=(5,5), pady=(5, 5), sticky="nsew")

        self.boton_caracteristicas_datos_historicos = LtkButtonLine(self.frame_clasificacion_configuracion, funcion=lambda: self.crear_componentes_datos_historicos(), nombre_boton="Datos historicos")
        self.boton_caracteristicas_datos_historicos.grid(row=5, column=0, padx=(5,5), pady=(5, 5), sticky="nsew")


    def crear_componentes_caracteristicas_cine(self):


        #Variables
        self.variable_opcion_eventos_especiales_cine = IntVar()
        self.variable_opcion_permitir_mascotas_cine = IntVar()


        self.lista_opciones_probabilidades_caracteristicas_cine = ["Atraccion de clientes", "Dias de promocion", "Eventos especiales", "Tipo de visita"]
        self.lista_opciones_precios_caracteristicas_cine = ["Precio de mantenimiento del cine", "Descuentos de promocion"]


        self.resetear_frame_caracteristicas()

        self.etiqueta_titulo_caracteristicas = LtkLabel(self.frame_caracteristicas, texto="Caracteristicas")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))

        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)


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


        #Datos historicos

        #Probabilidades
        self.etiqueta_opcion_datos_historicos_probabilidades_cine = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de probabilidades:")
        self.etiqueta_opcion_datos_historicos_probabilidades_cine.grid(row=5, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_datos_historicos_probabilidades_cine = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_probabilidades_caracteristicas_cine)
        self.opcion_datos_historicos_probabilidades_cine.grid(row=5, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_datos_historicos_probabilidades_cine = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_probabilidades_cine(), nombre_boton="Cargar datos")
        self.boton_cargar_datos_historicos_probabilidades_cine.grid(row=5, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")

        #Precios
        self.opcion_datos_precios_cine = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de precios:")
        self.opcion_datos_precios_cine.grid(row=6, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_datos_precios_cine = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_precios_caracteristicas_cine)
        self.opcion_datos_precios_cine.grid(row=6, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_datos_precios_cine = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar(), nombre_boton="Cargar datos")
        self.boton_cargar_datos_precios_cine.grid(row=6, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")


        #Opciones
        self.opcion_eventos_especiales_cine = LtkCheckBoxFill(self.frame_caracteristicas, texto="Eventos especiales", variable=self.variable_opcion_eventos_especiales_cine)
        self.opcion_eventos_especiales_cine.grid(row=6, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_permitir_mascotas = LtkCheckBoxFill(self.frame_caracteristicas, texto="Permitir mascotas", variable=self.variable_opcion_permitir_mascotas_cine)
        self.opcion_permitir_mascotas.grid(row=7, column=0, padx=(10,10), pady=(5, 2), sticky="w")

    def crear_componentes_edificios_internos(self):

        self.crear_componentes_salas_cine()
        self.crear_componentes_dulceria()
        self.crear_componentes_taquilla()
        self.crear_componentes_baños()



    def crear_componentes_salas_cine(self):

        self.opciones_lineas_espera_salas = ["Espera en sala de cine", "Tiempo de limpieza entre peliculas", "Tiempo de salida de sala", "Tiempo de entrada de sala"]
        self.opciones_probabilidades_salas = ["Fallos en el sistema de sala"]




        self.resetear_frame_caracteristicas()

        self.frame_caracteristicas.columnconfigure(1, weight=1)

        self.etiqueta_titulo_salas_cine = LtkLabel(self.frame_caracteristicas, texto="Salas de cine")
        self.etiqueta_titulo_salas_cine.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_salas_cine.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.etiqueta_cantidad_salas = LtkLabel(self.frame_caracteristicas, texto="Cantidad de salas:")
        self.etiqueta_cantidad_salas.grid(row=1, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_salas = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_salas.grid(row=1, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.etiqueta_capacidad_salas = LtkLabel(self.frame_caracteristicas, texto="Capacidad de las salas:")
        self.etiqueta_capacidad_salas.grid(row=2, column=0, padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_capacidad_salas = LtkEntryLine(self.frame_caracteristicas)
        self.entry_capacidad_salas.grid(row=2, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.etiqueta_cantidad_empleados_sala = LtkLabel(self.frame_caracteristicas, texto="Cantidad de empleados por sala:")
        self.etiqueta_cantidad_empleados_sala.grid(row=3, column=0, padx=(10,10), pady=(5, 10), sticky="w")
        self.entry_cantidad_empleados_sala = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_empleados_sala.grid(row=3, column=1, padx=(5,10), pady=(5, 15), sticky="nsew",columnspan=2)

        self.etiqueta_sueldo_empleados_sala = LtkLabel(self.frame_caracteristicas, texto="Sueldo de empleados por sala:")
        self.etiqueta_sueldo_empleados_sala.grid(row=4, column=0, padx=(10,10), pady=(5, 10), sticky="w")
        self.entry_sueldo_empleados_sala = LtkEntryLine(self.frame_caracteristicas)
        self.entry_sueldo_empleados_sala.grid(row=4, column=1, padx=(5,10), pady=(5, 15), sticky="nsew",columnspan=2)



        #Datos historicos

        #Lineas de espera
        self.etiqueta_opcion_datos_espera_sala = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de espera:")
        self.etiqueta_opcion_datos_espera_sala.grid(row=5, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_datos_espera_sala = LtkComboBoxLine(self.frame_caracteristicas, self.opciones_lineas_espera_salas)
        self.opcion_datos_espera_sala.grid(row=5, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_datos_espera_sala = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_espera_sala(), nombre_boton="Cargar datos")
        self.boton_datos_espera_sala.grid(row=5, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")

        #Probabilidades
        self.etiqueta_opcion_datos_probabilidades_sala = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de probabilidades:")
        self.etiqueta_opcion_datos_probabilidades_sala.grid(row=6, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_datos_probabilidades_sala = LtkComboBoxLine(self.frame_caracteristicas, self.opciones_probabilidades_salas)
        self.opcion_datos_probabilidades_sala.grid(row=6, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_datos_probabilidades_sala = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_probabilidades_sala(), nombre_boton="Cargar datos")
        self.boton_datos_probabilidades_sala.grid(row=6, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")




    def crear_componentes_dulceria(self):

        self.resetear_frame_caracteristicas()

        self.frame_caracteristicas.columnconfigure(1, weight=1)

        self.etiqueta_titulo_dulceria = LtkLabel(self.frame_caracteristicas, texto="Dulceria")
        self.etiqueta_titulo_dulceria.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_dulceria.grid(row=0, column=0, columnspan=2, pady=(5, 10))


        self.etiqueta_cantidad_empleados_dulceria = LtkLabel(self.frame_caracteristicas, texto="Cantidad de empleados:")
        self.etiqueta_cantidad_empleados_dulceria.grid(row=1, column=0, padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_empleados_dulceria = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_empleados_dulceria.grid(row=1, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.etiqueta_cantidad_cajas_dulceria = LtkLabel(self.frame_caracteristicas, texto="Cantidad de cajas:")
        self.etiqueta_cantidad_cajas_dulceria.grid(row=2, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_cajas_dulceria = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_cajas_dulceria.grid(row=2, column=1, padx=(5,10), pady=(5, 15), sticky="nsew",columnspan=2)

    def crear_componentes_taquilla(self):

        self.resetear_frame_caracteristicas()

        self.frame_caracteristicas.columnconfigure(1, weight=1)

        self.etiqueta_titulo_taquilla = LtkLabel(self.frame_caracteristicas, texto="Taquilla")
        self.etiqueta_titulo_taquilla.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_taquilla.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.etiqueta_cantidad_empleados_taquilla = LtkLabel(self.frame_caracteristicas, texto="Cantidad de empleados:")
        self.etiqueta_cantidad_empleados_taquilla.grid(row=1, column=0, padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_empleados_taquilla = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_empleados_taquilla.grid(row=1, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.etiqueta_cantidad_cajas_taquilla = LtkLabel(self.frame_caracteristicas, texto="Cantidad de cajas:")
        self.etiqueta_cantidad_cajas_taquilla.grid(row=2, column=0, padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_cajas_taquilla = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_cajas_taquilla.grid(row=2, column=1, padx=(5,10), pady=(5, 15), sticky="nsew",columnspan=2)

    def crear_componentes_baños(self):

        self.resetear_frame_caracteristicas()

        self.frame_caracteristicas.columnconfigure(1, weight=1)

        self.etiqueta_titulo_banos = LtkLabel(self.frame_caracteristicas, texto="Baños")
        self.etiqueta_titulo_banos.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_banos.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.etiqueta_cantidad_baños = LtkLabel(self.frame_caracteristicas, texto="Cantidad de baños:")
        self.etiqueta_cantidad_baños.grid(row=1, column=0, padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_baños = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_baños.grid(row=1, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.etiqueta_capacidad_baños = LtkLabel(self.frame_caracteristicas, texto="Capacidad de los baños:")
        self.etiqueta_capacidad_baños.grid(row=2, column=0, padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_capacidad_baños = LtkEntryLine(self.frame_caracteristicas)
        self.entry_capacidad_baños.grid(row=2, column=1, padx=(5,10), pady=(5, 15), sticky="nsew",columnspan=2)

    def crear_componentes_datos_historicos(self):

        self.resetear_frame_caracteristicas()


        self.frame_caracteristicas.columnconfigure(1, weight=1)

        self.etiqueta_titulo_datos_historicos = LtkLabel(self.frame_caracteristicas, texto="Datos historicos")
        self.etiqueta_titulo_datos_historicos.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_datos_historicos.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        #Probabilidades
        self.etiqueta_opcion_datos_historicos_probabilidades = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de probabilidades:")
        self.etiqueta_opcion_datos_historicos_probabilidades.grid(row=1, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_datos_historicos_probabilidades = LtkComboBoxLine(self.frame_caracteristicas, self.nombre_datos_historicos_probabilidades)
        self.opcion_datos_historicos_probabilidades.grid(row=1, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_datos_historicos_probabilidades = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_historicos_probabilidades(), nombre_boton="Cargar datos")
        self.boton_cargar_datos_historicos_probabilidades.grid(row=1, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")



        #Espera
        self.etiqueta_opcion_datos_historicos_espera = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de espera:")
        self.etiqueta_opcion_datos_historicos_espera.grid(row=2, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_datos_historicos_espera = LtkComboBoxLine(self.frame_caracteristicas, self.nombre_datos_historicos_espera)
        self.opcion_datos_historicos_espera.grid(row=2, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_datos_historicos_espera = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_historicos_espera(), nombre_boton="Cargar datos")
        self.boton_cargar_datos_historicos_espera.grid(row=2, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")


        self.etiqueta_opcion_datos_precios = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de precios:")
        self.etiqueta_opcion_datos_precios.grid(row=3, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_datos_precios = LtkComboBoxLine(self.frame_caracteristicas, self.nombre_datos_precios)
        self.opcion_datos_precios.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_datos_precios = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_precios(), nombre_boton="Cargar datos")
        self.boton_cargar_datos_precios.grid(row=3, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")

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

    def cargar_datos_precios(self):

        if self.opcion_datos_precios.get() == "Precio peliculas":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Precio peliculas")
            self.crear_ventana_emergente("Precio peliculas", path)

        elif self.opcion_datos_precios.get() == "precios de alimentos y bebidas":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\precios de alimentos y bebidas")
            self.crear_ventana_emergente("precios de alimentos y bebidas", path)

        elif self.opcion_datos_precios.get() == "Descuentos promocion":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Descuentos promocion")
            self.crear_ventana_emergente("Descuentos promocion", path)

        elif self.opcion_datos_precios.get() == "Precio baño":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Precio baño")
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



    #Carga de datos de datos historicos


    #Cine en general
    def cargar_datos_precios_cine(self):
        pass

    def cargar_datos_probabilidades_cine(self):
        pass


    #Salas de cine
    def cargar_datos_espera_sala(self):
        pass

    def cargar_datos_probabilidades_sala(self):
        pass
