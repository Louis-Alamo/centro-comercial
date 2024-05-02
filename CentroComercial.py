from tkinter import *
from componentes_graficos.LtkButton import LtkButtonFill


class CentroComercial():

    def __init__(self):

        self.ventana = Tk()
        self.ventana.title("Centro Comercial")
        self.ventana.geometry("800x600")
        self.ventana.resizable(0,0)
        self.ventana.config(bg = "#FFFFFF")

        self.titulo = Label(self.ventana, text = "Centro Comercial", font = ("Poppins", 20, "bold"), bg = "#FFFFFF", fg = "#000000")
        self.titulo.place(x = 300, y = 20)

        self.crear_componentes()

        self.ventana.mainloop()

    def crear_componentes(self):
        boton_ejecucion = LtkButtonFill(master=self.ventana, nombre_boton="Iniciar simulacion", funcion=lambda: self.iniciar_simulacion())
        boton_ejecucion.place(x = 300, y = 100)


    def iniciar_simulacion(self):
        print("Iniciando simulacion")

