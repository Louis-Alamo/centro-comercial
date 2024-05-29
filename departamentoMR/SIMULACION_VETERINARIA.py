from customtkinter import CTk, CTkLabel, CTkFrame, CTkCanvas, CTkScrollbar
from util.NumerosAleatorios import generar_aleatorio
from datetime import datetime, timedelta
from tkinter import ttk
import tkinter
import json
import os


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
    def __init__(self,cantidad_dias):
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
        
        for i in range(cantidad_dias):
            self.numeros_aleatorios = self.generar_hasta_horario_salida()
            self.total_personas = len(self.numeros_aleatorios) 
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
        columnas = ["ALEATORIOS", "MASCOTAS", "VETERINARIOS", "HORA INICIO", "HORA TERMINA", "ALIMENTO", "TOTAL AL", "RESTANTE AL", "MEDICAMENTO", "TOTAL M", "RESTANTE M", "ACCESORIOS", "TOTAL A", "RESTANTE A"]


        tree_frame = CTkFrame(self.inner_frame)
        tree_frame.pack(padx=20, pady=10, fill="x", expand=True)

        tree = ttk.Treeview(tree_frame, columns=columnas, show="headings")
        tree.pack(side="left", fill="both", expand=True)

        for columna, ancho in zip(columnas, [10]*14):
            tree.heading(columna, text=columna)
            tree.column(columna, width=ancho, anchor="center")

        scrollbar = CTkScrollbar(tree_frame, command=tree.yview)
        scrollbar.pack(side="right", fill="y")
        tree.configure(yscrollcommand=scrollbar.set)

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

            if inventario_restante_alimento <= 0 or cantidad_alimento > inventario_restante_alimento:
                cantidad_alimento = 0
                total_alimento = 0
            else:
                total_alimento = self.alimento_descuento * cantidad_alimento

            inventario_restante_alimento -= cantidad_alimento

            if inventario_restante_medicamento <= 0 or cantidad_medicamentos > inventario_restante_medicamento:
                cantidad_medicamentos = 0
                total_medicamentos = 0
            else:
                total_medicamentos = self.medicamento_descuento * cantidad_medicamentos

            inventario_restante_medicamento -= cantidad_medicamentos

            if inventario_restante_accesorios <= 0 or cantidad_accesorios > inventario_restante_accesorios:
                cantidad_accesorios = 0
                total_accesorios = 0
            else:
                total_accesorios = self.accesorio_descuento * cantidad_accesorios

            inventario_restante_accesorios -= cantidad_accesorios

            self.total_alimentos_vendidos += cantidad_alimento
            self.ganancia_alimentos += total_alimento
            self.total_medicamentos_vendidos += cantidad_medicamentos
            self.ganancia_medicamentos += total_medicamentos
            self.total_accesorios_vendidos += cantidad_accesorios
            self.ganancia_accesorios += total_accesorios


            tree.insert("", "end", values=(numero, cantidad_mascotas, cantidad_veterinarios, horario_inicio.strftime("%H:%M"),
                                        horario_termina.strftime("%H:%M"), cantidad_alimento, total_alimento,
                                        inventario_restante_alimento, cantidad_medicamentos, total_medicamentos,
                                        inventario_restante_medicamento, cantidad_accesorios, total_accesorios,
                                        inventario_restante_accesorios))

            hora_actual = horario_termina

            

    def resultados_finales(self):
        resultados_finales = tkinter.Toplevel()
        resultados_finales.title("Resultados Finales Veterinaria")
        resultados_finales.configure(bg="gray")

        total_mascotas_simuladas = self.total_mascotas
        total_alimentos_vendidos = self.total_alimentos_vendidos
        total_medicamentos_vendidos = self.total_medicamentos_vendidos
        total_accesorios_vendidos = self.total_accesorios_vendidos
        total_ganancia_alimentos = self.ganancia_alimentos
        total_ganancia_medicamentos = self.ganancia_medicamentos
        total_ganancia_accesorios = self.ganancia_accesorios
        horario_entrada = self.datos.get("horario_entrada", 0)
        horario_salida = self.datos.get("horario_salida", 0)
        cantidad_gerentes = self.datos.get("cantidad_gerentes", 0)
        sueldo_mensual_gerente = self.datos.get("sueldo_mensual_gerente", 0)
        cantidad_veterinarios = self.datos.get("cantidad_veterinarios", 0)
        sueldo_mensual_veterinario = self.datos.get("sueldo_mensual_veterinario", 0)
        pago_mensual_luz = self.datos.get("pago_mensual_luz", 0)
        pago_mensual_agua = self.datos.get("pago_mensual_agua", 0)
        pago_mensual_internet = self.datos.get("pago_mensual_internet", 0)
        pago_mensual_spotify = self.datos.get("pago_mensual_spotify", 0)
        pago_mensual_renta_local = self.datos.get("pago_mensual_renta_local", 0)

        gastos_servicios = pago_mensual_luz + pago_mensual_agua + pago_mensual_internet + pago_mensual_spotify
        sueldo_personal = cantidad_gerentes * sueldo_mensual_gerente + cantidad_veterinarios * sueldo_mensual_veterinario

        horario_label = CTkLabel(resultados_finales, text=f"En un horario de atención por día de: {horario_entrada} - {horario_salida}", font=("Arial", 18), text_color="white")
        horario_label.pack(padx=20, pady=10)
        
        total_mascotas_label = CTkLabel(resultados_finales, text=f"Se atendió a {total_mascotas_simuladas} mascotas", font=("Arial", 18), text_color="white")
        total_mascotas_label.pack(padx=20, pady=10)

        total_alimentos_label = CTkLabel(resultados_finales, text=f"En esos días simulados se vendieron: {total_alimentos_vendidos} paquetes de alimento", font=("Arial", 18), text_color="white")
        total_alimentos_label.pack(padx=20, pady=10)

        total_medicamentos_label = CTkLabel(resultados_finales, text=f"También se vendieron: {total_medicamentos_vendidos} de medicamentos y", font=("Arial", 18), text_color="white")
        total_medicamentos_label.pack(padx=20, pady=10)

        total_accesorios_label = CTkLabel(resultados_finales, text=f" {total_accesorios_vendidos} accesorios para las mascotas", font=("Arial", 18), text_color="white")
        total_accesorios_label.pack(padx=20, pady=10)

        total_ganancia = CTkLabel(resultados_finales, text=f"Con un total de ganancias por alimentos, medicamentos y accesorios de: ${total_ganancia_alimentos}, ${total_ganancia_medicamentos}, ${total_ganancia_accesorios}, respectivamente.", font=("Arial", 18), text_color="white")
        total_ganancia.pack(padx=20, pady=10)

        gastos_personal = CTkLabel(resultados_finales, text=f"Gastos mensuales en personal de: ${sueldo_personal}", font=("Arial", 18), text_color="white")
        gastos_personal.pack(padx=20, pady=10)

        gastos_servicios_label = CTkLabel(resultados_finales, text=f"Gastos mensuales en servicios de luz, agua, internet: ${gastos_servicios}", font=("Arial", 18), text_color="white")
        gastos_servicios_label.pack(padx=20, pady=10)

        gastos_renta = CTkLabel(resultados_finales, text=f"Y gastos mensuales en renta del local: ${pago_mensual_renta_local}", font=("Arial", 18), text_color="white")
        gastos_renta.pack(padx=20, pady=10)

        total_gastos = sueldo_personal + gastos_servicios + pago_mensual_renta_local
        total_ganancias = total_ganancia_alimentos + total_ganancia_medicamentos + total_ganancia_accesorios

        if total_ganancias >= total_gastos:
            veredicto = "Las ganancias cubren todos los gastos mensuales."
        else:
            veredicto = "Las ganancias no son suficientes para cubrir todos los gastos mensuales. Es necesario ajustar precios e inventarios."

        conclusion = CTkLabel(resultados_finales, text=f"Conclusion: {veredicto}", font=("Arial", 18), text_color="white")
        conclusion.pack(padx=20, pady=10)
