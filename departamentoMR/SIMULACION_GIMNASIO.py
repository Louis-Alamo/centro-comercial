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
        self.ventana = CTk()
        self.ventana.title("Gimnasio")
        self.ventana.geometry("950x800+350+100")
        self.ventana.configure(bg="#FFFFFF")

        # Crear un marco principal para el Canvas y el Scrollbar
        marco_principal = CTkFrame(self.ventana)
        marco_principal.pack(fill="both", expand=True)

        # Crear un Canvas
        canvas = CTkCanvas(marco_principal)
        canvas.pack(side="left", fill="both", expand=True)

        # Crear un Scrollbar y configurarlo con el Canvas
        scrollbar = CTkScrollbar(marco_principal, command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Crear un marco interior dentro del Canvas
        marco_interior = CTkFrame(canvas)
        canvas.create_window((0, 0), window=marco_interior, anchor="nw")

        # Configurar el redimensionamiento del marco interior
        marco_interior.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

        datos = cargar_datos()

        rangos_atencion = datos.get("rangos_atencion", [])
        rangos_descompostura = datos.get("rangos_descompostura", [])

        # Crear una etiqueta para mostrar todos los datos de la simulación
        datos_1 = CTkLabel(marco_interior, text=f"Datos de la simulación:\n{json.dumps(datos, indent=2)}", font=("Arial", 20))
        datos_1.pack(padx=20, pady=20)

        # Crear etiquetas para mostrar los rangos de atención y descompostura
        etiqueta_atencion = CTkLabel(marco_interior, text=f"Rangos de Atención: {rangos_atencion}", font=("Arial", 14))
        etiqueta_atencion.pack(padx=20, pady=20)
        
        etiqueta_descompostura = CTkLabel(marco_interior, text=f"Rangos de Descompostura: {rangos_descompostura}", font=("Arial", 14))
        etiqueta_descompostura.pack(padx=20, pady=20)

        self.ventana.mainloop()

SimulacionGimnasio()
