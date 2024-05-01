from tkinter import *
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkEntry import LtkEntryFill

class Alimentos(Frame):

    def __init__(self, master,):
        super().__init__(master)

        etiqueta1=LtkLabel(self, "PRECIO DE REVISTAS AL PUBLICO")
        etiqueta1.pack()
        etiqueta1.place(x=10, y=0)
        self.entrada1=LtkEntryFill(self)
        self.entrada1.pack()
        self.entrada1.place(x=10, y=30)
        etiqueta2=LtkLabel(self, "COSTO POR REVISTA DIRECTO AL PROVEEDOR")
        etiqueta2.pack()
        etiqueta2.place(x=10, y=60)
        self.entrada2=LtkEntryFill(self, placeholder="COSTO POR REVISTA DIRECTO AL PROVEEDOR")
        self.entrada2.pack()
        self.entrada2.place(x=10, y=90)
        etiqueta3=LtkLabel(self, "CANTIDAD DE REVISTAS PARA COMENZAR CADA MES")
        etiqueta3.pack()
        etiqueta3.place(x=10, y=120)
        self.entrada3=LtkEntryFill(self)
        self.entrada3.pack()
        self.entrada3.place(x=10, y=150)
        etiqueta4=LtkLabel(self, "PRECIO DE VOLVER A COMPRAR REVISTAS")
        etiqueta4.pack()
        etiqueta4.place(x=10, y=180)
        self.entrada4=LtkEntryFill(self)
        self.entrada4.pack()
        self.entrada4.place(x=10, y=210)
        etiqueta5=LtkLabel(self, "CUANTAS REVISTAS COMPRAR CADA 10 DIAS")
        etiqueta5.pack()
        etiqueta5.place(x=10, y=240)
        self.entrada5=LtkEntryFill(self)
        self.entrada5.pack()
        self.entrada5.place(x=10, y=270)
        etiqueta6=LtkLabel(self, "PRECIO DE VENDER REVISTAS SOBRANTES")
        etiqueta6.pack()
        etiqueta6.place(x=10, y=300)
        self.entrada6=LtkEntryFill(self)
        self.entrada6.pack()
        self.entrada6.place(x=10, y=330)
        etiqueta7=LtkLabel(self, "NOMBRE DEL ARCHIVO.TXT")
        etiqueta7.pack()

        self.entrada7=LtkEntryFill(self)
        self.entrada7.pack()
        etiqueta8=LtkLabel(self,"PRIMEROS 10 DIAS")
        etiqueta8.pack()
        etiqueta8.place(x=720, y=110)




        self.check1_var=IntVar()
        self.check1=Checkbutton(self, text="PROBABILIDAD ESTABLECIDA", variable=self.check1_var, command=lambda: self.obtener_probabilidades)
        self.check1.pack()
        self.check1.place(x=720, y=140)

        self.check2_var=IntVar()
        self.check2=Checkbutton(self, text="PROBABILIDAD PERSONALIZADA", variable=self.check2_var, command=lambda: self.ingresar_probabilidad)
        self.check2.pack()
        self.check2.place(x=720, y=160)
        etiqueta9=LtkLabel(self,"SIGUIENTES 20 DIAS")
        etiqueta9.pack()
        etiqueta9.place(x=720, y=200)
        self.check3_var=IntVar()
        self.check3=Checkbutton(self, text="PROBABILIDAD ESTABLECIDA", variable=self.check3_var, command=lambda: self.obtener_probabilidades)
        self.check3.pack()
        self.check3.place(x=720, y=230)

        self.check4_var=IntVar()
        self.check4=Checkbutton(self, text="PROBABILIDAD PERSONALIZADA", variable=self.check4_var, command=lambda: self.ingresar_probabilidad)
        self.check4.pack()
        self.check4.place(x=720, y=250)




ventana=Tk()
ventana.geometry("800x850")
ventana.title("ALIMENTOS")
ventana.resizable(width=False, height=False)
mr=Alimentos(ventana)
mr.pack(expand=True, fill=BOTH, padx=10, pady=10)
ventana.mainloop()









