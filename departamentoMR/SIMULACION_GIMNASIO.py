from customtkinter import CTk, CTkLabel, CTkFrame, CTkCanvas, CTkScrollbar
import json
import os
import random
from datetime import datetime, timedelta


ruta_archivo = os.path.dirname(os.path.abspath(__file__))
ruta_completa = os.path.join(ruta_archivo, 'gimnasio.json')

def cargar_datos():
    try:
        with open(ruta_completa, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("El archivo gimnasio.json no se encontró.")
        return {}
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
        return {}

def generar_numeros_aleatorios(cantidad):
    temporada = determinar_temporada()
    if temporada == "alta":
        cantidad = int(cantidad * 1.2)
    elif temporada == "baja":
        cantidad = int(cantidad * 0.8)
    numeros = [round(random.uniform(0, 1), 4) for _ in range(cantidad)]
    ruta_numeros = os.path.join(ruta_archivo, 'A_gimnasio.txt')
    with open(ruta_numeros, 'w') as file:
        for numero in numeros:
            file.write(f"{numero}\n")
    return numeros

def obtener_personas_segun_rango(rango_aleatorio, rangos_llegada_usuarios):
    for cantidad_personas, rango in rangos_llegada_usuarios:
        limite_inferior, limite_superior = map(float, rango.split("-"))
        if limite_inferior <= rango_aleatorio <= limite_superior:
            return cantidad_personas
    return 0

def obtener_duracion_segun_rango(rango_aleatorio, rangos_duracion_gym):
    for duracion, rango in rangos_duracion_gym:
        limite_inferior, limite_superior = map(float, rango.split("-"))
        if limite_inferior <= rango_aleatorio <= limite_superior:
            return duracion
    return 0

def obtener_tiempo_baño_segun_rango(rango_aleatorio, rangos_duracion_baño):
    for tiempo_baño, rango in rangos_duracion_baño:
        limite_inferior, limite_superior = map(float, rango.split("-"))
        if limite_inferior <= rango_aleatorio <= limite_superior:
            return tiempo_baño
    return 0

def determinar_temporada():
    datos = cargar_datos()
    if datos.get("temporada_alta", [False])[0]:
        return "alta"
    elif datos.get("temporada_regular", [False])[0]:
        return "regular"
    elif datos.get("temporada_baja", [False])[0]:
        return "baja"
    return "sin temporada"

def incrementar_hora(base_hora, incremento_minutos):
    base_hora_dt = datetime.strptime(base_hora, "%H:%M")
    nueva_hora_dt = base_hora_dt + timedelta(minutes=incremento_minutos)
    return nueva_hora_dt.strftime("%H:%M")

class SimulacionGimnasio:
    def __init__(self):
        self.total_cobro = 0
        self.ventana = CTk()
        self.ventana.title("Gimnasio")
        self.ventana.geometry("950x800+350+100")
        self.ventana.configure(bg="black")
        self.ventana.grid_rowconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(0, weight=1)
        
        self.frame = CTkFrame(self.ventana)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        
        self.canvas = CTkCanvas(self.frame, bg="black")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        
        self.scrollbar = CTkScrollbar(self.frame, command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.inner_frame = CTkFrame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        
        self.inner_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        
        self.datos = cargar_datos()
        self.ejecutar_simulacion()

        self.numeros_aleatorios = generar_numeros_aleatorios(30)
        self.crear_tabla_simulacion(self.numeros_aleatorios)
        self.ventana.mainloop()

    def on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event=None):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw"), width=canvas_width)
    
    def aplicar_descuento_temporada(self):
        temporada_regular = self.datos.get("temporada_regular", [False])[0]
        temporada_alta = self.datos.get("temporada_alta", [False])[0]
        temporada_baja = self.datos.get("temporada_baja", [False])[0]
        
        if temporada_regular:
            descuento = self.datos.get("descuento_regular", 0)
        elif temporada_alta:
            descuento = self.datos.get("descuento_alta", 0)
        elif temporada_baja:
            descuento = self.datos.get("descuento_baja", 0)
        else:
            descuento = 0
        
        return descuento

    def ejecutar_simulacion(self):
        descuento = self.aplicar_descuento_temporada()
        self.cobro = self.datos.get("cobro_usuario", 0)
        self.cobro_final = self.cobro * (1 - descuento)
        
        
        temporada_regular = self.datos.get("temporada_regular", [False])[0]
        temporada_alta = self.datos.get("temporada_alta", [False])[0]
        temporada_baja = self.datos.get("temporada_baja", [False])[0]


        if temporada_regular:
            temporada = "Temporada Regular"
        elif temporada_alta:
            temporada = "Temporada Alta"
        elif temporada_baja:
            temporada = "Temporada Baja"
        else:
            temporada = "Sin Temporada Específica"

        temporada_label = CTkLabel(self.inner_frame, text=f"Descuento del {descuento * 100}% aplicado en la mensualidad durante la {temporada}", font=("Arial", 12), text_color="white")
        temporada_label.pack(padx=20, pady=5)

        resultados = {
            "Cobro Por Usuario (Sin Descuento)": self.cobro,
            "Cobro Por Usuario (Con Descuento)": self.cobro_final,
            "Ganancia Del Dia": self.total_cobro,
        }

        resultados_label = CTkLabel(self.inner_frame, text=f"Resultados de la simulación:\n{json.dumps(resultados, indent=2)}", font=("Arial", 20), text_color="white")
        resultados_label.pack(padx=20, pady=20, fill="x", expand=True)
        

    def crear_tabla_simulacion(self, numeros):
        columnas = ["ALEATORIOS", "PERSONAS", "COBRO", "LLEGO", "DURACION", "TIEMPO BAÑO", "SALIDA", "MAQUINAS EN USO", "SIN USO"]
        llegada_usuarios = self.datos.get("llegada_usuarios", [])
        horario_apertura = self.datos.get("horario_apertura", "06:00")
        horario_cierre = self.datos.get("horario_cierre", "22:00")
        lapso_usuarios = self.datos.get("lapso_usuarios", [])
        duracion_gym = self.datos.get("duracion_gym", [])
        duracion_baño = self.datos.get("duracion_baño", [])
        cantidad_maquinas = self.datos.get("cantidad_maquinas", 0)

        header_frame = CTkFrame(self.inner_frame)
        header_frame.pack(padx=20, pady=10, fill="x")

        for i, columna in enumerate(columnas):
            columna_label = CTkLabel(header_frame, text=columna, font=("Arial", 12, "bold"), text_color="white")
            columna_label.grid(row=0, column=i, padx=10, pady=5, sticky="nsew")
            header_frame.grid_columnconfigure(i, weight=1)

        tabla_frame = CTkFrame(self.inner_frame)
        tabla_frame.pack(padx=20, pady=10, fill="both", expand=True)

        hora_actual = horario_apertura
        maquinas_en_uso = 0

        for i, numero in enumerate(numeros):
            numero_label = CTkLabel(tabla_frame, text=str(numero), font=("Arial", 12), text_color="white")
            numero_label.grid(row=i, column=0, padx=(10, 20), pady=10, sticky="nsew")

            personas = obtener_personas_segun_rango(numero, llegada_usuarios)
            personas_label = CTkLabel(tabla_frame, text=str(personas), font=("Arial", 12), text_color="white")
            personas_label.grid(row=i, column=1, padx=(60, 20), pady=10, sticky="nsew")

            cobro_desc = self.cobro_final * personas
            cobro_label = CTkLabel(tabla_frame, text=f"${cobro_desc}", font=("Arial", 12), text_color="white")
            cobro_label.grid(row=i, column=2, padx=(60, 20), pady=10, sticky="nsew")
            self.total_cobro += cobro_desc


            incremento_minutos = 0
            for incremento, rango in lapso_usuarios:
                limite_inferior, limite_superior = map(float, rango.split("-"))
                if limite_inferior <= numero <= limite_superior:
                    incremento_minutos = incremento
                    break

            hora_llegada = incrementar_hora(hora_actual, incremento_minutos)
            hora_actual = hora_llegada 

            hora_llegada_label = CTkLabel(tabla_frame, text=hora_llegada, font=("Arial", 12), text_color="white")
            hora_llegada_label.grid(row=i, column=3, padx=(50, 20), pady=10, sticky="nsew")

            duracion_gym_val = obtener_duracion_segun_rango(numero, duracion_gym)
            duracion_gym_label = CTkLabel(tabla_frame, text=str(duracion_gym_val), font=("Arial", 12), text_color="white")
            duracion_gym_label.grid(row=i, column=4, padx=(70, 20), pady=10, sticky="nsew")

            duracion_baño_val = obtener_tiempo_baño_segun_rango(numero, duracion_baño)
            duracion_baño_label = CTkLabel(tabla_frame, text=str(duracion_baño_val), font=("Arial", 12), text_color="white")
            duracion_baño_label.grid(row=i, column=5, padx=(60, 20), pady=10, sticky="nsew")


            hora_salida = incrementar_hora(hora_llegada, duracion_gym_val + duracion_baño_val)
            hora_salida_label = CTkLabel(tabla_frame, text=hora_salida, font=("Arial", 12), text_color="white")
            hora_salida_label.grid(row=i, column=6, padx=(60, 20), pady=10, sticky="nsew")

    
            if personas > 0:
                maquinas_en_uso += personas
            maquinas_sin_uso = cantidad_maquinas - maquinas_en_uso

            maquinas_en_uso_label = CTkLabel(tabla_frame, text=str(maquinas_en_uso), font=("Arial", 12), text_color="white")
            maquinas_en_uso_label.grid(row=i, column=7, padx=(60, 20), pady=10, sticky="nsew")

            maquinas_sin_uso_label = CTkLabel(tabla_frame, text=str(maquinas_sin_uso), font=("Arial", 12), text_color="white")
            maquinas_sin_uso_label.grid(row=i,column=8, padx=(60, 20), pady=10, sticky="nsew")

        for i in range(len(numeros)):
            tabla_frame.grid_rowconfigure(i, weight=1)






SimulacionGimnasio()
