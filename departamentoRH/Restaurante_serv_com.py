import tkinter as tk
class restaurante_ser_com:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Restaurante")
        self.ventana.geometry("600x600")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg="#FFFFFF")

        self.eti=tk.Label(self.ventana, text="Restaurante servicio completo",font=("Arial", 30, "bold"), bg="#FFFFFF", fg="#000000")
        self.eti.place(x=200, y=40)

        self.boton = tk.Button(self.ventana, text="Iniciar Simulacion")
        self.boton.place(x=200, y=120)

        self.ventana.mainloop()


