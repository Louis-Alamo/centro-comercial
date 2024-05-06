from tkinter import *
from customtkinter import CTk
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkButton import LtkButtonFill

class Supermercado:
    def __init__(self):
        self.ventana = CTk()
        self.ventana.title("Supermercado")
        self.ventana.geometry("1200x800")
        self.ventana.config(bg="#5B2800")

        self.frame_principal = Frame(self.ventana, bg="#5B2800")
        self.frame_principal.pack(expand=True, fill=BOTH)
        titulo_label = Label(self.frame_principal, text="Supermercado", font=('Poppins', 40, "bold", "underline"), bg="#5B2800", fg="#FFFFFF")
        titulo_label.pack(pady=(20, 20))
        frame_horarios = Frame(self.frame_principal, bg="#00ABC3")
        frame_horarios.pack(pady=10)
        

        label_apertura = Label(frame_horarios, text="Hora de Apertura:", bg="#00ABC3", fg="#FFFFFF", font=("Poppins", 15))
        label_apertura.pack(side=LEFT, padx=(50, 10))

        entry_apertura = LtkEntryLine(frame_horarios, "HH:MM")
        entry_apertura.pack(side=LEFT)

        label_cierre = Label(frame_horarios, text="Hora de Cierre:", bg="#00ABC3", fg="#FFFFFF", font=("Poppins", 15))
        label_cierre.pack(side=LEFT, padx=(50, 10))

        entry_cierre = LtkEntryLine(frame_horarios, "HH:MM")
        entry_cierre.pack(side=LEFT)

        label_capacidad = Label(frame_horarios, text="Capacidad de Personas:", bg="#00ABC3", fg="#FFFFFF", font=("Poppins", 15))
        label_capacidad.pack(side=LEFT, padx=(50, 10))

        entry_capacidad = LtkEntryLine(frame_horarios, "Usuarios")
        entry_capacidad.pack(side=LEFT)

        self.frame_cajas = Frame(self.frame_principal, bg="#5B2800")
        self.frame_cajas.pack(side=LEFT, padx=20, pady=20, fill=BOTH)


        titulo_cajas = Label(self.frame_cajas, text="Cajas", font=("Poppins", 15, "bold"), bg="#00ABC3", fg="#FFFFFF")
        titulo_cajas.pack()

        self.tiempos_cobranza = []
        for i in range(1, 6): 
            frame_caja = Frame(self.frame_cajas, bg="#00ABC3")
            frame_caja.pack(pady=5)

            label_caja = Label(frame_caja, text=f"Caja {i}:", font=("Poppins", 12), bg="#00ABC3", fg="#FFFFFF")
            label_caja.pack(side=LEFT, padx=10)

            entry_tiempo = LtkEntryLine(frame_caja, "Tiempo (min)")
            entry_tiempo.pack(side=LEFT, padx=10)
            self.tiempos_cobranza.append(entry_tiempo)

        self.frame_inventario = Frame(self.frame_principal, bg="#00ABC3", bd=5)
        self.frame_inventario.pack(side=LEFT, pady=20, padx=20, fill=BOTH, expand=True)

        self.actualizar_inventario()

        boton_actualizar = LtkButtonFill(self.frame_principal, nombre_boton="GUARDAR DATOS", funcion=self.guardar_modificaciones)
        boton_actualizar.pack(pady=20)

        self.text_area = Text(self.frame_principal, width=100, height=10)
        self.text_area.pack(pady=20, padx=20, fill=BOTH)

        self.ventana.mainloop()

    def actualizar_inventario(self):
        for widget in self.frame_inventario.winfo_children():
            widget.destroy()


        productos_inventario = [
            {"nombre": "Arroz", "cantidad": 100, "precio": 1.5},
            {"nombre": "Leche", "cantidad": 50, "precio": 2.0},
            {"nombre": "Jabón", "cantidad": 80, "precio": 1.0},
            {"nombre": "Papel Higiénico", "cantidad": 120, "precio": 1.2},
            {"nombre": "Refresco", "cantidad": 70, "precio": 1.8},
            {"nombre": "Aceite de Cocina", "cantidad": 90, "precio": 3.0},
            {"nombre": "Detergente", "cantidad": 60, "precio": 2.5}
        ]

        for producto in productos_inventario:
            producto_frame = Frame(self.frame_inventario, bg="#00ABC3")
            producto_frame.pack(pady=5, fill=X)

            label_producto = Label(producto_frame, text=producto["nombre"], font=("Poppins", 12), bg="#00ABC3", fg="#FFFFFF", width=20)
            label_producto.pack(side=LEFT, padx=10)

            entry_cantidad = LtkEntryLine(producto_frame, str(producto["cantidad"]))
            entry_cantidad.pack(side=LEFT, padx=10)

            entry_precio = LtkEntryLine(producto_frame, str(producto["precio"]))
            entry_precio.pack(side=LEFT, padx=10)

    def guardar_modificaciones(self):
        self.text_area.delete(1.0, END)
        self.text_area.insert(INSERT, "Inventario actualizado correctamente.\n")

        self.text_area.insert(INSERT, "Tiempos de cobranza por persona en cada caja:\n")
        for i, entry_tiempo in enumerate(self.tiempos_cobranza):
            tiempo = entry_tiempo.get()
            self.text_area.insert(INSERT, f"Caja {i+1}: {tiempo} minutos\n")
