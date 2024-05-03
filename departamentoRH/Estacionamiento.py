from tkinter import *
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkButton import LtkButtonFill

class estacionamiento:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Estacionamiento")
        self.ventana.geometry("1300x800")
        self.ventana.config(bg="#6B8E23")

        self.frame_principal = Frame(self.ventana, bg="#98FF98")
        self.frame_principal.pack(expand=True, fill=BOTH)

        titulo_label = LtkLabel(self.frame_principal, texto="Estacionamiento")
        titulo_label.configure(font=('Poppins', 50, "bold"))
        titulo_label.pack(pady=(20, 20))

        self.secciones()

        boton_ejecucion = LtkButtonFill(self.frame_principal, nombre_boton="Iniciar simulación", funcion=lambda: self.iniciar_simulacion())
        boton_ejecucion.pack(pady=20)

        self.text_area = Text(self.frame_principal, width=100, height=30)
        self.text_area.pack(pady=20, padx=50, fill=BOTH, expand=True)

        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)

        self.ventana.mainloop()

    def secciones(self):
        frame_pisos = Frame(self.frame_principal, bg="#228B22")
        frame_pisos.pack(pady=20)

        secciones = [
            ("Seccion A", 150),
            ("Seccion B", 450),
            ("Seccion C", 750),
            ("Seccion D", 1050)
        ]

        for piso, x_pos in secciones:
            frame_piso = Frame(frame_pisos, bg="grey")
            frame_piso.pack(side=LEFT, padx=50)

            label_piso = Label(frame_piso, text=piso, font=("Poppins", 15, "bold"), bg="grey", fg="#FFFFFF")
            label_piso.pack()

            entry_tarifa = LtkEntryLine(frame_piso, "Capacidad de cada seccion")
            entry_tarifa.pack(pady=10)

            frame_espacios = Frame(frame_piso, bg="#98FF98")
            frame_espacios.pack(pady=10)

            for i in range(1):
                self.crear_espacio(frame_espacios, f"")

    def crear_espacio(self, frame_espacios, nombre_espacio):
        frame_espacio = Frame(frame_espacios, bg="#E6E6E6", padx=10, pady=10)
        frame_espacio.pack(pady=5, fill=X)

        label_nombre = Label(frame_espacio, text=nombre_espacio, font=("Poppins", 12), bg="#E6E6E6", fg="#000000")
        label_nombre.pack(anchor=W)

        label_estado = Label(frame_espacio, text="Espacios Disponibles/No Disponible:", bg="#E6E6E6", fg="#000000")
        label_estado.pack(anchor=W)

        entry_estado = LtkEntryLine(frame_espacio, "Si/ No")
        entry_estado.pack(anchor=W)

        label_estado = Label(frame_espacio, text="Tiempo en encontrar estacionamiento:", bg="#E6E6E6", fg="#000000")
        label_estado.pack(anchor=W)

        entry_estado = LtkEntryLine(frame_espacio, "Minutos")
        entry_estado.pack(anchor=W)

        label_tiempo_ocupacion = Label(frame_espacio, text="Promedio de tiempo estacionado:", bg="#E6E6E6", fg="#000000")
        label_tiempo_ocupacion.pack(anchor=W)

        entry_tiempo_ocupacion = LtkEntryLine(frame_espacio, "Minutos")
        entry_tiempo_ocupacion.pack(anchor=W)

        label_tiempo_ocupacion = Label(frame_espacio, text="Prom. de tiempo en salir:", bg="#E6E6E6", fg="#000000")
        label_tiempo_ocupacion.pack(anchor=W)

        entry_tiempo_ocupacion = LtkEntryLine(frame_espacio, "Minutos")
        entry_tiempo_ocupacion.pack(anchor=W)

        label_tiempo_ocupacion = Label(frame_espacio, text="Eventos Especiales:", bg="#E6E6E6", fg="#000000")
        label_tiempo_ocupacion.pack(anchor=W)

        entry_tiempo_ocupacion = LtkEntryLine(frame_espacio, "Si/No")
        entry_tiempo_ocupacion.pack(anchor=W)

        label_tiempo_ocupacion = Label(frame_espacio, text="Autos Estacionados:", bg="#E6E6E6", fg="#000000")
        label_tiempo_ocupacion.pack(anchor=W)

        entry_tiempo_ocupacion = LtkEntryLine(frame_espacio, "Pueden ser 0")
        entry_tiempo_ocupacion.pack(anchor=W)

    def iniciar_simulacion(self):
        self.text_area.delete(1.0, END)
        self.text_area.insert(INSERT, "DATOS GUARDADOS\n")

estacionamiento()
