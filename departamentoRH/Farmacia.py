import tkinter as tk

class farmacia:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Farmacia")
        self.ventana.geometry("1300x800")
        self.ventana.config(bg="#6B8E23")

        self.frame_principal = tk.Frame(self.ventana, bg="#98FF98")
        self.frame_principal.pack(expand=True, fill=tk.BOTH)

        self.frame_izquierdo = tk.Frame(self.frame_principal, bg="#98FF98")
        self.frame_izquierdo.pack(side=tk.LEFT, fill=tk.Y)

        self.frame_derecho = tk.Frame(self.frame_principal, bg="#98FF98")
        self.frame_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.titulo_label = tk.Label(self.frame_izquierdo, text="Farmacia", font=('Poppins', 50, "bold"), bg="#98FF98")
        self.titulo_label.pack(pady=(20, 20), anchor=tk.W)

        self.label_personas = tk.Label(self.frame_izquierdo, text="Personas atendiendo:", font=('Poppins', 15, "bold"), bg="#98FF98")
        self.label_personas.pack(anchor=tk.W)

        self.entry_personas = tk.Entry(self.frame_izquierdo)
        self.entry_personas.pack(anchor=tk.W)

        self.label_inventario = tk.Label(self.frame_izquierdo, text="Inventario:", font=('Poppins', 15, "bold"), bg="#98FF98")
        self.label_inventario.pack(anchor=tk.W)

        self.entry_inventario = tk.Entry(self.frame_izquierdo)
        self.entry_inventario.pack(anchor=tk.W)

        self.label_promedio = tk.Label(self.frame_izquierdo, text="Promedio en ser atendido(minutos):", font=('Poppins', 15, "bold"), bg="#98FF98")
        self.label_promedio.pack(anchor=tk.W)

        self.entry_promedio = tk.Entry(self.frame_izquierdo)
        self.entry_promedio.pack(anchor=tk.W)

        self.label_promociones = tk.Label(self.frame_izquierdo, text="Promociones(Si/No):", font=('Poppins', 15, "bold"), bg="#98FF98")
        self.label_promociones.pack(anchor=tk.W)

        self.entry_promociones = tk.Entry(self.frame_izquierdo)
        self.entry_promociones.pack(anchor=tk.W)

        self.label_puerta = tk.Label(self.frame_izquierdo, text="Cerca de la Puerta?:", font=('Poppins', 15, "bold"), bg="#98FF98")
        self.label_puerta.pack(anchor=tk.W)

        self.entry_puerta = tk.Entry(self.frame_izquierdo)
        self.entry_puerta.pack(anchor=tk.W)

        self.boton_ejecucion = tk.Button(self.frame_izquierdo, text="Iniciar simulación", command=self.iniciar_simulacion)
        self.boton_ejecucion.pack(pady=20, anchor=tk.W)

        self.text_area = tk.Text(self.frame_derecho, width=100, height=30)
        self.text_area.pack(pady=20, padx=50, fill=tk.BOTH, expand=True)

        self.ventana.mainloop()

    def iniciar_simulacion(self):
        print ("iniciando...")