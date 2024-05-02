import tkinter as tk
class farmacia:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Farmacia")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0, 0)
        self.ventana.configure(bg="#FFFFFF")

        self.eti=tk.Label(self.ventana, text="Farmacia",font=("Arial", 30, "bold"), bg="#FFFFFF", fg="#000000")
        self.eti.place(x=200, y=40)

        self.boton = tk.Button(self.ventana, text="Iniciar Simulacion")
        self.boton.place(x=200, y=120)

        self.ventana.mainloop()

farmacia()

