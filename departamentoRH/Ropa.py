import os
import json
from tkinter import messagebox, simpledialog, IntVar, StringVar
import tkinter.ttk as ttk  # Asegúrate de importar ttk correctamente
import customtkinter as ctk
from customtkinter import CTk, CTkFrame, CTkButton, CTkToplevel

from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkLabel import LtkLabel

# Clase TablaPopupReabastecimiento con la importación de ttk corregida
class TablaPopupReabastecimiento:
    def __init__(self, ventana, title, file_path):
        self.top = CTkToplevel(ventana)
        self.top.title(title)
        self.top.transient(ventana)
        self.top.grab_set()

        self.file_path = file_path
        self.data = self.load_data()

        self.tree = ttk.Treeview(self.top, columns=("Cantidad", "Probabilidad"), show="headings")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Probabilidad", text="Probabilidad")
        self.tree.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.scrollbar = ttk.Scrollbar(self.top, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=3, sticky='ns')

        self.btn_add = CTkButton(self.top, text="Agregar", command=self.add_row)
        self.btn_add.grid(row=1, column=0, pady=10)

        self.btn_edit = CTkButton(self.top, text="Editar", command=self.edit_row)
        self.btn_edit.grid(row=1, column=1, pady=10)

        self.btn_delete = CTkButton(self.top, text="Eliminar", command=self.delete_row)
        self.btn_delete.grid(row=1, column=2, pady=10)

        self.populate_table()

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_data(self):
        data = [(self.tree.item(item)['values'][0], self.tree.item(item)['values'][1]) for item in self.tree.get_children()]
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def populate_table(self):
        for item in self.data:
            self.tree.insert('', 'end', values=item)

    def add_row(self):
        cantidad = simpledialog.askstring("Input", "Ingrese la cantidad:")
        probabilidad = simpledialog.askstring("Input", "Ingrese la probabilidad:")
        if cantidad and probabilidad:
            self.tree.insert('', 'end', values=(cantidad, probabilidad))
            self.save_data()

    def edit_row(self):
        selected_item = self.tree.selection()
        if selected_item:
            current_cantidad, current_probabilidad = self.tree.item(selected_item, 'values')
            new_cantidad = simpledialog.askstring("Input", "Ingrese la cantidad:", initialvalue=current_cantidad)
            new_probabilidad = simpledialog.askstring("Input", "Ingrese la probabilidad:", initialvalue=current_probabilidad)
            if new_cantidad and new_probabilidad:
                self.tree.item(selected_item, values=(new_cantidad, new_probabilidad))
                self.save_data()

    def delete_row(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)
            self.save_data()

# Asegúrate de que ttk también esté importado en otras clases que utilicen Treeview
class TablaPopup:
    def __init__(self, ventana, title, file_path):
        self.top = CTkToplevel(ventana)
        self.top.title(title)
        self.top.transient(ventana)
        self.top.grab_set()

        self.file_path = file_path
        self.data = self.load_data()

        self.tree = ttk.Treeview(self.top, columns=("Valor", "Probabilidad"), show="headings")
        self.tree.heading("Valor", text="Valor")
        self.tree.heading("Probabilidad", text="Probabilidad")
        self.tree.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.scrollbar = ttk.Scrollbar(self.top, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=3, sticky='ns')

        self.btn_add = CTkButton(self.top, text="Agregar", command=self.add_row)
        self.btn_add.grid(row=1, column=0, pady=10)

        self.btn_edit = CTkButton(self.top, text="Editar", command=self.edit_row)
        self.btn_edit.grid(row=1, column=1, pady=10)

        self.btn_delete = CTkButton(self.top, text="Eliminar", command=self.delete_row)
        self.btn_delete.grid(row=1, column=2, pady=10)

        self.populate_table()

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_data(self):
        data = [(self.tree.item(item)['values'][0], self.tree.item(item)['values'][1]) for item in
                self.tree.get_children()]
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def populate_table(self):
        for item in self.data:
            self.tree.insert('', 'end', values=item)

    def add_row(self):
        value = simpledialog.askstring("Input", "Ingrese el valor:")
        probability = simpledialog.askstring("Input", "Ingrese la probabilidad:")
        if value and probability:
            self.tree.insert('', 'end', values=(value, probability))
            self.save_data()

    def edit_row(self):
        selected_item = self.tree.selection()
        if selected_item:
            current_value, current_probability = self.tree.item(selected_item, 'values')
            new_value = simpledialog.askstring("Input", "Ingrese el valor:", initialvalue=current_value)
            new_probability = simpledialog.askstring("Input", "Ingrese la probabilidad:",
                                                     initialvalue=current_probability)
            if new_value and new_probability:
                self.tree.item(selected_item, values=(new_value, new_probability))
                self.save_data()

    def delete_row(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)
            self.save_data()

