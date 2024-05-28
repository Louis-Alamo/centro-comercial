from customtkinter import CTk, CTkLabel, CTkFrame, CTkCanvas, CTkScrollbar
from datetime import datetime, timedelta
import json
import os
import tkinter as tk
from util.NumerosAleatorios import generar_aleatorio, generar_numeros_aleatorios


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
        self.total_mascotas = 0  
        self.total_personas = 0 
        self.total_alimentos_vendidos = 0
        self.ganancia_alimentos = 0
        self.total_medicamentos_vendidos = 0
        self.ganancia_medicamentos = 0
        self.total_accesorios_vendidos = 0
        self.ganancia_accesorios = 0
        self.datos = cargar_datos()
        self.almacen_alimentos = self.datos.get("paquetes_alimento", 0)
        self.almacen_medicamentos = self.datos.get("cantidad_medicamento", 0)
        self.almacen_accesorios = self.datos.get("cantidad_accesorios", 0)
        self.ventana = CTk()
        self.ventana.title("Veterinaria")
        self.ventana.geometry("1250x800+350+100")
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
        self.numeros_aleatorios = self.generar_hasta_horario_salida()
        self.total_personas = len(self.numeros_aleatorios) 
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

        temporada_label = CTkLabel(self.inner_frame, text=f"Descuento del {descuento * 100}% aplicado durante la {temporada}", font=("Arial", 15), text_color="white")
        temporada_label.pack(padx=20, pady=5)

        resultados = {
            "Precio Normal Alimento": self.costo_alimento_normal,
            "Precio Alimento Con Descuento": self.alimento_descuento,
            "Precio Normal Medicamento": self.costo_medicamento_normal,
            "Precio Medicamento Con Descuento": self.medicamento_descuento,
            "Precio Normal Accesorio": self.costo_accesorio_normal,
            "Precio Accesorio Con Descuento": self.accesorio_descuento
        }

        resultados_label = CTkLabel(self.inner_frame, text=f"Resultados de la simulación VETERINARIA:\n{json.dumps(resultados, indent=2)}", font=("Arial", 15), text_color="white")
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

    def generar_hasta_horario_salida(self):
        horario_salida = datetime.strptime(self.datos.get("horario_salida", "17:00"), "%H:%M")
        horario_entrada = datetime.strptime(self.datos.get("horario_entrada", "08:00"), "%H:%M")
        hora_actual = horario_entrada
        numeros = []

        while hora_actual < horario_salida:
            numero = round(generar_aleatorio(), 4)
            numeros.append(numero)
            tiempo_consulta = self.obtener_tiempo_consulta(numero, self.datos.get("lista_tiempo", []))
            hora_actual += timedelta(minutes=tiempo_consulta)

        return numeros


    def crear_tabla_simulacion(self, numeros):
        columnas = ["ALEATORIOS", "MASCOTAS","VETERINARIOS", "HORA INICIO", "HORA TERMINA", "ALIMENTO", "TOTAL", "RESTANTE", "MEDICAMENTO", "TOTAL", "RESTANTE", "ACCESORIOS", "TOTAL", "RESTANTE"]

        header_frame = CTkFrame(self.inner_frame)
        header_frame.pack(padx=20, pady=10, fill="x")

        for i, columna in enumerate(columnas):
            columna_label = CTkLabel(header_frame, text=columna, font=("Arial", 12), text_color="white")
            columna_label.grid(row=0, column=i, padx=10, pady=5, sticky="nsew")

        tabla_frame = CTkFrame(self.inner_frame)
        tabla_frame.pack(padx=20, pady=10, fill="both", expand=True)

        lista_tiempo = self.datos.get("lista_tiempo", [])
        lista_alimento = self.datos.get("lista_alimento", [])
        lista_medicamento = self.datos.get("lista_medicamento", [])
        lista_accesorios = self.datos.get("lista_accesorios", [])
        lista_mascotas = self.datos.get("lista_mascotas", [])
        cantidad_veterinarios = self.datos.get("cantidad_veterinarios", 0)
        
        inventario_restante_alimento = self.inventario_inicial
        inventario_restante_medicamento = self.datos.get("cantidad_medicamento", 0)
        inventario_restante_accesorios = self.datos.get("cantidad_accesorios", 0)

        horario_entrada = self.datos.get("horario_entrada", "08:00")
        hora_actual = datetime.strptime(horario_entrada, "%H:%M")

        for i, numero in enumerate(numeros):
            tiempo_consulta = self.obtener_tiempo_consulta(numero, lista_tiempo)
            cantidad_alimento = self.obtener_cantidad_alimento(numero, lista_alimento)
            cantidad_medicamentos = self.obtener_cantidad_medicamentos(numero, lista_medicamento)
            cantidad_accesorios = self.obtener_cantidad_accesorios(numero, lista_accesorios)
            cantidad_mascotas = self.obtener_cantidad_mascotas(numero, lista_mascotas)

            self.total_mascotas += cantidad_mascotas

            horario_inicio = hora_actual
            horario_termina = horario_inicio + timedelta(minutes=tiempo_consulta)

            aleatorio_label = CTkLabel(tabla_frame, text=str(numero), font=("Arial", 12), text_color="white")
            aleatorio_label.grid(row=i, column=1, padx=(20, 20), pady=10, sticky="nsew")
            
            mascotas_label = CTkLabel(tabla_frame, text=str(cantidad_mascotas), font=("Arial", 12), text_color="white")
            mascotas_label.grid(row=i, column=2, padx=40, pady=10, sticky="nsew")

            veterinarios_label = CTkLabel(tabla_frame, text=str(cantidad_veterinarios), font=("Arial", 12), text_color="white")
            veterinarios_label.grid(row=i, column=3, padx=40, pady=10, sticky="nsew")

            hora_inicio_label = CTkLabel(tabla_frame, text=horario_inicio.strftime("%H:%M"), font=("Arial", 12), text_color="white")
            hora_inicio_label.grid(row=i, column=4, padx=40, pady=10, sticky="nsew")

            hora_termina_label = CTkLabel(tabla_frame, text=horario_termina.strftime("%H:%M"), font=("Arial", 12), text_color="white")
            hora_termina_label.grid(row=i, column=5, padx=40, pady=10, sticky="nsew")

            if inventario_restante_alimento <= 0 or cantidad_alimento > inventario_restante_alimento:
                cantidad_alimento = 0
                total_alimento = 0
            else:
                total_alimento = self.alimento_descuento * cantidad_alimento

            cantidad_alimento_label = CTkLabel(tabla_frame, text=str(cantidad_alimento), font=("Arial", 12), text_color="white")
            cantidad_alimento_label.grid(row=i, column=6, padx=40, pady=10, sticky="nsew")

            total_alimento_label = CTkLabel(tabla_frame, text=str(total_alimento), font=("Arial", 12), text_color="white")
            total_alimento_label.grid(row=i, column=7, padx=20, pady=10, sticky="nsew")

            inventario_restante_alimento -= cantidad_alimento
            inventario_restante_alimento_label = CTkLabel(tabla_frame, text=str(inventario_restante_alimento), font=("Arial", 12), text_color="white")
            inventario_restante_alimento_label.grid(row=i, column=8, padx=30, pady=10, sticky="nsew")
            
            self.total_alimentos_vendidos += cantidad_alimento
            total_alimento = self.alimento_descuento * cantidad_alimento
            self.ganancia_alimentos += total_alimento
    

            if inventario_restante_medicamento <= 0 or cantidad_medicamentos > inventario_restante_medicamento:
                cantidad_medicamentos = 0
                total_medicamentos = 0
            else:
                total_medicamentos = self.medicamento_descuento * cantidad_medicamentos

            cantidad_medicamentos_label = CTkLabel(tabla_frame, text=str(cantidad_medicamentos), font=("Arial", 12), text_color="white")
            cantidad_medicamentos_label.grid(row=i, column=9, padx=40, pady=10, sticky="nsew")

            total_medicamentos_label = CTkLabel(tabla_frame, text=str(total_medicamentos), font=("Arial", 12), text_color="white")
            total_medicamentos_label.grid(row=i, column=10, padx=25, pady=10, sticky="nsew")

            inventario_restante_medicamento -= cantidad_medicamentos
            inventario_restante_medicamento_label = CTkLabel(tabla_frame, text=str(inventario_restante_medicamento), font=("Arial", 12), text_color="white")
            inventario_restante_medicamento_label.grid(row=i, column=11, padx=40, pady=10, sticky="nsew")

            self.total_medicamentos_vendidos += cantidad_medicamentos
            total_medicamentos = self.medicamento_descuento * cantidad_medicamentos
            self.ganancia_medicamentos += total_medicamentos


            if inventario_restante_accesorios <= 0 or cantidad_accesorios > inventario_restante_accesorios:
                cantidad_accesorios = 0
                total_accesorios = 0
            else:
                total_accesorios = self.accesorio_descuento * cantidad_accesorios

            cantidad_accesorios_label = CTkLabel(tabla_frame, text=str(cantidad_accesorios), font=("Arial", 12), text_color="white")
            cantidad_accesorios_label.grid(row=i, column=12, padx=35, pady=10, sticky="nsew")

            total_accesorios_label = CTkLabel(tabla_frame, text=str(total_accesorios), font=("Arial", 12), text_color="white")
            total_accesorios_label.grid(row=i, column=13, padx=25, pady=10, sticky="nsew")

            inventario_restante_accesorios -= cantidad_accesorios
            inventario_restante_accesorios_label = CTkLabel(tabla_frame, text=str(inventario_restante_accesorios), font=("Arial", 12), text_color="white")
            inventario_restante_accesorios_label.grid(row=i, column=14, padx=30, pady=10, sticky="nsew")

            self.total_accesorios_vendidos += cantidad_accesorios
            total_accesorios = self.accesorio_descuento * cantidad_accesorios
            self.ganancia_accesorios += total_accesorios


            hora_actual = horario_termina 

        for i in range(len(numeros)):
            tabla_frame.grid_rowconfigure(i, weight=1)


        def show_results():
            window = tk.Toplevel()
            window.title("Resultados")
            
            
            total_personas_label = tk.Label(window, text=f"Total de Personas Atendidas: {self.total_personas}", font=("Arial", 15), fg="black")
            total_personas_label.pack(pady=10)
            en_un_horario_de= tk.Label(window, text=f"En un horario de {horario_entrada} a {self.datos.get('horario_salida')}", font=("Arial", 15), fg="black")
            en_un_horario_de.pack(pady=10)
            total_mascotas_label = tk.Label(window, text=f"Total de Mascotas Atendidas: {self.total_mascotas}", font=("Arial", 15), fg="black")
            total_mascotas_label.pack(pady=10)
            
            resultados_alimentos_label = tk.Label(window, text=f"Total Por Paquetes De Alimentos Vendidos: {self.total_alimentos_vendidos}\n"
                                                               f"Ganancia de Alimentos: {self.ganancia_alimentos}\n"
                                                               f"Alimentos Restantes en Almacén: {self.almacen_alimentos - self.total_alimentos_vendidos}\n",
                                                  font=("Arial", 15), fg="black")
            resultados_alimentos_label.pack(padx=10, pady=10, fill="x")

            resultados_medicamentos_label = tk.Label(window, text=f"Total Medicamentos Vendidos: {self.total_medicamentos_vendidos}\n"
                                                                 f"Ganancia de Medicamentos: {self.ganancia_medicamentos}\n"
                                                                 f"Medicamentos Restantes en Almacén: {self.almacen_medicamentos - self.total_medicamentos_vendidos}\n",
                                                     font=("Arial", 15), fg="black")
            resultados_medicamentos_label.pack(padx=10, pady=10, fill="x")

            resultados_accesorios_label = tk.Label(window, text=f"Total Accesorios Vendidos: {self.total_accesorios_vendidos}\n"
                                                                f"Ganancia de Accesorios: {self.ganancia_accesorios}\n"
                                                                f"Accesorios Restantes en Almacén: {self.almacen_accesorios - self.total_accesorios_vendidos}\n",
                                                   font=("Arial", 15), fg="black")
            resultados_accesorios_label.pack(padx=10, pady=10, fill="x")

            ganancia_total = self.ganancia_alimentos + self.ganancia_medicamentos + self.ganancia_accesorios

            sueldo_gerente = self.datos.get("sueldo_mensual_gerente", 0)
            sueldog = sueldo_gerente * self.datos.get("cantidad_gerentes", 0)
            sueldo_veterinario = self.datos.get("sueldo_mensual_veterinario", 0)
            sueldov = sueldo_veterinario * self.datos.get("cantidad_veterinarios", 0)

            sueldos_totales = sum([sueldog]) + sum([sueldov])

            gasto_luz = self.datos.get("pago_mensual_luz", 0)
            gasto_agua = self.datos.get("pago_mensual_agua", 0)
            gasto_internet = self.datos.get("pago_mensual_internet", 0)
            gasto_spotify = self.datos.get("pago_mensual_spotify", 0)
            gasto_renta_local = self.datos.get("pago_mensual_renta_local", 0)
            gastos_mensuales = sum([gasto_luz, gasto_agua, gasto_internet, gasto_spotify, gasto_renta_local])

            analisis_ganancia = "buena" if ganancia_total >= sueldos_totales + gastos_mensuales else "insuficiente"
            sueldoPersonal = f"Sueldo Por Gerentes: ${sueldog} + Sueldo Por Veterinarios: ${sueldov}\n generan un total de: ${sueldos_totales} mensuales"
            gastos = f"Gastos Mensuales Contemplando Todos Los Servicios: ${gastos_mensuales}"
            comentario = f"SE OBTUVO UNA GANANCIA TOTAL DE ${ganancia_total}, que es {analisis_ganancia} para cubrir los sueldos y gastos mensuales."

            sueldoPersonal_label = tk.Label(window, text=sueldoPersonal, font=("Arial", 15), fg="black")
            sueldoPersonal_label.pack(padx=10, pady=10, fill="x")
            
            gastos_label = tk.Label(window, text=gastos, font=("Arial", 15), fg="black")
            gastos_label.pack(padx=10, pady=10, fill="x")
            
            resultado_label = tk.Label(window, text=comentario, font=("Arial", 15), fg="black")
            resultado_label.pack(padx=10, pady=10, fill="x")

        show_results()


        