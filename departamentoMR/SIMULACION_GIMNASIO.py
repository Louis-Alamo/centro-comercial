from customtkinter import CTk, CTkLabel, CTkFrame, CTkCanvas, CTkScrollbar
import json
import os

ruta_archivo = os.path.dirname(os.path.abspath(__file__))
ruta_completa = os.path.join(ruta_archivo, 'gimnasio.json')

def cargar_datos():
    with open(ruta_completa, 'r') as file:
        return json.load(file)

class SimulacionGimnasio:
    def __init__(self):
        self.ventana = CTk()
        self.ventana.title("Gimnasio")
        self.ventana.geometry("950x800+350+100")
        self.ventana.grid_rowconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(0, weight=1)

        self.canvas = CTkCanvas(self.ventana)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar = CTkScrollbar(self.ventana, command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.frame = CTkFrame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        self.frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)



        self.datos = cargar_datos()

        datos_label = CTkLabel(self.frame, text=f"Datos de la simulación:\n{json.dumps(self.datos, indent=2)}", font=("Arial", 20))
        datos_label.pack(padx=20, pady=20)
























        self.ventana.mainloop()

    def on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    def on_canvas_configure(self, event=None):
        self.canvas.itemconfig(self.canvas.create_window((0, 0), window=self.frame, anchor="nw"), width=event.width)

SimulacionGimnasio()
