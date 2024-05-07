from tkinter import *
from customtkinter import CTk
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkButton import LtkButtonFill

class Veterinaria:
    def __init__(self):
        self.ventana = CTk()
        self.ventana.title("Veterinaria")
        self.ventana.geometry("1500x900")
        self.ventana.config(bg="#7C0B1E")

        self.frame_principal = Frame(self.ventana, bg="#7C0B1E")
        self.frame_principal.pack(expand=True, fill=BOTH)

        titulo_label = LtkLabel(self.frame_principal, texto="Veterinaria")
        titulo_label.configure(font=('Poppins', 80, "bold", "underline"))
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

        self.crear_seccion_productos_vendidos() 
        self.crear_seccion_almacen()

        boton_ejecucion = LtkButtonFill(self.frame_principal, nombre_boton="GUARDAR DATOS", funcion=lambda: self.iniciar_simulacion())
        boton_ejecucion.pack(pady=20)

        self.text_area = Text(self.frame_principal, width=10, height=10)
        self.text_area.pack(pady=20, padx=50, fill=BOTH, expand=True)

        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)

        self.ventana.mainloop()

    def crear_seccion_productos_vendidos(self):
        frame_productos = Frame(self.frame_principal, bg="#7C0B1E")
        frame_productos.pack(pady=20, side=LEFT)

        label_productos = Label(frame_productos, text="Productos Vendidos", font=("Poppins", 15, "bold"), bg="#00ABC3", fg="#FFFFFF")
        label_productos.pack()

        productos = ["Comida para Mascotas", "Juguetes", "Accesorios", "Medicamentos"]

        for producto in productos:
            producto_frame = Frame(frame_productos, bg="#00ABC3")
            producto_frame.pack(pady=5)

            label_producto = Label(producto_frame, text=producto, font=("Poppins", 12), bg="#00ABC3", fg="#FFFFFF")
            label_producto.pack(side=LEFT, padx=10)

            entry_cantidad_producto = LtkEntryLine(producto_frame, "Cantidad")
            entry_cantidad_producto.pack(side=LEFT, padx=10)

            entry_precio_producto = LtkEntryLine(producto_frame, "Precio")
            entry_precio_producto.pack(side=LEFT, padx=10)

    def crear_seccion_almacen(self):
        frame_almacen = Frame(self.frame_principal, bg="#7C0B1E")
        frame_almacen.pack(pady=20, side=LEFT)

        label_almacen = Label(frame_almacen, text="Almacen de mascotas", font=("Poppins", 15, "bold"), bg="#00ABC3", fg="#FFFFFF")
        label_almacen.pack()

        for i in range(10):
            mascota_frame = Frame(frame_almacen, bg="#00ABC3")
            mascota_frame.pack(pady=5)

            label_mascota = Label(mascota_frame, text=f"Mascota {i+1}", font=("Poppins", 12), bg="#00ABC3", fg="#FFFFFF")
            label_mascota.pack(side=LEFT, padx=10)

            entry_mascota_estado = LtkEntryLine(mascota_frame, "Estado")
            entry_mascota_estado.pack(side=LEFT, padx=10)

    def iniciar_simulacion(self):
        self.text_area.delete(1.0, END)
        self.text_area.insert(INSERT, "DATOS GUARDADOS\n")

