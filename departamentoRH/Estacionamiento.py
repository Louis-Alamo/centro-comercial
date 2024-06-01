import os
import json
from tkinter import messagebox, simpledialog, IntVar, StringVar
import tkinter.ttk as ttk
import customtkinter as ctk
from customtkinter import CTk, CTkFrame, CTkButton, CTkToplevel

from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkLabel import LtkLabel

class TablaPopupTiempos:
    def __init__(self, ventana, titulo, ruta_archivo):
        self.top = CTkToplevel(ventana)
        self.top.title(titulo)
        self.top.transient(ventana)
        self.top.grab_set()

        self.ruta_archivo = ruta_archivo
        self.datos = self.cargar_datos()

        self.arbol = ttk.Treeview(self.top, columns=("Tiempo", "Probabilidad"), show="headings")
        self.arbol.heading("Tiempo", text="Tiempo (minutos)")
        self.arbol.heading("Probabilidad", text="Probabilidad")
        self.arbol.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.scrollbar = ttk.Scrollbar(self.top, orient="vertical", command=self.arbol.yview)
        self.arbol.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=3, sticky='ns')

        self.btn_agregar = CTkButton(self.top, text="Agregar", command=self.agregar_fila)
        self.btn_agregar.grid(row=1, column=0, pady=10)

        self.btn_editar = CTkButton(self.top, text="Editar", command=self.editar_fila)
        self.btn_editar.grid(row=1, column=1, pady=10)

        self.btn_eliminar = CTkButton(self.top, text="Eliminar", command=self.eliminar_fila)
        self.btn_eliminar.grid(row=1, column=2, pady=10)

        self.llenar_tabla()

    def cargar_datos(self):
        if os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, 'r') as archivo:
                return json.load(archivo)
        else:
            return []

    def guardar_datos(self):
        datos = [(self.arbol.item(item)['values'][0], self.arbol.item(item)['values'][1]) for item in self.arbol.get_children()]
        with open(self.ruta_archivo, 'w') as archivo:
            json.dump(datos, archivo, indent=4)

    def llenar_tabla(self):
        for item in self.datos:
            self.arbol.insert('', 'end', values=item)

    def agregar_fila(self):
        tiempo = simpledialog.askstring("Input", "Ingrese el tiempo (minutos):")
        probabilidad = simpledialog.askstring("Input", "Ingrese la probabilidad:")
        if tiempo and probabilidad:
            self.arbol.insert('', 'end', values=(tiempo, probabilidad))
            self.guardar_datos()

    def editar_fila(self):
        item_seleccionado = self.arbol.selection()
        if item_seleccionado:
            tiempo_actual, probabilidad_actual = self.arbol.item(item_seleccionado, 'values')
            nuevo_tiempo = simpledialog.askstring("Input", "Ingrese el tiempo (minutos):", initialvalue=tiempo_actual)
            nueva_probabilidad = simpledialog.askstring("Input", "Ingrese la probabilidad:", initialvalue=probabilidad_actual)
            if nuevo_tiempo and nueva_probabilidad:
                self.arbol.item(item_seleccionado, values=(nuevo_tiempo, nueva_probabilidad))
                self.guardar_datos()

    def eliminar_fila(self):
        item_seleccionado = self.arbol.selection()
        if item_seleccionado:
            self.arbol.delete(item_seleccionado)
            self.guardar_datos()

