from tkinter import *
from customtkinter import CTk
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkButton import LtkButtonFill

class Gimnasio:
    def __init__(self):
        self.ventana = CTk()
        self.ventana.title("Gimnasio")
        self.ventana.geometry("1500x900")
        self.ventana.config(bg="#1B0018")

        self.frame_principal = Frame(self.ventana, bg="#1B0018")
        self.frame_principal.pack(expand=True, fill=BOTH)

        titulo_label = LtkLabel(self.frame_principal, texto="Configuracion Gimnasio")
        titulo_label.configure(font=('Poppins', 80, "bold"))
        titulo_label.pack(pady=(20, 20))


Gimnasio()