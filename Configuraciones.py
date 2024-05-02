from tkinter import *
from componentes_graficos.LtkComboBox import LtkComboBoxLine
from componentes_graficos.LtkButton import LtkButtonFill

from centro_comercial_configuraciones import Centro_comercial_configuraciones
from departamentoLG.cine.ConfiguracionCine import ConfiguracionCine



from departamentoMR.gimnasio import Gimnasio
from departamentoMR.banco import Banco
from departamentoMR.supermercado import Supermercado
from departamentoMR.veterinaria import Veterinaria
from departamentoMR.alimentos import Alimentos

class Configuraciones:

    def __init__(self):

        self.ventana = Tk()
        self.ventana.title("Configuraciones")
        self.ventana.resizable(False, False)
        self.ventana.config(bg = "#FFFFFF")



        self.titulo = Label(self.ventana, text = "Configuraciones", font = ("Poppins", 20, "bold"), bg = "#FFFFFF", fg = "#000000")
        self.titulo.pack(pady = 20, fill = X)

        self.crear_componentes()

        self.ventana.mainloop()

    def crear_componentes(self):

        self.frame1 = Frame(self.ventana, bg = "#FFFFFF")
        self.frame1.pack()

        self.combo = LtkComboBoxLine(master=self.frame1,
                                     opciones=["Centro Comercial", "Cine", "Electronica", "Jugeteria", "libreria",
                                               "Restaurante", "Alimentos", "Banco", "Gimnasio", "Supermercado",
                                               "Veterinaria"])
        self.combo.pack(pady = 20, padx = 20, side = LEFT)

        self.boton_abrir_configuracion = LtkButtonFill(master=self.frame1, funcion=lambda: self.abrir_configuracion(),nombre_boton="Abrir configuracion")
        self.boton_abrir_configuracion.pack(pady = 20, padx = 20, side = LEFT)

    def abrir_configuracion(self):
        if self.combo.get() == "Centro Comercial":
            self.configuracion_centro_comercial()

        elif self.combo.get() == "Cine":
            self.configuracion_cine()

        elif self.combo.get() == "Electronica":
            self.configuracion_electronica()

        elif self.combo.get() == "Jugeteria":
            self.configuracion_jugeteria()

        elif self.combo.get() == "libreria":
            self.configuracion_libreria()

        elif self.combo.get() == "Restaurante":
            self.configuracion_restaurante()

        elif self.combo.get() == "Alimentos":
            self.configuracion_alimentos()

        elif self.combo.get() == "Banco":
            self.configuracion_banco()

        elif self.combo.get() == "Gimnasio":
            self.configuracion_gimnasios()

        elif self.combo.get() == "Supermercado":
            self.configuracion_supermercado()

        elif self.combo.get() == "Veterinaria":
            self.configuracion_veterinaria()


    def configuracion_centro_comercial(self):
        Centro_comercial_configuraciones()

    def configuracion_cine(self):
        ConfiguracionCine()

    def configuracion_electronica(self):
        print("Configuracion Electronica")

    def configuracion_jugeteria(self):
        print("Configuracion Jugeteria")

    def configuracion_libreria(self):
        print("Configuracion libreria")

    def configuracion_restaurante(self):
        print("Configuracion Restaurante")

    def configuracion_alimentos(self):
        Alimentos()

    def configuracion_banco(self):
        Banco()

    def configuracion_gimnasios(self):
        Gimnasio()

    def configuracion_supermercado(self):
        Supermercado()

    def configuracion_veterinaria(self):
        Veterinaria()





