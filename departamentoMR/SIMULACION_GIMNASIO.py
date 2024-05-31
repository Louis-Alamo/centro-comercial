from util.NumerosAleatorios import generar_aleatorio, generar_numeros_aleatorios
from customtkinter import CTk, CTkLabel, CTkFrame, CTkCanvas, CTkScrollbar
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from tkinter import ttk
import tkinter
import json
import os

ruta_archivo=os.path.dirname(os.path.abspath(__file__))
ruta_completa=os.path.join(ruta_archivo, 'gimnasio.json')

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
    numeros=[]
    hora_actual=hora_apertura
    while True:
        numero=round(generar_aleatorio(), 4)
        incremento_minutos=0
        for incremento, rango in lapso_usuarios:
            limite_inferior, limite_superior=map(float, rango.split("-"))
            if limite_inferior <= numero <= limite_superior:
                incremento_minutos=incremento
                break
        hora_salida=incrementar_hora(hora_actual, incremento_minutos)
        if hora_salida > hora_cierre:
            break
        numeros.append(numero)
        hora_actual=hora_salida
    return numeros

def obtener_personas_segun_rango(rango_aleatorio, rangos_llegada_usuarios):
    for cantidad_personas, rango in rangos_llegada_usuarios:
        limite_inferior, limite_superior=map(float, rango.split("-"))
        if limite_inferior <= rango_aleatorio <= limite_superior:
            return cantidad_personas
    return 0

def obtener_lapso_segun_rango(rango_aleatorio, rangos_lapso_usuarios):
    for lapso, rango in rangos_lapso_usuarios:
        limite_inferior, limite_superior=map(float, rango.split("-"))
        if limite_inferior <= rango_aleatorio <= limite_superior:
            return lapso
    return 0

def obtener_duracion_segun_rango(rango_aleatorio, rangos_duracion_gym):
    for duracion, rango in rangos_duracion_gym:
        limite_inferior, limite_superior=map(float, rango.split("-"))
        if limite_inferior <= rango_aleatorio <= limite_superior:
            return duracion
    return 0

def obtener_tiempo_baño_segun_rango(rango_aleatorio, rangos_duracion_baño):
    for tiempo_baño, rango in rangos_duracion_baño:
        limite_inferior, limite_superior=map(float, rango.split("-"))
        if limite_inferior <= rango_aleatorio <= limite_superior:
            return tiempo_baño
    return 0

def obtener_genero_segun_rango(rango_aleatorio, lista_sexo):
    for genero, rango in lista_sexo:
        limite_inferior, limite_superior=map(float, rango.split("-"))
        if limite_inferior <= rango_aleatorio <= limite_superior:
            return genero
    return "Otro" 

def determinar_temporada():
    datos=cargar_datos()
    if datos.get("temporada_alta", [False])[0]:
        return "alta"
    elif datos.get("temporada_regular", [False])[0]:
        return "regular"
    elif datos.get("temporada_baja", [False])[0]:
        return "baja"
    return "sin temporada"

def incrementar_hora(base_hora, incremento_minutos):
    base_hora_dt=datetime.strptime(base_hora, "%H:%M")
    nueva_hora_dt=base_hora_dt + timedelta(minutes=incremento_minutos)
    return nueva_hora_dt.strftime("%H:%M")