class TablaProbabilidadesVentas:
    def __init__(self, ventana, title, file_path):
        self.top = CTkToplevel(ventana)
        self.top.title(title)
        self.top.transient(ventana)
        self.top.grab_set()

        self.file_path = file_path
        self.data = self.load_data()

        self.tree = ttk.Treeview(self.top, columns=("Producto", "Cantidad", "Probabilidad"), show="headings")
        self.tree.heading("Producto", text="Producto")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Probabilidad", text="Probabilidad")
        self.tree.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.scrollbar = ttk.Scrollbar(self.top, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=3, sticky='ns')

        self.btn_add = CTkButton(self.top, text="Agregar", command=self.add_row)
        self.btn_add.grid(row=1, column=0, pady=10)

        self.btn_edit = CTkButton(self.top, text="Editar", command=self.edit_row)
        self.btn_edit.grid(row=1, column=1, pady=10)

        self.btn_delete = CTkButton(self.top, text="Eliminar", command=self.delete_row)
        self.btn_delete.grid(row=1, column=2, pady=10)

        self.populate_table()

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_data(self):
        data = [(self.tree.item(item)['values'][0], self.tree.item(item)['values'][1], self.tree.item(item)['values'][2]) for item in self.tree.get_children()]
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def populate_table(self):
        for item in self.data:
            self.tree.insert('', 'end', values=item)

    def add_row(self):
        producto = simpledialog.askstring("Input", "Ingrese el producto (pantalones, blusas, ropa_interior):")
        cantidad = simpledialog.askstring("Input", "Ingrese la cantidad:")
        probabilidad = simpledialog.askstring("Input", "Ingrese la probabilidad:")
        if producto and cantidad and probabilidad:
            self.tree.insert('', 'end', values=(producto, cantidad, probabilidad))
            self.save_data()

    def edit_row(self):
        selected_item = self.tree.selection()
        if selected_item:
            current_producto, current_cantidad, current_probabilidad = self.tree.item(selected_item, 'values')
            new_producto = simpledialog.askstring("Input", "Ingrese el producto (pantalones, blusas, ropa_interior):", initialvalue=current_producto)
            new_cantidad = simpledialog.askstring("Input", "Ingrese la cantidad:", initialvalue=current_cantidad)
            new_probabilidad = simpledialog.askstring("Input", "Ingrese la probabilidad:", initialvalue=current_probabilidad)
            if new_producto and new_cantidad and new_probabilidad:
                self.tree.item(selected_item, values=(new_producto, new_cantidad, new_probabilidad))
                self.save_data()

    def delete_row(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)
            self.save_data()

