from customtkinter import CTk, CTkLabel, CTkFrame, CTkCanvas, CTkScrollbar
import NumerosAleatorios
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

def obtener_tipo_cliente(rango_aleatorio, tipo):
    for tipo_cliente, rango in tipo:
        limite_inferior, limite_superior = map(float, rango.split("-"))
        if limite_inferior <= rango_aleatorio <= limite_superior:
            return tipo_cliente
    return "Error"

def obtener_acude_cliente(rango_aleatorio, acude):
    for acude_cliente, rango in acude:
        limite_inferior, limite_superior = map(float, rango.split("-"))
        if limite_inferior <= rango_aleatorio <= limite_superior:
            return acude_cliente
    return "Error"

def obtener_tiempo_llegada(rango_aleatorio, horario_llegada):
    for llegada_cliente, rango in horario_llegada:
        limite_inferior, limite_superior = map(float, rango.split("-"))
        if limite_inferior <= rango_aleatorio <= limite_superior:
            return llegada_cliente
    return "Error"

def obtener_duracion_ventanilla(rango_aleatorio, duracion_ventanilla):
    for ventanilla_cliente, rango in duracion_ventanilla:
        limite_inferior, limite_superior = map(float, rango.split("-"))
        if limite_inferior <= rango_aleatorio <= limite_superior:
            return int(ventanilla_cliente)
    return "Error"

def obtener_duracion_secretaria(rango_aleatorio, duracion_secre):
    for secre_cliente, rango in duracion_secre:
        limite_inferior, limite_superior = map(float, rango.split("-"))
        if limite_inferior <= rango_aleatorio <= limite_superior:
            return int(secre_cliente)
    return "Error"

def obtener_duracion_cajero(rango_aleatorio, duracion_cajero_a):
    for cajero_cliente, rango in duracion_cajero_a:
        limite_inferior, limite_superior = map(float, rango.split("-"))
        if limite_inferior <= rango_aleatorio <= limite_superior:
            return int(cajero_cliente)
    return "Error"

