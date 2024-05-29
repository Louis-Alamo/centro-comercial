from util.NumerosAleatorios import generar_aleatorio, generar_numeros_aleatorios
from customtkinter import CTk, CTkLabel, CTkFrame, CTkCanvas, CTkScrollbar
from datetime import datetime, timedelta
from tkinter import ttk
import tkinter
import json
import os


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

def generar_numeros_aleatorios(hora_apertura, hora_cierre, lapso_usuarios):
    numeros = []
    hora_actual = hora_apertura
    while True:
        numero = round(generar_aleatorio(), 4)
        incremento_minutos = 0
        for incremento, rango in lapso_usuarios:
            limite_inferior, limite_superior = map(float, rango.split("-"))
            if limite_inferior <= numero <= limite_superior:
                incremento_minutos = incremento
                break
        hora_salida = incrementar_hora(hora_actual, incremento_minutos)
        if hora_salida > hora_cierre:
            break
        numeros.append(numero)
        hora_actual = hora_salida
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

def obtener_genero_segun_rango(rango_aleatorio, lista_sexo):
    for genero, rango in lista_sexo:
        limite_inferior, limite_superior = map(float, rango.split("-"))
        if limite_inferior <= rango_aleatorio <= limite_superior:
            return genero
    return "Otro" 

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
    def __init__(self, cantidad_dias):
        self.total_cobro = 0
        self.total_personas = 0
        self.total_hombres = 0
        self.total_mujeres = 0
        self.total_otros = 0
        self.ventana = CTk()
        self.ventana.title("Gimnasio")
        self.ventana.geometry("1150x800+350+100")
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
        horario_apertura = self.datos.get("horario_apertura", [])
        horario_cierre = self.datos.get("horario_cierre", [])
        lapso_usuarios = self.datos.get("lapso_usuarios", [])
        self.capacidad_gym = self.datos.get("capacidad_gym", 0)

        self.ejecutar_simulacion()
        for i in range(cantidad_dias):
            self.numeros_aleatorios = generar_numeros_aleatorios(horario_apertura, horario_cierre, lapso_usuarios)
            self.crear_tabla_simulacion(self.numeros_aleatorios)
        self.resultados_finales()
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

        temporada_label = CTkLabel(self.inner_frame, text=f"Descuento del {descuento * 100}% aplicado durante la {temporada}", font=("Arial", 12), text_color="white")
        temporada_label.pack(padx=20, pady=5)

        resultados = {
            "Cobro Por Usuario (Sin Descuento)": self.cobro,
            "Cobro Por Usuario (Con Descuento)": self.cobro_final}

        resultados_label = CTkLabel(self.inner_frame, text=f"Resultados de la simulación GIMNASIO:\n{json.dumps(resultados, indent=2)}", font=("Arial", 20), text_color="white")
        resultados_label.pack(padx=20, pady=20, fill="x", expand=True)

    def crear_tabla_simulacion(self, numeros):
        columnas = ["ALEATORIOS", "PERSONAS", "COBRO", "LLEGO", "DURACION", "TIEMPO BAÑO", "SALIDA", "MAQUINAS USO", "SIN USO", "HOMBRE/MUJER/OTRO"]
        llegada_usuarios = self.datos.get("llegada_usuarios", [])
        horario_apertura = self.datos.get("horario_apertura", [])
        horario_cierre = self.datos.get("horario_cierre", [])
        lapso_usuarios = self.datos.get("lapso_usuarios", [])
        duracion_gym = self.datos.get("duracion_gym", [])
        duracion_baño = self.datos.get("duracion_baño", [])
        cantidad_maquinas = self.datos.get("cantidad_maquinas", 0)
        lista_sexo = self.datos.get("lista_sexo", [])

        tabla_frame = CTkFrame(self.inner_frame)
        tabla_frame.pack(padx=20, pady=10, fill="x", expand=True)

        tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings")
        tabla.pack(side="left", fill="both", expand=True)

        for columna, ancho in zip(columnas, [10]*14):
            tabla.heading(columna, text=columna)
            tabla.column(columna, width=ancho, anchor="center")

        scrollbar = CTkScrollbar(tabla_frame, command=tabla.yview)
        scrollbar.pack(side="right", fill="y")
        tabla.configure(yscrollcommand=scrollbar.set)

        total_cobro = 0
        total_cobro_descuento = 0

        for i, aleatorio in enumerate(numeros):
            personas = obtener_personas_segun_rango(aleatorio, llegada_usuarios)
            llego = incrementar_hora(horario_apertura, i * lapso_usuarios[0][0])
            duracion = obtener_duracion_segun_rango(aleatorio, duracion_gym)
            tiempo_baño = obtener_tiempo_baño_segun_rango(aleatorio, duracion_baño)
            salida = incrementar_hora(llego, duracion + tiempo_baño)
            genero = obtener_genero_segun_rango(aleatorio, lista_sexo)
            cobro = self.cobro_final * personas
            maquinas_en_uso = personas
            maquinas_sin_uso = cantidad_maquinas - maquinas_en_uso
            total_cobro += self.cobro * personas
            total_cobro_descuento += cobro

            fila = [aleatorio, personas, cobro, llego, duracion, tiempo_baño, salida, maquinas_en_uso, maquinas_sin_uso, genero]
            tabla.insert("", "end", values=fila)

            self.total_personas += personas
            if genero == "Masculino":
                self.total_hombres += personas
            elif genero == "Femenino":
                self.total_mujeres += personas
            else:
                self.total_otros += personas

        self.total_cobro = total_cobro
        self.total_cobro_descuento = total_cobro_descuento

    def resultados_finales(self):
        resultados_finales = tkinter.Toplevel()
        resultados_finales.title("Resultados Finales Gimnasio")
        resultados_finales.configure(bg="gray")


        total_personas_label = CTkLabel(resultados_finales, text=f"Cantidad Total de Personas: {self.total_personas}", font=("Arial", 18), text_color="white")
        total_personas_label.pack(padx=20, pady=10)
 
        total_hombres_label = CTkLabel(resultados_finales, text=f"Cantidad Total de Hombres: {self.total_hombres}", font=("Arial", 18), text_color="white")
        total_hombres_label.pack(padx=20, pady=10)
        total_mujeres_label = CTkLabel(resultados_finales, text=f"Cantidad Total de Mujeres: {self.total_mujeres}", font=("Arial", 18), text_color="white")
        total_mujeres_label.pack(padx=20, pady=10)
        total_otros_label = CTkLabel(resultados_finales, text=f"Cantidad Total de Otros: {self.total_otros}", font=("Arial", 18), text_color="white")
        total_otros_label.pack(padx=20, pady=10)

 
