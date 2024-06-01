import os
import json
import random
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Toplevel, ttk
from customtkinter import CTk, CTkButton, CTkToplevel

class SimulacionFarmacia:
    def __init__(self, ventana, titulo):
        self.top = CTkToplevel(ventana)
        self.top.title(titulo)
        self.top.geometry("1200x600")
        self.top.transient(ventana)
        self.top.grab_set()
        self.top.resizable(True, True)

        self.rutas_archivos = {
            "probabilidades_ventas": "prob_ventas1.json",
            "costos_precios": "configuracion_farmacia1.json"
        }

        self.probabilidades_ventas = self.cargar_datos(self.rutas_archivos["probabilidades_ventas"])
        self.costos = self.cargar_costos()

        self.resultados_simulacion, self.resultados_financieros = self.simular_ventas(
            self.probabilidades_ventas, self.costos, dias=30)

        self.configurar_ui()
        self.mostrar_resultados_simulacion()
        self.mostrar_resultados_financieros()

    def configurar_ui(self):
        self.arbol_simulacion = ttk.Treeview(self.top)
        self.arbol_simulacion.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.barra_desplazamiento_simulacion_y = ttk.Scrollbar(self.top, orient="vertical", command=self.arbol_simulacion.yview)
        self.barra_desplazamiento_simulacion_y.grid(row=0, column=3, sticky='ns')
        self.barra_desplazamiento_simulacion_x = ttk.Scrollbar(self.top, orient="horizontal", command=self.arbol_simulacion.xview)
        self.barra_desplazamiento_simulacion_x.grid(row=1, column=0, columnspan=3, sticky='ew')

        self.arbol_simulacion.configure(yscrollcommand=self.barra_desplazamiento_simulacion_y.set, xscrollcommand=self.barra_desplazamiento_simulacion_x.set)

        self.arbol_rangos = ttk.Treeview(self.top)
        self.arbol_rangos.grid(row=2, column=0, columnspan=3, sticky='nsew')

        self.barra_desplazamiento_rangos_y = ttk.Scrollbar(self.top, orient="vertical", command=self.arbol_rangos.yview)
        self.barra_desplazamiento_rangos_y.grid(row=2, column=3, sticky='ns')
        self.barra_desplazamiento_rangos_x = ttk.Scrollbar(self.top, orient="horizontal", command=self.arbol_rangos.xview)
        self.barra_desplazamiento_rangos_x.grid(row=3, column=0, columnspan=3, sticky='ew')

        self.arbol_rangos.configure(yscrollcommand=self.barra_desplazamiento_rangos_y.set, xscrollcommand=self.barra_desplazamiento_rangos_x.set)

        self.boton_graficar = CTkButton(self.top, text="Graficar Resultados", command=self.graficar_resultados)
        self.boton_graficar.grid(row=4, column=0, columnspan=3, pady=10)

        self.boton_mostrar_finales = CTkButton(self.top, text="Mostrar Resultados Finales", command=self.mostrar_resultados_finales)
        self.boton_mostrar_finales.grid(row=5, column=0, columnspan=3, pady=10)

        self.arbol_financieros = ttk.Treeview(self.top)
        self.arbol_financieros.grid(row=6, column=0, columnspan=3, sticky='nsew')

        self.barra_desplazamiento_financieros_y = ttk.Scrollbar(self.top, orient="vertical", command=self.arbol_financieros.yview)
        self.barra_desplazamiento_financieros_y.grid(row=6, column=3, sticky='ns')
        self.barra_desplazamiento_financieros_x = ttk.Scrollbar(self.top, orient="horizontal", command=self.arbol_financieros.xview)
        self.barra_desplazamiento_financieros_x.grid(row=7, column=0, columnspan=3, sticky='ew')

        self.arbol_financieros.configure(yscrollcommand=self.barra_desplazamiento_financieros_y.set, xscrollcommand=self.barra_desplazamiento_financieros_x.set)

        for i in range(8):
            self.top.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.top.grid_columnconfigure(i, weight=1)

    def cargar_datos(self, ruta_archivo):
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, 'r') as archivo:
                try:
                    datos = json.load(archivo)
                    claves_requeridas = ["medicamentos", "vitaminas", "equipo_medico"]
                    for clave in claves_requeridas:
                        if clave not in datos or not isinstance(datos[clave], list) or not all(isinstance(item, list) and len(item) == 2 for item in datos[clave]):
                            raise KeyError(f"Falta la clave '{clave}' o el formato es incorrecto en {ruta_archivo}.")
                    return datos
                except (json.JSONDecodeError, ValueError, KeyError) as e:
                    print(f"Error al cargar {ruta_archivo}: {e}")
                    return {
                        "medicamentos": [],
                        "vitaminas": [],
                        "equipo_medico": []
                    }
        else:
            print(f"El archivo {ruta_archivo} no existe.")
            return {
                "medicamentos": [],
                "vitaminas": [],
                "equipo_medico": []
            }

    def cargar_costos(self):
        ruta_archivo = self.rutas_archivos["costos_precios"]
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, 'r') as archivo:
                try:
                    datos = json.load(archivo)
                    costos = datos.get("costos", {})
                    precios = datos.get("precios", {})

                    claves_requeridas_costos = ["costo_fijo_diario", "costo_medicamento", "costo_vitaminas", "costo_equipo_medico"]
                    claves_requeridas_precios = ["precio_medicamento", "precio_vitaminas", "precio_equipo_medico"]

                    for clave in claves_requeridas_costos:
                        if clave not in costos:
                            raise KeyError(f"Falta el costo '{clave}' en {ruta_archivo}.")
                        costos[clave] = float(costos[clave])

                    for clave in claves_requeridas_precios:
                        if clave not in precios:
                            raise KeyError(f"Falta el precio '{clave}' en {ruta_archivo}.")
                        precios[clave] = float(precios[clave])

                    return {**costos, **precios}
                except json.JSONDecodeError:
                    raise ValueError(f"El archivo de configuración {ruta_archivo} está corrupto.")
        else:
            raise FileNotFoundError(f"El archivo de configuración {ruta_archivo} no existe.")

    def simular_ventas(self, probabilidades, costos, dias=30):
        claves_requeridas = ["medicamentos", "vitaminas", "equipo_medico"]
        for clave in claves_requeridas:
            if clave not in probabilidades or not probabilidades[clave]:
                raise ValueError(f"Faltan datos de probabilidad para '{clave}'.")

        resultados = {
            "dia": [],
            "medicamentos_vendidos": [],
            "vitaminas_vendidas": [],
            "equipo_medico_vendido": [],
            "clientes": [],
            "clientes_se_fueron": [],
            "frecuencia_acumulada_medicamentos": [],
            "frecuencia_acumulada_vitaminas": [],
            "frecuencia_acumulada_equipo_medico": [],
            "tiempo_fila": []
        }

        resultados_financieros = {
            "dia": [],
            "ganancias_diarias": [],
            "costos_diarios": [],
            "beneficio_neto_diario": []
        }

        frecuencia_acumulada_medicamentos = self.calcular_frecuencia_acumulada(probabilidades["medicamentos"])
        frecuencia_acumulada_vitaminas = self.calcular_frecuencia_acumulada(probabilidades["vitaminas"])
        frecuencia_acumulada_equipo_medico = self.calcular_frecuencia_acumulada(probabilidades["equipo_medico"])

        for dia in range(1, dias + 1):
            clientes = random.randint(50, 150)
            clientes_se_fueron = random.randint(0, int(clientes * 0.1))

            medicamentos_vendidos = sum(self.simular_venta(probabilidades["medicamentos"]) for _ in range(clientes - clientes_se_fueron))
            vitaminas_vendidas = sum(self.simular_venta(probabilidades["vitaminas"]) for _ in range(clientes - clientes_se_fueron))
            equipo_medico_vendido = sum(self.simular_venta(probabilidades["equipo_medico"]) for _ in range(clientes - clientes_se_fueron))

            ganancias_diarias = (medicamentos_vendidos * costos["precio_medicamento"] +
                                 vitaminas_vendidas * costos["precio_vitaminas"] +
                                 equipo_medico_vendido * costos["precio_equipo_medico"])

            costos_diarios = costos["costo_fijo_diario"] + (
                medicamentos_vendidos * costos["costo_medicamento"] +
                vitaminas_vendidas * costos["costo_vitaminas"] +
                equipo_medico_vendido * costos["costo_equipo_medico"]
            )
            beneficio_neto_diario = ganancias_diarias - costos_diarios

            tiempo_fila = random.uniform(5, 20)

            resultados["dia"].append(dia)
            resultados["medicamentos_vendidos"].append(medicamentos_vendidos)
            resultados["vitaminas_vendidas"].append(vitaminas_vendidas)
            resultados["equipo_medico_vendido"].append(equipo_medico_vendido)
            resultados["clientes"].append(clientes)
            resultados["clientes_se_fueron"].append(clientes_se_fueron)
            resultados["tiempo_fila"].append(tiempo_fila)

            resultados_financieros["dia"].append(dia)
            resultados_financieros["ganancias_diarias"].append(ganancias_diarias)
            resultados_financieros["costos_diarios"].append(costos_diarios)
            resultados_financieros["beneficio_neto_diario"].append(beneficio_neto_diario)

        resultados["frecuencia_acumulada_medicamentos"] = frecuencia_acumulada_medicamentos
        resultados["frecuencia_acumulada_vitaminas"] = frecuencia_acumulada_vitaminas
        resultados["frecuencia_acumulada_equipo_medico"] = frecuencia_acumulada_equipo_medico

        return resultados, resultados_financieros

    def calcular_frecuencia_acumulada(self, probabilidades):
        frecuencias = [probabilidad for _, probabilidad in probabilidades]
        frecuencia_acumulada = []
        suma = 0
        for frecuencia in frecuencias:
            suma += frecuencia
            frecuencia_acumulada.append(suma)
        return frecuencia_acumulada

    def simular_venta(self, probabilidades):
        valores, probs = zip(*probabilidades)
        ventas = random.choices(valores, probs, k=1)
        return ventas[0]

    def crear_dataframe(self, datos):
        longitud_maxima = max(len(v) for v in datos.values())
        datos_alineados = {k: (v + [None] * (longitud_maxima - len(v))) for k, v in datos.items()}
        return pd.DataFrame(datos_alineados)

    def mostrar_resultados_simulacion(self):
        df = self.crear_dataframe(self.resultados_simulacion)
        self.arbol_simulacion["column"] = list(df.columns)
        self.arbol_simulacion["show"] = "headings"
        for column in self.arbol_simulacion["columns"]:
            self.arbol_simulacion.heading(column, text=column)
        for _, row in df.iterrows():
            self.arbol_simulacion.insert("", "end", values=list(row))

        frecuencias_df = pd.DataFrame({
            "Producto": ["Medicamentos", "Vitaminas", "Equipo Médico"],
            "Frecuencia Acumulada": [self.resultados_simulacion["frecuencia_acumulada_medicamentos"],
                                     self.resultados_simulacion["frecuencia_acumulada_vitaminas"],
                                     self.resultados_simulacion["frecuencia_acumulada_equipo_medico"]]
        })

        self.arbol_rangos["column"] = list(frecuencias_df.columns)
        self.arbol_rangos["show"] = "headings"
        for column in self.arbol_rangos["columns"]:
            self.arbol_rangos.heading(column, text=column)
        for _, row in frecuencias_df.iterrows():
            self.arbol_rangos.insert("", "end", values=list(row))

    def mostrar_resultados_financieros(self):
        df = self.crear_dataframe(self.resultados_financieros)
        self.arbol_financieros["column"] = list(df.columns)
        self.arbol_financieros["show"] = "headings"
        for column in self.arbol_financieros["columns"]:
            self.arbol_financieros.heading(column, text=column)
        for _, row in df.iterrows():
            self.arbol_financieros.insert("", "end", values=list(row))

    def graficar_resultados(self):
        fig, ax = plt.subplots(2, 1, figsize=(12, 10))

        df_simulacion = self.crear_dataframe(self.resultados_simulacion)
        df_financieros = self.crear_dataframe(self.resultados_financieros)

        ax[0].plot(df_simulacion["dia"], df_simulacion["medicamentos_vendidos"], label="Medicamentos Vendidos")
        ax[0].plot(df_simulacion["dia"], df_simulacion["vitaminas_vendidas"], label="Vitaminas Vendidas")
        ax[0].plot(df_simulacion["dia"], df_simulacion["equipo_medico_vendido"], label="Equipo Médico Vendido")
        ax[0].set_title("Ventas Diarias")
        ax[0].set_xlabel("Día")
        ax[0].set_ylabel("Cantidad Vendida")
        ax[0].legend()

        ax[1].plot(df_financieros["dia"], df_financieros["ganancias_diarias"], label="Ganancias Diarias")
        ax[1].plot(df_financieros["dia"], df_financieros["costos_diarios"], label="Costos Diarios")
        ax[1].plot(df_financieros["dia"], df_financieros["beneficio_neto_diario"], label="Beneficio Neto Diario")
        ax[1].set_title("Resultados Financieros Diarios")
        ax[1].set_xlabel("Día")
        ax[1].set_ylabel("Monto")
        ax[1].legend()

        plt.tight_layout()
        plt.show()

    def mostrar_resultados_finales(self):
        resultados_finales = {
            "Total de días": len(self.resultados_simulacion["dia"]),
            "Total de ganancias": sum(self.resultados_financieros["ganancias_diarias"]),
            "Total de costos": sum(self.resultados_financieros["costos_diarios"]),
            "Beneficio neto total": sum(self.resultados_financieros["beneficio_neto_diario"]),
            "Promedio de clientes por día": sum(self.resultados_simulacion["clientes"]) / len(self.resultados_simulacion["dia"]),
            "Total de medicamentos vendidos": sum(self.resultados_simulacion["medicamentos_vendidos"]),
            "Total de vitaminas vendidas": sum(self.resultados_simulacion["vitaminas_vendidas"]),
            "Total de equipo médico vendido": sum(self.resultados_simulacion["equipo_medico_vendido"]),
            "Clientes que se fueron sin comprar": sum(self.resultados_simulacion["clientes_se_fueron"]),
            "Promedio de tiempo en fila (minutos)": sum(self.resultados_simulacion["tiempo_fila"]) / len(self.resultados_simulacion["dia"])
        }

        self.top_finales = CTkToplevel(self.top)
        self.top_finales.title("Resultados Finales")
        self.top_finales.transient(self.top)
        self.top_finales.grab_set()
        self.top_finales.geometry("600x400")
        self.top_finales.resizable(True, True)

        arbol_finales = ttk.Treeview(self.top_finales)
        arbol_finales.grid(row=0, column=0, columnspan=3, sticky='nsew')

        barra_desplazamiento_finales_y = ttk.Scrollbar(self.top_finales, orient="vertical", command=arbol_finales.yview)
        arbol_finales.configure(yscrollcommand=barra_desplazamiento_finales_y.set)
        barra_desplazamiento_finales_y.grid(row=0, column=3, sticky='ns')

        barra_desplazamiento_finales_x = ttk.Scrollbar(self.top_finales, orient="horizontal", command=arbol_finales.xview)
        arbol_finales.configure(xscrollcommand=barra_desplazamiento_finales_x.set)
        barra_desplazamiento_finales_x.grid(row=1, column=0, columnspan=3, sticky='ew')

        arbol_finales["column"] = ["Métrica", "Valor"]
        arbol_finales["show"] = "headings"
        for column in arbol_finales["columns"]:
            arbol_finales.heading(column, text=column)
        for clave, valor in resultados_finales.items():
            arbol_finales.insert("", "end", values=(clave, valor))

if __name__ == "__main__":
    raiz = Tk()
    raiz.withdraw()
    app = SimulacionFarmacia(raiz, "Resultados de la Simulación")
    raiz.mainloop()
