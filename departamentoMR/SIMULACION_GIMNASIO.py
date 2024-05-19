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
        self.ejecutar_simulacion()

        self.ventana.mainloop()

    def on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event=None):
        self.canvas.itemconfig(self.canvas.create_window((0, 0), window=self.frame, anchor="nw"), width=event.width)

    def aplicar_descuento_temporada(self):
        descuento = 0
        temporada_actual = None
        for temporada, info in self.datos.items():
            if isinstance(info, list) and len(info) == 2 and info[1]:
                temporada_actual = temporada
                if temporada_actual == "temporada_alta":
                    descuento = 0.15
                elif temporada_actual == "temporada_baja":
                    descuento = 0.05
                elif temporada_actual == "temporada_regular":
                    descuento = 0.10
                break

        if temporada_actual is not None:
            self.datos["cobro_mensual_usuario"] *= (1 - descuento)
            temporada_label = CTkLabel(self.frame, text=f"Descuento del {descuento * 100}% aplicado en la mensualidad durante la temporada {temporada_actual}", font=("Arial", 12))
            temporada_label.pack(padx=20, pady=5)
        else:
            print("No hay temporada activa para aplicar descuento en la mensualidad.")

    def ejecutar_simulacion(self):
        self.aplicar_descuento_temporada()

        costo_personal = (
            self.datos["cantidad_recepcionistas"] * self.datos["sueldo_mensual_recepcionista"] +
            self.datos["cantidad_personal_limpieza"] * self.datos["sueldo_mensual_personal_limpieza"] +
            self.datos["cantidad_gerentes"] * self.datos["sueldo_mensual_gerente"] +
            self.datos["cantidad_entrenadores"] * self.datos["sueldo_mensual_entrenador"] +
            self.datos["cantidad_personal_tecnico"] * self.datos["sueldo_mensual_personal_tecnico"]
        )
        costo_operacional = (
            self.datos["pago_mensual_luz"] +
            self.datos["pago_mensual_agua"] +
            self.datos["pago_mensual_internet"] +
            self.datos["pago_mensual_spotify"] +
            self.datos["pago_mensual_renta_local"]
        )
        costo_total_mensual = costo_personal + costo_operacional

        ingresos_mensuales = self.datos["capacidad_gym"] * self.datos["cobro_mensual_usuario"]

        resultados = {
            "Costo Total Mensual": costo_total_mensual,
            "Ingresos Mensuales": ingresos_mensuales,
            "Ganancia/Perdida": ingresos_mensuales - costo_total_mensual
        }
        resultados_label = CTkLabel(self.frame, text=f"Resultados de la simulación:\n{json.dumps(resultados, indent=2)}", font=("Arial", 20))
        resultados_label.pack(padx=20, pady=20)

SimulacionGimnasio()
