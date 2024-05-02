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

        titulo_label = LtkLabel(self.frame_principal, texto="Gimnasio")
        titulo_label.configure(font=('Poppins', 80, "bold"))
        titulo_label.pack(pady=(20, 20))


        self.crear_seccion_pasillos()

        boton_ejecucion = LtkButtonFill(self.frame_principal, nombre_boton="Iniciar simulación", funcion=lambda: self.iniciar_simulacion())
        boton_ejecucion.pack(pady=20)

        self.text_area = Text(self.frame_principal, width=100, height=30)
        self.text_area.pack(pady=20, padx=50, fill=BOTH, expand=True)

        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)

        self.ventana.mainloop()

    def crear_seccion_pasillos(self):
        frame_pasillos = Frame(self.frame_principal, bg="#1B0018")
        frame_pasillos.pack(pady=20)

        pasillos = [
            ("Pasillo 1", 150),
            ("Pasillo 2", 450),
            ("Pasillo 3", 750),
            ("Pasillo 4", 1050)
        ]

        for pasillo, x_pos in pasillos:
            frame_pasillo = Frame(frame_pasillos, bg="#66005B")
            frame_pasillo.pack(side=LEFT, padx=50)

            label_pasillo = Label(frame_pasillo, text=pasillo, font=("Poppins", 15, "bold"), bg="#66005B", fg="#FFFFFF")
            label_pasillo.pack()

            entry_atraccion = LtkEntryLine(frame_pasillo, "% de atracción")
            entry_atraccion.pack(pady=10)


            frame_maquinas = Frame(frame_pasillo, bg="#66005B")
            frame_maquinas.pack(pady=10)

            for i in range(3):
                self.crear_maquina(frame_maquinas, f"Máquina {i+1}")

    def crear_maquina(self, frame_maquinas, nombre_maquina):
        frame_maquina = Frame(frame_maquinas, bg="#E6E6E6", padx=10, pady=10)
        frame_maquina.pack(pady=5, fill=X)

        label_nombre = Label(frame_maquina, text=nombre_maquina, font=("Poppins", 12), bg="#E6E6E6", fg="#000000")
        label_nombre.pack(anchor=W)

        label_tiempo_uso = Label(frame_maquina, text="Tiempo de uso:", bg="#E6E6E6", fg="#000000")
        label_tiempo_uso.pack(anchor=W)

        entry_tiempo_uso = LtkEntryLine(frame_maquina, "Minutos")
        entry_tiempo_uso.pack(anchor=W)

        label_prob_descomponer = Label(frame_maquina, text="Capacidad de Personas:", bg="#E6E6E6", fg="#000000")
        label_prob_descomponer.pack(anchor=W)

        entry_prob_descomponer = LtkEntryLine(frame_maquina, "Usuarios")
        entry_prob_descomponer.pack(anchor=W)


    def iniciar_simulacion(self):
        self.text_area.delete(1.0, END)
        self.text_area.insert(INSERT, "DATOS GUARDADOS\n")

