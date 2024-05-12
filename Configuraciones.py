from tkinter import *
from customtkinter import CTk, CTkFrame
from componentes_graficos.LtkComboBox import LtkComboBoxLine
from componentes_graficos.LtkButton import LtkButtonFill
from componentes_graficos.LtkLabel import LtkLabel

from centro_comercial_configuraciones import Centro_comercial_configuraciones
from departamentoLG.cine.ConfiguracionCine import ConfiguracionCine
from departamentoLG.jugueteria.ConfiguracionJugueteria import Configuracion_jugueteria
from departamentoLG.libreria.ConfiguracionLibreria import ConfiguracionLibreria
from departamentoLG.electronica.ConfiguracionElectronica import ConfiguracionElectronica
from departamentoLG.restaurante.ConfiguracionRestaurante import ConfiguracionRestaurante



from departamentoMR.gimnasio import Gimnasio
from departamentoMR.banco import Banco
from departamentoMR.supermercado import Supermercado
from departamentoMR.veterinaria import Veterinaria
from departamentoMR.alimentos import Alimentos



from departamentoRH.Ropa import ropa
from departamentoRH.Hogar import hogar
from departamentoRH.Farmacia import farmacia
from departamentoRH.Estacionamiento import estacionamiento
from departamentoRH.Restaurante_serv_com import restaurante_ser_com



from CentroComercial import CentroComercial



class Configuraciones:

    def __init__(self):

        self.ventana = CTk()
        self.ventana.title("Configuraciones")
        self.ventana.resizable(False, False)
        #self.ventana.config(bg = "#FFFFFF")



        self.titulo = LtkLabel(self.ventana, texto = "Configuraciones de los departamentos")
        self.titulo.configure(font = ("Poppins", 20, "bold"))
        self.titulo.pack(pady = 20, fill = X)

        self.crear_componentes()

        self.ventana.mainloop()

    def crear_componentes(self):

        self.frame1 = CTkFrame(self.ventana)
        self.frame1.pack(pady = 20, padx = 20,  fill = X)

        self.combo = LtkComboBoxLine(master=self.frame1,
                                     opciones=["Centro Comercial", "Cine", "Electronica", "libreria",
                                               "Restaurante", "Alimentos", "Banco", "Gimnasio", "Supermercado",
                                               "Veterinaria", "Ropa", "Hogar", "Farmacia", "Estacionamiento","Restaurante_serv_com"])
        self.combo.pack(pady = 20, padx = 20, side = LEFT)

        self.boton_abrir_configuracion = LtkButtonFill(master=self.frame1, funcion=lambda: self.abrir_configuracion(),nombre_boton="Abrir configuracion")
        self.boton_abrir_configuracion.pack(pady = 20, padx = 20, side = LEFT)

        self.boton_comenzar_simulacion = LtkButtonFill(master=self.ventana, funcion=lambda: self.comenzar_simulacion(),nombre_boton="Comenzar simulacion")
        self.boton_comenzar_simulacion.pack(pady = 20, padx = 20, side = BOTTOM)


    def comenzar_simulacion(self):
        self.ventana.withdraw()
        CentroComercial()

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

        elif self.combo.get() == "Ropa":
            self.configuracion_ropa()

        elif self.combo.get() == "Hogar":
            self.configuracion_hogar()

        elif self.combo.get() == "Farmacia":
            self.configuracion_farmacia()

        elif self.combo.get() == "Estacionamiento":
            self.configuracion_estacionamiento()

        elif self.combo.get() == "Restaurante_serv_com":
            self.configuracion_restaurante_serv_com()



    def configuracion_centro_comercial(self):
        Centro_comercial_configuraciones()

    def configuracion_cine(self):
        ConfiguracionCine()

    def configuracion_electronica(self):
        ConfiguracionElectronica()

    def configuracion_jugeteria(self):
        Configuracion_jugueteria()

    def configuracion_libreria(self):
        ConfiguracionLibreria()

    def configuracion_restaurante(self):
        ConfiguracionRestaurante()

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

    def configuracion_ropa(self):
        ropa()

    def configuracion_hogar(self):
        hogar()

    def configuracion_farmacia(self):
        farmacia()

    def configuracion_estacionamiento(self):
        estacionamiento()

    def configuracion_restaurante_serv_com(self):
        restaurante_ser_com()