class TablaFrecuenciaPopup:
    def __init__(self, ventana, title, file_path):
        self.top = CTkToplevel(ventana)
        self.top.title(title)
        self.top.transient(ventana)
        self.top.grab_set()

        self.file_path = file_path
        self.data = self.load_data()

        self.tree = ttk.Treeview(self.top, columns=("Prenda", "Frecuencia"), show="headings")
        self.tree.heading("Prenda", text="Prenda")
        self.tree.heading("Frecuencia", text="Frecuencia (días)")
        self.tree.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.scrollbar = ttk.Scrollbar(self.top, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=3, sticky='ns')

        self.btn_add = CTkButton(self.top, text="Agregar", command=self.add_row)
        self.btn_add.grid(row=1, column=0, pady=10)

        self.btn_edit = CTkButton(self.top, text="Editar", command=self.edit_row)
        self.btn_edit.grid(row=1, column=1, pady=10)

        self.btn_delete = CTkButton(self.top, text="Eliminar", command=self.delete_row)
        self.btn_delete.grid(row=1, column=2, pady=10)

        self.populate_table()

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    messagebox.showerror("Error", "El archivo de datos está corrupto.")
                    return []
        else:
            return []

    def save_data(self):
        data = [(self.tree.item(item)['values'][0], self.tree.item(item)['values'][1]) for item in
                self.tree.get_children()]
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def populate_table(self):
        for item in self.data:
            self.tree.insert('', 'end', values=item)

    def add_row(self):
        prenda = simpledialog.askstring("Input", "Ingrese la prenda:")
        frecuencia = simpledialog.askstring("Input", "Ingrese la frecuencia (días):")
        if prenda and frecuencia:
            self.tree.insert('', 'end', values=(prenda, frecuencia))
            self.save_data()

    def edit_row(self):
        selected_item = self.tree.selection()
        if selected_item:
            current_prenda, current_frecuencia = self.tree.item(selected_item, 'values')
            new_prenda = simpledialog.askstring("Input", "Ingrese la prenda:", initialvalue=current_prenda)
            new_frecuencia = simpledialog.askstring("Input", "Ingrese la frecuencia (días):", initialvalue=current_frecuencia)
            if new_prenda and new_frecuencia:
                self.tree.item(selected_item, values=(new_prenda, new_frecuencia))
                self.save_data()

    def delete_row(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)
            self.save_data()