class TablaFrecuenciaEntrada:
    def __init__(self, ventana, titulo, ruta_archivo):
        self.top = CTkToplevel(ventana)
        self.top.title(titulo)
        self.top.transient(ventana)
        self.top.grab_set()

        self.ruta_archivo = ruta_archivo
        self.datos = self.cargar_datos()

        self.arbol = ttk.Treeview(self.top, columns=("Intervalo", "Frecuencia"), show="headings")
        self.arbol.heading("Intervalo", text="Intervalo (minutos)")
        self.arbol.heading("Frecuencia", text="Frecuencia")
        self.arbol.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.scrollbar = ttk.Scrollbar(self.top, orient="vertical", command=self.arbol.yview)
        self.arbol.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=3, sticky='ns')

        self.btn_agregar = CTkButton(self.top, text="Agregar", command=self.agregar_fila)
        self.btn_agregar.grid(row=1, column=0, pady=10)

        self.btn_editar = CTkButton(self.top, text="Editar", command=self.editar_fila)
        self.btn_editar.grid(row=1, column=1, pady=10)

        self.btn_eliminar = CTkButton(self.top, text="Eliminar", command=self.eliminar_fila)
        self.btn_eliminar.grid(row=1, column=2, pady=10)

        self.llenar_tabla()

    def cargar_datos(self):
        if os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, 'r') as archivo:
                return json.load(archivo)
        else:
            return []

    def guardar_datos(self):
        datos = [(self.arbol.item(item)['values'][0], self.arbol.item(item)['values'][1]) for item in self.arbol.get_children()]
        with open(self.ruta_archivo, 'w') as archivo:
            json.dump(datos, archivo, indent=4)

    def llenar_tabla(self):
        for item in self.datos:
            self.arbol.insert('', 'end', values=item)

    def agregar_fila(self):
        intervalo = simpledialog.askstring("Input", "Ingrese el intervalo (minutos):")
        frecuencia = simpledialog.askstring("Input", "Ingrese la frecuencia:")
        if intervalo and frecuencia:
            self.arbol.insert('', 'end', values=(intervalo, frecuencia))
            self.guardar_datos()

    def editar_fila(self):
        item_seleccionado = self.arbol.selection()
        if item_seleccionado:
            intervalo_actual, frecuencia_actual = self.arbol.item(item_seleccionado, 'values')
            nuevo_intervalo = simpledialog.askstring("Input", "Ingrese el intervalo (minutos):", initialvalue=intervalo_actual)
            nueva_frecuencia = simpledialog.askstring("Input", "Ingrese la frecuencia:", initialvalue=frecuencia_actual)
            if nuevo_intervalo and nueva_frecuencia:
                self.arbol.item(item_seleccionado, values=(nuevo_intervalo, nueva_frecuencia))
                self.guardar_datos()

    def eliminar_fila(self):
        item_seleccionado = self.arbol.selection()
        if item_seleccionado:
            self.arbol.delete(item_seleccionado)
            self.guardar_datos()

