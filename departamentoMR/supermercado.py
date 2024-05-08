from customtkinter import *
from tkinter import messagebox

from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine
from componentes_graficos.LtkEntry import LtkEntryLine, LtkEntryFill
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkComboBox import LtkComboBoxLine
from componentes_graficos.LtkTreeView import LtkFileInputTreeView

import json
import os

class Supermercado:
    def __init__(self):
        ventana = CTk()
        ventana.title("Configuracion Supermercado")
        ventana.geometry("1200x800+350+100")
        ventana.configure(bg="#FFFFFF")

        #Frame para titulo
        frame_titulo = CTkFrame(ventana)
        frame_titulo.pack(fill=BOTH, expand=True)
        titulo = LtkLabel(frame_titulo, "Configuracion Supermercado")
        titulo.configure(font=("Poppins", 40, "bold"))
        titulo.pack(side=TOP, padx=20, pady=20)

        #Frame para empleados supermercado
        frame_empleados = CTkFrame(ventana)
        frame_empleados.pack(fill=BOTH, expand=True)
        boton_empleados = LtkButtonFill(frame_empleados, self.empleados_super, "Empleados")
        boton_empleados.pack(side=LEFT, padx=70, pady=20)

        #Frame para servicio general
        frame_serviciogeneral = CTkFrame(ventana)
        frame_serviciogeneral.pack(fill=BOTH, expand=True)
        boton_serviciogeneral = LtkButtonFill(frame_serviciogeneral, self.serviciogeneral, "Servicio General")
        boton_serviciogeneral.pack(side=LEFT, padx=70, pady=10)

        #Frame cajas
        frame_cajas = CTkFrame(ventana)
        frame_cajas.pack(fill=BOTH, expand=True)
        boton_cajas = LtkButtonFill(frame_cajas, self.cajas, "Cajas")
        boton_cajas.pack(side=LEFT, padx=70, pady=10)

        #Frame para horarios
        frame_horarios = CTkFrame(ventana)
        frame_horarios.pack(fill=BOTH, expand=True)
        boton_horarios = LtkButtonFill(frame_horarios, self.horarios, "Horarios")
        boton_horarios.pack(side=LEFT, padx=70, pady=10)

        #Frame para inventario productos
        frame_inventario = CTkFrame(ventana)
        frame_inventario.pack(fill=BOTH, expand=True)
        boton_inventario = LtkButtonFill(frame_inventario, self.inventario, "Inventario Productos")
        boton_inventario.pack(side=LEFT, padx=70, pady=10)

        #Frame proveedores
        frame_proveedores = CTkFrame(ventana)
        frame_proveedores.pack(fill=BOTH, expand=True)
        boton_proveedores = LtkButtonFill(frame_proveedores, self.proveedores, "Proveedores")
        boton_proveedores.pack(side=LEFT, padx=70, pady=10)

        #Frame clientes
        frame_clientes = CTkFrame(ventana)
        frame_clientes.pack(fill=BOTH, expand=True)
        boton_clientes = LtkButtonFill(frame_clientes, self.clientes, "Clientes")
        boton_clientes.pack(side=LEFT, padx=70, pady=10)

        #Frame pagos
        frame_pagos = CTkFrame(ventana)
        frame_pagos.pack(fill=BOTH, expand=True)
        boton_pagos = LtkButtonFill(frame_pagos, self.pagos, "Pagos")
        boton_pagos.pack(side=LEFT, padx=70, pady=10)

        #Frame temporadas
        frame_temporadas = CTkFrame(ventana)
        frame_temporadas.pack(fill=BOTH, expand=True)
        boton_temporadas = LtkButtonFill(frame_temporadas, self.temporadas, "Temporadas")
        boton_temporadas.pack(side=LEFT, padx=70, pady=10)


        #Frame para salir configuracion
        frame_guardar = CTkFrame(ventana)
        frame_guardar.pack(fill=BOTH, expand=True)
        boton_guardar = LtkButtonFill(frame_guardar, self.salir, "Salir de Configuracion Supermercado")
        boton_guardar.pack(side=BOTTOM, padx=20, pady=20)
        
        ventana.mainloop()

    def salir(self):
        messagebox.showinfo("SALIENDO", "Configuracion Guardada")
        exit()

    def empleados_super(self):
        self.empleados_supermercado=CTk()
        self.empleados_supermercado.title("Ajustes Empleados Supermercado")
        self.empleados_supermercado.geometry("800x600+660+210")
        self.empleados_supermercado.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.empleados_supermercado, self.guardar_empleados_super, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=70, pady=20)
        self.empleados_supermercado.mainloop()
    def guardar_empleados_super(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.empleados_supermercado.destroy()


    def serviciogeneral(self):
        self.serviciogeneral=CTk()
        self.serviciogeneral.title("Ajustes Servicio General")
        self.serviciogeneral.geometry("800x600+660+210")
        self.serviciogeneral.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.serviciogeneral, self.guardar_serviciogeneral, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=70, pady=20)
        self.serviciogeneral.mainloop()
    def guardar_serviciogeneral(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.serviciogeneral.destroy()

    def cajas(self):
        self.cajas=CTk()
        self.cajas.title("Ajustes Cajas")
        self.cajas.geometry("800x600+660+210")
        self.cajas.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.cajas, self.guardar_cajas, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=70, pady=20)
        self.cajas.mainloop()
    def guardar_cajas(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.cajas.destroy()

    def horarios(self):
        self.horarios=CTk()
        self.horarios.title("Ajustes Horarios")
        self.horarios.geometry("800x600+660+210")
        self.horarios.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.horarios, self.guardar_horarios, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=70, pady=20)
        self.horarios.mainloop()
    def guardar_horarios(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.horarios.destroy()


    def inventario(self):
        self.inventario=CTk()
        self.inventario.title("Ajustes Inventario")
        self.inventario.geometry("800x600+660+210")
        self.inventario.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.inventario, self.guardar_inventario, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=70, pady=20)
        self.inventario.mainloop()
    def guardar_inventario(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.inventario.destroy()

    def proveedores(self):
        self.proveedores=CTk()
        self.proveedores.title("Ajustes Proveedores")
        self.proveedores.geometry("800x600+660+210")
        self.proveedores.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.proveedores, self.guardar_proveedores, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=70, pady=20)
        self.proveedores.mainloop()
    def guardar_proveedores(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.proveedores.destroy()

    def clientes(self):
        self.clientes=CTk()
        self.clientes.title("Ajustes Clientes")
        self.clientes.geometry("800x600+660+210")
        self.clientes.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.clientes, self.guardar_clientes, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=70, pady=20)
        self.clientes.mainloop()
    def guardar_clientes(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.clientes.destroy()

    def pagos(self):
        self.pagos=CTk()
        self.pagos.title("Ajustes Pagos")
        self.pagos.geometry("800x600+660+210")
        self.pagos.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.pagos, self.guardar_pagos, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=70, pady=20)
        self.pagos.mainloop()
    def guardar_pagos(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.pagos.destroy()

    def temporadas(self):
        self.temporadas=CTk()
        self.temporadas.title("Ajustes Temporadas")
        self.temporadas.geometry("800x600+660+210")
        self.temporadas.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.temporadas, self.guardar_temporadas, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=70, pady=20)
        self.temporadas.mainloop()
    def guardar_temporadas(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.temporadas.destroy()

