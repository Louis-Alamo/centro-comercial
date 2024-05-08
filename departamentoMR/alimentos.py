from customtkinter import *
from tkinter import messagebox

from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine
from componentes_graficos.LtkEntry import LtkEntryLine, LtkEntryFill
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkComboBox import LtkComboBoxLine
from componentes_graficos.LtkTreeView import LtkFileInputTreeView

import json
import os

class Alimentos:
    def __init__(self):
        ventana = CTk()
        ventana.title("Configuracion Alimentos")
        ventana.geometry("1200x800+350+100")
        ventana.configure(bg="#FFFFFF")

        #Frame para titulo
        frame_titulo = CTkFrame(ventana)
        frame_titulo.pack(fill=BOTH, expand=True)
        titulo = LtkLabel(frame_titulo, "Configuracion Alimentos")
        titulo.configure(font=("Poppins", 40, "bold"))
        titulo.pack(side=TOP, padx=20, pady=20)

        
        ventana.mainloop()

    def salir(self):
        messagebox.showinfo("SALIENDO", "Configuracion Guardada")
        exit()

Alimentos()