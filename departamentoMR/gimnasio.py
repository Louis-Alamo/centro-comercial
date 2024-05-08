from customtkinter import *
from tkinter import messagebox

from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine
from componentes_graficos.LtkEntry import LtkEntryLine, LtkEntryFill
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkComboBox import LtkComboBoxLine
from componentes_graficos.LtkTreeView import LtkFileInputTreeView

import json
import os

class Gimnasio:
    def __init__(self):
        ventana = CTk()
        ventana.title("Configuracion Gimnasio")
        ventana.geometry("1200x800+350+100")
        ventana.configure(bg="#FFFFFF")

        #Frame para titulo
        frame_titulo = CTkFrame(ventana)
        frame_titulo.pack(fill=BOTH, expand=True)
        titulo = LtkLabel(frame_titulo, "Configuracion Gimnasio")
        titulo.configure(font=("Poppins", 40, "bold"))
        titulo.pack(side=TOP, padx=20, pady=20)


        #Frame para personalGYM
        frame_personalGYM = CTkFrame(ventana)
        frame_personalGYM.pack(fill=BOTH, expand=True)
        boton_personalGYM = LtkButtonFill(frame_personalGYM, self.personalgym, "Personal del GYM")
        boton_personalGYM.pack(side=LEFT, padx=70, pady=20)
        
        #Frame costo
        frame_costo = CTkFrame(ventana)
        frame_costo.pack(fill=BOTH, expand=True)
        boton_costos = LtkButtonFill(frame_costo, self.costos, "Costos")
        boton_costos.pack(side=LEFT, padx=70, pady=10)

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

        #Frame para maquinas
        frame_maquinas = CTkFrame(ventana)
        frame_maquinas.pack(fill=BOTH, expand=True)
        boton_maquinas = LtkButtonFill(frame_maquinas, self.maquinas, "Maquinas")
        boton_maquinas.pack(side=LEFT, padx=70, pady=10)

        #Frame para servicio general
        frame_serviciogeneral = CTkFrame(ventana)
        frame_serviciogeneral.pack(fill=BOTH, expand=True)
        boton_serviciogeneral = LtkButtonFill(frame_serviciogeneral, self.serviciogeneral, "Servicio General")
        boton_serviciogeneral.pack(side=LEFT, padx=70, pady=10)

        #Frame para baños
        frame_baños = CTkFrame(ventana)
        frame_baños.pack(fill=BOTH, expand=True)
        boton_baños = LtkButtonFill(frame_baños, self.baños, "Baños")
        boton_baños.pack(side=LEFT, padx=70, pady=10)

        #Frame para vestidores
        frame_vestidores = CTkFrame(ventana)
        frame_vestidores.pack(fill=BOTH, expand=True)
        boton_vestidores = LtkButtonFill(frame_vestidores, self.vestidores, "Vestidores")
        boton_vestidores.pack(side=LEFT, padx=70, pady=10)

        #Frame para temporadas
        frame_temporadas = CTkFrame(ventana)
        frame_temporadas.pack(fill=BOTH, expand=True)
        boton_temporadas = LtkButtonFill(frame_temporadas, self.temporadas, "Temporadas")
        boton_temporadas.pack(side=LEFT, padx=70, pady=10)

        #Frame para salir configuracion
        frame_guardar = CTkFrame(ventana)
        frame_guardar.pack(fill=BOTH, expand=True)
        boton_guardar = LtkButtonFill(frame_guardar, self.salir, "Salir de Configuracion Gimnasio")
        boton_guardar.pack(side=BOTTOM, padx=20, pady=20)
        
        ventana.mainloop()

    def salir(self):
        messagebox.showinfo("SALIENDO", "Configuracion Guardada")
        exit()



    def personalgym(self):
        self.ajustes_personal = CTk()
        self.ajustes_personal.title("Ajustes Personal del GYM")
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

    
    def maquinas(self):
        self.ajustes_maquinas = CTk()
        self.ajustes_maquinas.title("Ajustes Maquinas")
        self.ajustes_maquinas.geometry("800x600+660+210")
        self.ajustes_maquinas.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.ajustes_maquinas, self.guardar_maquinas, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=20, pady=20)
        self.ajustes_maquinas.mainloop()
    def guardar_maquinas(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.ajustes_maquinas.destroy()

    def serviciogeneral(self):
        self.ajustes_serviciogeneral = CTk()
        self.ajustes_serviciogeneral.title("Ajustes Servicio General")
        self.ajustes_serviciogeneral.geometry("800x600+660+210")
        self.ajustes_serviciogeneral.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.ajustes_serviciogeneral, self.guardar_serviciogeneral, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=20, pady=20)
        self.ajustes_serviciogeneral.mainloop()
    def guardar_serviciogeneral(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.ajustes_serviciogeneral.destroy()


    def baños(self):
        self.ajustes_baños = CTk()
        self.ajustes_baños.title("Ajustes Baños")
        self.ajustes_baños.geometry("800x600+660+210")
        self.ajustes_baños.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.ajustes_baños, self.guardar_baños, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=20, pady=20)
        self.ajustes_baños.mainloop()
    def guardar_baños(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.ajustes_baños.destroy()

    def vestidores(self):
        self.ajustes_vestidores = CTk()
        self.ajustes_vestidores.title("Ajustes Vestidores")
        self.ajustes_vestidores.geometry("800x600+660+210")
        self.ajustes_vestidores.configure(bg="#FFFFFF")
        boton_guardar = LtkButtonFill(self.ajustes_vestidores, self.guardar_vestidores, "Guardar Y Salir De Ajustes")
        boton_guardar.pack(side=BOTTOM, padx=20, pady=20)
        self.ajustes_vestidores.mainloop()
    def guardar_vestidores(self):
        messagebox.showinfo("GUARDADO", "Ajustes Guardados")
        self.ajustes_vestidores.destroy()

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