class Estacionamiento:
    def __init__(self):
        self.ventana = ctk.CTk()
        self.archivo_configuracion = "configuracion_estacionamiento.json"
        self.archivo_tiempos_entrada = "tiempos_entrada.json"
        self.archivo_fila_entrada = "fila_entrada.json"
        self.archivo_frecuencia_mantenimiento = "frecuencia_mantenimiento.json"
        self.ventana.title("Estacionamiento")
        self.ventana.geometry("900x600+350+100")
        self.ventana.configure(bg="#FFFFFF")
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)
        self.ventana.rowconfigure(1, weight=1)

        self.ruta_ventana = os.path.dirname(os.path.abspath(__file__))

        self.frame_caracteristicas = ctk.CTkFrame(self.ventana)
        self.frame_caracteristicas.grid(row=1, column=1, sticky="nsew")
        self.ventana.columnconfigure(1, weight=25)
        self.ventana.rowconfigure(1, weight=2)
        self.frame_caracteristicas.columnconfigure(0, weight=1)

        frame_titulo = ctk.CTkFrame(self.ventana)
        frame_titulo.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)
        titulo = LtkLabel(frame_titulo, texto="Configuración de Estacionamiento")
        titulo.configure(font=('Poppins', 30, "bold"))
        titulo.grid(row=0, column=0, pady=(1, 1), sticky="nsew")
        frame_titulo.columnconfigure(0, weight=1)
        frame_titulo.rowconfigure(0, weight=1)

        frame_opciones = ctk.CTkFrame(self.ventana)
        frame_opciones.grid(row=1, column=0, pady=(10, 10))
        self.ventana.columnconfigure(0, weight=2)
        self.ventana.rowconfigure(1, weight=1)

        boton_opciones = LtkButtonLine(frame_opciones, self.personal, "Personal")
        boton_opciones.grid(row=0, column=0, padx=(5, 5), pady=(5, 5))
        boton_costos = LtkButtonLine(frame_opciones, self.costos, "Costos")
        boton_costos.grid(row=1, column=0, padx=(5, 5), pady=(5, 5))
        boton_horarios = LtkButtonLine(frame_opciones, self.horarios, "Horarios")
        boton_horarios.grid(row=2, column=0, padx=(5, 5), pady=(5, 5))
        boton_fila_entrada = LtkButtonLine(frame_opciones, self.fila_entrada, "Fila de Entrada")
        boton_fila_entrada.grid(row=3, column=0, padx=(5, 5), pady=(5, 5))
        boton_tiempos_entrada = LtkButtonLine(frame_opciones, self.tiempos_entrada, "Tiempos de Entrada")
        boton_tiempos_entrada.grid(row=4, column=0, padx=(5, 5), pady=(5, 5))
        boton_precios = LtkButtonLine(frame_opciones, self.precios, "Precios")
        boton_precios.grid(row=5, column=0, padx=(5, 5), pady=(5, 5))

        frame_guardar = ctk.CTkFrame(self.ventana)
        frame_guardar.grid(row=2, column=0, columnspan=2, sticky="nsew")
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(2, weight=1)
        frame_guardar.columnconfigure(0, weight=1)
        frame_guardar.rowconfigure(0, weight=1)

        boton_guardar_datos = LtkButtonFill(frame_guardar, self.guardar_y_cerrar, "Guardar Datos")
        boton_guardar_datos.grid(row=1, column=0, padx=100, pady=40, sticky="nsew")
        frame_guardar.columnconfigure(0, weight=1)
        frame_guardar.rowconfigure(1, weight=1)

        self.ventana.protocol("WM_DELETE_WINDOW", self.guardar_y_cerrar)
        self.ventana.mainloop()

    def resetear_frame_caracteristicas(self):
        for widget in self.frame_caracteristicas.winfo_children():
            widget.destroy()

    def mostrar_tiempos_entrada(self):
        TablaPopupTiempos(self.ventana, "Tiempos de Entrada", self.archivo_tiempos_entrada)

    def mostrar_fila_entrada(self):
        TablaPopupTiempos(self.ventana, "Fila de Entrada", self.archivo_fila_entrada)

    def personal(self):
        self.resetear_frame_caracteristicas()
        self.cantidad_empleados = IntVar()
        self.empleados = IntVar()
        self.supervisores = IntVar()
        self.limpieza = IntVar()
        self.mantenimiento = IntVar()
        self.etiqueta_titulo_caracteristicas = LtkLabel(self.frame_caracteristicas, texto="Ajustes del Personal")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)

        self.label_cantidad_empleados = LtkLabel(self.frame_caracteristicas, texto="Cantidad de empleados en caja:")
        self.label_cantidad_empleados.grid(row=3, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.cantidad_empleados = LtkEntryLine(self.frame_caracteristicas)
        self.cantidad_empleados.grid(row=3, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_empleados = LtkLabel(self.frame_caracteristicas, texto="Cantidad de empleados de atención:")
        self.label_empleados.grid(row=4, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.empleados = LtkEntryLine(self.frame_caracteristicas)
        self.empleados.grid(row=4, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_supervisores = LtkLabel(self.frame_caracteristicas, texto="Cantidad de supervisores:")
        self.label_supervisores.grid(row=5, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.supervisores = LtkEntryLine(self.frame_caracteristicas)
        self.supervisores.grid(row=5, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_limpieza = LtkLabel(self.frame_caracteristicas, texto="Cantidad de empleados de limpieza:")
        self.label_limpieza.grid(row=6, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.limpieza = LtkEntryLine(self.frame_caracteristicas)
        self.limpieza.grid(row=6, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_mantenimiento = LtkLabel(self.frame_caracteristicas, texto="Cantidad de empleados de mantenimiento:")
        self.label_mantenimiento.grid(row=7, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.mantenimiento = LtkEntryLine(self.frame_caracteristicas)
        self.mantenimiento.grid(row=7, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        boton_guardar_personal = LtkButtonFill(self.frame_caracteristicas, self.guardar_datos, "Guardar")
        boton_guardar_personal.grid(row=8, column=0, columnspan=3, pady=(10, 0))

    def costos(self):
        self.resetear_frame_caracteristicas()
        self.gerente = StringVar()
        self.pa_cajero = StringVar()
        self.pa_asesor = StringVar()
        self.pa_limpieza = StringVar()
        self.pa_mantenimiento = StringVar()
        self.pa_basicos = StringVar()
        self.pa_renta = StringVar()

        self.etiqueta_titulo_caracteristicas = ctk.CTkLabel(self.frame_caracteristicas, text="Ajustes de Costos")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)

        self.label_gerente = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de Gerente/Supervisor:")
        self.label_gerente.grid(row=3, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_gerente = ctk.CTkEntry(self.frame_caracteristicas, textvariable=self.gerente)
        self.entry_gerente.grid(row=3, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_pa_cajero = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de Cajeros:")
        self.label_pa_cajero.grid(row=4, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_pa_cajero = ctk.CTkEntry(self.frame_caracteristicas, textvariable=self.pa_cajero)
        self.entry_pa_cajero.grid(row=4, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_pa_asesor = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de Asesores de ventas:")
        self.label_pa_asesor.grid(row=5, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_pa_asesor = ctk.CTkEntry(self.frame_caracteristicas, textvariable=self.pa_asesor)
        self.entry_pa_asesor.grid(row=5, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_pa_limpieza = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de Personal de limpieza:")
        self.label_pa_limpieza.grid(row=6, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_pa_limpieza = ctk.CTkEntry(self.frame_caracteristicas, textvariable=self.pa_limpieza)
        self.entry_pa_limpieza.grid(row=6, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_pa_mantenimiento = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de Personal de mantenimiento:")
        self.label_pa_mantenimiento.grid(row=7, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_pa_mantenimiento = ctk.CTkEntry(self.frame_caracteristicas, textvariable=self.pa_mantenimiento)
        self.entry_pa_mantenimiento.grid(row=7, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_pa_basicos = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de Servicios básicos:")
        self.label_pa_basicos.grid(row=8, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_pa_basicos = ctk.CTkEntry(self.frame_caracteristicas, textvariable=self.pa_basicos)
        self.entry_pa_basicos.grid(row=8, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_pa_renta = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de Renta:")
        self.label_pa_renta.grid(row=9, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_pa_renta = ctk.CTkEntry(self.frame_caracteristicas, textvariable=self.pa_renta)
        self.entry_pa_renta.grid(row=9, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_costo_mantenimiento = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de mantenimiento por unidad diaria:")
        self.label_costo_mantenimiento.grid(row=10, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_costo_mantenimiento = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_costo_mantenimiento.grid(row=10, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_costo_abandono_cliente = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de abandono por cliente:")
        self.label_costo_abandono_cliente.grid(row=11, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_costo_abandono_cliente = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_costo_abandono_cliente.grid(row=11, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_costo_fijo_diario = ctk.CTkLabel(self.frame_caracteristicas, text="Costo fijo diario:")
        self.label_costo_fijo_diario.grid(row=12, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_costo_fijo_diario = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_costo_fijo_diario.grid(row=12, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        boton_guardar_costos = LtkButtonFill(self.frame_caracteristicas, self.guardar_datos, "Guardar")
        boton_guardar_costos.grid(row=13, column=0, columnspan=3, pady=(10, 0))

    def horarios(self):
        self.resetear_frame_caracteristicas()
        self.horario_inicio = LtkEntryLine(self.frame_caracteristicas)
        self.horario_inicio.grid(row=3, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")
        self.horario_cierre = LtkEntryLine(self.frame_caracteristicas)
        self.horario_cierre.grid(row=4, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")

        self.etiqueta_titulo_caracteristicas = LtkLabel(self.frame_caracteristicas, texto="Ajustes de Horarios")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)

        self.label_horario_inicio = LtkLabel(self.frame_caracteristicas, texto="Hora de inicio:")
        self.label_horario_inicio.grid(row=3, column=0, padx=(10, 10), pady=(5, 2), sticky="w")

        self.label_horario_cierre = LtkLabel(self.frame_caracteristicas, texto="Hora de cierre:")
        self.label_horario_cierre.grid(row=4, column=0, padx=(10, 10), pady=(5, 2), sticky="w")

        boton_guardar_personal = LtkButtonFill(self.frame_caracteristicas, self.guardar_datos, "Guardar")
        boton_guardar_personal.grid(row=8, column=0, columnspan=3, pady=(10, 0))

    def fila_entrada(self):
        self.resetear_frame_caracteristicas()

        self.etiqueta_titulo_fila_entrada = LtkLabel(self.frame_caracteristicas, texto="Configuración de Fila de Entrada")
        self.etiqueta_titulo_fila_entrada.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_fila_entrada.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)
        self.cantidad_entradas = IntVar()
        self.entradas_funcionamiento = IntVar()
        self.btn_uso_entradas = LtkButtonLine(self.frame_caracteristicas, self.mostrar_tiempos_entrada, "Tiempos de Entrada")
        self.btn_uso_entradas.grid(row=1, column=0, padx=(10, 10), pady=(5, 5), sticky="nsew")

        self.btn_fila_entrada = LtkButtonLine(self.frame_caracteristicas, self.mostrar_fila_entrada, "Fila de Entrada")
        self.btn_fila_entrada.grid(row=2, column=0, padx=(10, 10), pady=(5, 5), sticky="nsew")

        self.label_cantidad_entradas = ctk.CTkLabel(self.frame_caracteristicas, text="Cantidad de entradas:")
        self.label_cantidad_entradas.grid(row=8, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.cantidad_entradas = ctk.CTkEntry(self.frame_caracteristicas, textvariable=self.cantidad_entradas)
        self.cantidad_entradas.grid(row=8, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_entradas_funcionamiento = ctk.CTkLabel(self.frame_caracteristicas, text="Entradas en funcionamiento:")
        self.label_entradas_funcionamiento.grid(row=9, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entradas_funcionamiento = ctk.CTkEntry(self.frame_caracteristicas, textvariable=self.entradas_funcionamiento)
        self.entradas_funcionamiento.grid(row=9, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        boton_guardar_personal = LtkButtonFill(self.frame_caracteristicas, self.guardar_datos, "Guardar")
        boton_guardar_personal.grid(row=10, column=0, columnspan=3, pady=(10, 0))

    def tiempos_entrada(self):
        self.resetear_frame_caracteristicas()

        self.etiqueta_titulo_caracteristicas = ctk.CTkLabel(self.frame_caracteristicas, text="Ajustes de Tiempos de Entrada")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)

        self.label_tiempo_min = ctk.CTkLabel(self.frame_caracteristicas, text="Tiempo mínimo de entrada (minutos):")
        self.label_tiempo_min.grid(row=1, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_tiempo_min = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_tiempo_min.grid(row=1, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_tiempo_max = ctk.CTkLabel(self.frame_caracteristicas, text="Tiempo máximo de entrada (minutos):")
        self.label_tiempo_max.grid(row=2, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_tiempo_max = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_tiempo_max.grid(row=2, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.btn_abrir_tabla_tiempos = CTkButton(self.frame_caracteristicas, text="Abrir Tabla de Tiempos de Entrada", command=self.abrir_tabla_tiempos_entrada)
        self.btn_abrir_tabla_tiempos.grid(row=3, column=0, columnspan=3, pady=10)

    def abrir_tabla_tiempos_entrada(self):
        self.archivo_tiempos_entrada = "tiempos_entrada.json"
        TablaPopupTiempos(self.ventana, "Tiempos de Entrada", self.archivo_tiempos_entrada)

    def precios(self):
        self.resetear_frame_caracteristicas()

        self.etiqueta_titulo_caracteristicas = ctk.CTkLabel(self.frame_caracteristicas, text="Ajustes de Precios")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)

        self.label_precio_hora = ctk.CTkLabel(self.frame_caracteristicas, text="Precio por hora:")
        self.label_precio_hora.grid(row=1, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_precio_hora = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_precio_hora.grid(row=1, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_precio_dia = ctk.CTkLabel(self.frame_caracteristicas, text="Precio por día:")
        self.label_precio_dia.grid(row=2, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_precio_dia = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_precio_dia.grid(row=2, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        boton_guardar_precios = LtkButtonFill(self.frame_caracteristicas, self.guardar_datos, "Guardar")
        boton_guardar_precios.grid(row=3, column=0, columnspan=3, pady=(10, 0))

    def guardar_informacion(self):
        configuracion = self.leer_configuracion()

        if hasattr(self, 'cantidad_empleados') and self.cantidad_empleados.winfo_exists():
            configuracion["personal"] = {
                "cantidad_empleados": self.cantidad_empleados.get(),
                "empleados": self.empleados.get(),
                "supervisores": self.supervisores.get(),
                "limpieza": self.limpieza.get(),
                "mantenimiento": self.mantenimiento.get()
            }

        if hasattr(self, 'horario_inicio') and self.horario_inicio.winfo_exists():
            configuracion["horarios"] = {
                "horario_inicio": self.horario_inicio.get(),
                "horario_cierre": self.horario_cierre.get()
            }

        if hasattr(self, 'gerente') and self.entry_gerente.winfo_exists():
            configuracion["costos"] = {
                "costo_gerente": self.gerente.get(),
                "costo_cajero": self.pa_cajero.get(),
                "costo_asesor": self.pa_asesor.get(),
                "costo_limpieza": self.pa_limpieza.get(),
                "costo_mantenimiento": self.pa_mantenimiento.get(),
                "costo_basicos": self.pa_basicos.get(),
                "costo_renta": self.pa_renta.get(),
                "costo_mantenimiento_por_unidad_diaria": self.entry_costo_mantenimiento.get(),
                "costo_abandono_por_cliente": self.entry_costo_abandono_cliente.get(),
                "costo_fijo_diario": self.entry_costo_fijo_diario.get()
            }

        if hasattr(self, 'precio_hora') and self.entry_precio_hora.winfo_exists():
            configuracion["precios"] = {
                "precio_hora": self.entry_precio_hora.get(),
                "precio_dia": self.entry_precio_dia.get()
            }

        with open(self.archivo_configuracion, "w") as archivo:
            json.dump(configuracion, archivo, indent=4)

        messagebox.showinfo("Información", "Configuración guardada con éxito")

    def guardar_datos(self):
        self.guardar_informacion()
        messagebox.showinfo("Éxito", "Los datos se han guardado correctamente.")

    def guardar_y_cerrar(self):
        self.guardar_informacion()
        messagebox.showinfo("Éxito", "Los datos se han guardado correctamente.")
        self.ventana.destroy()

    def leer_configuracion(self):
        if os.path.exists(self.archivo_configuracion):
            with open(self.archivo_configuracion, 'r') as archivo:
                try:
                    configuracion = json.load(archivo)
                    if "costos" not in configuracion:
                        configuracion["costos"] = {}
                    if "precios" not in configuracion:
                        configuracion["precios"] = {}
                    return configuracion
                except json.JSONDecodeError:
                    return {
                        "costos": {},
                        "precios": {}
                    }
        else:
            return {
                "costos": {},
                "precios": {}
            }

if __name__ == "__main__":
    app = Estacionamiento()