class ropa:
    def __init__(self):
        self.ventana = ctk.CTk()
        self.file_configuracion = "configuracion.json"
        self.file_uso_probadores = "uso_probadores.json"
        self.file_fila_probadores = "fila_probadores.json"
        self.file_frecuencia_reabastecimiento = "frecuencia_reabastecimiento.json"
        self.file_reabastecimiento_pantalones = "reabastecimiento.json"
        self.file_reabastecimiento_blusas = "reabastecimiento.json"
        self.file_reabastecimiento_ropa_interior = "reabastecimiento.json"
        self.ventana.title("Tienda de Ropa")
        self.ventana.geometry("900x600+350+100")
        self.ventana.configure(bg="#FFFFFF")
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)
        self.ventana.rowconfigure(1, weight=1)

        self.ruta_ventana = os.path.dirname(os.path.abspath(__file__))

        # Frame de características
        self.frame_caracteristicas = ctk.CTkFrame(self.ventana)
        self.frame_caracteristicas.grid(row=1, column=1, sticky="nsew")
        self.ventana.columnconfigure(1, weight=25)
        self.ventana.rowconfigure(1, weight=2)
        self.frame_caracteristicas.columnconfigure(0, weight=1)
        # Frame para el título
        frame_titulo = ctk.CTkFrame(self.ventana)
        frame_titulo.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)
        titulo = LtkLabel(frame_titulo, texto="Configuración de Tienda de ropa")
        titulo.configure(font=('Poppins', 30, "bold"))
        titulo.grid(row=0, column=0, pady=(1, 1), sticky="nsew")
        frame_titulo.columnconfigure(0, weight=1)
        frame_titulo.rowconfigure(0, weight=1)

        # Frame para las opciones
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
        boton_probadores = LtkButtonLine(frame_opciones, self.probadores, "Probadores")
        boton_probadores.grid(row=3, column=0, padx=(5, 5), pady=(5, 5))
        boton_inventario = LtkButtonLine(frame_opciones, self.inventario, "Inventario")
        boton_inventario.grid(row=4, column=0, padx=(5, 5), pady=(5, 5))
        boton_inventario = LtkButtonLine(frame_opciones, self.precios, "Precios")
        boton_inventario.grid(row=5, column=0, padx=(5, 5), pady=(5, 5))

        # Frame para el botón de guardar
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

        self.ventana.protocol("WM_DELETE_WINDOW", self.guardar_y_cerrar)  # Guardar datos al cerrar la ventana
        self.ventana.mainloop()

    def resetear_frame_caracteristicas(self):
        for widget in self.frame_caracteristicas.winfo_children():
            widget.destroy()

    def mostrar_uso_probadores(self):
        TablaPopup(self.ventana, "Uso de Probadores", self.file_uso_probadores)

    def mostrar_fila_probadores(self):
        TablaPopup(self.ventana, "Fila de Probadores", self.file_fila_probadores)

    def personal(self):
        self.resetear_frame_caracteristicas()
        self.cantidad_empleados = IntVar()
        self.empleados = IntVar()
        self.super = IntVar()
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

        self.label_empleados = LtkLabel(self.frame_caracteristicas, texto="Cantidad de empleados que atienden:")
        self.label_empleados.grid(row=4, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.empleados = LtkEntryLine(self.frame_caracteristicas)
        self.empleados.grid(row=4, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_super = LtkLabel(self.frame_caracteristicas, texto="Cantidad de supervisores:")
        self.label_super.grid(row=5, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.super = LtkEntryLine(self.frame_caracteristicas)
        self.super.grid(row=5, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

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
        self.pa_asesor = StringVar()
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

        self.label_pa_asesor = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de Asesores de ventas:")
        self.label_pa_asesor.grid(row=5, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_pa_asesor = ctk.CTkEntry(self.frame_caracteristicas, textvariable=self.pa_asesor)
        self.entry_pa_asesor.grid(row=5, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_pa_limpieza = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de Personal de limpieza:")
        self.label_pa_limpieza.grid(row=6, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_pa_limpieza = ctk.CTkEntry(self.frame_caracteristicas, textvariable=self.pa_limpieza)
        self.entry_pa_limpieza.grid(row=6, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_pa_inventario = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de Personal de inventario:")
        self.label_pa_inventario.grid(row=7, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_pa_inventario = ctk.CTkEntry(self.frame_caracteristicas, textvariable=self.pa_inventario)
        self.entry_pa_inventario.grid(row=7, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_pa_basicos = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de Servicios básicos:")
        self.label_pa_basicos.grid(row=8, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_pa_basicos = ctk.CTkEntry(self.frame_caracteristicas, textvariable=self.pa_basicos)
        self.entry_pa_basicos.grid(row=8, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_pa_renta = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de Renta:")
        self.label_pa_renta.grid(row=9, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_pa_renta = ctk.CTkEntry(self.frame_caracteristicas, textvariable=self.pa_renta)
        self.entry_pa_renta.grid(row=9, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_ordering_cost = ctk.CTkLabel(self.frame_caracteristicas, text="Costo de administración de pedidos:")
        self.label_ordering_cost.grid(row=10, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_ordering_cost = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_ordering_cost.grid(row=10, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_cost_pantalon = ctk.CTkLabel(self.frame_caracteristicas, text="Costo por pantalón:")
        self.label_cost_pantalon.grid(row=11, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_cost_pantalon = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_cost_pantalon.grid(row=11, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_cost_blusa = ctk.CTkLabel(self.frame_caracteristicas, text="Costo por blusa:")
        self.label_cost_blusa.grid(row=12, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_cost_blusa = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_cost_blusa.grid(row=12, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_cost_ropa_interior = ctk.CTkLabel(self.frame_caracteristicas, text="Costo por ropa interior:")
        self.label_cost_ropa_interior.grid(row=13, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_cost_ropa_interior = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_cost_ropa_interior.grid(row=13, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_holding_cost_per_unit_per_day = ctk.CTkLabel(self.frame_caracteristicas,
                                                                text="Costo de almacenamiento por unidad diaria:")
        self.label_holding_cost_per_unit_per_day.grid(row=14, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_holding_cost_per_unit_per_day = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_holding_cost_per_unit_per_day.grid(row=14, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew",
                                                      columnspan=2)

        self.label_abandonment_cost_per_customer = ctk.CTkLabel(self.frame_caracteristicas,
                                                                text="Costo de abandono por cliente:")
        self.label_abandonment_cost_per_customer.grid(row=15, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_abandonment_cost_per_customer = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_abandonment_cost_per_customer.grid(row=15, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew",
                                                      columnspan=2)

        self.label_costo_fijo_diario = ctk.CTkLabel(self.frame_caracteristicas, text="Costo fijo diario:")
        self.label_costo_fijo_diario.grid(row=16, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_costo_fijo_diario = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_costo_fijo_diario.grid(row=16, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        boton_guardar_costos = LtkButtonFill(self.frame_caracteristicas, self.guardar_datos, "Guardar")
        boton_guardar_costos.grid(row=17, column=0, columnspan=3, pady=(10, 0))

    def horarios(self):
        self.resetear_frame_caracteristicas()
        self.entry_horario_inicio = LtkEntryLine(self.frame_caracteristicas)
        self.entry_horario_inicio.grid(row=3, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")
        self.entry_horario_cierre = LtkEntryLine(self.frame_caracteristicas)
        self.entry_horario_cierre.grid(row=4, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")

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

    def probadores(self):
        self.resetear_frame_caracteristicas()

        self.etiqueta_titulo_probadores = LtkLabel(self.frame_caracteristicas, texto="Configuración de Probadores")
        self.etiqueta_titulo_probadores.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_probadores.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)
        self.cantidad_probadores = IntVar()
        self.probadores_funcionamiento = IntVar()
        self.btn_uso_probadores = LtkButtonLine(self.frame_caracteristicas, self.mostrar_uso_probadores,
                                                "Uso de Probadores")
        self.btn_uso_probadores.grid(row=1, column=0, padx=(10, 10), pady=(5, 5), sticky="nsew")

        self.btn_fila_probadores = LtkButtonLine(self.frame_caracteristicas, self.mostrar_fila_probadores,
                                                 "Fila de Probadores")
        self.btn_fila_probadores.grid(row=2, column=0, padx=(10, 10), pady=(5, 5), sticky="nsew")

        self.label_pa_proba = ctk.CTkLabel(self.frame_caracteristicas, text="Cantidad de probadores:")
        self.label_pa_proba.grid(row=8, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.cantidad_probadores = ctk.CTkEntry(self.frame_caracteristicas, textvariable=self.cantidad_probadores)
        self.cantidad_probadores.grid(row=8, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_pa_prob = ctk.CTkLabel(self.frame_caracteristicas, text="Probadores en funcionamiento:")
        self.label_pa_prob.grid(row=9, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.probadores_funcionamiento = ctk.CTkEntry(self.frame_caracteristicas,
                                                      textvariable=self.probadores_funcionamiento)
        self.probadores_funcionamiento.grid(row=9, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        boton_guardar_personal = LtkButtonFill(self.frame_caracteristicas, self.guardar_datos, "Guardar")
        boton_guardar_personal.grid(row=10, column=0, columnspan=3, pady=(10, 0))

    def precios(self):
        self.resetear_frame_caracteristicas()

        self.etiqueta_titulo_caracteristicas = ctk.CTkLabel(self.frame_caracteristicas,
                                                            text="Ajustes de Probabilidades y Precios de Ventas")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)

        self.label_precio_pantalon = ctk.CTkLabel(self.frame_caracteristicas, text="Precio de Pantalones:")
        self.label_precio_pantalon.grid(row=1, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_precio_pantalon = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_precio_pantalon.grid(row=1, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_precio_blusa = ctk.CTkLabel(self.frame_caracteristicas, text="Precio de Blusas:")
        self.label_precio_blusa.grid(row=2, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_precio_blusa = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_precio_blusa.grid(row=2, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_precio_ropa_interior = ctk.CTkLabel(self.frame_caracteristicas, text="Precio de Ropa Interior:")
        self.label_precio_ropa_interior.grid(row=3, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_precio_ropa_interior = ctk.CTkEntry(self.frame_caracteristicas)
        self.entry_precio_ropa_interior.grid(row=3, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.btn_abrir_tabla = CTkButton(self.frame_caracteristicas, text="Abrir Tabla de Probabilidades de Ventas",
                                         command=self.abrir_tabla_probabilidades)
        self.btn_abrir_tabla.grid(row=4, column=0, columnspan=3, pady=10)

    def abrir_tabla_probabilidades(self):
        self.file_probabilidades_ventas = "prob_ventas.json"
        TablaProbabilidadesVentas(self.ventana, "Probabilidades de Ventas", self.file_probabilidades_ventas)

    def inventario(self):
        self.resetear_frame_caracteristicas()

        self.inventario_pantalones = IntVar()
        self.inventario_blusas = IntVar()
        self.inventario_ropa_interior = IntVar()
        self.cantidad_pantalones = IntVar()
        self.cantidad_blusas = IntVar()
        self.cantidad_ropa_interior = IntVar()

        self.etiqueta_titulo_caracteristicas = LtkLabel(self.frame_caracteristicas, texto="Configuración de Inventario")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)

        self.label_inventario_pantalones = LtkLabel(self.frame_caracteristicas,
                                                    texto="Inventario inicial de pantalones:")
        self.label_inventario_pantalones.grid(row=1, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_inventario_pantalones = LtkEntryLine(self.frame_caracteristicas)
        self.entry_inventario_pantalones.grid(row=1, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_inventario_blusas = LtkLabel(self.frame_caracteristicas, texto="Inventario inicial de blusas:")
        self.label_inventario_blusas.grid(row=2, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_inventario_blusas = LtkEntryLine(self.frame_caracteristicas)
        self.entry_inventario_blusas.grid(row=2, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_inventario_ropa_interior = LtkLabel(self.frame_caracteristicas,
                                                       texto="Inventario inicial de ropa interior:")
        self.label_inventario_ropa_interior.grid(row=3, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_inventario_ropa_interior = LtkEntryLine(self.frame_caracteristicas)
        self.entry_inventario_ropa_interior.grid(row=3, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew",
                                                 columnspan=2)

        self.label_cantidad_pantalones = LtkLabel(self.frame_caracteristicas,
                                                  texto="Cantidad de reabastecimiento de pantalones:")
        self.label_cantidad_pantalones.grid(row=4, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_cantidad_pantalones = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_pantalones.grid(row=4, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_cantidad_blusas = LtkLabel(self.frame_caracteristicas,
                                              texto="Cantidad de reabastecimiento de blusas:")
        self.label_cantidad_blusas.grid(row=5, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_cantidad_blusas = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_blusas.grid(row=5, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.label_cantidad_ropa_interior = LtkLabel(self.frame_caracteristicas,
                                                     texto="Cantidad de reabastecimiento de ropa interior:")
        self.label_cantidad_ropa_interior.grid(row=6, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        self.entry_cantidad_ropa_interior = LtkEntryLine(self.frame_caracteristicas)
        self.entry_cantidad_ropa_interior.grid(row=6, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew", columnspan=2)

        self.btn_reabastecimiento = LtkButtonLine(self.frame_caracteristicas, self.mostrar_reabastecimiento,
                                                  "Reabastecimiento")
        self.btn_reabastecimiento.grid(row=4, column=0, padx=(10, 10), pady=(5, 5), sticky="nsew")

        boton_guardar_inventario = LtkButtonFill(self.frame_caracteristicas, self.guardar_datos, "Guardar")
        boton_guardar_inventario.grid(row=10, column=0, columnspan=3, pady=(10, 0))

    def mostrar_reabastecimiento(self):
        TablaPopupReabastecimiento(self.ventana, "Reabastecimiento", self.file_reabastecimiento)

    def guardar_informacion(self):
        configuracion = self.leer_configuracion()

        # Guardar la información personal si los widgets existen
        if hasattr(self, 'cantidad_empleados') and self.cantidad_empleados.winfo_exists():
            configuracion["personal"] = {
                "cantidad_empleados": self.cantidad_empleados.get(),
                "empleados": self.empleados.get(),
                "supervisores": self.super.get(),
                "limpieza": self.limpieza.get(),
                "inventario": self.inventario.get()
            }

        # Guardar la información de horarios si los widgets existen
        if hasattr(self, 'entry_horario_inicio') and self.entry_horario_inicio.winfo_exists():
            configuracion["horarios"] = {
                "horario_inicio": self.entry_horario_inicio.get(),
                "horario_cierre": self.entry_horario_cierre.get()
            }

        # Guardar la información de costos si los widgets existen
        if hasattr(self, 'gerente') and self.entry_gerente.winfo_exists():
            configuracion["costos"] = {
                "costo_gerente": self.gerente.get(),
                "costo_cajero": self.pa_cajero.get(),
                "costo_asesor": self.pa_asesor.get(),
                "costo_limpieza": self.pa_limpieza.get(),
                "costo_inventario": self.pa_inventario.get(),
                "costo_basicos": self.pa_basicos.get(),
                "costo_renta": self.pa_renta.get(),
                "costo_pedidos": self.entry_ordering_cost.get(),
                "costo_pantalon": self.entry_cost_pantalon.get(),
                "costo_blusa": self.entry_cost_blusa.get(),
                "costo_ropa_interior": self.entry_cost_ropa_interior.get(),
                "costo_almacenamiento_por_unidad_diaria": self.entry_holding_cost_per_unit_per_day.get(),
                "costo_abandono_por_cliente": self.entry_abandonment_cost_per_customer.get(),
                "costo_fijo_diario": self.entry_costo_fijo_diario.get()
            }

        # Guardar la información de precios si los widgets existen
        if hasattr(self, 'precio_pantalon') and self.entry_precio_pantalon.winfo_exists():
            configuracion["precios"] = {
                "precio_pantalon": self.precio_pantalon.get(),
                "precio_blusa": self.precio_blusa.get(),
                "precio_ropa_interior": self.precio_ropa_interior.get()
            }

        # Guardar la información de inventario si los widgets existen
        if hasattr(self, 'entry_inventario_pantalones') and self.entry_inventario_pantalones.winfo_exists():
            configuracion["inventario"] = {
                "pantalones": self.entry_inventario_pantalones.get(),
                "blusas": self.entry_inventario_blusas.get(),
                "ropa_interior": self.entry_inventario_ropa_interior.get(),
                "cantidad_reabastecimiento": {
                    "pantalones": self.entry_cantidad_pantalones.get(),
                    "blusas": self.entry_cantidad_blusas.get(),
                    "ropa_interior": self.entry_cantidad_ropa_interior.get()
                }
            }

        with open(self.file_configuracion, "w") as archivo:
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
        if os.path.exists(self.file_configuracion):
            with open(self.file_configuracion, 'r') as archivo:
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
        TablaFrecuenciaPopup(self.ventana, "Frecuencia de Reabastecimiento", self.file_frecuencia_reabastecimiento)

# Ejecución del programa
if __name__ == "__main__":
    app = ropa()
