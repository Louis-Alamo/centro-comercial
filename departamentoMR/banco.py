from customtkinter import *
from tkinter import messagebox

from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine
from componentes_graficos.LtkEntry import LtkEntryLine, LtkEntryFill
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkComboBox import LtkComboBoxLine
from componentes_graficos.LtkTreeView import LtkFileInputTreeView

import json
import os

class Banco:
    def __init__(self):
        ventana = CTk()
        ventana.title("Configuracion Banco")
        ventana.geometry("1200x800+350+100")
        ventana.configure(bg="#FFFFFF")

        #Frame para titulo
        frame_titulo = CTkFrame(ventana)
        frame_titulo.pack(fill=BOTH, expand=True)
        titulo = LtkLabel(frame_titulo, "Configuracion Banco")
        titulo.configure(font=("Poppins", 40, "bold"))
        titulo.pack(side=TOP, padx=20, pady=20)


        #Frame para personal banco
        frame_personalbanco = CTkFrame(ventana)
        frame_personalbanco.pack(fill=BOTH, expand=True)
        boton_personalbanco = LtkButtonFill(frame_personalbanco, self.personalbanco, "Personal del banco")
        boton_personalbanco.pack(side=LEFT, padx=70, pady=20)
        
        #Frame para horarios
        frame_horarios = CTkFrame(ventana)
        frame_horarios.pack(fill=BOTH, expand=True)
        boton_horarios = LtkButtonFill(frame_horarios, self.horarios, "Horarios")
        boton_horarios.pack(side=LEFT, padx=70, pady=10)

        #Frame para usuarios
        frame_usuarios = CTkFrame(ventana)
        frame_usuarios.pack(fill=BOTH, expand=True)
        boton_usuarios = LtkButtonFill(frame_usuarios, self.usuarios, "Usuarios")
        boton_usuarios.pack(side=LEFT, padx=70, pady=10)

        #Frame para cuentas
        frame_cuentas = CTkFrame(ventana)
        frame_cuentas.pack(fill=BOTH, expand=True)
        boton_cuentas = LtkButtonFill(frame_cuentas, self.cuentas, "Cuentas")
        boton_cuentas.pack(side=LEFT, padx=70, pady=10)

        #Frame para cajeros_automaticos
        frame_cajeros_automaticos = CTkFrame(ventana)
        frame_cajeros_automaticos.pack(fill=BOTH, expand=True)
        boton_cajeros_automaticos = LtkButtonFill(frame_cajeros_automaticos, self.cajeros_automaticos, "Cajeros Automaticos")
        boton_cajeros_automaticos.pack(side=LEFT, padx=70, pady=10)

        #Frame para temporadas
        frame_temporadas = CTkFrame(ventana)
        frame_temporadas.pack(fill=BOTH, expand=True)
        boton_temporadas = LtkButtonFill(frame_temporadas, self.temporadas, "Temporadas")
        boton_temporadas.pack(side=LEFT, padx=70, pady=10)

        frame_guardar = CTkFrame(ventana)
        frame_guardar.pack(fill=BOTH, expand=True)
        boton_guardar = LtkButtonFill(frame_guardar, self.salir, "Salir de Configuracion Banco")
        boton_guardar.pack(side=BOTTOM, padx=20, pady=20)
        
        ventana.mainloop()

    def salir(self):
        messagebox.showinfo("SALIENDO", "Configuracion Guardada")
        exit()



    def personalbanco(self):
        self.ajustes_personal = CTk()
        self.ajustes_personal.title("Ajustes Personal del banco")
        self.ajustes_personal.geometry("800x600+660+210")
        self.ajustes_personal.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.ajustes_personal, self.guardar_personal, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=20, pady=20)
        self.ajustes_personal.mainloop()
    def guardar_personal(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.ajustes_personal.destroy()


    def costos(self):
        self.ajustes_costos = CTk()
        self.ajustes_costos.title("Ajustes Costos")
        self.ajustes_costos.geometry("800x600+660+210")
        self.ajustes_costos.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.ajustes_costos, self.guardar_costos, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=20, pady=20)
        self.ajustes_costos.mainloop()
    def guardar_costos(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.ajustes_costos.destroy()



    def horarios(self):
        self.ajustes_horarios = CTk()
        self.ajustes_horarios.title("Ajustes Horarios")
        self.ajustes_horarios.geometry("800x600+660+210")
        self.ajustes_horarios.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.ajustes_horarios, self.guardar_horarios, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=20, pady=20)
        self.ajustes_horarios.mainloop()
    def guardar_horarios(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.ajustes_horarios.destroy()


    def usuarios(self):
        self.ajustes_usuarios = CTk()
        self.ajustes_usuarios.title("Ajustes Usuarios")
        self.ajustes_usuarios.geometry("800x600+660+210")
        self.ajustes_usuarios.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.ajustes_usuarios, self.guardar_usuarios, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=20, pady=20)
        self.ajustes_usuarios.mainloop()
    def guardar_usuarios(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.ajustes_usuarios.destroy()

    def cuentas(self):
        self.ajustes_cuentas = CTk()
        self.ajustes_cuentas.title("Ajustes Cuentas")
        self.ajustes_cuentas.geometry("800x600+660+210")
        self.ajustes_cuentas.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.ajustes_cuentas, self.guardar_cuentas, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=20, pady=20)
        self.ajustes_cuentas.mainloop()
    def guardar_cuentas(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.ajustes_cuentas.destroy()

    
    def cajeros_automaticos(self):
        self.ajustes_cajeros_automaticos = CTk()
        self.ajustes_cajeros_automaticos.title("Ajustes Cajeros Automaticos")
        self.ajustes_cajeros_automaticos.geometry("800x600+660+210")
        self.ajustes_cajeros_automaticos.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.ajustes_cajeros_automaticos, self.guardar_cajeros_automaticos, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=20, pady=20)
        self.ajustes_cajeros_automaticos.mainloop()
    def guardar_cajeros_automaticos(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.ajustes_cajeros_automaticos.destroy()


    def temporadas(self):
        self.ajustes_temporadas = CTk()
        self.ajustes_temporadas.title("Ajustes Temporadas")
        self.ajustes_temporadas.geometry("800x600+660+210")
        self.ajustes_temporadas.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.ajustes_temporadas, self.guardar_temporadas, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=20, pady=20)
        self.ajustes_temporadas.mainloop()
    def guardar_temporadas(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.ajustes_temporadas.destroy()

