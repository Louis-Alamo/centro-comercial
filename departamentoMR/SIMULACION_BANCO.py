from customtkinter import CTk, CTkLabel, CTkFrame, CTkCanvas, CTkScrollbar
from util.NumerosAleatorios import generar_aleatorio, generar_numeros_aleatorios
import json
import os
from datetime import datetime, timedelta

ruta_archivo = os.path.dirname(os.path.abspath(__file__))
ruta_completa = os.path.join(ruta_archivo, 'banco.json')

def cargar_datos():
    try:
        with open(ruta_completa, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("El archivo banco.json no se encontró.")
        return {}
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
        return {}

def obtener_rango(rango_aleatorio, datos):
    for valor, rango in datos:
        limite_inferior, limite_superior = map(float, rango.split("-"))
        if limite_inferior <= rango_aleatorio <= limite_superior:
            return valor
    return "Error"

class SimulacionBanco:
    def __init__(self):
        self.ventana = CTk()
        self.ventana.title("Banco")
        self.ventana.geometry("1350x800+350+100")
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
        self.crear_tabla_simulacion()
        self.ventana.mainloop()

    def on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event=None):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw"), width=canvas_width)

    def ejecutar_simulacion(self):
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

        temporada_label = CTkLabel(self.inner_frame, text=f"Simulacion en base a la temporada {temporada}", font=("Arial", 12), text_color="white")
        temporada_label.pack(padx=20, pady=5)

        resultados = {
            "resultados": "aqui iran mas resultados de la simulacion del banco"
        }

        resultados_label = CTkLabel(self.inner_frame, text=f"Resultados de la simulación BANCO:\n{json.dumps(resultados, indent=2)}", font=("Arial", 20), text_color="white")
        resultados_label.pack(padx=20, pady=20, fill="x", expand=True)

    def crear_tabla_simulacion(self):
        columnas = ["ALEATORIOS", "TIPO CLIENTE", "ACUDIO", "HORA LLEGADA", "DURACION", "CAJA EN USO", "DISPONIBLE", "SECRE EN USO", "DISPONIBLE", "CAJERO A. EN USO", "DISPONIBLE", "HORA SALIDA", "OLVIDO TARJETA"]

        header_frame = CTkFrame(self.inner_frame)
        header_frame.pack(padx=20, pady=10, fill="x")

        for i, columna in enumerate(columnas):
            columna_label = CTkLabel(header_frame, text=columna, font=("Arial", 12, "bold"), text_color="white")
            columna_label.grid(row=0, column=i, padx=10, pady=5, sticky="nsew")
            header_frame.grid_columnconfigure(i, weight=1)

        tabla_frame = CTkFrame(self.inner_frame)
        tabla_frame.pack(padx=20, pady=10, fill="both", expand=True)

        numeros_aleatorios = generar_numeros_aleatorios(10000)

        tipo = self.datos.get("tipo", [])
        acude = self.datos.get("acude", [])
        horario_llegada = self.datos.get("horario_llegada", [])
        duracion_ventanilla = self.datos.get("duracion_ventanilla", [])
        duracion_secre = self.datos.get("duracion_secre", [])
        duracion_cajero_a = self.datos.get("duracion_cajero_a", [])
        olvido = self.datos.get("olvido", [])
        cantidad_ventanillas = self.datos.get("cantidad_ventanillas", 0)
        cantidad_secretarias = self.datos.get("cantidad_secretarias", 0)
        cantidad_cajeros_automaticos = self.datos.get("cantidad_cajeros_automaticos", 0)

        horario_entrada = self.datos.get("horario_entrada", "08:00")
        horario_cierre = self.datos.get("horario_cierre", "20:00")

        horarios_entrada = {}

        ventanillas_disponibles = cantidad_ventanillas
        secretarias_disponibles = cantidad_secretarias
        cajero_automatico_disponible = cantidad_cajeros_automaticos

        eventos_salida = []

        for i, numero in enumerate(numeros_aleatorios):
            aleatorio_label = CTkLabel(tabla_frame, text=str(numero), font=("Arial", 12), text_color="white")
            aleatorio_label.grid(row=i, column=0, padx=20, pady=10, sticky="nsew")

            tipo_cliente = obtener_rango(numero, tipo)
            tipo_label = CTkLabel(tabla_frame, text=tipo_cliente, font=("Arial", 12), text_color="white")
            tipo_label.grid(row=i, column=1, padx=35, pady=10, sticky="nsew")

            acude_cliente = obtener_rango(numero, acude)
            acude_label = CTkLabel(tabla_frame, text=acude_cliente, font=("Arial", 12), text_color="white")
            acude_label.grid(row=i, column=2, padx=10, pady=10, sticky="nsew")

            horario_llegada_cliente = obtener_rango(numero, horario_llegada)
            if acude_cliente not in horarios_entrada:
                horarios_entrada[acude_cliente] = datetime.strptime(horario_entrada, "%H:%M")
            horarios_entrada[acude_cliente] += timedelta(minutes=int(horario_llegada_cliente))
            horario_label = CTkLabel(tabla_frame, text=horarios_entrada[acude_cliente].strftime("%H:%M"), font=("Arial", 12), text_color="white")
            horario_label.grid(row=i, column=3, padx=30, pady=10, sticky="nsew")

            duracion = 0

            if acude_cliente == "Ventanilla":
                duracion = int(obtener_rango(numero, duracion_ventanilla))
                if ventanillas_disponibles > 0:
                    ventanillas_disponibles -= 1
                else:
                    duracion = 0

            elif acude_cliente == "Secretaria":
                duracion = int(obtener_rango(numero, duracion_secre))
                if secretarias_disponibles > 0:
                    secretarias_disponibles -= 1
                else:
                    duracion = 0

            elif acude_cliente == "Cajero":
                duracion = int(obtener_rango(numero, duracion_cajero_a))
                if cajero_automatico_disponible > 0:
                    cajero_automatico_disponible -= 1
                else:
                    duracion = 0

            duracion_label = CTkLabel(tabla_frame, text=str(duracion), font=("Arial", 12), text_color="white")
            duracion_label.grid(row=i, column=4, padx=40, pady=10, sticky="nsew")

            if acude_cliente == "Ventanilla":
                caja_en_uso_label = CTkLabel(tabla_frame, text=str(cantidad_ventanillas - ventanillas_disponibles), font=("Arial", 12), text_color="white")
                caja_en_uso_label.grid(row=i, column=5, padx=40, pady=10, sticky="nsew")

                caja_disponible_label = CTkLabel(tabla_frame, text=str(ventanillas_disponibles), font=("Arial", 12), text_color="white")
                caja_disponible_label.grid(row=i, column=6, padx=40, pady=10, sticky="nsew")

            elif acude_cliente == "Secretaria":
                secre_en_uso_label = CTkLabel(tabla_frame, text=str(cantidad_secretarias - secretarias_disponibles), font=("Arial", 12), text_color="white")
                secre_en_uso_label.grid(row=i, column=7, padx=60, pady=10, sticky="nsew")

                secre_disponible_label = CTkLabel(tabla_frame, text=str(secretarias_disponibles), font=("Arial", 12), text_color="white")
                secre_disponible_label.grid(row=i, column=8, padx=40, pady=10, sticky="nsew")

            elif acude_cliente == "Cajero":
                cajero_en_uso_label = CTkLabel(tabla_frame, text=str(cantidad_cajeros_automaticos - cajero_automatico_disponible), font=("Arial", 12), text_color="white")
                cajero_en_uso_label.grid(row=i, column=9, padx=40, pady=10, sticky="nsew")

                cajero_disponible_label = CTkLabel(tabla_frame, text=str(cajero_automatico_disponible), font=("Arial", 12), text_color="white")
                cajero_disponible_label.grid(row=i, column=10, padx=60, pady=10, sticky="nsew")

            hora_salida = horarios_entrada[acude_cliente] + timedelta(minutes=duracion)
            hora_salida_label = CTkLabel(tabla_frame, text=hora_salida.strftime("%H:%M"), font=("Arial", 12), text_color="white")
            hora_salida_label.grid(row=i, column=11, padx=50, pady=10, sticky="nsew")

            olvido_tarjt = obtener_rango(numero, olvido)
            olvido_label = CTkLabel(tabla_frame, text=olvido_tarjt, font=("Arial", 12), text_color="white")
            olvido_label.grid(row=i, column=12, padx=20, pady=10, sticky="nsew")

            eventos_salida.append((hora_salida, acude_cliente))

            if hora_salida.strftime("%H:%M") >= horario_cierre:
                break

        eventos_salida.sort()

        for evento in eventos_salida:
            hora_salida, acude_cliente = evento
            if acude_cliente == "Ventanilla":
                ventanillas_disponibles += 1
            elif acude_cliente == "Secretaria":
                secretarias_disponibles += 1
            elif acude_cliente == "Cajero":
                cajero_automatico_disponible += 1


