from componentes_graficos.LtkButton import LtkButtonFill
from componentes_graficos.LtkTextBox import LtkTextboxFill
from tkinter import *
from PIL import Image, ImageTk

class Gimnasio():

    def __init__(self):
        self.ventana=Tk()
        self.ventana.title("Gimnasio")
        self.ventana.geometry("1500x900")
        self.ventana.resizable(0,0)
        self.ventana.config(bg="#FFFFFF")

        ruta_imagen="D:\\MIIGUEL ROSALES\\Documentos\\ISC - ITSZaS\\Cuarto Semestre\\SIMULACION\\PROYECTO\\centro-comercial\\departamentoMR\\gimnasio.jpg"

        imagen=Image.open(ruta_imagen)
        foto=ImageTk.PhotoImage(imagen)
        self.label_imagen=Label(self.ventana, image=foto, bg="#FFFFFF")
        self.label_imagen.image=foto
        self.label_imagen.place(x=0, y=0)


        self.titulo=Label(self.ventana, text="Gimnasio", font=("Poppins", 20, "bold"), bg="#FFFFFF", fg="#000000")
        self.titulo.place(x=300, y=10)

        self.crear_componentes()

        self.ventana.mainloop()

    def crear_componentes(self):
        boton_ejecucion=LtkButtonFill(master=self.ventana, nombre_boton="Iniciar simulacion", funcion=lambda: self.iniciar_simulacion())
        boton_ejecucion.place(x=295, y=50)

        pasillo1=Label(self.ventana,text="Pasillo 1",font=("Poppins", 15, "bold"),bg="#FFFFFF",fg="#000000")
        pasillo1.place(x=150,y=200)
        pasillo2=Label(self.ventana,text="Pasillo 2",font=("Poppins", 15, "bold"),bg="#FFFFFF",fg="#000000")
        pasillo2.place(x=150,y=350)
        pasillo3=Label(self.ventana,text="Pasillo 3",font=("Poppins", 15, "bold"),bg="#FFFFFF",fg="#000000")
        pasillo3.place(x=150,y=400)
        pasillo4=Label(self.ventana,text="Pasillo 4",font=("Poppins", 15, "bold"),bg="#FFFFFF",fg="#000000")
        pasillo4.place(x=150,y=550)

        self.textarea=Text(self.ventana, width=100, height=30)
        self.textarea.place(x=680, y=20) 


    def iniciar_simulacion(self):
        print("Iniciando simulacion")


Gimnasio()