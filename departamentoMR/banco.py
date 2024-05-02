from tkinter import *
from customtkinter import CTk
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkButton import LtkButtonFill

class Banco:
    def __init__(self):
        self.ventana = CTk()
        self.ventana.title("Banco")
        
        self.ventana.geometry("1500x900")
        self.ventana.config(bg="#002C6C")

        self.frame_principal = Frame(self.ventana, bg="#002C6C")
        self.frame_principal.pack(expand=True, fill=BOTH)

        titulo_label = LtkLabel(self.frame_principal, texto="Banco")
        titulo_label.configure(font=('Poppins', 80, "bold", "underline"))
        titulo_label.pack(pady=(3, 3))
        
        self.crear_seccion_cajeros()
        self.crear_seccion_secretarias()
        self.crear_seccion_cajerosautomaticos()
        

        boton_ejecucion = LtkButtonFill(self.frame_principal, nombre_boton="Iniciar simulación", funcion=lambda: self.iniciar_simulacion())
        boton_ejecucion.pack(pady=3)

        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)
        self.text_area = Text(self.frame_principal, width=10, height=30)
        self.text_area.pack(pady=10, padx=400, fill=BOTH, expand=True)


        self.ventana.mainloop()

    def crear_seccion_cajeros(self):
        frame_cajeros = Frame(self.frame_principal, bg="#002C6C")
        frame_cajeros.pack(pady=3)

        cajeros = [
            ("VENTANILLA 1", 150),
            ("VENTANILLA 2", 450),
            ("VENTANILLA 3", 750),
            ("VENTANILLA 4", 1050)
        ]

        for caja, x_pos in cajeros:
            frame_caja = Frame(frame_cajeros, bg="#458FFB")
            frame_caja.pack(side=LEFT, padx=50)

            label_caja = Label(frame_caja, text=caja, font=("Poppins", 15, "bold"), bg="#458FFB", fg="#FFFFFF")
            label_caja.pack()

            entry_atraccion = LtkEntryLine(frame_caja, "% de atracción")
            entry_atraccion.pack(pady=10)

            frame_cajas = Frame(frame_caja, bg="#458FFB")
            frame_cajas.pack(pady=10)

            for i in range(1):
                self.crear_caja(frame_cajas, f"ATENCION AL CLIENTE")

    def crear_caja(self, frame_cajas, nombre_caja):
        frame_caja = Frame(frame_cajas, bg="#E6E6E6", padx=10, pady=10)
        frame_caja.pack(pady=5, fill=X)

        label_nombre = Label(frame_caja, text=nombre_caja, font=("Poppins", 12), bg="#E6E6E6", fg="#000000")
        label_nombre.pack(anchor=W)

        label_disponibilidad = Label(frame_caja, text="DISPONIBILIDAD", bg="#E6E6E6", fg="#000000")
        label_disponibilidad.pack(anchor=W)

        entry_disponibilidad = LtkEntryLine(frame_caja, "True/False")
        entry_disponibilidad.pack(anchor=W)

        label_atencion = Label(frame_caja, text="Tiempo de atención:", bg="#E6E6E6", fg="#000000")
        label_atencion.pack(anchor=W)

        entry_atencion = LtkEntryLine(frame_caja, "Minutos")
        entry_atencion.pack(anchor=W)

    def crear_seccion_cajerosautomaticos(self):
        frame_cajerosautomaticos = Frame(self.frame_principal, bg="#002C6C")
        frame_cajerosautomaticos.pack(pady=3)

        cajerosautomaticos = [
            ("CAJERO AUTOMATICO 1", 150),
            ("CAJERO AUTOMATICO 2", 450),
            ("CAJERO AUTOMATICO 3", 750)
        ]

        for cajero, x_pos in cajerosautomaticos:
            frame_cajero = Frame(frame_cajerosautomaticos, bg="#458FFB")
            frame_cajero.pack(side=LEFT, padx=50)

            label_cajero = Label(frame_cajero, text=cajero, font=("Poppins", 15, "bold"), bg="#458FFB", fg="#FFFFFF")
            label_cajero.pack()

            entry_atraccion = LtkEntryLine(frame_cajero, "% de atracción")
            entry_atraccion.pack(pady=10)

            frame_cajasca = Frame(frame_cajero, bg="#458FFB")
            frame_cajasca.pack(pady=10)

            for i in range(1):
                self.crear_cajaca(frame_cajasca, f"")

    def crear_cajaca(self, frame_cajasca, nombre_cajaca):
        frame_cajaca = Frame(frame_cajasca, bg="#E6E6E6", padx=10, pady=10)
        frame_cajaca.pack(pady=5, fill=X)

        label_nombre = Label(frame_cajaca, text=nombre_cajaca, font=("Poppins", 12), bg="#E6E6E6", fg="#000000")
        label_nombre.pack(anchor=W)

        label_disponibilidad = Label(frame_cajaca, text="DISPONIBILIDAD", bg="#E6E6E6", fg="#000000")
        label_disponibilidad.pack(anchor=W)

        entry_disponibilidad = LtkEntryLine(frame_cajaca, "True/False")
        entry_disponibilidad.pack(anchor=W)

        label_atencion = Label(frame_cajaca, text="Tiempo de atención:", bg="#E6E6E6", fg="#000000")
        label_atencion.pack(anchor=W)

        entry_atencion = LtkEntryLine(frame_cajaca, "Minutos")
        entry_atencion.pack(anchor=W)

    def crear_seccion_secretarias(self):
        frame_secretarias = Frame(self.frame_principal, bg="#002C6C")
        frame_secretarias.pack(pady=3)

        secretarias = [
            ("Secretaria 1", 150),
            ("Secretaria 2", 450),
            ("Secretaria 3", 750)
        ]

        for secretaria, x_pos in secretarias:
            frame_secretaria = Frame(frame_secretarias, bg="#458FFB")
            frame_secretaria.pack(side=LEFT, padx=50)

            label_secretaria = Label(frame_secretaria, text=secretaria, font=("Poppins", 15, "bold"), bg="#458FFB", fg="#FFFFFF")
            label_secretaria.pack()

            entry_atraccion = LtkEntryLine(frame_secretaria, "% de atracción")
            entry_atraccion.pack(pady=10)

            frame_cajassecretarias = Frame(frame_secretaria, bg="#458FFB")
            frame_cajassecretarias.pack(pady=10)

            for i in range(1):
                self.crear_cajaSecretaria(frame_cajassecretarias, f"ATENCION AL CLIENTE")

    def crear_cajaSecretaria(self, frame_cajassecretarias, nombre_cajasecretaria):
        frame_cajaSecretaria = Frame(frame_cajassecretarias, bg="#E6E6E6", padx=10, pady=10)
        frame_cajaSecretaria.pack(pady=5, fill=X)

        label_nombre = Label(frame_cajaSecretaria, text=nombre_cajasecretaria, font=("Poppins", 12), bg="#E6E6E6", fg="#000000")
        label_nombre.pack(anchor=W)

        label_disponibilidad = Label(frame_cajaSecretaria, text="DISPONIBILIDAD", bg="#E6E6E6", fg="#000000")
        label_disponibilidad.pack(anchor=W)

        entry_disponibilidad = LtkEntryLine(frame_cajaSecretaria, "True/False")
        entry_disponibilidad.pack(anchor=W)

        label_atencion = Label(frame_cajaSecretaria, text="Tiempo de atención:", bg="#E6E6E6", fg="#000000")
        label_atencion.pack(anchor=W)

        entry_atencion = LtkEntryLine(frame_cajaSecretaria, "Minutos")
        entry_atencion.pack(anchor=W)

    def iniciar_simulacion(self):
        self.text_area.delete(1.0, END)
        self.text_area.insert(INSERT, "DATOS GUARDADOS\n")