def obtener_olvido_tarjeta(rango_aleatorio, olvido):
    for olvido_cliente, rango in olvido:
        limite_inferior, limite_superior = map(float, rango.split("-"))
        if limite_inferior <= rango_aleatorio <= limite_superior:
            return olvido_cliente
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

        numeros_aleatorios = [round(num, 4) for num in NumerosAleatorios.generar_numeros_aleatorios(10000)]

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
        ventanillas_en_uso = 0
        ventanillas_ocupadas = []

        secretarias_disponibles = cantidad_secretarias
        secretarias_en_uso = 0
        secretarias_ocupadas = []

        cajero_automatico_disponible = cantidad_cajeros_automaticos
        cajero_automatico_en_uso = 0
        cajero_automatico_ocupado = []

        for i, numero in enumerate(numeros_aleatorios):
            aleatorio_label = CTkLabel(tabla_frame, text=str(numero), font=("Arial", 12), text_color="white")
            aleatorio_label.grid(row=i, column=0, padx=20, pady=10, sticky="nsew")

            tipo_cliente = obtener_tipo_cliente(numero, tipo)
            tipo_label = CTkLabel(tabla_frame, text=tipo_cliente, font=("Arial", 12), text_color="white")
            tipo_label.grid(row=i, column=1, padx=35, pady=10, sticky="nsew")

            acude_cliente = obtener_acude_cliente(numero, acude)
            acude_label = CTkLabel(tabla_frame, text=acude_cliente, font=("Arial", 12), text_color="white")
            acude_label.grid(row=i, column=2, padx=10, pady=10, sticky="nsew")

            horario_llegada_cliente = obtener_tiempo_llegada(numero, horario_llegada)
            if acude_cliente not in horarios_entrada:
                horarios_entrada[acude_cliente] = datetime.strptime(horario_entrada, "%H:%M")
            horarios_entrada[acude_cliente] += timedelta(minutes=horario_llegada_cliente)
            horario_label = CTkLabel(tabla_frame, text=horarios_entrada[acude_cliente].strftime("%H:%M"), font=("Arial", 12), text_color="white")
            horario_label.grid(row=i, column=3, padx=30, pady=10, sticky="nsew")

            if acude_cliente == "Ventanilla":
                tiempo = obtener_duracion_ventanilla(numero, duracion_ventanilla)
                if ventanillas_disponibles > 0:
                    ventanillas_disponibles -= 1
                    ventanillas_en_uso += 1
                    ventanillas_ocupadas.append((horarios_entrada[acude_cliente], tiempo))
                else:
                    tiempo = 0
                caja_en_uso_label = CTkLabel(tabla_frame, text=str(ventanillas_en_uso), font=("Arial", 12), text_color="white")
                caja_en_uso_label.grid(row=i, column=5, padx=40, pady=10, sticky="nsew")

                caja_disponible_label = CTkLabel(tabla_frame, text=str(ventanillas_disponibles), font=("Arial", 12), text_color="white")
                caja_disponible_label.grid(row=i, column=6, padx=40, pady=10, sticky="nsew")
            else:
                tiempo = obtener_duracion_secretaria(numero, duracion_secre) if acude_cliente == "Secretaria" else obtener_duracion_cajero(numero, duracion_cajero_a)


            if acude_cliente == "Secretaria":
                tiempo = obtener_duracion_secretaria(numero, duracion_secre)
                if secretarias_disponibles > 0:
                    secretarias_disponibles -= 1
                    secretarias_en_uso += 1
                    secretarias_ocupadas.append((horarios_entrada[acude_cliente], tiempo))

                else:
                    tiempo = 0
                secre_en_uso_label = CTkLabel(tabla_frame, text=str(secretarias_en_uso), font=("Arial", 12), text_color="white")
                secre_en_uso_label.grid(row=i, column=7, padx=60, pady=10, sticky="nsew")

                secre_disponible_label = CTkLabel(tabla_frame, text=str(secretarias_disponibles), font=("Arial", 12), text_color="white")
                secre_disponible_label.grid(row=i, column=8, padx=40, pady=10, sticky="nsew")
            else:
                tiempo= obtener_duracion_cajero(numero, duracion_cajero_a) if acude_cliente == "Cajero" else obtener_duracion_ventanilla(numero, duracion_ventanilla)


            if acude_cliente == "Cajero":
                tiempo = obtener_duracion_cajero(numero, duracion_cajero_a)
                if cajero_automatico_disponible > 0:
                    cajero_automatico_disponible -= 1
                    cajero_automatico_en_uso += 1
                    cajero_automatico_ocupado.append((horarios_entrada[acude_cliente], tiempo))
                else:
                    tiempo = 0
                cajero_en_uso_label = CTkLabel(tabla_frame, text=str(cajero_automatico_en_uso), font=("Arial", 12), text_color="white")
                cajero_en_uso_label.grid(row=i, column=9, padx=40, pady=10, sticky="nsew")

                cajero_disponible_label = CTkLabel(tabla_frame, text=str(cajero_automatico_disponible), font=("Arial", 12), text_color="white")
                cajero_disponible_label.grid(row=i, column=10, padx=60, pady=10, sticky="nsew")

            else:
                tiempo = obtener_duracion_ventanilla(numero, duracion_ventanilla) if acude_cliente == "Ventanilla" else obtener_duracion_secretaria(numero, duracion_secre)


            tiempo_label = CTkLabel(tabla_frame, text=tiempo, font=("Arial", 12), text_color="white")
            tiempo_label.grid(row=i, column=4, padx=40, pady=10, sticky="nsew")

            hora_salida = horarios_entrada[acude_cliente] + timedelta(minutes=tiempo)
            hora_salida_label = CTkLabel(tabla_frame, text=hora_salida.strftime("%H:%M"), font=("Arial", 12), text_color="white")
            hora_salida_label.grid(row=i, column=11, padx=50, pady=10, sticky="nsew")

            olvido_tarjt = obtener_olvido_tarjeta(numero, olvido)
            olvido_label = CTkLabel(tabla_frame, text=olvido_tarjt, font=("Arial", 12), text_color="white")
            olvido_label.grid(row=i, column=12, padx=20, pady=10, sticky="nsew")

            if acude_cliente == "Ventanilla" and tiempo > 0:
                horarios_entrada[acude_cliente] = hora_salida
                for ventana, dur in ventanillas_ocupadas:
                    if hora_salida >= ventana + timedelta(minutes=dur):
                        ventanillas_ocupadas.remove((ventana, dur))
                        ventanillas_disponibles += 1
                        ventanillas_en_uso -= 1
                        break

            if acude_cliente == "Secretaria" and tiempo > 0:
                horarios_entrada[acude_cliente] = hora_salida
                for secre, dur in secretarias_ocupadas:
                    if hora_salida >= secre + timedelta(minutes=dur):
                        secretarias_ocupadas.remove((secre, dur))
                        secretarias_disponibles += 1
                        secretarias_en_uso -= 1
                        break

            if acude_cliente == "Cajero" and tiempo > 0:
                horarios_entrada[acude_cliente] = hora_salida
                for cajero, dur in cajero_automatico_ocupado:
                    if hora_salida >= cajero + timedelta(minutes=dur):
                        cajero_automatico_ocupado.remove((cajero, dur))
                        cajero_automatico_disponible += 1
                        cajero_automatico_en_uso -= 1
                        break

            if hora_salida.strftime("%H:%M") >= horario_cierre:
                break

