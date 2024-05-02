from tkinter import *
from customtkinter import CTk
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkButton import LtkButtonFill

class Veterinaria:
    def __init__(self):
        self.ventana = CTk()
        self.ventana.title("Veterinaria")
        self.ventana.geometry("1500x900")
        self.ventana.config(bg="#5B2800")

        self.frame_principal = Frame(self.ventana, bg="#5B2800")
        self.frame_principal.pack(expand=True, fill=BOTH)

        titulo_label = LtkLabel(self.frame_principal, texto="Veterinaria")
        titulo_label.configure(font=('Poppins', 80, "bold", "underline"))
        titulo_label.pack(pady=(20, 20))

        self.crear_seccion_veterinarios()
        self.crear_seccion_almacen()

        boton_ejecucion = LtkButtonFill(self.frame_principal, nombre_boton="Iniciar simulación", funcion=lambda: self.iniciar_simulacion())
        boton_ejecucion.pack(pady=20)

        self.text_area = Text(self.frame_principal, width=100, height=30)
        self.text_area.pack(pady=20, padx=50, fill=BOTH, expand=True)

        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)

        self.ventana.mainloop()

    def crear_seccion_veterinarios(self):
        frame_veterinarios = Frame(self.frame_principal, bg="#5B2800")
        frame_veterinarios.pack(pady=20)

        for i in range(2):
            frame_vet = Frame(frame_veterinarios, bg="#00ABC3")
            frame_vet.pack(pady=10)

            label_vet = Label(frame_vet, text=f"Veterinario {i+1}", font=("Poppins", 12), bg="#00ABC3", fg="#FFFFFF")
            label_vet.pack()

            entry_atraccion_vet = LtkEntryLine(frame_vet, "% de atracción")
            entry_atraccion_vet.pack(pady=5)

    def crear_seccion_almacen(self):
        frame_almacen = Frame(self.frame_principal, bg="#5B2800")
        frame_almacen.pack(pady=20)

        label_almacen = Label(frame_almacen, text="Almacen de mascotas", font=("Poppins", 15, "bold"), bg="#00ABC3", fg="#FFFFFF")
        label_almacen.pack()

        for i in range(10):
            mascota_frame = Frame(frame_almacen, bg="#00ABC3")
            mascota_frame.pack(pady=5)

            label_mascota = Label(mascota_frame, text=f"Mascota {i+1}", font=("Poppins", 12), bg="#00ABC3", fg="#FFFFFF")
            label_mascota.pack(side=LEFT, padx=10)

            entry_mascota_estado = LtkEntryLine(mascota_frame, "Estado")
            entry_mascota_estado.pack(side=LEFT, padx=10)

    def iniciar_simulacion(self):
        self.text_area.delete(1.0, END)
        self.text_area.insert(INSERT, "DATOS GUARDADOS\n")
