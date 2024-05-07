import tkinter as tk

class ropa:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ropa")
        self.ventana.geometry("900x800")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg="#FFFFFF")

        self.frame_principal = tk.Frame(self.ventana, bg="#98FF98")
        self.frame_principal.pack(expand=True, fill=tk.BOTH)

        self.frame_izquierdo = tk.Frame(self.frame_principal, bg="#98FF98")
        self.frame_izquierdo.pack(side=tk.LEFT, fill=tk.Y)

        self.eti = tk.Label(self.frame_izquierdo, text="Tienda de Ropa", font=("Arial", 40, "bold"), bg="#98FF98", fg="#000000")
        self.eti.pack(anchor=tk.W)

        self.frame_derecho = tk.Frame(self.frame_principal, bg="#98FF98")
        self.frame_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.label_personas = tk.Label(self.frame_izquierdo, text="Personas atendiendo:", font=('Poppins', 15, "bold"),bg="#98FF98")
        self.label_personas.pack(anchor=tk.W)

        self.entry_personas = tk.Entry(self.frame_izquierdo)
        self.entry_personas.pack(anchor=tk.W)

        self.label_ropa = tk.Label(self.frame_izquierdo, text="Tiempo promedio en probarse la ropa:", font=('Poppins', 15, "bold"),bg="#98FF98")
        self.label_ropa.pack(anchor=tk.W)

        self.entry_ropa = tk.Entry(self.frame_izquierdo)
        self.entry_ropa.pack(anchor=tk.W)

        self.label_prob = tk.Label(self.frame_izquierdo, text="Numero de probadores:",font=('Poppins', 15, "bold"), bg="#98FF98")
        self.label_prob.pack(anchor=tk.W)

        self.entry_prob = tk.Entry(self.frame_izquierdo)
        self.entry_prob.pack(anchor=tk.W)

        self.label_promedio = tk.Label(self.frame_izquierdo, text="Promedio en ser atendido(minutos):", font=('Poppins', 15, "bold"), bg="#98FF98")
        self.label_promedio.pack(anchor=tk.W)

        self.entry_promedio = tk.Entry(self.frame_izquierdo)
        self.entry_promedio.pack(anchor=tk.W)

        self.label_promo = tk.Label(self.frame_izquierdo, text="Promociones Si/No:", font=('Poppins', 15, "bold"), bg="#98FF98")
        self.label_promo.pack(anchor=tk.W)

        self.entry_promo= tk.Entry(self.frame_izquierdo)
        self.entry_promo.pack(anchor=tk.W)

        self.label_cajas = tk.Label(self.frame_izquierdo, text="Cajas abiertas:", font=('Poppins', 15, "bold"),bg="#98FF98")
        self.label_cajas.pack(anchor=tk.W)

        self.entry_cajas = tk.Entry(self.frame_izquierdo)
        self.entry_cajas.pack(anchor=tk.W)

        self.label_fila = tk.Label(self.frame_izquierdo, text="Tiempo promedio en la fila:", font=('Poppins', 15, "bold"),bg="#98FF98")
        self.label_fila.pack(anchor=tk.W)

        self.entry_fila = tk.Entry(self.frame_izquierdo)
        self.entry_fila.pack(anchor=tk.W)

        self.boton = tk.Button(self.frame_izquierdo, text="Iniciar Simulacion", command=self.iniciar_simulacion)
        self.boton.pack(anchor=tk.W)

        self.text_area = tk.Text(self.frame_derecho, width=100, height=30)
        self.text_area.pack(pady=20, padx=50, fill=tk.BOTH, expand=True)

        self.ventana.mainloop()

    def iniciar_simulacion(self):
        print("iniciando...")
