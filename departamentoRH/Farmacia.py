import os
import json
from tkinter import messagebox, simpledialog, IntVar, StringVar
import tkinter.ttk as ttk
import customtkinter as ctk
from customtkinter import CTk, CTkFrame, CTkButton, CTkToplevel

from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkLabel import LtkLabel

class TablaPopupReabastecimiento:
    def __init__(self, ventana, titulo, ruta_archivo):
        self.top = CTkToplevel(ventana)
        self.top.title(titulo)
        self.top.transient(ventana)
        self.top.grab_set()

        self.ruta_archivo = ruta_archivo
        self.datos = self.cargar_datos()

        self.arbol = ttk.Treeview(self.top, columns=("Cantidad", "Probabilidad"), show="headings")
        self.arbol.heading("Cantidad", text="Cantidad")
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
        cantidad = simpledialog.askstring("Input", "Ingrese la cantidad:")
        probabilidad = simpledialog.askstring("Input", "Ingrese la probabilidad:")
        if cantidad and probabilidad:
            self.arbol.insert('', 'end', values=(cantidad, probabilidad))
            self.guardar_datos()

    def editar_fila(self):
        item_seleccionado = self.arbol.selection()
        if item_seleccionado:
            cantidad_actual, probabilidad_actual = self.arbol.item(item_seleccionado, 'values')
            nueva_cantidad = simpledialog.askstring("Input", "Ingrese la cantidad:", initialvalue=cantidad_actual)
            nueva_probabilidad = simpledialog.askstring("Input", "Ingrese la probabilidad:", initialvalue=probabilidad_actual)
            if nueva_cantidad and nueva_probabilidad:
                self.arbol.item(item_seleccionado, values=(nueva_cantidad, nueva_probabilidad))
                self.guardar_datos()

    def eliminar_fila(self):
        item_seleccionado = self.arbol.selection()
        if item_seleccionado:
            self.arbol.delete(item_seleccionado)
            self.guardar_datos()

class TablaPopup:
    def __init__(self, ventana, titulo, ruta_archivo):
        self.top = CTkToplevel(ventana)
        self.top.title(titulo)
        self.top.transient(ventana)
        self.top.grab_set()

        self.ruta_archivo = ruta_archivo
        self.datos = self.cargar_datos()

        self.arbol = ttk.Treeview(self.top, columns=("Valor", "Probabilidad"), show="headings")
        self.arbol.heading("Valor", text="Valor")
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
        valor = simpledialog.askstring("Input", "Ingrese el valor:")
        probabilidad = simpledialog.askstring("Input", "Ingrese la probabilidad:")
        if valor and probabilidad:
            self.arbol.insert('', 'end', values=(valor, probabilidad))
            self.guardar_datos()

    def editar_fila(self):
        item_seleccionado = self.arbol.selection()
        if item_seleccionado:
            valor_actual, probabilidad_actual = self.arbol.item(item_seleccionado, 'values')
            nuevo_valor = simpledialog.askstring("Input", "Ingrese el valor:", initialvalue=valor_actual)
            nueva_probabilidad = simpledialog.askstring("Input", "Ingrese la probabilidad:", initialvalue=probabilidad_actual)
            if nuevo_valor and nueva_probabilidad:
                self.arbol.item(item_seleccionado, values=(nuevo_valor, nueva_probabilidad))
                self.guardar_datos()

    def eliminar_fila(self):
        item_seleccionado = self.arbol.selection()
        if item_seleccionado:
            self.arbol.delete(item_seleccionado)
            self.guardar_datos()

