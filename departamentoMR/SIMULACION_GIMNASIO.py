from customtkinter import CTk, CTkLabel
import json

def cargar_datos():
    with open('D:\\MIIGUEL ROSALES\\Documentos\\ISC - ITSZaS\\Cuarto Semestre\\SIMULACION\\PROYECTO\\centro-comercial\\departamentoMR\\gimnasio.json', 'r') as file:
        return json.load(file)

class SimulacionGimnasio:
    def __init__(self):
        self.ventana = CTk()
        self.ventana.title("Gimnasio")
        self.ventana.geometry("950x800+350+100")
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)
        self.ventana.rowconfigure(1, weight=1)
        self.ventana.rowconfigure(2, weight=1)
        
        datos = cargar_datos()

        rangos_atencion = datos.get("rangos_atencion", [])
        rangos_descompostura = datos.get("rangos_descompostura", [])

        # Crear una etiqueta para mostrar todos los datos de la simulación
        datos_1 = CTkLabel(self.ventana, text=f"Datos de la simulación:\n{json.dumps(datos, indent=2)}", font=("Arial", 20))
        datos_1.grid(row=0, column=0, padx=20, pady=20)

        # Crear etiquetas para mostrar los rangos de atención y descompostura
        etiqueta_atencion = CTkLabel(self.ventana, text=f"Rangos de Atención: {rangos_atencion}", font=("Arial", 14))
        etiqueta_atencion.grid(row=1, column=0, padx=20, pady=20)
        
        etiqueta_descompostura = CTkLabel(self.ventana, text=f"Rangos de Descompostura: {rangos_descompostura}", font=("Arial", 14))
        etiqueta_descompostura.grid(row=2, column=0, padx=20, pady=20)

        self.ventana.mainloop()

SimulacionGimnasio()
