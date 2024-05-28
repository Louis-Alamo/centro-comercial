import os
import json
from customtkinter import *
from tkinter import messagebox

from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine
from componentes_graficos.LtkEntry import LtkEntryLine, LtkEntryFill
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkComboBox import LtkComboBoxLine
from componentes_graficos.LtkTreeView import LtkFileInputTreeView

class ConfiguracionLibreria:

    def __init__(self):
        self.ruta_ventana = os.path.dirname(os.path.abspath(__file__))

        self.ventana = CTkToplevel()
        self.ventana.title("Configuración de la librería")

        self.ventana.grid_columnconfigure(1, weight=1)
        self.ventana.grid_rowconfigure(1, weight=1)

        self.crear_componentes()
        self.ventana.mainloop()

    def crear_componentes(self):
        self.frame_clasificacion_configuracion = CTkFrame(self.ventana)
        self.frame_clasificacion_configuracion.grid(row=1, column=0, padx=(10, 5), pady=(10, 10), sticky="ns")

        self.frame_clasificacion_configuracion.columnconfigure(0, weight=1)
        self.crear_botones_clasificacion_caracteristicas_libreria()

        # Frame de características
        self.frame_caracteristicas = CTkFrame(self.ventana)
        self.frame_caracteristicas.grid(row=1, column=1, padx=(5, 10), pady=(10, 10), sticky="nsew")

        self.frame_caracteristicas.columnconfigure(0, weight=1)
        self.frame_caracteristicas.columnconfigure(1, weight=1)

        # Etiqueta de título principal
        self.etiqueta_titulo_principal = LtkLabel(self.ventana, texto="Configuración de la librería")
        self.etiqueta_titulo_principal.configure(font=('Poppins', 20, "bold"))
        self.etiqueta_titulo_principal.grid(row=0, column=0, pady=(10, 20), sticky="ew", columnspan=2)
        self.etiqueta_titulo_principal.columnconfigure(0, weight=1)

        self.inicializar_componentes()

        self.boton_cerrar = LtkButtonFill(self.ventana, funcion=lambda: self.ventana.destroy(), nombre_boton="Cerrar")
        self.boton_cerrar.grid(row=2, column=0, columnspan=4, padx=(10, 10), pady=(10, 20), sticky="w")

        self.boton_guardar = LtkButtonFill(self.ventana, funcion=lambda: self.guardar_informacion(), nombre_boton="Guardar")
        self.boton_guardar.grid(row=2, column=1, columnspan=4, padx=(10, 10), pady=(10, 20), sticky="nsew")

    def crear_botones_clasificacion_caracteristicas_libreria(self):
        self.boton_caracteristicas_principales = LtkButtonLine(self.frame_clasificacion_configuracion, funcion=lambda: self.caracteristicas_libreria(), nombre_boton="Opciones generales")
        self.boton_caracteristicas_principales.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")

        self.boton_crear_componentes_edificio_caja = LtkButtonLine(self.frame_clasificacion_configuracion, funcion=lambda: self.crear_componentes_edificio_caja(), nombre_boton="Opciones de caja")
        self.boton_crear_componentes_edificio_caja.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")

    def resetear_frame_caracteristicas(self):
        for widget in self.frame_caracteristicas.winfo_children():
            widget.grid_remove()

    def inicializar_componentes(self):
        self.crear_componentes_edificio_caja()
        self.caracteristicas_libreria()

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

    def caracteristicas_libreria(self):
        self.lista_opciones_probabilidad_general = ["Cantidad libros a comprar", "Temporadas de afluencia", "Tiempo de llegada cliente"]
        self.lista_opciones_precio_general = ["Costo de mantenimiento de librería", "Descuentos por promoción", "Días de promoción"]

        self.resetear_frame_caracteristicas()
        self.frame_caracteristicas.columnconfigure(1, weight=1)

        self.etiqueta_titulo_caracteristicas_libreria = LtkLabel(self.frame_caracteristicas, texto="Características de la librería")
        self.etiqueta_titulo_caracteristicas_libreria.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas_libreria.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.etiqueta_cantidad_maxima_personas = LtkLabel(self.frame_caracteristicas, texto="Cantidad máxima de personas:")
        self.etiqueta_cantidad_maxima_personas.grid(row=1, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_cantidad_maxima_personas = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_maxima_personas.grid(row=1, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.etiqueta_horario = LtkLabel(self.frame_caracteristicas, texto="Horario:")
        self.etiqueta_horario.grid(row=3, column=0, padx=(10, 10), pady=(5, 10), sticky="w")

        self.entry_horario_inicio = LtkEntryLine(self.frame_caracteristicas, "Hora inicio")
        self.entry_horario_inicio.grid(row=3, column=1, padx=(5, 10), pady=(5, 15), sticky="nsew")
        self.entry_horario_cierre = LtkEntryLine(self.frame_caracteristicas, "Hora cierre")
        self.entry_horario_cierre.grid(row=3, column=2, padx=(5, 10), pady=(5, 15), sticky="nsew")

        # Datos históricos

        # Probabilidades
        self.etiqueta_opcion_probabilidades_general = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de probabilidades:")
        self.etiqueta_opcion_probabilidades_general.grid(row=5, column=0, padx=(10, 10), pady=(5, 2), sticky="w")

        self.opcion_probabilidades_general = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_probabilidad_general)
        self.opcion_probabilidades_general.grid(row=5, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.boton_cargar_probabilidades_general = LtkButtonFill(self.frame_caracteristicas, funcion=lambda: self.cargar_datos_general(), nombre_boton="Cargar datos")
        self.boton_cargar_probabilidades_general.grid(row=5, column=3, padx=(5, 10), pady=(5, 5), sticky="nsew")

        # Precio
        self.etiqueta_opcion_precio_general = LtkLabel(self.frame_caracteristicas, texto="Seleccionar datos de precio:")
        self.etiqueta_opcion_precio_general.grid(row=6, column=0, padx=(10, 10), pady=(5, 2), sticky="w")

        self.opcion_precio_general = LtkComboBoxLine(self.frame_caracteristicas, self.lista_opciones_precio_general)
        self.opcion_precio_general.grid(row=6, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.boton_cargar_precio_general = LtkButtonFill(self.frame_caracteristicas, funcion=lambda: self.cargar_datos_general(), nombre_boton="Cargar datos")
        self.boton_cargar_precio_general.grid(row=6, column=3, padx=(5, 10), pady=(5, 5), sticky="nsew")



    def crear_componentes_edificio_caja(self):
        self.resetear_frame_caracteristicas()
        self.frame_caracteristicas.columnconfigure(1, weight=1)

        self.etiqueta_titulo_caja = LtkLabel(self.frame_caracteristicas, texto="Opciones de caja")
        self.etiqueta_titulo_caja.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caja.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.etiqueta_cantidad_cajas = LtkLabel(self.frame_caracteristicas, texto="Cantidad de cajas:")
        self.etiqueta_cantidad_cajas.grid(row=1, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_cantidad_cajas = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_cajas.grid(row=1, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.etiqueta_sueldo_empleado = LtkLabel(self.frame_caracteristicas, texto="Sueldo por empleado:")
        self.etiqueta_sueldo_empleado.grid(row=2, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_sueldo_empleado = LtkEntryLine(self.frame_caracteristicas)
        self.entry_sueldo_empleado.grid(row=2, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.etiqueta_rendimiento_empleado = LtkLabel(self.frame_caracteristicas, texto="Rendimiento por empleado:")
        self.etiqueta_rendimiento_empleado.grid(row=3, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_rendimiento_empleado = LtkEntryLine(self.frame_caracteristicas)
        self.entry_rendimiento_empleado.grid(row=3, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

    def cargar_datos_general(self):
        if self.opcion_probabilidades_general.get() != "":
            datos = self.obtener_datos_archivo("historicos", self.opcion_probabilidades_general.get())
            self.arbol_entrada_datos_general.llenar_treeview(datos)
            return

        if self.opcion_precio_general.get() != "":
            datos = self.obtener_datos_archivo("historicos", self.opcion_precio_general.get())
            self.arbol_entrada_datos_general.llenar_treeview(datos)

    def obtener_datos_archivo(self, carpeta, archivo):
        path = os.path.join(self.ruta_ventana, carpeta, archivo + ".json")

        if not os.path.exists(path):
            messagebox.showwarning("Advertencia", f"El archivo {archivo} no existe")
            return []

        try:
            with open(path, 'r') as archivo:
                datos = json.load(archivo)
            return datos
        except json.JSONDecodeError:
            messagebox.showerror("Error", f"Error al decodificar el archivo {archivo}")
            return []

    def guardar_informacion(self):
        # Recolectar datos de entrada
        self.configuracion_caja["Cantidad de cajas"] = int(self.entry_cantidad_cajas.get())
        self.configuracion_caja["Pago por empleado"] = int(self.entry_sueldo_empleado.get())
        self.configuracion_caja["Rendimiento por empleado"] = int(self.entry_rendimiento_empleado.get())

        self.datos_generales["capacidad_maxima_personas"] = int(self.entry_cantidad_maxima_personas.get())
        self.datos_generales["horario_inicio"] = self.entry_horario_inicio.get()
        self.datos_generales["horario_cierre"] = self.entry_horario_cierre.get()

        try:
            with open(os.path.join(self.ruta_ventana, "configuracion_libreria.json"), 'w') as archivo_config:
                json.dump({"configuracion_caja": self.configuracion_caja, "datos_generales": self.datos_generales}, archivo_config, indent=4)

            messagebox.showinfo("Éxito", "Configuración guardada exitosamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar la configuración: {str(e)}")

if __name__ == "__main__":
    ConfiguracionLibreria()