class TablaProbabilidadesVentas:
    def __init__(self, ventana, titulo, ruta_archivo):
        self.top = CTkToplevel(ventana)
        self.top.title(titulo)
        self.top.transient(ventana)
        self.top.grab_set()

        self.ruta_archivo = ruta_archivo
        self.datos = self.cargar_datos()

        self.arbol = ttk.Treeview(self.top, columns=("Producto", "Cantidad", "Probabilidad"), show="headings")
        self.arbol.heading("Producto", text="Producto")
        self.arbol.heading("Cantidad", text="Cantidad")
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
        datos = [(self.arbol.item(item)['values'][0], self.arbol.item(item)['values'][1], self.arbol.item(item)['values'][2]) for item in self.arbol.get_children()]
        with open(self.ruta_archivo, 'w') as archivo:
            json.dump(datos, archivo, indent=4)

    def llenar_tabla(self):
        for item in self.datos:
            self.arbol.insert('', 'end', values=item)

    def agregar_fila(self):
        producto = simpledialog.askstring("Input", "Ingrese el producto (medicamento, vitaminas, equipo_medico):")
        cantidad = simpledialog.askstring("Input", "Ingrese la cantidad:")
        probabilidad = simpledialog.askstring("Input", "Ingrese la probabilidad:")
        if producto and cantidad and probabilidad:
            self.arbol.insert('', 'end', values=(producto, cantidad, probabilidad))
            self.guardar_datos()

    def editar_fila(self):
        item_seleccionado = self.arbol.selection()
        if item_seleccionado:
            producto_actual, cantidad_actual, probabilidad_actual = self.arbol.item(item_seleccionado, 'values')
            nuevo_producto = simpledialog.askstring("Input", "Ingrese el producto (medicamento, vitaminas, equipo_medico):", initialvalue=producto_actual)
            nueva_cantidad = simpledialog.askstring("Input", "Ingrese la cantidad:", initialvalue=cantidad_actual)
            nueva_probabilidad = simpledialog.askstring("Input", "Ingrese la probabilidad:", initialvalue=probabilidad_actual)
            if nuevo_producto and nueva_cantidad and nueva_probabilidad:
                self.arbol.item(item_seleccionado, values=(nuevo_producto, nueva_cantidad, nueva_probabilidad))
                self.guardar_datos()

    def eliminar_fila(self):
        item_seleccionado = self.arbol.selection()
        if item_seleccionado:
            self.arbol.delete(item_seleccionado)
            self.guardar_datos()

class TablaFrecuenciaPopup:
    def __init__(self, ventana, titulo, ruta_archivo):
        self.top = CTkToplevel(ventana)
        self.top.title(titulo)
        self.top.transient(ventana)
        self.top.grab_set()

        self.ruta_archivo = ruta_archivo
        self.datos = self.cargar_datos()

        self.arbol = ttk.Treeview(self.top, columns=("Medicamento", "Frecuencia"), show="headings")
        self.arbol.heading("Medicamento", text="Medicamento")
        self.arbol.heading("Frecuencia", text="Frecuencia (días)")
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
                try:
                    return json.load(archivo)
                except json.JSONDecodeError:
                    messagebox.showerror("Error", "El archivo de datos está corrupto.")
                    return []
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
        medicamento = simpledialog.askstring("Input", "Ingrese el medicamento:")
        frecuencia = simpledialog.askstring("Input", "Ingrese la frecuencia (días):")
        if medicamento and frecuencia:
            self.arbol.insert('', 'end', values=(medicamento, frecuencia))
            self.guardar_datos()

    def editar_fila(self):
        item_seleccionado = self.arbol.selection()
        if item_seleccionado:
            medicamento_actual, frecuencia_actual = self.arbol.item(item_seleccionado, 'values')
            nuevo_medicamento = simpledialog.askstring("Input", "Ingrese el medicamento:", initialvalue=medicamento_actual)
            nueva_frecuencia = simpledialog.askstring("Input", "Ingrese la frecuencia (días):", initialvalue=frecuencia_actual)
            if nuevo_medicamento and nueva_frecuencia:
                self.arbol.item(item_seleccionado, values=(nuevo_medicamento, nueva_frecuencia))
                self.guardar_datos()

    def eliminar_fila(self):
        item_seleccionado = self.arbol.selection()
        if item_seleccionado:
            self.arbol.delete(item_seleccionado)
            self.guardar_datos()

