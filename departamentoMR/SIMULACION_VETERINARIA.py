from customtkinter import CTk, CTkLabel, CTkFrame, CTkCanvas, CTkScrollbar
import json
import os
import random
from datetime import datetime, timedelta

ruta_archivo = os.path.dirname(os.path.abspath(__file__))
ruta_completa = os.path.join(ruta_archivo, 'veterinaria.json')

def cargar_datos():
    try:
        with open(ruta_completa, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("El archivo veterinaria.json no se encontró.")
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
    ruta_numeros = os.path.join(ruta_archivo, 'A_veterinaria.txt')
    with open(ruta_numeros, 'w') as file:
        for numero in numeros:
            file.write(f"{numero}\n")
    return numeros

def determinar_temporada():
    datos = cargar_datos()
    if datos.get("temporada_alta", [False])[0]:
        return "alta"
    elif datos.get("temporada_regular", [False])[0]:
        return "regular"
    elif datos.get("temporada_baja", [False])[0]:
        return "baja"
    return "sin temporada"

class SimulacionVeterinaria:
    def __init__(self):
        self.total_cobro = 0
        self.ventana = CTk()
        self.ventana.title("Veterinaria")
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
        self.inventario_inicial = self.datos.get("paquetes_alimento", 0) 
        self.ejecutar_simulacion()
        self.numeros_aleatorios = generar_numeros_aleatorios(10)
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
        
        self.costo_alimento_normal = self.datos.get("precio_por_alimento", 0)
        self.costo_medicamento_normal = self.datos.get("precio_medicamento", 0)
        self.costo_accesorio_normal = self.datos.get("precio_accesorios", 0)
        
        self.alimento_descuento = self.costo_alimento_normal * (1 - descuento)
        self.medicamento_descuento = self.costo_medicamento_normal * (1 - descuento)
        self.accesorio_descuento = self.costo_accesorio_normal * (1 - descuento)

        temporada_regular = self.datos.get("temporada_regular", False)
        temporada_alta = self.datos.get("temporada_alta", False)
        temporada_baja = self.datos.get("temporada_baja", False)

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
            "Precio Normal Alimento": self.costo_alimento_normal,
            "Precio Alimento Con Descuento": self.alimento_descuento,
            "Precio Normal Medicamento": self.costo_medicamento_normal,
            "Precio Medicamento Con Descuento": self.medicamento_descuento,
            "Precio Normal Accesorio": self.costo_accesorio_normal,
            "Precio Accesorio Con Descuento": self.accesorio_descuento
        }

        resultados_label = CTkLabel(self.inner_frame, text=f"Resultados de la simulación VETERINARIA:\n{json.dumps(resultados, indent=2)}", font=("Arial", 20), text_color="white")
        resultados_label.pack(padx=20, pady=20, fill="x", expand=True)

    def obtener_tiempo_consulta(self, aleatorio, lista_tiempo):
        for tiempo, rango in lista_tiempo:
            rango_inicio, rango_fin = map(float, rango.split('-'))
            if rango_inicio <= aleatorio <= rango_fin:
                return tiempo
        return 0

    def obtener_cantidad_alimento(self, aleatorio, lista_alimento):
        for cantidad, rango in lista_alimento:
            rango_inicio, rango_fin = map(float, rango.split('-'))
            if rango_inicio <= aleatorio <= rango_fin:
                return cantidad
        return 0

    def obtener_cantidad_medicamentos(self, aleatorio, lista_medicamento):
        for cantidad, rango in lista_medicamento:
            rango_inicio, rango_fin = map(float, rango.split('-'))
            if rango_inicio <= aleatorio <= rango_fin:
                return cantidad
        return 0
    
    def obtener_cantidad_accesorios(self, aleatorio, lista_accesorios):
        for cantidad, rango in lista_accesorios:
            rango_inicio, rango_fin = map(float, rango.split('-'))
            if rango_inicio <= aleatorio <= rango_fin:
                return cantidad
        return 0
    def obtener_cantidad_mascotas(self, aleatorio, lista_mascotas):
        for cantidad, rango in lista_mascotas:
            rango_inicio, rango_fin = map(float, rango.split('-'))
            if rango_inicio <= aleatorio <= rango_fin:
                return cantidad
        return 0

    def crear_tabla_simulacion(self, numeros):
        columnas = ["ALEATORIOS", "HORA INICIO", "HORA TERMINA", "ALIMENTO", "TOTAL", "RESTANTE", "MEDICAMENTO", "TOTAL", "RESTANTE", "ACCESORIOS", "TOTAL", "RESTANTE","MASCOTAS ATENDIDAS"]

        header_frame = CTkFrame(self.inner_frame)
        header_frame.pack(padx=20, pady=10, fill="x")

        for i, columna in enumerate(columnas):
            columna_label = CTkLabel(header_frame, text=columna, font=("Arial", 12, "bold"), text_color="white")
            columna_label.grid(row=0, column=i, padx=10, pady=5, sticky="nsew")
            header_frame.grid_columnconfigure(i, weight=1)

        tabla_frame = CTkFrame(self.inner_frame)
        tabla_frame.pack(padx=20, pady=10, fill="both", expand=True)

        lista_tiempo = self.datos.get("lista_tiempo", [])
        lista_alimento = self.datos.get("lista_alimento", [])
        lista_medicamento = self.datos.get("lista_medicamento", [])
        lista_accesorios = self.datos.get("lista_accesorios", [])
        lista_mascotas = self.datos.get("lista_mascotas", [])
        horario_entrada = datetime.strptime(self.datos["horario_entrada"], "%H:%M")
        hora_salida_almuerzo = datetime.strptime(self.datos["horario_salida_almuerzo"], "%H:%M")
        hora_regreso_almuerzo = datetime.strptime(self.datos["horario_entrada_almuerzo"], "%H:%M")
        
        inventario_restante_alimento = self.inventario_inicial
        inventario_restante_medicamento = self.datos.get("cantidad_medicamento", 0)
        inventario_restante_accesorios = self.datos.get("cantidad_accesorios", 0)

        for i, numero in enumerate(numeros):
            tiempo_consulta = self.obtener_tiempo_consulta(numero, lista_tiempo)
            cantidad_alimento = self.obtener_cantidad_alimento(numero, lista_alimento)
            cantidad_medicamentos = self.obtener_cantidad_medicamentos(numero, lista_medicamento)
            cantidad_accesorios = self.obtener_cantidad_accesorios(numero, lista_accesorios)
            horario_salida = horario_entrada + timedelta(minutes=tiempo_consulta)

            if horario_salida > hora_salida_almuerzo and horario_entrada < hora_salida_almuerzo:
                tiempo_antes_almuerzo = (hora_salida_almuerzo - horario_entrada).seconds // 60
                tiempo_despues_almuerzo = tiempo_consulta - tiempo_antes_almuerzo
                horario_salida = hora_regreso_almuerzo + timedelta(minutes=tiempo_despues_almuerzo)

            total_alimento_descuento = cantidad_alimento * self.alimento_descuento

            if inventario_restante_alimento > 0:
                if inventario_restante_alimento >= cantidad_alimento:
                    inventario_restante_alimento -= cantidad_alimento
                else:
                    cantidad_alimento = inventario_restante_alimento
                    inventario_restante_alimento = 0

            if inventario_restante_alimento == 0:
                cantidad_alimento = 0
                total_alimento_descuento = 0
            else:
                total_alimento_descuento = cantidad_alimento * self.alimento_descuento

            if inventario_restante_medicamento > 0:
                if inventario_restante_medicamento >= cantidad_medicamentos:
                    inventario_restante_medicamento -= cantidad_medicamentos
                else:
                    cantidad_medicamentos = inventario_restante_medicamento
                    inventario_restante_medicamento = 0

            if inventario_restante_medicamento == 0:
                cantidad_medicamentos = 0
                total_medicamentos_descuento = 0 
            else:
                total_medicamentos_descuento = cantidad_medicamentos * self.medicamento_descuento

            if inventario_restante_accesorios > 0:
                if inventario_restante_accesorios >= cantidad_accesorios:
                    inventario_restante_accesorios -= cantidad_accesorios
                else:
                    cantidad_accesorios = inventario_restante_accesorios
                    inventario_restante_accesorios = 0

            if inventario_restante_accesorios == 0:
                cantidad_accesorios = 0
                total_accesorios_descuento = 0
            else:
                total_accesorios_descuento = cantidad_accesorios * self.accesorio_descuento

            cantidad_mascotas_atendidas = self.obtener_cantidad_mascotas(numero, lista_mascotas)

            aleatorio_label = CTkLabel(tabla_frame, text=str(numero), font=("Arial", 12), text_color="white")
            aleatorio_label.grid(row=i, column=0, padx=(10, 20), pady=10, sticky="nsew")
            horario_inicio_label = CTkLabel(tabla_frame, text=horario_entrada.strftime("%H:%M"), font=("Arial", 12), text_color="white")
            horario_inicio_label.grid(row=i, column=1, padx=(60, 20), pady=10, sticky="nsew")
            horario_salida_label = CTkLabel(tabla_frame, text=horario_salida.strftime("%H:%M"), font=("Arial", 12), text_color="white")
            horario_salida_label.grid(row=i, column=2, padx=(60, 20), pady=10, sticky="nsew")
            alimento_label = CTkLabel(tabla_frame, text=str(cantidad_alimento), font=("Arial", 12), text_color="white")
            alimento_label.grid(row=i, column=3, padx=(60, 20), pady=10, sticky="nsew")
            total_alimento_label = CTkLabel(tabla_frame, text=f"{total_alimento_descuento:.2f}", font=("Arial", 12), text_color="white")
            total_alimento_label.grid(row=i, column=4, padx=(50, 20), pady=10, sticky="nsew")
            restante_alimento_label = CTkLabel(tabla_frame, text=str(inventario_restante_alimento), font=("Arial", 12), text_color="white")
            restante_alimento_label.grid(row=i, column=5, padx=(50, 20), pady=10, sticky="nsew")
            medicamento_label = CTkLabel(tabla_frame, text=str(cantidad_medicamentos), font=("Arial", 12), text_color="white")
            medicamento_label.grid(row=i, column=6, padx=(60, 20), pady=10, sticky="nsew")
            total_medicamentos_label = CTkLabel(tabla_frame, text=f"{total_medicamentos_descuento:.2f}", font=("Arial", 12), text_color="white")
            total_medicamentos_label.grid(row=i, column=7, padx=(50, 20), pady=10, sticky="nsew")
            restante_medicamento_label = CTkLabel(tabla_frame, text=str(inventario_restante_medicamento), font=("Arial", 12), text_color="white")
            restante_medicamento_label.grid(row=i, column=8, padx=(50, 20), pady=10, sticky="nsew")
            accesorio_label = CTkLabel(tabla_frame, text=str(cantidad_accesorios), font=("Arial", 12), text_color="white")
            accesorio_label.grid(row=i, column=9, padx=(60, 20), pady=10, sticky="nsew")
            total_accesorios_label = CTkLabel(tabla_frame, text=f"{total_accesorios_descuento:.2f}", font=("Arial", 12), text_color="white")
            total_accesorios_label.grid(row=i, column=10, padx=(50, 20), pady=10, sticky="nsew")
            restante_accesorios_label = CTkLabel(tabla_frame, text=str(inventario_restante_accesorios), font=("Arial", 12), text_color="white")
            restante_accesorios_label.grid(row=i, column=11, padx=(50, 20), pady=10, sticky="nsew")
            mascotas_atendidas_label = CTkLabel(tabla_frame, text=str(cantidad_mascotas_atendidas), font=("Arial", 12), text_color="white")
            mascotas_atendidas_label.grid(row=i, column=12, padx=(60, 20), pady=10, sticky="nsew")

            horario_entrada = horario_salida

        for i in range(len(numeros)):
            tabla_frame.grid_rowconfigure(i, weight=1)

SimulacionVeterinaria()


