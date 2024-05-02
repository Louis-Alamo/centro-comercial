from componentes_graficos.LtkButton import LtkButtonFill
from componentes_graficos.LtkEntry import LtkEntryLine
from tkinter import *

class Gimnasio():

    def __init__(self):
        self.ventana=Tk()
        self.ventana.title("Gimnasio")
        self.ventana.geometry("1500x900")
        self.ventana.resizable(0,0)
        self.ventana.config(bg="#FFFFFF")

        self.titulo=Label(self.ventana, text="Gimnasio", font=("Poppins", 20, "bold"), bg="#FFFFFF", fg="#000000")
        self.titulo.place(x=690, y=485)

        boton_ejecucion=LtkButtonFill(master=self.ventana, nombre_boton="Iniciar simulacion", funcion=lambda: self.iniciar_simulacion())
        boton_ejecucion.place(x=685, y=520)


        EnEspera=Label(self.ventana,text="EN ESPERA",font=("Poppins", 15, "bold"),bg="#FF0000",fg="#000000")
        EnEspera.place(x=1,y=1)
        pasillo1=Label(self.ventana,text="Pasillo 1",font=("Poppins", 15, "bold"),bg="#FFFFFF",fg="#000000")
        pasillo1.place(x=150,y=80)
        entry1=LtkEntryLine(self.ventana, "% de atraccion")
        entry1.place(x=150,y=120)
        pasillo2=Label(self.ventana,text="Pasillo 2",font=("Poppins", 15, "bold"),bg="#FFFFFF",fg="#000000")
        pasillo2.place(x=150,y=500)
        entry2=LtkEntryLine(self.ventana, "% de atraccion")
        entry2.place(x=150,y=540)
        pasillo3=Label(self.ventana,text="Pasillo 3",font=("Poppins", 15, "bold"),bg="#FFFFFF",fg="#000000")
        pasillo3.place(x=1300,y=80)
        entry3=LtkEntryLine(self.ventana, "% de atraccion")
        entry3.place(x=1300,y=120)
        pasillo4=Label(self.ventana,text="Pasillo 4",font=("Poppins", 15, "bold"),bg="#FFFFFF",fg="#000000")
        pasillo4.place(x=1300,y=500)
        entry4=LtkEntryLine(self.ventana, "% de atraccion")
        entry4.place(x=1300,y=540)

        self.textarea=Text(self.ventana, width=100, height=30)
        self.textarea.place(x=370, y=1) 

        self.ventana.mainloop()


    def iniciar_simulacion(self):
        print("Iniciando simulacion")


