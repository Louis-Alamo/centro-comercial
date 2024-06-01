from tkinter import *
from componentes_graficos.LtkButton import LtkButtonFill
from departamentoMR.SIMULACION_VETERINARIA import SimulacionVeterinaria
from departamentoMR.SIMULACION_GIMNASIO import SimulacionGimnasio
from departamentoMR.SIMULACION_BANCO import SimulacionBanco

from departamentoRH.Simulacion_ropa import SimulacionRopa
from departamentoRH.Simulacion_farmacia import SimulacionFarmacia
from departamentoRH.configuracion_estacionamiento import SimulacionEstacionamiento

class CentroComercial():

    def __init__(self, cantidad_dias):
        print(cantidad_dias)
        self.cantidad_dias = cantidad_dias
        self.ventana = Tk()
        self.ventana.title("Centro Comercial")
        self.ventana.geometry("800x600")
        self.ventana.config(bg = "#FFFFFF")

        self.titulo = Label(self.ventana, text = "Centro Comercial", font = ("Poppins", 20, "bold"), bg = "#FFFFFF", fg = "#000000")
        self.titulo.place(x = 300, y = 20)

        self.crear_componentes()

        self.ventana.mainloop()

    def crear_componentes(self):
        frame_botones = Frame(self.ventana, bg="#FFFFFF")
        frame_botones.place(relx=0.5, rely=0.5, anchor=CENTER)

        boton_gimnasio = LtkButtonFill(frame_botones, funcion=lambda: self.abrir_gimnasio(), nombre_boton="Gimnasio")
        boton_gimnasio.grid(row=0, column=0, padx=20, pady=20)

        boton_banco = LtkButtonFill(frame_botones, funcion=lambda: self.abrir_banco(), nombre_boton="Banco")
        boton_banco.grid(row=0, column=1, padx=20, pady=20)

        boton_veterinaria = LtkButtonFill(frame_botones, funcion=lambda: self.abrir_veterinaria(), nombre_boton="Veterinaria")
        boton_veterinaria.grid(row=0, column=2, padx=20, pady=20)

        boton_estacionamiento = LtkButtonFill(frame_botones, funcion=lambda: self.abrir_estacionamiento(), nombre_boton="Estacionamiento")
        boton_estacionamiento.grid(row=1, column=0, padx=20, pady=20)

        boton_farmacia = LtkButtonFill(frame_botones, funcion=lambda: self.abrir_farmacia, nombre_boton="Farmacia")
        boton_farmacia.grid(row=1, column=1, padx=20, pady=20)

        boton_ropa = LtkButtonFill(frame_botones, funcion=lambda: self.abrir_ropa(), nombre_boton="Ropa")
        boton_ropa.grid(row=1, column=2, padx=20, pady=20)

        boton_jugueteria = LtkButtonFill(frame_botones, funcion=lambda: self.abrir_tienda(), nombre_boton="Jugueteria")
        boton_jugueteria.grid(row=2, column=0, padx=20, pady=20)

        boton_libreria = LtkButtonFill(frame_botones, funcion=lambda: self.abrir_tienda(), nombre_boton="Libreria")
        boton_libreria.grid(row=2, column=1, padx=20, pady=20)

        boton_electronica = LtkButtonFill(frame_botones, funcion=lambda: self.abrir_tienda(), nombre_boton="Electronica")
        boton_electronica.grid(row=2, column=2, padx=20, pady=20)

    def abrir_gimnasio(self):
        SimulacionGimnasio(self.cantidad_dias)

    def abrir_banco(self):
        SimulacionBanco(self.cantidad_dias)

    def abrir_veterinaria(self):
        SimulacionVeterinaria(self.cantidad_dias)

    def abrir_estacionamiento(self):
        SimulacionEstacionamiento(self.cantidad_dias)

    def abrir_farmacia(self):
        SimulacionFarmacia(self.cantidad_dias)

    def abrir_ropa(self):
        SimulacionRopa(self.cantidad_dias)
