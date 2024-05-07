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

        frame_configuracion = Frame(self.frame_principal, bg="#66005B")
        frame_configuracion.pack(pady=10, padx=50, anchor=CENTER)

        self.configurar_horarios_y_capacidad(frame_configuracion)
        self.crear_seccion_baños("Mujeres")
        self.crear_seccion_baños("Hombres")

        frame_cantidad_personas = Frame(self.frame_principal, bg="#66005B")
        frame_cantidad_personas.pack(pady=20, padx=50)

        label_mujeres = Label(frame_cantidad_personas, text="Mujeres:", bg="#66005B", fg="#FFFFFF", font=("Poppins", 15))
        label_mujeres.pack(side=LEFT, padx=(20, 10))
        entry_porcentaje_mujeres = LtkEntryLine(frame_cantidad_personas, "Porcentaje Mujeres")
        entry_porcentaje_mujeres.pack(side=LEFT, padx=10)

        label_hombres = Label(frame_cantidad_personas, text="Hombres:", bg="#66005B", fg="#FFFFFF", font=("Poppins", 15))
        label_hombres.pack(side=LEFT, padx=(50, 10))

        entry_porcentaje_hombres = LtkEntryLine(frame_cantidad_personas, "Porcentaje Hombres")
        entry_porcentaje_hombres.pack(side=LEFT)

        self.crear_seccion_pasillos()

        boton_ejecucion = LtkButtonFill(self.frame_principal, nombre_boton="GUARDAR DATOS", funcion=lambda: self.iniciar_simulacion())
        boton_ejecucion.pack(pady=20)

        self.text_area = Text(self.frame_principal, width=100, height=30)
        self.text_area.pack(pady=20, padx=50, fill=BOTH, expand=True)

        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)

        self.ventana.mainloop()

    def configurar_horarios_y_capacidad(self, parent_frame):
        label_apertura = Label(parent_frame, text="Hora de Apertura:", bg="#66005B", fg="#FFFFFF", font=("Poppins", 15))
        label_apertura.pack(side=LEFT, padx=(50, 10))

        entry_apertura = LtkEntryLine(parent_frame, "HH:MM")
        entry_apertura.pack(side=LEFT)

        label_cierre = Label(parent_frame, text="Hora de Cierre:", bg="#66005B", fg="#FFFFFF", font=("Poppins", 15))
        label_cierre.pack(side=LEFT, padx=(50, 10))

        entry_cierre = LtkEntryLine(parent_frame, "HH:MM")
        entry_cierre.pack(side=LEFT)

        label_capacidad = Label(parent_frame, text="Capacidad de Personas:", bg="#66005B", fg="#FFFFFF", font=("Poppins", 15))
        label_capacidad.pack(side=LEFT, padx=(50, 10))

        entry_capacidad = LtkEntryLine(parent_frame, "Usuarios")
        entry_capacidad.pack(side=LEFT)

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
            entry_capacidad_pasillo = LtkEntryLine(frame_pasillo, "Capacidad de Personas")
            entry_capacidad_pasillo.pack()

            for i in range(3):
                self.crear_maquina(frame_pasillo, f"Máquina {i+1}")

    def crear_maquina(self, parent_frame, nombre_maquina):
        frame_maquina = Frame(parent_frame, bg="#E6E6E6", padx=10, pady=10)
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

    def crear_seccion_baños(self, tipo):
        frame_baños = Frame(self.frame_principal, bg="#66005B")
        frame_baños.pack(side=LEFT, padx=50)

        label_tipo = Label(frame_baños, text=f"Baños {tipo}", font=("Poppins", 15, "bold"), bg="#66005B", fg="#FFFFFF")
        label_tipo.pack()

        for i in range(3):
            frame_baño = Frame(frame_baños, bg="#66005B")
            frame_baño.pack(pady=5)

            label_baño = Label(frame_baño, text=f"Baño {i+1}", font=("Poppins", 12, "bold"), bg="#66005B", fg="#FFFFFF")
            label_baño.pack(anchor=W)

            label_tiempo_ducha = Label(frame_baño, text="Tiempo de ducha (min):", bg="#66005B", fg="#FFFFFF")
            label_tiempo_ducha.pack(anchor=W)

            entry_tiempo_ducha = LtkEntryLine(frame_baño, "Minutos")
            entry_tiempo_ducha.pack(anchor=W)

    def iniciar_simulacion(self):
        self.text_area.delete(1.0, END)
        self.text_area.insert(INSERT, "DATOS GUARDADOS\n")

Gimnasio()