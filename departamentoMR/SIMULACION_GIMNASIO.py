from customtkinter import CTk, CTkLabel, CTkFrame, CTkCanvas, CTkScrollbar
import json
import os

ruta_archivo=os.path.dirname(os.path.abspath(__file__))
ruta_completa=os.path.join(ruta_archivo, 'gimnasio.json')

def cargar_datos():
    with open(ruta_completa, 'r') as file:
        return json.load(file)

class SimulacionGimnasio:
    def __init__(self):
        self.ventana=CTk()
        self.ventana.title("Gimnasio")
        self.ventana.geometry("950x800+350+100")
        self.ventana.configure(bg="black")
        self.ventana.grid_rowconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(0, weight=1)
        self.frame=CTkFrame(self.ventana, bg_color="black")
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.canvas=CTkCanvas(self.frame, bg="black") 
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar=CTkScrollbar(self.frame, command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.inner_frame=CTkFrame(self.canvas, bg_color="black")
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        self.inner_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        
        self.datos=cargar_datos()
        self.ejecutar_simulacion()

        self.ventana.mainloop()

    def on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event=None):
        canvas_width=event.width
        self.canvas.itemconfig(self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw"), width=canvas_width)
    
    def aplicar_descuento_temporada(self):
        temporada_regular=self.datos.get("temporada_regular", [False])[0]
        temporada_alta=self.datos.get("temporada_alta", [False])[0]
        temporada_baja=self.datos.get("temporada_baja", [False])[0]
        
        if temporada_regular:
            descuento=self.datos.get("descuento_regular", 0)
        elif temporada_alta:
            descuento=self.datos.get("descuento_alta", 0)
        elif temporada_baja:
            descuento=self.datos.get("descuento_baja", 0)
        else:
            descuento=0
        
        return descuento
    
        

    def ejecutar_simulacion(self):
        descuento=self.aplicar_descuento_temporada()
        cobro_mensual=self.datos.get("cobro_mensual_usuario", 0)
        cobro_final=cobro_mensual * (1 - descuento)
        temporada_regular = self.datos.get("temporada_regular", [False])[0]
        temporada_alta = self.datos.get("temporada_alta", [False])[0]
        temporada_baja = self.datos.get("temporada_baja", [False])[0]

        if temporada_regular:
            temporada = "Temporada Regular"
        elif temporada_alta:
            temporada = "Temporada Alta"
        elif temporada_baja:
            temporada = "Temporada Baja"

        temporada_label = CTkLabel(self.inner_frame, text=f"Descuento del {descuento * 100}% aplicado en la mensualidad durante la {temporada}", font=("Arial", 12), bg_color="black", text_color="white")
        temporada_label.pack(padx=20, pady=5)

        resultados={
            "Cobro Mensual Por Usuario (Sin Descuento)": cobro_mensual,
            "Cobro Mensual Por Usuario (Con Descuento)": cobro_final
        }

        resultados_label=CTkLabel(self.inner_frame, text=f"Resultados de la simulación:\n{json.dumps(resultados, indent=2)}", font=("Arial", 20), bg_color="black", text_color="white")
        resultados_label.pack(padx=20, pady=20, fill="both", expand=True)

SimulacionGimnasio()