class SimulacionGimnasio:
    def __init__(self, cantidad_dias):
        self.ganancias_por_tabla=[] 
        self.personas_por_tabla=[] 
        self.total_cobro=0
        self.total_personas=0
        self.total_hombres=0
        self.total_mujeres=0
        self.total_otros=0
        self.total_ganancias=0
        self.total_duracion=0
        self.total_tiempo_baño=0
        self.ventana=CTk()
        self.ventana.title("Gimnasio")
        self.ventana.geometry("1150x800+350+100")
        self.ventana.configure(bg="black")
        self.ventana.grid_rowconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(0, weight=1)

        self.frame=CTkFrame(self.ventana)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.canvas=CTkCanvas(self.frame, bg="black")
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.scrollbar=CTkScrollbar(self.frame, command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.inner_frame=CTkFrame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        self.inner_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        self.datos=cargar_datos()
        horario_apertura=self.datos.get("horario_apertura", [])
        horario_cierre=self.datos.get("horario_cierre", [])
        lapso_usuarios=self.datos.get("lapso_usuarios", [])
        self.capacidad_gym=self.datos.get("capacidad_gym", 0)

        self.ejecutar_simulacion()
        for i in range(cantidad_dias):
            self.numeros_aleatorios=generar_numeros_aleatorios(horario_apertura, horario_cierre, lapso_usuarios)
            self.crear_tabla_simulacion(self.numeros_aleatorios)
        self.resultados_finales()
        self.ventana.mainloop()

    def on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event=None):
        canvas_width=event.width
        self.canvas.itemconfig(self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw"), width=canvas_width)

    def aplicar_descuento_temporada(self):
        temporada_regular=self.datos.get("temporada_regular", [False])[0]
        temporada_alta=self.datos.get("temporada_alta", [False])[0]
        temporada_baja=self.datos.get("temporada_baja", [False])[0]

        if temporada_regular:
            descuento=self.datos.get("descuento_regular", 0)
        elif temporada_alta:
            descuento=self.datos.get("descuento_alta", 0)
        elif temporada_baja:
            descuento=self.datos.get("descuento_baja", 0)
        else:
            descuento=0

        return descuento

    def ejecutar_simulacion(self):
        descuento=self.aplicar_descuento_temporada()
        self.cobro=self.datos.get("cobro_usuario", 0)
        self.cobro_final=self.cobro * (1 - descuento)

        temporada_regular=self.datos.get("temporada_regular", [False])[0]
        temporada_alta=self.datos.get("temporada_alta", [False])[0]
        temporada_baja=self.datos.get("temporada_baja", [False])[0]

        if temporada_regular:
            temporada="Temporada Regular"
        elif temporada_alta:
            temporada="Temporada Alta"
        elif temporada_baja:
            temporada="Temporada Baja"
        else:
            temporada="Sin Temporada Específica"

        temporada_label=CTkLabel(self.inner_frame, text=f"Descuento del {descuento * 100}% aplicado durante la {temporada}", font=("Arial", 12), text_color="white")
        temporada_label.pack(padx=20, pady=5)

        resultados={
            "Cobro Por Usuario (Sin Descuento)": self.cobro,
            "Cobro Por Usuario (Con Descuento)": self.cobro_final}

        resultados_label=CTkLabel(self.inner_frame, text=f"Resultados de la simulación GIMNASIO:\n{json.dumps(resultados, indent=2)}", font=("Arial", 20), text_color="white")
        resultados_label.pack(padx=20, pady=20, fill="x", expand=True)

    def crear_tabla_simulacion(self, numeros):
        columnas=["ALEATORIOS", "PERSONAS", "COBRO", "LLEGO", "DURACION", "TIEMPO BAÑO", "SALIDA", "MAQUINAS USO", "SIN USO", "FEMENINO/MASCULINO"]
        llegada_usuarios=self.datos.get("llegada_usuarios", [])
        horario_apertura=self.datos.get("horario_apertura", [])
        horario_cierre=self.datos.get("horario_cierre", [])
        lapso_usuarios=self.datos.get("lapso_usuarios", [])
        duracion_gym=self.datos.get("duracion_gym", [])
        duracion_baño=self.datos.get("duracion_baño", [])
        cantidad_maquinas=self.datos.get("cantidad_maquinas", 0)
        lista_sexo=self.datos.get("lista_sexo", [])

        tabla_frame=CTkFrame(self.inner_frame)
        tabla_frame.pack(padx=20, pady=10, fill="x", expand=True)

        tabla=ttk.Treeview(tabla_frame, columns=columnas, show="headings")
        tabla.pack(side="left", fill="both", expand=True)

        for columna, ancho in zip(columnas, [10]*14):
            tabla.heading(columna, text=columna)
            tabla.column(columna, width=ancho, anchor="center")

        scrollbar=CTkScrollbar(tabla_frame, command=tabla.yview)
        scrollbar.pack(side="right", fill="y")
        tabla.configure(yscrollcommand=scrollbar.set)

        total_personas_tabla=0
        total_ganancias_tabla=0
        total_cobro=0
        total_cobro_descuento=0
        llego_anterior=horario_apertura 
        total_maquinas_uso=0
        total_personas_sin_maquina=0

        for i, aleatorio in enumerate(numeros):
            lapso=obtener_lapso_segun_rango(aleatorio, lapso_usuarios)
            llego=llego_anterior 
            llego_anterior=incrementar_hora(llego_anterior, lapso)
            personas=obtener_personas_segun_rango(aleatorio, llegada_usuarios)
            duracion=obtener_duracion_segun_rango(aleatorio, duracion_gym)
            tiempo_baño=obtener_tiempo_baño_segun_rango(aleatorio, duracion_baño)
            salida=incrementar_hora(llego, duracion + tiempo_baño)
            genero=obtener_genero_segun_rango(aleatorio, lista_sexo)
            cobro=self.cobro_final * personas
            maquinas_en_uso=min(personas, cantidad_maquinas)
            maquinas_sin_uso=max(0, cantidad_maquinas - maquinas_en_uso)
            total_cobro += self.cobro * personas
            total_cobro_descuento += cobro
            total_ganancias_tabla += cobro
            total_personas_tabla += personas

            total_maquinas_uso += maquinas_en_uso
            total_personas_sin_maquina += max(0, personas - maquinas_en_uso)

            fila=[aleatorio, personas, cobro, llego, duracion, tiempo_baño, salida, maquinas_en_uso, maquinas_sin_uso, genero]
            tabla.insert("", "end", values=fila)

            self.total_personas += personas
            if genero == "Masculino":
                self.total_hombres += personas
            elif genero == "Femenino":
                self.total_mujeres += personas
            else:
                self.total_otros += personas

            self.total_ganancias += cobro
            self.total_duracion += duracion * personas
            self.total_tiempo_baño += tiempo_baño * personas

        self.total_cobro=total_cobro
        self.total_cobro_descuento=total_cobro_descuento
        self.total_maquinas_uso=total_maquinas_uso
        self.total_personas_sin_maquina=total_personas_sin_maquina
        self.ganancias_por_tabla.append(total_ganancias_tabla)
        self.personas_por_tabla.append(total_personas_tabla) 

    def resultados_finales(self):
        resultados_finales=tkinter.Toplevel()
        resultados_finales.title("Resultados Finales Gimnasio")
        resultados_finales.configure(bg="gray")
        horario_apertura=self.datos.get("horario_apertura", [])
        horario_cierre=self.datos.get("horario_cierre", [])
        cantidad_recepcionistas=self.datos.get("cantidad_recepcionistas", 0)
        cantidad_personal_limpieza=self.datos.get("cantidad_personal_limpieza", 0)
        cantidad_gerentes=self.datos.get("cantidad_gerentes", 0)
        cantidad_entrenadores=self.datos.get("cantidad_entrenadores", 0)
        cantidad_personal_tecnico=self.datos.get("cantidad_personal_tecnico", 0)
        sueldo_mensual_gerente=self.datos.get("sueldo_mensual_gerente", 0)
        sueldo_mensual_entrenador=self.datos.get("sueldo_mensual_entrenador", 0)
        sueldo_mensual_recepcionista=self.datos.get("sueldo_mensual_recepcionista", 0)
        sueldo_mensual_personal_limpieza=self.datos.get("sueldo_mensual_personal_limpieza", 0)
        sueldo_mensual_personal_tecnico=self.datos.get("sueldo_mensual_personal_tecnico", 0)

        pago_mensual_luz=self.datos.get("pago_mensual_luz", 0)
        pago_mensual_agua=self.datos.get("pago_mensual_agua", 0)
        pago_mensual_internet=self.datos.get("pago_mensual_internet", 0)
        pago_mensual_spotify=self.datos.get("pago_mensual_spotify", 0)
        pago_mensual_renta_local=self.datos.get("pago_mensual_renta_local", 0)

        total_salarios=(
            cantidad_recepcionistas * sueldo_mensual_recepcionista +
            cantidad_personal_limpieza * sueldo_mensual_personal_limpieza +
            cantidad_gerentes * sueldo_mensual_gerente +
            cantidad_entrenadores * sueldo_mensual_entrenador +
            cantidad_personal_tecnico * sueldo_mensual_personal_tecnico)

        total_gastos_servicios=(pago_mensual_luz + pago_mensual_agua + pago_mensual_internet + pago_mensual_spotify + pago_mensual_renta_local)

        promedio_duracion=self.total_duracion / self.total_personas if self.total_personas > 0 else 0
        promedio_tiempo_baño=self.total_tiempo_baño / self.total_personas if self.total_personas > 0 else 0

        total_personas_label=tkinter.Label(resultados_finales, text=f"La cantidad total de personas que acudieron al Gimnasio fue de: {self.total_personas}", font=("Arial", 18), bg="gray", fg="white")
        total_personas_label.pack(padx=20, pady=10)

        total_sexo_label=tkinter.Label(resultados_finales, text=f"Cantidad de Masculinos: {self.total_hombres}, Femeninas: {self.total_mujeres}", font=("Arial", 18), bg="gray", fg="white")
        total_sexo_label.pack(padx=20, pady=10)

        horario_etiqueta=tkinter.Label(resultados_finales, text=f"En un horario de atención por día de: {horario_apertura} - {horario_cierre}", font=("Arial", 18), bg="gray", fg="white")
        horario_etiqueta.pack(padx=20, pady=10)

        ganancias_totales=tkinter.Label(resultados_finales, text=f"Las ganancias totales durante la simulación fueron de: ${self.total_ganancias}", font=("Arial", 18), bg="gray", fg="white")
        ganancias_totales.pack(padx=20, pady=10)

        promedio_duracion_label=tkinter.Label(resultados_finales, text=f"El tiempo promedio de duración en el gimnasio por persona fue de: {promedio_duracion:.2f} minutos", font=("Arial", 18), bg="gray", fg="white")
        promedio_duracion_label.pack(padx=20, pady=10)

        promedio_tiempo_baño_label=tkinter.Label(resultados_finales, text=f"El tiempo promedio en el baño por persona fue de: {promedio_tiempo_baño:.2f} minutos", font=("Arial", 18), bg="gray", fg="white")
        promedio_tiempo_baño_label.pack(padx=20, pady=10)
      
        total_gastos_label=tkinter.Label(resultados_finales, text=f"Los gastos totales en salarios de todo el personal fue de: ${total_salarios}", font=("Arial", 18), bg="gray", fg="white")
        total_gastos_label.pack(padx=20, pady=10)

        si_restamos_gastos_a_ganancias=tkinter.Label(resultados_finales, text=f"Si restamos los gastos a las ganancias, obtenemos: ${self.total_ganancias - (total_salarios + total_gastos_servicios)}", font=("Arial", 18), bg="gray", fg="white")
        si_restamos_gastos_a_ganancias.pack(padx=20, pady=10)


        total_maquinas_label=tkinter.Label(resultados_finales, text=f"La cantidad total de veces que se utilizaron las maquinas fue de: {self.total_maquinas_uso}", font=("Arial", 18), bg="gray", fg="white")
        total_maquinas_label.pack(padx=20, pady=10)

        total_personas_sin_maquina_label=tkinter.Label(resultados_finales, text=f"La cantidad de personas que no usaron máquinas fue de: {self.total_personas_sin_maquina}", font=("Arial", 18), bg="gray", fg="white")
        total_personas_sin_maquina_label.pack(padx=20, pady=10)

        fig, axes=plt.subplots(2, 2, figsize=(10, 8))

        axes[0, 0].pie([promedio_duracion, 100 - promedio_duracion], labels=["Promedio", "Restante"], autopct='%1.1f%%', colors=["blue", "lightgrey"])
        axes[0, 0].set_title("Duración Promedio en el Gimnasio")

        axes[0, 1].plot(range(1, len(self.personas_por_tabla) + 1), self.personas_por_tabla, marker='o', color='green', linestyle='-')
        axes[0, 1].set_title('Cantidad de Personas por Dia')
        axes[0, 1].set_xlabel('Dia')
        axes[0, 1].set_ylabel('Cantidad de Personas')
        axes[0, 1].grid(True)

        sexos=['Masculino', 'Femenino']
        cantidades=[self.total_hombres, self.total_mujeres]
        axes[1, 0].bar(sexos, cantidades, color=['blue', 'pink'])
        axes[1, 0].set_title("Cantidad de Personas por Sexo")
        axes[1, 0].set_ylabel("Cantidad")

        axes[1, 1].plot(range(1, len(self.ganancias_por_tabla) + 1), self.ganancias_por_tabla, marker='o', color='b', linestyle='-')
        axes[1, 1].set_title('Ganancias por Dia')
        axes[1, 1].set_xlabel('Dia')
        axes[1, 1].set_ylabel('Ganancias')
        axes[1, 1].grid(True)

        plt.tight_layout()
        plt.show()