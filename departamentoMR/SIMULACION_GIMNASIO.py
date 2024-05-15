from customtkinter import CTk, CTkLabel
import json
import random

def cargar_datos():
    with open('D:\\MIIGUEL ROSALES\\Documentos\\ISC - ITSZaS\\Cuarto Semestre\\SIMULACION\\PROYECTO\\centro-comercial\\departamentoMR\\gimnasio.json', 'r') as file:
        return json.load(file)

class SimulacionGimnasio:
    def __init__(self):
        self.ventana = CTk()
        self.ventana.title("Gimnasio")
        self.ventana.geometry("950x800+350+100")
        self.ventana.configure(bg="#FFFFFF")
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)
        self.ventana.rowconfigure(1, weight=1)
        datos = cargar_datos()

        usuarios_en_espera = datos.get("usuarios_en_espera", 0)
        rangos_atencion = datos.get("rangos_atencion", [])

        aleatorios = [round(random.random(), 4) for i in range(usuarios_en_espera)]

        # Función para determinar el rango
        def determinar_rango(valor):
            for rango in rangos_atencion:
                if rango["inicio"] <= valor < rango["fin"]:
                    return f"{rango['nombre']} ({rango['inicio']} - {rango['fin']})"
            return "Fuera de rango"

        # Mostrar resultados aleatorios con rangos correspondientes
        for i in range(usuarios_en_espera):
            valor_aleatorio = aleatorios[i]
            rango = determinar_rango(valor_aleatorio)
            label_resultado = CTkLabel(self.ventana, text=f"Usuario {i+1}: {valor_aleatorio} - {rango}")
            label_resultado.grid(row=i+1, column=0, padx=10, pady=5)

        self.ventana.mainloop()

SimulacionGimnasio()