class Farmacia:
    def __init__(self):
        self.ventana = ctk.CTk()
        self.archivo_configuracion = "configuracion_farmacia1.json"
        self.archivo_uso_caja = "uso_caja1.json"
        self.archivo_fila_caja = "fila_caja1.json"
        self.archivo_frecuencia_reabastecimiento = "frecuencia_reabastecimiento1.json"
        self.archivo_reabastecimiento_medicamento = "reabastecimiento_medicamento1.json"
        self.archivo_reabastecimiento_vitaminas = "reabastecimiento_vitaminas1.json"
        self.archivo_reabastecimiento_equipo_medico = "reabastecimiento_equipo_medico1.json"
        self.ventana.title("Farmacia")
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
        titulo = LtkLabel(frame_titulo, texto="Configuración de Farmacia")
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
        boton_caja = LtkButtonLine(frame_opciones, self.caja, "Caja")
        boton_caja.grid(row=3, column=0, padx=(5, 5), pady=(5, 5))
        boton_inventario = LtkButtonLine(frame_opciones, self.inventario, "Inventario")
        boton_inventario.grid(row=4, column=0, padx=(5, 5), pady=(5, 5))
        boton_inventario = LtkButtonLine(frame_opciones, self.precios, "Precios")
        boton_inventario.grid(row=5, column=0, padx=(5, 5), pady=(5, 5))

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

    def mostrar_uso_caja(self):
        TablaPopup(self.ventana, "Uso de Caja", self.archivo_uso_caja)

    def mostrar_fila_caja(self):
        TablaPopup(self.ventana, "Fila de Caja", self.archivo_fila_caja)

    def personal(self):
        self.resetear_frame_caracteristicas()
        self.cantidad_empleados = IntVar()
        self.doctores = IntVar()
        self.farmaceuticos = IntVar()
        self.limpieza = IntVar()
        self.inventario = IntVar()
        self.etiqueta_titulo_caracteristicas = LtkLabel(self.frame_caracteristicas, texto="Ajustes Del Personal")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)

        self.label_cantidad_empleados = LtkLabel(self.frame_caracteristicas, texto="Cantidad de encargados de caja:")
        self.label_cantidad_empleados.grid(row=3, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.cantidad_empleados = LtkEntryLine(self.frame_caracteristicas)
        self.cantidad_empleados.grid(row=3, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_doctores = LtkLabel(self.frame_caracteristicas, texto="Cantidad de doctores:")
        self.label_doctores.grid(row=4, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.doctores = LtkEntryLine(self.frame_caracteristicas)
        self.doctores.grid(row=4, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_farmaceuticos = LtkLabel(self.frame_caracteristicas, texto="Cantidad de farmacéuticos:")
        self.label_farmaceuticos.grid(row=5, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.farmaceuticos = LtkEntryLine(self.frame_caracteristicas)
        self.farmaceuticos.grid(row=5, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_limpieza = LtkLabel(self.frame_caracteristicas, texto="Cantidad de empleados de limpieza:")
        self.label_limpieza.grid(row=6, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.limpieza = LtkEntryLine(self.frame_caracteristicas)
        self.limpieza.grid(row=6, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_inventario = LtkLabel(self.frame_caracteristicas, texto="Cantidad de encargados de inventario:")
        self.label_inventario.grid(row=7, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.inventario = LtkEntryLine(self.frame_caracteristicas)
        self.inventario.grid(row=7, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        boton_guardar_personal = LtkButtonFill(self.frame_caracteristicas, self.guardar_datos, "Guardar")
        boton_guardar_personal.grid(row=8, column=0, columnspan=3, pady=(10, 0))

    def costos(self):
        self.resetear_frame_caracteristicas()
        self.gerente = StringVar()
        self.pa_cajero = StringVar()
        self.pa_doctor = StringVar()
        self.pa_farmaceutico = StringVar()
        self.pa_limpieza = StringVar()
        self.pa_inventario = StringVar()
        self.pa_basicos = StringVar()
        self.pa_renta = StringVar()

        self.etiqueta_titulo_caracteristicas = ctk.CTkLabel(self.frame_caracteristicas, text="Ajustes De Costos")
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

        self.label_pa_doctor = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de Doctores:")
        self.label_pa_doctor.grid(row=5, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_pa_doctor = ctk.CTkEntry(self.frame_caracteristicas, textvariable=self.pa_doctor)
        self.entry_pa_doctor.grid(row=5, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_pa_farmaceutico = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de Farmacéuticos:")
        self.label_pa_farmaceutico.grid(row=6, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_pa_farmaceutico = ctk.CTkEntry(self.frame_caracteristicas, textvariable=self.pa_farmaceutico)
        self.entry_pa_farmaceutico.grid(row=6, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_pa_limpieza = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de Personal de limpieza:")
        self.label_pa_limpieza.grid(row=7, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_pa_limpieza = ctk.CTkEntry(self.frame_caracteristicas, textvariable=self.pa_limpieza)
        self.entry_pa_limpieza.grid(row=7, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_pa_inventario = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de Personal de inventario:")
        self.label_pa_inventario.grid(row=8, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_pa_inventario = ctk.CTkEntry(self.frame_caracteristicas, textvariable=self.pa_inventario)
        self.entry_pa_inventario.grid(row=8, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_pa_basicos = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de Servicios básicos:")
        self.label_pa_basicos.grid(row=9, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_pa_basicos = ctk.CTkEntry(self.frame_caracteristicas, textvariable=self.pa_basicos)
        self.entry_pa_basicos.grid(row=9, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_pa_renta = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de Renta:")
        self.label_pa_renta.grid(row=10, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_pa_renta = ctk.CTkEntry(self.frame_caracteristicas, textvariable=self.pa_renta)
        self.entry_pa_renta.grid(row=10, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_costo_pedidos = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de administración de pedidos:")
        self.label_costo_pedidos.grid(row=11, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_costo_pedidos = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_costo_pedidos.grid(row=11, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_costo_medicamento = ctk.CTkLabel(self.frame_caracteristicas, text="Costo por medicamento:")
        self.label_costo_medicamento.grid(row=12, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_costo_medicamento = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_costo_medicamento.grid(row=12, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_costo_vitaminas = ctk.CTkLabel(self.frame_caracteristicas, text="Costo por vitaminas:")
        self.label_costo_vitaminas.grid(row=13, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_costo_vitaminas = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_costo_vitaminas.grid(row=13, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_costo_equipo_medico = ctk.CTkLabel(self.frame_caracteristicas, text="Costo por equipo médico:")
        self.label_costo_equipo_medico.grid(row=14, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_costo_equipo_medico = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_costo_equipo_medico.grid(row=14, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_costo_almacenamiento = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de almacenamiento por unidad diaria:")
        self.label_costo_almacenamiento.grid(row=15, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_costo_almacenamiento = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_costo_almacenamiento.grid(row=15, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_costo_abandono_cliente = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de abandono por cliente:")
        self.label_costo_abandono_cliente.grid(row=16, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_costo_abandono_cliente = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_costo_abandono_cliente.grid(row=16, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_costo_fijo_diario = ctk.CTkLabel(self.frame_caracteristicas, text="Costo fijo diario:")
        self.label_costo_fijo_diario.grid(row=17, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_costo_fijo_diario = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_costo_fijo_diario.grid(row=17, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        boton_guardar_costos = LtkButtonFill(self.frame_caracteristicas, self.guardar_datos, "Guardar")
        boton_guardar_costos.grid(row=18, column=0, columnspan=3, pady=(10, 0))

    def horarios(self):
        self.resetear_frame_caracteristicas()
        self.horario_inicio = LtkEntryLine(self.frame_caracteristicas)
        self.horario_inicio.grid(row=3, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")
        self.horario_cierre = LtkEntryLine(self.frame_caracteristicas)
        self.horario_cierre.grid(row=4, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")

        self.etiqueta_titulo_caracteristicas = LtkLabel(self.frame_caracteristicas, texto="Ajustes De Horarios")
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

    def caja(self):
        self.resetear_frame_caracteristicas()

        self.etiqueta_titulo_caja = LtkLabel(self.frame_caracteristicas, texto="Configuración de Caja")
        self.etiqueta_titulo_caja.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caja.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)
        self.cantidad_caja = IntVar()
        self.caja_funcionamiento = IntVar()
        self.btn_uso_caja = LtkButtonLine(self.frame_caracteristicas, self.mostrar_uso_caja, "Uso de Caja")
        self.btn_uso_caja.grid(row=1, column=0, padx=(10, 10), pady=(5, 5), sticky="nsew")

        self.btn_fila_caja = LtkButtonLine(self.frame_caracteristicas, self.mostrar_fila_caja, "Fila de Caja")
        self.btn_fila_caja.grid(row=2, column=0, padx=(10, 10), pady=(5, 5), sticky="nsew")

        self.label_cantidad_caja = ctk.CTkLabel(self.frame_caracteristicas, text="Cantidad de cajas:")
        self.label_cantidad_caja.grid(row=8, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.cantidad_caja = ctk.CTkEntry(self.frame_caracteristicas, textvariable=self.cantidad_caja)
        self.cantidad_caja.grid(row=8, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_caja_funcionamiento = ctk.CTkLabel(self.frame_caracteristicas, text="Cajas en funcionamiento:")
        self.label_caja_funcionamiento.grid(row=9, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.caja_funcionamiento = ctk.CTkEntry(self.frame_caracteristicas, textvariable=self.caja_funcionamiento)
        self.caja_funcionamiento.grid(row=9, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        boton_guardar_personal = LtkButtonFill(self.frame_caracteristicas, self.guardar_datos, "Guardar")
        boton_guardar_personal.grid(row=10, column=0, columnspan=3, pady=(10, 0))

    def precios(self):
        self.resetear_frame_caracteristicas()

        self.etiqueta_titulo_caracteristicas = ctk.CTkLabel(self.frame_caracteristicas, text="Ajustes de Probabilidades y Precios de Ventas")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)

        self.label_precio_medicamento = ctk.CTkLabel(self.frame_caracteristicas, text="Precio de Medicamentos:")
        self.label_precio_medicamento.grid(row=1, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_precio_medicamento = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_precio_medicamento.grid(row=1, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_precio_vitaminas = ctk.CTkLabel(self.frame_caracteristicas, text="Precio de Vitaminas:")
        self.label_precio_vitaminas.grid(row=2, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_precio_vitaminas = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_precio_vitaminas.grid(row=2, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_precio_equipo_medico = ctk.CTkLabel(self.frame_caracteristicas, text="Precio de Equipo Médico:")
        self.label_precio_equipo_medico.grid(row=3, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_precio_equipo_medico = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_precio_equipo_medico.grid(row=3, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.btn_abrir_tabla = CTkButton(self.frame_caracteristicas, text="Abrir Tabla de Probabilidades de Ventas", command=self.abrir_tabla_probabilidades)
        self.btn_abrir_tabla.grid(row=4, column=0, columnspan=3, pady=10)

    def abrir_tabla_probabilidades(self):
        self.archivo_probabilidades_ventas = "prob_ventas1.json"
        TablaProbabilidadesVentas(self.ventana, "Probabilidades de Ventas", self.archivo_probabilidades_ventas)

    def inventario(self):
        self.resetear_frame_caracteristicas()

        self.inventario_medicamento = IntVar()
        self.inventario_vitaminas = IntVar()
        self.inventario_equipo_medico = IntVar()
        self.cantidad_medicamento = IntVar()
        self.cantidad_vitaminas = IntVar()
        self.cantidad_equipo_medico = IntVar()

        self.etiqueta_titulo_caracteristicas = LtkLabel(self.frame_caracteristicas, texto="Configuración de Inventario")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)

        self.label_inventario_medicamento = LtkLabel(self.frame_caracteristicas, texto="Inventario inicial de medicamentos:")
        self.label_inventario_medicamento.grid(row=1, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_inventario_medicamento = LtkEntryLine(self.frame_caracteristicas)
        self.entry_inventario_medicamento.grid(row=1, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_inventario_vitaminas = LtkLabel(self.frame_caracteristicas, texto="Inventario inicial de vitaminas:")
        self.label_inventario_vitaminas.grid(row=2, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_inventario_vitaminas = LtkEntryLine(self.frame_caracteristicas)
        self.entry_inventario_vitaminas.grid(row=2, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_inventario_equipo_medico = LtkLabel(self.frame_caracteristicas, texto="Inventario inicial de equipo médico:")
        self.label_inventario_equipo_medico.grid(row=3, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_inventario_equipo_medico = LtkEntryLine(self.frame_caracteristicas)
        self.entry_inventario_equipo_medico.grid(row=3, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_cantidad_medicamento = LtkLabel(self.frame_caracteristicas, texto="Cantidad de reabastecimiento de medicamentos:")
        self.label_cantidad_medicamento.grid(row=4, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_cantidad_medicamento = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_medicamento.grid(row=4, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_cantidad_vitaminas = LtkLabel(self.frame_caracteristicas, texto="Cantidad de reabastecimiento de vitaminas:")
        self.label_cantidad_vitaminas.grid(row=5, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_cantidad_vitaminas = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_vitaminas.grid(row=5, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_cantidad_equipo_medico = LtkLabel(self.frame_caracteristicas, texto="Cantidad de reabastecimiento de equipo médico:")
        self.label_cantidad_equipo_medico.grid(row=6, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_cantidad_equipo_medico = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_equipo_medico.grid(row=6, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)


        boton_guardar_inventario = LtkButtonFill(self.frame_caracteristicas, self.guardar_datos, "Guardar")
        boton_guardar_inventario.grid(row=10, column=0, columnspan=3, pady=(10, 0))

    def guardar_informacion(self):
        configuracion = self.leer_configuracion()

        if hasattr(self, 'cantidad_empleados') and self.cantidad_empleados.winfo_exists():
            configuracion["personal"] = {
                "cantidad_empleados": self.cantidad_empleados.get(),
                "doctores": self.doctores.get(),
                "farmaceuticos": self.farmaceuticos.get(),
                "limpieza": self.limpieza.get(),
                "inventario": self.inventario.get()
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
                "costo_doctor": self.pa_doctor.get(),
                "costo_farmaceutico": self.pa_farmaceutico.get(),
                "costo_limpieza": self.pa_limpieza.get(),
                "costo_inventario": self.pa_inventario.get(),
                "costo_basicos": self.pa_basicos.get(),
                "costo_renta": self.pa_renta.get(),
                "costo_pedidos": self.entry_costo_pedidos.get(),
                "costo_medicamento": self.entry_costo_medicamento.get(),
                "costo_vitaminas": self.entry_costo_vitaminas.get(),
                "costo_equipo_medico": self.entry_costo_equipo_medico.get(),
                "costo_almacenamiento_por_unidad_diaria": self.entry_costo_almacenamiento.get(),
                "costo_abandono_por_cliente": self.entry_costo_abandono_cliente.get(),
                "costo_fijo_diario": self.entry_costo_fijo_diario.get()
            }

        if hasattr(self, 'precio_medicamento') and self.entry_precio_medicamento.winfo_exists():
            configuracion["precios"] = {
                "precio_medicamento": self.precio_medicamento.get(),
                "precio_vitaminas": self.precio_vitaminas.get(),
                "precio_equipo_medico": self.precio_equipo_medico.get()
            }

        if hasattr(self, 'entry_inventario_medicamento') and self.entry_inventario_medicamento.winfo_exists():
            configuracion["inventario"] = {
                "medicamentos": self.entry_inventario_medicamento.get(),
                "vitaminas": self.entry_inventario_vitaminas.get(),
                "equipo_medico": self.entry_inventario_equipo_medico.get(),
                "cantidad_reabastecimiento": {
                    "medicamentos": self.entry_cantidad_medicamento.get(),
                    "vitaminas": self.entry_cantidad_vitaminas.get(),
                    "equipo_medico": self.entry_cantidad_equipo_medico.get()
                }
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
                    if "inventario" not in configuracion:
                        configuracion["inventario"] = {}
                    return configuracion
                except json.JSONDecodeError:
                    return {
                        "costos": {},
                        "precios": {},
                        "inventario": {}
                    }
        else:
            return {
                "costos": {},
                "precios": {},
                "inventario": {}
            }

    def mostrar_frecuencia_reabastecimiento(self):
        TablaFrecuenciaPopup(self.ventana, "Frecuencia de Reabastecimiento", self.archivo_frecuencia_reabastecimiento)

if __name__ == "__main__":
    app = Farmacia()
