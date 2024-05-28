import json
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Datos de ejemplo
datos_servidores = {
    "Servidores": {
        "Servidor 1": {
            "Numero de servidor": 1,
            "Hora inicio": "08:00 AM",
            "Hora fin": "06:00 PM",
            "dias": {
                "Dia 1": {
                    "Numero de personas atendidas": 14,
                    "Numero de personas maximo en espera": 0,
                    "Tiempo ocio servidor": 0
                },
                "Dia 2": {
                    "Numero de personas atendidas": 0,
                    "Numero de personas maximo en espera": 0,
                    "Tiempo ocio servidor": 0
                }
            }
        },
        "Servidor 2": {
            "Numero de servidor": 2,
            "Hora inicio": "08:00 AM",
            "Hora fin": "06:00 PM",
            "dias": {
                "Dia 1": {
                    "Numero de personas atendidas": 14,
                    "Numero de personas maximo en espera": 4,
                    "Tiempo ocio servidor": 0
                },
                "Dia 2": {
                    "Numero de personas atendidas": 0,
                    "Numero de personas maximo en espera": 0,
                    "Tiempo ocio servidor": 0
                }
            }
        }
    },
    "Personas no atendidas": 0
}

datos_ventas = {
    "dias": {
        "Dia 1": {
            "Productos vendidos": [
                ["Munecas y figuras de accion", 3],
                ["Juegos de construccion", 13],
                ["Juegos de mesa y puzzles", 7],
                ["Peluches y juguetes de felpa", 3],
                ["Juguetes electronicos", 13],
                ["Juguetes de imitacion", 22]
            ],
            "Dinero total": 8294.0,
            "Numero de ventas": 61
        }
    }
}

datos_pedidos = {
    "Pedidos": {
        "Pedido 1": {
            "Producto": "Juguetes electronicos",
            "Cantidad": 104,
            "Costo por producto": 220.0,
            "Costo total": 22880.0,
            "Dia de pedido": 1,
            "Tiempo de entrega": 3,
            "Fecha de entrega": 4
        },
        "Pedido 2": {
            "Producto": "Juguetes electronicos",
            "Cantidad": 104,
            "Costo por producto": 220.0,
            "Costo total": 22880.0,
            "Dia de pedido": 1,
            "Tiempo de entrega": 4,
            "Fecha de entrega": 5
        }
    },
    "Numero de pedidos": 0,
    "Dinero total": 0
}

datos_generales = {
    "General": {
        "capacidad_maxima_personas": 50,
        "horario_inicio": "08:00 AM",
        "horario_cierre": "06:00 PM"
    },
    "Caja": {
        "Cantidad de cajas": 2,
        "Pago por empleado": 1000,
        "Rendimiento por empleado": 10
    }
}


# Función para procesar datos y calcular promedios
def procesar_datos():
    # Procesar datos de servidores
    total_personas_atendidas = 0
    total_tiempo_ocio = 0
    total_dias = 0

    for servidor, datos in datos_servidores["Servidores"].items():
        for dia, valores in datos["dias"].items():
            total_personas_atendidas += valores["Numero de personas atendidas"]
            total_tiempo_ocio += valores["Tiempo ocio servidor"]
            total_dias += 1

    promedio_personas_atendidas = total_personas_atendidas / total_dias if total_dias else 0
    promedio_tiempo_ocio = total_tiempo_ocio / total_dias if total_dias else 0

    return promedio_personas_atendidas, promedio_tiempo_ocio


# Función para crear gráficos
def crear_graficos(frame):
    fig = Figure(figsize=(6, 4))
    ax = fig.add_subplot(111)
    ax.bar(["Servidor 1", "Servidor 2"], [14, 14])
    ax.set_title("Número de personas atendidas por servidor")
    ax.set_xlabel("Servidores")
    ax.set_ylabel("Personas atendidas")

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


# Crear la interfaz gráfica
root = tk.Tk()
root.title("Análisis de Datos")

# Crear un notebook (pestañas)
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand='yes')

# Pestaña de Servidores
frame_servidores = ttk.Frame(notebook)
notebook.add(frame_servidores, text="Servidores")

promedio_personas_atendidas, promedio_tiempo_ocio = procesar_datos()

label_promedio_personas = tk.Label(frame_servidores,
                                   text=f"Promedio de personas atendidas: {promedio_personas_atendidas:.2f}")
label_promedio_personas.pack(pady=10)

label_promedio_ocio = tk.Label(frame_servidores, text=f"Promedio de tiempo de ocio: {promedio_tiempo_ocio:.2f}")
label_promedio_ocio.pack(pady=10)

crear_graficos(frame_servidores)

# Pestañas adicionales para Ventas, Pedidos, General se pueden agregar aquí

root.mainloop()
