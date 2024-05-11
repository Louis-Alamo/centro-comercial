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



        self.ruta_ventana = os.path.dirname(os.path.abspath(__file__))

        self.ventana = CTk()
        self.ventana.title("Configuracion Cine")


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
        self.etiqueta_titulo_principal = LtkLabel(self.ventana, texto="Configuracion Cine")
        self.etiqueta_titulo_principal.configure(font=('Poppins', 20, "bold"))
        self.etiqueta_titulo_principal.grid(row=0, column=0, pady=(10, 20), sticky="ew", columnspan=2)
        self.etiqueta_titulo_principal.columnconfigure(0,weight=1)  # Para que la etiqueta se expanda solo horizontalmente y esté centrada


        self.inicializar_componentes()


        self.boton_cerrar = LtkButtonFill(self.ventana,funcion=lambda: self.ventana.destroy(), nombre_boton="Cerrar")
        self.boton_cerrar.grid(row=2, column=0, columnspan=4, padx=(10,10), pady=(10, 20), sticky="w")

        self.boton_guardar = LtkButtonFill(self.ventana,funcion=lambda: self.guardar_informacion(), nombre_boton="Guardar")
        self.boton_guardar.grid(row=2, column=1, columnspan=4, padx=(10,10), pady=(10, 20), sticky="nsew")


        
        # self.boton_guardar = LtkButtonFill(self.ventana,funcion=lambda: self.guardar_informacion(), nombre_boton="Guardar")
        # self.boton_guardar.grid(row=4, column=0, columnspan=4, padx=(10,10), pady=(10, 20), sticky="nsew")

    def guardar_informacion(self):


        configuracion_cine ={
            "General": self.general,
            "Salas de cine": self.salas_de_cine,
            "Dulceria": self.dulceria,
            "Taquilla": self.taquilla,
            "Baños": self.baños
        }

        informacion_json = json.dumps(configuracion_cine, indent=4)

        dir_path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(dir_path, r'datos\configuracion_cine.json')

        # Escribe la cadena JSON en un archivo
        with open(config_path, 'w') as f:
            f.write(informacion_json)

        messagebox.showinfo("Informacion", "Informacion guardada correctamente")

    def resetear_frame_caracteristicas(self):
        for widget in self.frame_caracteristicas.winfo_children():
            widget.grid_remove()

    def inicializar_componentes(self):

        self.crear_componentes_salas_cine()
        self.crear_componentes_dulceria()
        self.crear_componentes_taquilla()
        self.crear_componentes_baños()
        self.crear_componentes_caracteristicas_cine()

        self.general = {
            "Capacidad del cine": int(
                100 if self.entry_capacidad_cine.get() == "" else self.entry_capacidad_cine.get()),
            "Horario": {
                "Entrada": "08:00" if self.entry_horario_inicio.get() == "" else self.entry_horario_inicio.get(),
                "Cierre": "22:00" if self.entry_horario_cierre.get() == "" else self.entry_horario_cierre.get()
            },
            "Eventos especiales": self.variable_opcion_eventos_especiales_cine.get(),
            "Permitir mascotas": self.variable_opcion_permitir_mascotas_cine.get(),
        }
        self.salas_de_cine = {
            "Cantidad de salas": int(5 if self.entry_cantidad_salas.get() == "" else self.entry_cantidad_salas.get()),
            "Capacidad de las salas": int(
                100 if self.entry_capacidad_salas.get() == "" else self.entry_capacidad_salas.get()),
            "Cantidad de empleados por sala": int(
                2 if self.entry_cantidad_empleados_sala.get() == "" else self.entry_cantidad_empleados_sala.get()),
            "Sueldo de empleados por sala": int(
                1000 if self.entry_sueldo_empleados_sala.get() == "" else self.entry_sueldo_empleados_sala.get())
        }
        self.dulceria = {
            "Cantidad de cajas": int(
                5 if self.entry_cantidad_cajas_dulceria.get() == "" else self.entry_cantidad_cajas_dulceria.get()),
            "Sueldo de empleados": int(
                1000 if self.entry_sueldo_empleados_cine.get() == "" else self.entry_sueldo_empleados_cine.get()),
            "Rendimiento de empleados": int(
                100 if self.entry_rendimiento_de_empleados_dulceria.get() == "" else self.entry_rendimiento_de_empleados_dulceria.get()),
            "Probabilidad de compra de productos": int(
                100 if self.entry_probabilidad_compra_dulceria.get() == "" else self.entry_probabilidad_compra_dulceria.get())
        }
        self.taquilla = {
            "Cantidad de cajas": int(
                5 if self.entry_cantidad_cajas_taquilla.get() == "" else self.entry_cantidad_cajas_taquilla.get()),
            "Sueldo de empleados": int(
                1000 if self.entry_sueldo_empleado_taquilla.get() == "" else self.entry_sueldo_empleado_taquilla.get()),
            "Rendimiento de empleados": int(
                100 if self.entry_rendimiento_empleados_taquilla.get() == "" else self.entry_rendimiento_empleados_taquilla.get())
        }
        self.baños = {
            "Cantidad de baños": int(5 if self.entry_cantidad_baños.get() == "" else self.entry_cantidad_baños.get()),
            "Capacidad de los baños": int(
                100 if self.entry_capacidad_baños.get() == "" else self.entry_capacidad_baños.get()),
            "Precio de entrada": int(
                5 if self.entry_precio_entrada_baños.get() == "" else self.entry_precio_entrada_baños.get())
        }

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

    def crear_componentes_caracteristicas_cine(self):


        #Variables
        self.variable_opcion_eventos_especiales_cine = IntVar()
        self.variable_opcion_permitir_mascotas_cine = IntVar()


        self.lista_opciones_probabilidades_caracteristicas_cine = ["Atraccion de clientes", "Dias de promocion", "Eventos especiales", "Tipo de visita", "Temporadas de afluencia"]
        self.lista_opciones_precios_caracteristicas_cine = ["Precio de mantenimiento del cine", "Descuentos por promocion productos"]

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
        self.etiqueta_opcion_datos_precios_cine = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de precios:")
        self.etiqueta_opcion_datos_precios_cine.grid(row=6, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_datos_precios_cine = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_precios_caracteristicas_cine)
        self.opcion_datos_precios_cine.grid(row=6, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_datos_precios_cine = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_precios_cine(), nombre_boton="Cargar datos")
        self.boton_cargar_datos_precios_cine.grid(row=6, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")


        #Opciones
        self.opcion_eventos_especiales_cine = LtkCheckBoxFill(self.frame_caracteristicas, texto="Eventos especiales", variable=self.variable_opcion_eventos_especiales_cine)
        self.opcion_eventos_especiales_cine.grid(row=7, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_permitir_mascotas = LtkCheckBoxFill(self.frame_caracteristicas, texto="Permitir mascotas", variable=self.variable_opcion_permitir_mascotas_cine)
        self.opcion_permitir_mascotas.grid(row=8, column=0, padx=(10,10), pady=(5, 2), sticky="w")


        self.boton_guardar_datos_generales = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.guardar_datos_cine(), nombre_boton="Guardar datos")
        self.boton_guardar_datos_generales.grid(row=9, column=0, padx=(20,20), pady=(50, 20), sticky="nsew", columnspan=4)

    def crear_componentes_salas_cine(self):

        self.opciones_lineas_espera_salas = ["Espera en sala de cine", "Tiempo de limpieza entre peliculas", "Tiempo de salida de sala", "Tiempo de entrada de sala"]
        self.opciones_probabilidades_salas = ["Fallos en el sistema de sala"]
        self.opcion_datos_costos_sala = ["Costo de limpieza de la sala", "Costo de operacion de sala", "Costo de mantenimiento de sala"]


        self.resetear_frame_caracteristicas()

        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)

        self.etiqueta_titulo_salas_cine = LtkLabel(self.frame_caracteristicas, texto="Salas de cine")
        self.etiqueta_titulo_salas_cine.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_salas_cine.grid(row=0, column=0, columnspan=3, pady=(5, 10))

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

        #Costos
        self.etiqueta_opcion_datos_costos_sala = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de costos:")
        self.etiqueta_opcion_datos_costos_sala.grid(row=7, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_datos_costos_sala_cine = LtkComboBoxLine(self.frame_caracteristicas, self.opcion_datos_costos_sala)
        self.opcion_datos_costos_sala_cine.grid(row=7, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)


        self.boton_datos_costos_sala = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_costos_sala(), nombre_boton="Cargar datos")
        self.boton_datos_costos_sala.grid(row=7, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")


        self.boton_guardar_datos_salas = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.guardar_datos_sala(), nombre_boton="Guardar datos")
        self.boton_guardar_datos_salas.grid(row=8, column=0, padx=(20,20), pady=(50, 20),sticky="nsew", columnspan=4)


    def crear_componentes_dulceria(self):


        self.lista_opciones_probabilidades_dulceria = ["Demanda de productos", "Fallos en el sistema de dulceria", "Tipo de productos (inventario)", ]
        self.lista_opciones_tiempo_espera_dulceria = ["Tiempo de servicio de dulceria", "Tiempo de espera en la dulceria"]
        self.lista_opciones_precios = ["Precio de productos", "Descuentos promocion", "Costo de mantenimineto y limpieza", "Costos de operacion"]


        self.resetear_frame_caracteristicas()

        self.frame_caracteristicas.columnconfigure(1, weight=1)

        self.etiqueta_titulo_dulceria = LtkLabel(self.frame_caracteristicas, texto="Dulceria")
        self.etiqueta_titulo_dulceria.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_dulceria.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.etiqueta_cantidad_cajas_dulceria = LtkLabel(self.frame_caracteristicas, texto="Cantidad de cajas(empleado por caja):")
        self.etiqueta_cantidad_cajas_dulceria.grid(row=1, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_cajas_dulceria = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_cajas_dulceria.grid(row=1, column=1, padx=(5,10), pady=(5, 15), sticky="nsew",columnspan=2)

        self.etiqueta_sueldo_empleados_cine = LtkLabel(self.frame_caracteristicas, texto="Sueldo de empleados de la dulceria:")
        self.etiqueta_sueldo_empleados_cine.grid(row=2, column=0, padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_sueldo_empleados_cine = LtkEntryLine(self.frame_caracteristicas)
        self.entry_sueldo_empleados_cine.grid(row=2, column=1, padx=(5,10), pady=(5, 15), sticky="nsew",columnspan=2)

        self.etiqueta_rendimiento_de_empleados_dulceria = LtkLabel(self.frame_caracteristicas, texto="Rendimiento de empleados de la dulceria:")
        self.etiqueta_rendimiento_de_empleados_dulceria.grid(row=3, column=0, padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_rendimiento_de_empleados_dulceria = LtkEntryLine(self.frame_caracteristicas)
        self.entry_rendimiento_de_empleados_dulceria.grid(row=3, column=1, padx=(5,10), pady=(5, 15), sticky="nsew",columnspan=2)

        self.etiqueta_probabilidad_compra_dulceria = LtkLabel(self.frame_caracteristicas, texto="Probabilidad de compra de productos:")
        self.etiqueta_probabilidad_compra_dulceria.grid(row=4, column=0, padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_probabilidad_compra_dulceria = LtkEntryLine(self.frame_caracteristicas)
        self.entry_probabilidad_compra_dulceria.grid(row=4, column=1, padx=(5,10), pady=(5, 15), sticky="nsew",columnspan=2)

        #Datos historicos

        #Probabilidades
        self.etiqueta_opcion_datos_probabilidades_dulceria = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de probabilidades:")
        self.etiqueta_opcion_datos_probabilidades_dulceria.grid(row=5, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_datos_probabilidades_dulceria = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_probabilidades_dulceria)
        self.opcion_datos_probabilidades_dulceria.grid(row=5, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_datos_probabilidades_dulceria = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_probabilidades_dulceria(), nombre_boton="Cargar datos")
        self.boton_cargar_datos_probabilidades_dulceria.grid(row=5, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")

        #Tiempo de espera
        self.etiqueta_opcion_datos_tiempo_espera_dulceria = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de tiempo de espera:")
        self.etiqueta_opcion_datos_tiempo_espera_dulceria.grid(row=6, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_datos_tiempo_espera_dulceria = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_tiempo_espera_dulceria)
        self.opcion_datos_tiempo_espera_dulceria.grid(row=6, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_datos_tiempo_espera_dulceria = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_tiempo_espera_dulceria(), nombre_boton="Cargar datos")
        self.boton_cargar_datos_tiempo_espera_dulceria.grid(row=6, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")

        #Precios
        self.etiqueta_opcion_datos_precios_dulceria = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de precios:")
        self.etiqueta_opcion_datos_precios_dulceria.grid(row=7, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_datos_precios_dulceria = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_precios)
        self.opcion_datos_precios_dulceria.grid(row=7, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_datos_precios_dulceria = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_precios_dulceria(), nombre_boton="Cargar datos")
        self.boton_cargar_datos_precios_dulceria.grid(row=7, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")

        self.boton_guardar_datos_dulceria = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.guardar_datos_dulceria(), nombre_boton="Guardar datos")
        self.boton_guardar_datos_dulceria.grid(row=8, column=0, padx=(20,20), pady=(50, 20), sticky="nsew", columnspan=4)


    def crear_componentes_taquilla(self):

        self.lista_opciones_probabilidad_taquilla = ["Demanda de entradas", "Fallos de sistema de taquilla"]
        self.lista_opciones_tiempo_espera_taquilla = ["Tiempo de espera en la taquilla", "Tiempo de servicio en la taquilla"]
        self.lista_opciones_precios_taquilla = ["Precios de entradas", "Descuentos por promocion o dias especiales", "Costos de mantenimieto y limpieza"]
        self.lista_opciones_configuracion_peliculas = ["Clasificacion de peliculas", "Duracion de peliculas", "Tipo de peliculas", "Precio de peliculas"]

        self.resetear_frame_caracteristicas()

        self.frame_caracteristicas.columnconfigure(1, weight=1)

        self.etiqueta_titulo_taquilla = LtkLabel(self.frame_caracteristicas, texto="Taquilla")
        self.etiqueta_titulo_taquilla.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_taquilla.grid(row=0, column=0, columnspan=2, pady=(5, 10))


        self.etiqueta_cantidad_cajas_taquilla = LtkLabel(self.frame_caracteristicas, texto="Cantidad de cajas (empleado por caja):")
        self.etiqueta_cantidad_cajas_taquilla.grid(row=1, column=0, padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_cantidad_cajas_taquilla = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_cajas_taquilla.grid(row=1, column=1, padx=(5,10), pady=(5, 15), sticky="nsew",columnspan=2)

        self.etiqueta_sueldo_empleado_taquilla = LtkLabel(self.frame_caracteristicas, texto="Sueldo de empleados de la taquilla:")
        self.etiqueta_sueldo_empleado_taquilla.grid(row=2, column=0, padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_sueldo_empleado_taquilla = LtkEntryLine(self.frame_caracteristicas)
        self.entry_sueldo_empleado_taquilla.grid(row=2, column=1, padx=(5,10), pady=(5, 15), sticky="nsew",columnspan=2)

        self.etiqueta_rendimiento_empleados_taquilla = LtkLabel(self.frame_caracteristicas, texto="Rendimiento de empleados de la taquilla:")
        self.etiqueta_rendimiento_empleados_taquilla.grid(row=3, column=0, padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_rendimiento_empleados_taquilla = LtkEntryLine(self.frame_caracteristicas)
        self.entry_rendimiento_empleados_taquilla.grid(row=3, column=1, padx=(5,10), pady=(5, 15), sticky="nsew",columnspan=2)

        #Datos historicos

        #Probabilidades
        self.etiqueta_opcion_datos_probabilidades_taquilla = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de probabilidades:")
        self.etiqueta_opcion_datos_probabilidades_taquilla.grid(row=4, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_datos_probabilidades_taquilla = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_probabilidad_taquilla)
        self.opcion_datos_probabilidades_taquilla.grid(row=4, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_datos_probabilidades_taquilla = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_probabilidades_taquilla(), nombre_boton="Cargar datos")
        self.boton_cargar_datos_probabilidades_taquilla.grid(row=4, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")

        #Tiempo de espera
        self.etiqueta_opcion_datos_tiempo_espera_taquilla = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de tiempo de espera:")
        self.etiqueta_opcion_datos_tiempo_espera_taquilla.grid(row=5, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_datos_tiempo_espera_taquilla = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_tiempo_espera_taquilla)
        self.opcion_datos_tiempo_espera_taquilla.grid(row=5, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_datos_tiempo_espera_taquilla = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_tiempo_espera_taquilla(), nombre_boton="Cargar datos")
        self.boton_cargar_datos_tiempo_espera_taquilla.grid(row=5, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")

        #Precios
        self.etiqueta_opcion_datos_precios_taquilla = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de precios:")
        self.etiqueta_opcion_datos_precios_taquilla.grid(row=6, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_datos_precios_taquilla = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_precios_taquilla)
        self.opcion_datos_precios_taquilla.grid(row=6, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_datos_precios_taquilla = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_precios_taquilla(), nombre_boton="Cargar datos")
        self.boton_cargar_datos_precios_taquilla.grid(row=6, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")

        #Configuracion de peliculas
        self.etiqueta_opcion_datos_configuracion_peliculas = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de configuracion de peliculas:")
        self.etiqueta_opcion_datos_configuracion_peliculas.grid(row=7, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_datos_configuracion_peliculas = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_configuracion_peliculas)
        self.opcion_datos_configuracion_peliculas.grid(row=7, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_cargar_datos_configuracion_peliculas = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_configuracion_peliculas(), nombre_boton="Cargar datos")
        self.boton_cargar_datos_configuracion_peliculas.grid(row=7, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")

        self.boton_guardar_datos_taquilla = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.guardar_datos_taquilla(), nombre_boton="Guardar datos")
        self.boton_guardar_datos_taquilla.grid(row=8, column=0, padx=(20,20), pady=(50, 20), sticky="nsew", columnspan=4)


    def crear_componentes_baños(self):

        self.resetear_frame_caracteristicas()

        self.lista_opciones_de_baños = ["Tiempo de espera en fila", "Tiempo de servicio en baños", "Fallos en el sistema de baños", "Demanda de uso", "Costos de mantenimineto"]

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

        self.etiqueta_precio_entrada_baños = LtkLabel(self.frame_caracteristicas, texto="Precio de entrada a los baños:")
        self.etiqueta_precio_entrada_baños.grid(row=3, column=0, padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_precio_entrada_baños = LtkEntryLine(self.frame_caracteristicas)
        self.entry_precio_entrada_baños.grid(row=3, column=1, padx=(5,10), pady=(5, 15), sticky="nsew",columnspan=2)

        #Datos historicos
        self.etiqueta_opcion_datos_baños = LtkLabel(self.frame_caracteristicas, texto="Seleccionar configuracion: ")
        self.etiqueta_opcion_datos_baños.grid(row=4, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.opcion_datos_baños = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_de_baños)
        self.opcion_datos_baños.grid(row=4, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.boton_opcion_datos_baños = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.cargar_datos_baños(), nombre_boton="Cargar datos")
        self.boton_opcion_datos_baños.grid(row=4, column=3, padx=(5,10), pady=(5, 5), sticky="nsew")

        self.boton_guardar_datos_baños = LtkButtonFill(self.frame_caracteristicas,funcion=lambda: self.guardar_datos_baños(), nombre_boton="Guardar datos")
        self.boton_guardar_datos_baños.grid(row=5, column=0,padx=(20,20), pady=(50, 20), sticky="nsew", columnspan=4)

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

        if self.opcion_datos_precios_cine.get() == "Precio de mantenimiento del cine":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Precio de mantenimiento del cine")
            self.crear_ventana_emergente("Precio de mantenimiento del cine", path)

        elif self.opcion_datos_precios_cine.get() == "Descuentos por promocion productos":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Descuentos por promocion productos")
            self.crear_ventana_emergente("Descuentos por promocion productos", path)

    def cargar_datos_probabilidades_cine(self):

        if self.opcion_datos_historicos_probabilidades_cine.get() == "Atraccion de clientes":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Atraccion de clientes")
            self.crear_ventana_emergente("Atraccion de clientes", path)

        elif self.opcion_datos_historicos_probabilidades_cine.get() == "Dias de promocion":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Dias de promocion")
            self.crear_ventana_emergente("Dias de promocion", path)

        elif self.opcion_datos_historicos_probabilidades_cine.get() == "Eventos especiales":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Eventos especiales")
            self.crear_ventana_emergente("Eventos especiales", path)

        elif self.opcion_datos_historicos_probabilidades_cine.get() == "Tipo de visita":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Tipo de visita")
            self.crear_ventana_emergente("Tipo de visita", path)

        elif self.opcion_datos_historicos_probabilidades_cine.get() == "Temporadas de afluencia":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Temporadas de afluencia")
            self.crear_ventana_emergente("Tipo de peliculas", path)


    #Salas de cine
    def cargar_datos_espera_sala(self):

        if self.opcion_datos_espera_sala.get() == "Espera en sala de cine":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Espera en sala de cine")
            self.crear_ventana_emergente("Espera en sala de cine", path)

        elif self.opcion_datos_espera_sala.get() == "Tiempo de limpieza entre peliculas":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Tiempo de limpieza entre peliculas")
            self.crear_ventana_emergente("Tiempo de limpieza entre peliculas", path)

        elif self.opcion_datos_espera_sala.get() == "Tiempo de salida de sala":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Tiempo de salida de sala")
            self.crear_ventana_emergente("Tiempo de salida de sala", path)

        elif self.opcion_datos_espera_sala.get() == "Tiempo de entrada de sala":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Tiempo de entrada de sala")
            self.crear_ventana_emergente("Tiempo de entrada de sala", path)

    def cargar_datos_probabilidades_sala(self):

        if self.opcion_datos_probabilidades_sala.get() == "Fallos en el sistema de sala":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Fallos en el sistema de sala")
            self.crear_ventana_emergente("Fallos en el sistema de sala", path)

    def cargar_datos_costos_sala(self):

        if self.opcion_datos_costos_sala_cine.get() == "Costo de mantenimiento de sala":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Costo de mantenimiento de sala")
            self.crear_ventana_emergente("Costo de mantenimiento de sala", path)

        elif self.opcion_datos_costos_sala_cine.get() == "Costo de operacion de sala":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Costo de operacion de sala")
            self.crear_ventana_emergente("Costo de operacion de sala", path)

        elif self.opcion_datos_costos_sala_cine.get() == "Costo de limpieza de la sala":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Costo de limpieza de sala")
            self.crear_ventana_emergente("Costo de limpieza de sala", path)

    #Dulceria
    def cargar_datos_probabilidades_dulceria(self):

        if self.opcion_datos_probabilidades_dulceria.get() == "Demanda de productos":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Demanda de productos")
            self.crear_ventana_emergente("Demanda de productos", path)

        elif self.opcion_datos_probabilidades_dulceria.get() == "Fallos en el sistema de dulceria":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Fallos en el sistema de dulceria")
            self.crear_ventana_emergente("Fallos en el sistema de dulceria", path)

        elif self.opcion_datos_probabilidades_dulceria.get() == "Tipo de productos (inventario)":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Tipo de productos (inventario)")
            self.crear_ventana_emergente("Tipo de productos (inventario)", path)

    def cargar_datos_tiempo_espera_dulceria(self):

        if self.opcion_datos_tiempo_espera_dulceria.get() == "Tiempo de servicio de dulceria":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Tiempo de servicio de dulceria")
            self.crear_ventana_emergente("Tiempo de servicio de dulceria", path)

        elif self.opcion_datos_tiempo_espera_dulceria.get() == "Tiempo de espera en la dulceria":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Tiempo de espera en la dulceria")
            self.crear_ventana_emergente("Tiempo de espera en la dulceria", path)

    def cargar_datos_precios_dulceria(self):

        if self.opcion_datos_precios_dulceria.get() == "Precio de productos":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Precio de productos")
            self.crear_ventana_emergente("Precio de productos", path)

        elif self.opcion_datos_precios_dulceria.get() == "Descuentos promocion":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Descuentos promocion dulceria")
            self.crear_ventana_emergente("Descuentos promocion", path)

        elif self.opcion_datos_precios_dulceria.get() == "Costo de mantenimineto y limpieza":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Costo de mantenimineto y limpieza dulceria")
            self.crear_ventana_emergente("Costo de mantenimineto y limpieza", path)

        elif self.opcion_datos_precios_dulceria.get() == "Costos de operacion":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Costos de operacion dulceria")
            self.crear_ventana_emergente("Costos de operacion", path)


    #Taquilla
    def cargar_datos_probabilidades_taquilla(self):

        if self.opcion_datos_probabilidades_taquilla.get() == "Demanda de entradas":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Demanda de entradas")
            self.crear_ventana_emergente("Demanda de entradas", path)

        elif self.opcion_datos_probabilidades_taquilla.get() == "Fallos de sistema de taquilla":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Fallos de sistema de taquilla")
            self.crear_ventana_emergente("Fallos de sistema de taquilla", path)

    def cargar_datos_tiempo_espera_taquilla(self):

        if self.opcion_datos_tiempo_espera_taquilla.get() == "Tiempo de espera en la taquilla":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Tiempo de espera en la taquilla")
            self.crear_ventana_emergente("Tiempo de espera en la taquilla", path)

        elif self.opcion_datos_tiempo_espera_taquilla.get() == "Tiempo de servicio en la taquilla":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Tiempo de servicio en la taquilla")
            self.crear_ventana_emergente("Tiempo de servicio en la taquilla", path)

    def cargar_datos_precios_taquilla(self):

        if self.opcion_datos_precios_taquilla.get() == "Precios de entradas":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Precios de entradas")
            self.crear_ventana_emergente("Precios de entradas", path)

        elif self.opcion_datos_precios_taquilla.get() == "Descuentos por promocion o dias especiales":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Descuentos por promocion o dias especiales taquilla")
            self.crear_ventana_emergente("Descuentos por promocion o dias especiales", path)

        elif self.opcion_datos_precios_taquilla.get() == "Costos de mantenimieto y limpieza":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Costos de mantenimieto y limpieza taquilla")
            self.crear_ventana_emergente("Costos de mantenimieto y limpieza", path)

    def cargar_datos_configuracion_peliculas(self):

        if self.opcion_datos_configuracion_peliculas.get() == "Clasificacion de peliculas":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Clasificacion de peliculas")
            self.crear_ventana_emergente("Clasificacion de peliculas", path)

        elif self.opcion_datos_configuracion_peliculas.get() == "Duracion de peliculas":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Duracion de peliculas")
            self.crear_ventana_emergente("Duracion de peliculas", path)

        elif self.opcion_datos_configuracion_peliculas.get() == "Tipo de peliculas":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Tipo de peliculas")
            self.crear_ventana_emergente("Tipo de peliculas", path)

        elif self.opcion_datos_configuracion_peliculas.get() == "Precio de peliculas":
            path = os.path.join(self.ruta_ventana, "datos\\precios\\Precio de peliculas")
            self.crear_ventana_emergente("Precio de peliculas", path)

    #Baños
    def cargar_datos_baños(self):

        if self.opcion_datos_baños.get() == "Tiempo de espera en fila":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Tiempo de espera en fila de baño")
            self.crear_ventana_emergente("Tiempo de espera en fila", path)

        elif self.opcion_datos_baños.get() == "Tiempo de servicio en baños":
            path = os.path.join(self.ruta_ventana, "datos\\lineas de espera\\Tiempo de servicio en baños")
            self.crear_ventana_emergente("Tiempo de servicio en baños", path)

        elif self.opcion_datos_baños.get() == "Fallos en el sistema de baños":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Fallos en el sistema de baños")
            self.crear_ventana_emergente("Fallos en el sistema de baños", path)

        elif self.opcion_datos_baños.get() == "Demanda de uso":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Demanda de uso")
            self.crear_ventana_emergente("Demanda de uso", path)

        elif self.opcion_datos_baños.get() == "Costos de mantenimineto":
            path = os.path.join(self.ruta_ventana, "datos\\probabilidades\\Costos de mantenimineto baños")
            self.crear_ventana_emergente("Costos de mantenimineto", path)




    #Guardar datos
    def guardar_datos_cine(self):
        self.general = {
            "Capacidad del cine": int(100 if self.entry_capacidad_cine.get() == "" else self.entry_capacidad_cine.get()),
            "Horario": {
                "Entrada": "08:00" if self.entry_horario_inicio.get() == "" else self.entry_horario_inicio.get(),
                "Cierre": "22:00" if self.entry_horario_cierre.get() == "" else self.entry_horario_cierre.get()
            },
            "Eventos especiales": self.variable_opcion_eventos_especiales_cine.get(),
            "Permitir mascotas": self.variable_opcion_permitir_mascotas_cine.get(),
        }
        messagebox.showinfo("Se guardo", "Se guardo la configuracion local ")
    def guardar_datos_sala(self):
        self.salas_de_cine = {
            "Cantidad de salas": int(5 if self.entry_cantidad_salas.get() == "" else self.entry_cantidad_salas.get()),
            "Capacidad de las salas": int(100 if self.entry_capacidad_salas.get() == "" else self.entry_capacidad_salas.get()),
            "Cantidad de empleados por sala": int(2 if self.entry_cantidad_empleados_sala.get() == "" else self.entry_cantidad_empleados_sala.get()),
            "Sueldo de empleados por sala": int(1000 if self.entry_sueldo_empleados_sala.get() == "" else self.entry_sueldo_empleados_sala.get())
        }
        messagebox.showinfo("Se guardo", "Se guardo la configuracion local ")


    def guardar_datos_dulceria(self):
        self.dulceria = {
            "Cantidad de cajas": int(5 if self.entry_cantidad_cajas_dulceria.get() == "" else self.entry_cantidad_cajas_dulceria.get()),
            "Sueldo de empleados": int(1000 if self.entry_sueldo_empleados_cine.get() == "" else self.entry_sueldo_empleados_cine.get()),
            "Rendimiento de empleados": int(100 if self.entry_rendimiento_de_empleados_dulceria.get() == "" else self.entry_rendimiento_de_empleados_dulceria.get()),
            "Probabilidad de compra de productos": int(100 if self.entry_probabilidad_compra_dulceria.get() == "" else self.entry_probabilidad_compra_dulceria.get())
        }
        messagebox.showinfo("Se guardo", "Se guardo la configuracion local ")

    def guardar_datos_taquilla(self):
        self.taquilla = {
            "Cantidad de cajas": int(5 if self.entry_cantidad_cajas_taquilla.get() == "" else self.entry_cantidad_cajas_taquilla.get()),
            "Sueldo de empleados": int(1000 if self.entry_sueldo_empleado_taquilla.get() == "" else self.entry_sueldo_empleado_taquilla.get()),
            "Rendimiento de empleados": int(100 if self.entry_rendimiento_empleados_taquilla.get() == "" else self.entry_rendimiento_empleados_taquilla.get())
        }
        messagebox.showinfo("Se guardo", "Se guardo la configuracion local ")

    def guardar_datos_baños(self):
        self.baños = {
            "Cantidad de baños": int(5 if self.entry_cantidad_baños.get() == "" else self.entry_cantidad_baños.get()),
            "Capacidad de los baños": int(100 if self.entry_capacidad_baños.get() == "" else self.entry_capacidad_baños.get()),
            "Precio de entrada": int(5 if self.entry_precio_entrada_baños.get() == "" else self.entry_precio_entrada_baños.get())
        }
        messagebox.showinfo("Se guardo", "Se guardo la configuracion local ")



