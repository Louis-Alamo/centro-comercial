import os
import json
import random
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Toplevel, ttk
from customtkinter import CTk, CTkButton, CTkToplevel

class SimulacionResultados:
    def __init__(self, ventana, title):
        self.top = CTkToplevel(ventana)
        self.top.title(title)
        self.top.geometry("1200x600")  # Ajusta el tamaño inicial de la ventana
        self.top.transient(ventana)
        self.top.grab_set()
        self.top.resizable(True, True)  # Permitir redimensionar la ventana

        self.file_paths = {
            "probabilidades_ventas": "prob_ventas.json",
            "costos_precios": "configuracion.json"
        }

        self.probabilidades_ventas = self.load_data(self.file_paths["probabilidades_ventas"])
        self.costos = self.load_costos()

        self.resultados_simulacion, self.resultados_financieros = self.simular_ventas(
            self.probabilidades_ventas, self.costos, dias=30)

        self.setup_ui()

        self.mostrar_resultados_simulacion()
        self.mostrar_resultados_financieros()

    def setup_ui(self):
        # Configurar la interfaz de usuario
        self.tree_simulacion = ttk.Treeview(self.top)
        self.tree_simulacion.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.scrollbar_simulacion_y = ttk.Scrollbar(self.top, orient="vertical", command=self.tree_simulacion.yview)
        self.scrollbar_simulacion_y.grid(row=0, column=3, sticky='ns')
        self.scrollbar_simulacion_x = ttk.Scrollbar(self.top, orient="horizontal", command=self.tree_simulacion.xview)
        self.scrollbar_simulacion_x.grid(row=1, column=0, columnspan=3, sticky='ew')

        self.tree_simulacion.configure(yscrollcommand=self.scrollbar_simulacion_y.set, xscrollcommand=self.scrollbar_simulacion_x.set)

        self.tree_rangos = ttk.Treeview(self.top)
        self.tree_rangos.grid(row=2, column=0, columnspan=3, sticky='nsew')

        self.scrollbar_rangos_y = ttk.Scrollbar(self.top, orient="vertical", command=self.tree_rangos.yview)
        self.scrollbar_rangos_y.grid(row=2, column=3, sticky='ns')
        self.scrollbar_rangos_x = ttk.Scrollbar(self.top, orient="horizontal", command=self.tree_rangos.xview)
        self.scrollbar_rangos_x.grid(row=3, column=0, columnspan=3, sticky='ew')

        self.tree_rangos.configure(yscrollcommand=self.scrollbar_rangos_y.set, xscrollcommand=self.scrollbar_rangos_x.set)

        self.btn_graficar = CTkButton(self.top, text="Graficar Resultados", command=self.graficar_resultados)
        self.btn_graficar.grid(row=4, column=0, columnspan=3, pady=10)

        self.btn_mostrar_finales = CTkButton(self.top, text="Mostrar Resultados Finales", command=self.mostrar_resultados_finales)
        self.btn_mostrar_finales.grid(row=5, column=0, columnspan=3, pady=10)

        self.tree_financieros = ttk.Treeview(self.top)
        self.tree_financieros.grid(row=6, column=0, columnspan=3, sticky='nsew')

        self.scrollbar_financieros_y = ttk.Scrollbar(self.top, orient="vertical", command=self.tree_financieros.yview)
        self.scrollbar_financieros_y.grid(row=6, column=3, sticky='ns')
        self.scrollbar_financieros_x = ttk.Scrollbar(self.top, orient="horizontal", command=self.tree_financieros.xview)
        self.scrollbar_financieros_x.grid(row=7, column=0, columnspan=3, sticky='ew')

        self.tree_financieros.configure(yscrollcommand=self.scrollbar_financieros_y.set, xscrollcommand=self.scrollbar_financieros_x.set)

        # Configurar la expansión de las filas y columnas
        for i in range(8):
            self.top.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.top.grid_columnconfigure(i, weight=1)

    def load_data(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                try:
                    data = json.load(file)
                    required_keys = ["pantalones", "blusas", "ropa_interior"]
                    for key in required_keys:
                        if key not in data or not isinstance(data[key], list) or not all(isinstance(item, list) and len(item) == 2 for item in data[key]):
                            raise KeyError(f"Falta la clave '{key}' o el formato es incorrecto en {file_path}.")
                    return data
                except (json.JSONDecodeError, ValueError, KeyError) as e:
                    print(f"Error al cargar {file_path}: {e}")
                    return {
                        "pantalones": [],
                        "blusas": [],
                        "ropa_interior": []
                    }
        else:
            print(f"El archivo {file_path} no existe.")
            return {
                "pantalones": [],
                "blusas": [],
                "ropa_interior": []
            }

    def load_costos(self):
        file_path = self.file_paths["costos_precios"]
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                try:
                    data = json.load(file)
                    costos = data.get("costos", {})
                    precios = data.get("precios", {})

                    required_cost_keys = ["costo_fijo_diario", "costo_pantalon", "costo_blusa", "costo_ropa_interior"]
                    required_price_keys = ["precio_pantalon", "precio_blusa", "precio_ropa_interior"]

                    for key in required_cost_keys:
                        if key not in costos:
                            raise KeyError(f"Falta el costo '{key}' en {file_path}.")
                        costos[key] = float(costos[key])

                    for key in required_price_keys:
                        if key not in precios:
                            raise KeyError(f"Falta el precio '{key}' en {file_path}.")
                        precios[key] = float(precios[key])

                    return {**costos, **precios}
                except json.JSONDecodeError:
                    raise ValueError(f"El archivo de configuración {file_path} está corrupto.")
        else:
            raise FileNotFoundError(f"El archivo de configuración {file_path} no existe.")

    def simular_ventas(self, probabilidades, costos, dias=30):
        required_keys = ["pantalones", "blusas", "ropa_interior"]
        for key in required_keys:
            if key not in probabilidades or not probabilidades[key]:
                raise ValueError(f"Faltan datos de probabilidad para '{key}'.")

        resultados = {
            "dia": [],
            "pantalones_vendidos": [],
            "blusas_vendidas": [],
            "ropa_interior_vendida": [],
            "clientes": [],
            "clientes_se_fueron": [],
            "frecuencia_acumulada_pantalones": [],
            "frecuencia_acumulada_blusas": [],
            "frecuencia_acumulada_ropa_interior": []
        }

        resultados_financieros = {
            "dia": [],
            "ganancias_diarias": [],
            "costos_diarios": [],
            "beneficio_neto_diario": []
        }

        freq_acumulada_pantalones = self.calcular_frecuencia_acumulada(probabilidades["pantalones"])
        freq_acumulada_blusas = self.calcular_frecuencia_acumulada(probabilidades["blusas"])
        freq_acumulada_ropa_interior = self.calcular_frecuencia_acumulada(probabilidades["ropa_interior"])

        for dia in range(1, dias + 1):
            clientes = random.randint(50, 150)
            clientes_se_fueron = random.randint(0, int(clientes * 0.1))

            pantalones_vendidos = sum(self.simular_venta(probabilidades["pantalones"]) for _ in range(clientes - clientes_se_fueron))
            blusas_vendidas = sum(self.simular_venta(probabilidades["blusas"]) for _ in range(clientes - clientes_se_fueron))
            ropa_interior_vendida = sum(self.simular_venta(probabilidades["ropa_interior"]) for _ in range(clientes - clientes_se_fueron))

            ganancias_diarias = (pantalones_vendidos * costos["precio_pantalon"] +
                                 blusas_vendidas * costos["precio_blusa"] +
                                 ropa_interior_vendida * costos["precio_ropa_interior"])

            costos_diarios = costos["costo_fijo_diario"] + (
                pantalones_vendidos * costos["costo_pantalon"] +
                blusas_vendidas * costos["costo_blusa"] +
                ropa_interior_vendida * costos["costo_ropa_interior"]
            )
            beneficio_neto_diario = ganancias_diarias - costos_diarios

            resultados["dia"].append(dia)
            resultados["pantalones_vendidos"].append(pantalones_vendidos)
            resultados["blusas_vendidas"].append(blusas_vendidas)
            resultados["ropa_interior_vendida"].append(ropa_interior_vendida)
            resultados["clientes"].append(clientes)
            resultados["clientes_se_fueron"].append(clientes_se_fueron)

            resultados_financieros["dia"].append(dia)
            resultados_financieros["ganancias_diarias"].append(ganancias_diarias)
            resultados_financieros["costos_diarios"].append(costos_diarios)
            resultados_financieros["beneficio_neto_diario"].append(beneficio_neto_diario)

        resultados["frecuencia_acumulada_pantalones"] = freq_acumulada_pantalones
        resultados["frecuencia_acumulada_blusas"] = freq_acumulada_blusas
        resultados["frecuencia_acumulada_ropa_interior"] = freq_acumulada_ropa_interior

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
        ventas = random.choices(valores, probs, k=1)  # Suponiendo una sola venta por cliente
        return ventas[0]

    def crear_dataframe(self, data):
        max_length = max(len(v) for v in data.values())
        data_aligned = {k: (v + [None] * (max_length - len(v))) for k, v in data.items()}
        return pd.DataFrame(data_aligned)

    def mostrar_resultados_simulacion(self):
        # Crear el DataFrame para los resultados
        df = self.crear_dataframe(self.resultados_simulacion)
        self.tree_simulacion["column"] = list(df.columns)
        self.tree_simulacion["show"] = "headings"
        for column in self.tree_simulacion["columns"]:
            self.tree_simulacion.heading(column, text=column)
        for _, row in df.iterrows():
            self.tree_simulacion.insert("", "end", values=list(row))

        # Crear DataFrame para frecuencias acumuladas
        frecuencias_df = pd.DataFrame({
            "Producto": ["Pantalones", "Blusas", "Ropa Interior"],
            "Frecuencia Acumulada": [self.resultados_simulacion["frecuencia_acumulada_pantalones"],
                                     self.resultados_simulacion["frecuencia_acumulada_blusas"],
                                     self.resultados_simulacion["frecuencia_acumulada_ropa_interior"]]
        })

        # Mostrar DataFrame de frecuencias acumuladas
        self.tree_rangos["column"] = list(frecuencias_df.columns)
        self.tree_rangos["show"] = "headings"
        for column in self.tree_rangos["columns"]:
            self.tree_rangos.heading(column, text=column)
        for _, row in frecuencias_df.iterrows():
            self.tree_rangos.insert("", "end", values=list(row))

    def mostrar_resultados_financieros(self):
        df = self.crear_dataframe(self.resultados_financieros)
        self.tree_financieros["column"] = list(df.columns)
        self.tree_financieros["show"] = "headings"
        for column in self.tree_financieros["columns"]:
            self.tree_financieros.heading(column, text=column)
        for _, row in df.iterrows():
            self.tree_financieros.insert("", "end", values=list(row))

    def graficar_resultados(self):
        fig, ax = plt.subplots(2, 1, figsize=(12, 10))

        df_simulacion = self.crear_dataframe(self.resultados_simulacion)
        df_financieros = self.crear_dataframe(self.resultados_financieros)

        ax[0].plot(df_simulacion["dia"], df_simulacion["pantalones_vendidos"], label="Pantalones Vendidos")
        ax[0].plot(df_simulacion["dia"], df_simulacion["blusas_vendidas"], label="Blusas Vendidas")
        ax[0].plot(df_simulacion["dia"], df_simulacion["ropa_interior_vendida"], label="Ropa Interior Vendida")
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
            "Total de pantalones vendidos": sum(self.resultados_simulacion["pantalones_vendidos"]),
            "Total de blusas vendidas": sum(self.resultados_simulacion["blusas_vendidas"]),
            "Total de ropa interior vendida": sum(self.resultados_simulacion["ropa_interior_vendida"]),
            "Clientes que se fueron sin comprar": sum(self.resultados_simulacion["clientes_se_fueron"])
        }

        self.top_finales = CTkToplevel(self.top)
        self.top_finales.title("Resultados Finales")
        self.top_finales.transient(self.top)
        self.top_finales.grab_set()
        self.top_finales.geometry("600x400")  # Ajusta el tamaño inicial de la ventana de resultados finales
        self.top_finales.resizable(True, True)  # Permitir redimensionar la ventana de resultados finales

        tree_finales = ttk.Treeview(self.top_finales)
        tree_finales.grid(row=0, column=0, columnspan=3, sticky='nsew')

        scrollbar_finales_y = ttk.Scrollbar(self.top_finales, orient="vertical", command=tree_finales.yview)
        tree_finales.configure(yscrollcommand=scrollbar_finales_y.set)
        scrollbar_finales_y.grid(row=0, column=3, sticky='ns')

        scrollbar_finales_x = ttk.Scrollbar(self.top_finales, orient="horizontal", command=tree_finales.xview)
        tree_finales.configure(xscrollcommand=scrollbar_finales_x.set)
        scrollbar_finales_x.grid(row=1, column=0, columnspan=3, sticky='ew')

        tree_finales["column"] = ["Métrica", "Valor"]
        tree_finales["show"] = "headings"
        for column in tree_finales["columns"]:
            tree_finales.heading(column, text=column)
        for key, value in resultados_finales.items():
            tree_finales.insert("", "end", values=(key, value))

if __name__ == "__main__":
    root = Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter
    app = SimulacionResultados(root, "Resultados de la Simulación")
    root.mainloop()
