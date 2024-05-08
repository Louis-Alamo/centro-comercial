from customtkinter import *
from tkinter import messagebox

from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine
from componentes_graficos.LtkEntry import LtkEntryLine, LtkEntryFill
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkComboBox import LtkComboBoxLine
from componentes_graficos.LtkTreeView import LtkFileInputTreeView

import json
import os

class Veterinaria:
    def __init__(self):
        ventana = CTk()
        ventana.title("Configuracion Veterinaria")
        ventana.geometry("1200x800+350+100")
        ventana.configure(bg="#FFFFFF")

        #Frame para titulo
        frame_titulo = CTkFrame(ventana)
        frame_titulo.pack(fill=BOTH, expand=True)
        titulo = LtkLabel(frame_titulo, "Configuracion Veterinaria")
        titulo.configure(font=("Poppins", 40, "bold"))
        titulo.pack(side=TOP, padx=20, pady=20)

        #Frame servicio general
        frame_serviciogeneral = CTkFrame(ventana)
        frame_serviciogeneral.pack(fill=BOTH, expand=True)
        boton_serviciogeneral = LtkButtonFill(frame_serviciogeneral, self.serviciogeneral, "Servicio General")
        boton_serviciogeneral.pack(side=LEFT, padx=70, pady=10)

        #Frame personal
        frame_personal = CTkFrame(ventana)
        frame_personal.pack(fill=BOTH, expand=True)
        boton_personal = LtkButtonFill(frame_personal, self.personal, "Personal")
        boton_personal.pack(side=LEFT, padx=70, pady=20)

        #Frame atencion
        frame_atencion = CTkFrame(ventana)
        frame_atencion.pack(fill=BOTH, expand=True)
        boton_atencion = LtkButtonFill(frame_atencion, self.atencion, "Atencion")
        boton_atencion.pack(side=LEFT, padx=70, pady=10)

        #Frame productos
        frame_productos = CTkFrame(ventana)
        frame_productos.pack(fill=BOTH, expand=True)
        boton_productos = LtkButtonFill(frame_productos, self.productos, "Productos")
        boton_productos.pack(side=LEFT, padx=70, pady=10)

        #Frame costos
        frame_costos = CTkFrame(ventana)
        frame_costos.pack(fill=BOTH, expand=True)
        boton_costos = LtkButtonFill(frame_costos, self.costos, "Costos")
        boton_costos.pack(side=LEFT, padx=70, pady=10)

        #Frame mascotas
        frame_mascotas = CTkFrame(ventana)
        frame_mascotas.pack(fill=BOTH, expand=True)
        boton_mascotas = LtkButtonFill(frame_mascotas, self.mascotas, "Mascotas")
        boton_mascotas.pack(side=LEFT, padx=70, pady=10)

        #Frame para salir configuracion
        frame_guardar = CTkFrame(ventana)
        frame_guardar.pack(fill=BOTH, expand=True)
        boton_guardar = LtkButtonFill(frame_guardar, self.salir, "Salir de Configuracion Supermercado")
        boton_guardar.pack(side=BOTTOM, padx=20, pady=20)
        
        ventana.mainloop()

    def salir(self):
        messagebox.showinfo("SALIENDO", "Configuracion Guardada")
        exit()

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

    def personal(self):
        self.personal=CTk()
        self.personal.title("Ajustes personal")
        self.personal.geometry("800x600+660+210")
        self.personal.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.personal, self.guardar_personal, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=70, pady=20)
        self.personal.mainloop()
    def guardar_personal(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.personal.destroy()


    def atencion(self):
        self.atencion=CTk()
        self.atencion.title("Ajustes Atencion")
        self.atencion.geometry("800x600+660+210")
        self.atencion.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.atencion, self.guardar_atencion, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=70, pady=20)
        self.atencion.mainloop()
    def guardar_atencion(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.atencion.destroy()


    def productos(self):
        self.productos=CTk()
        self.productos.title("Ajustes Productos")
        self.productos.geometry("800x600+660+210")
        self.productos.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.productos, self.guardar_productos, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=70, pady=20)
        self.productos.mainloop()
    def guardar_productos(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.productos.destroy()


    def costos(self):
        self.costos=CTk()
        self.costos.title("Ajustes Costos")
        self.costos.geometry("800x600+660+210")
        self.costos.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.costos, self.guardar_costos, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=70, pady=20)
        self.costos.mainloop()
    def guardar_costos(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.costos.destroy()


    def mascotas(self):
        self.mascotas=CTk()
        self.mascotas.title("Ajustes Mascotas")
        self.mascotas.geometry("800x600+660+210")
        self.mascotas.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.mascotas, self.guardar_mascotas, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=70, pady=20)
        self.mascotas.mainloop()
    def guardar_mascotas(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.mascotas.destroy()

