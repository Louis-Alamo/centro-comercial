from customtkinter import *
from tkinter import messagebox, simpledialog
from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine, LtkButtonTransparentBackground
from componentes_graficos.LtkEntry import LtkEntryLine, LtkEntryFill
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkCheckBox import LtkCheckBoxFill
from componentes_graficos.LtkComboBox import LtkComboBoxLine
from componentes_graficos.LtkTreeView import LtkFileInputTreeView
import json
import os

class Gimnasio:
    def __init__(self):
        self.ventana=CTk()
        self.ventana.title("Gimnasio")
        self.ventana.geometry("900x600+350+100")
        self.ventana.configure(bg="#FFFFFF")
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)
        self.ventana.rowconfigure(1, weight=1)

        self.ruta_ventana=os.path.dirname(os.path.abspath(__file__))
        
        # Frame para el título
        frame_titulo = CTkFrame(self.ventana)
        frame_titulo.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)
        titulo=LtkLabel(frame_titulo, texto="Configuración del Gimnasio")
        titulo.configure(font=('Poppins', 30, "bold"))
        titulo.grid(row=0, column=0, pady=(1, 1), sticky="nsew")
        frame_titulo.columnconfigure(0, weight=1)
        frame_titulo.rowconfigure(0, weight=1)

        # Frame para las opciones
        frame_opciones=CTkFrame(self.ventana)
        frame_opciones.grid(row=1, column=0, pady=(10, 10))
        self.ventana.columnconfigure(0, weight=2)
        self.ventana.rowconfigure(1, weight=1)


        boton_opciones=LtkButtonLine(frame_opciones, self.personal, "Personal del GYM")
        boton_opciones.grid(row=0, column=0, padx=(5,5), pady=(5, 5))
        boton_costos=LtkButtonLine(frame_opciones, self.costos, "Costos")
        boton_costos.grid(row=1, column=0, padx=(5,5), pady=(5, 5))
        boton_horarios=LtkButtonLine(frame_opciones, self.horarios, "Horarios")
        boton_horarios.grid(row=2, column=0, padx=(5,5), pady=(5, 5))
        boton_usuarios=LtkButtonLine(frame_opciones, self.usuarios, "Usuarios")
        boton_usuarios.grid(row=3, column=0, padx=(5,5), pady=(5, 5))
        boton_maquinas=LtkButtonLine(frame_opciones, self.maquinas, "Maquinas")
        boton_maquinas.grid(row=4, column=0, padx=(5,5), pady=(5, 5))
        boton_servicios_generales=LtkButtonLine(frame_opciones, self.servicios_generales, "Servicios Generales")
        boton_servicios_generales.grid(row=5, column=0, padx=(5,5), pady=(5, 5))
        boton_baños=LtkButtonLine(frame_opciones, self.baños, "Baños")
        boton_baños.grid(row=6, column=0, padx=(5,5), pady=(5, 5))
        boton_vestidores=LtkButtonLine(frame_opciones, self.vestidores, "Vestidores")
        boton_vestidores.grid(row=7, column=0, padx=(5,5), pady=(5, 5))
        boton_temporadas=LtkButtonLine(frame_opciones, self.temporadas, "Temporadas")
        boton_temporadas.grid(row=8, column=0, padx=(5,5), pady=(5, 5))


        # Frame de características
        self.frame_caracteristicas = CTkFrame(self.ventana)
        self.frame_caracteristicas.grid(row=1, column=1, sticky="nsew")
        self.ventana.columnconfigure(1, weight=25)
        self.ventana.rowconfigure(1, weight=2)
        self.frame_caracteristicas.columnconfigure(0, weight=1)


        # Frame para el botón de guardar
        frame_guardar = CTkFrame(self.ventana)
        frame_guardar.grid(row=2, column=0, columnspan=2, sticky="nsew")
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(2, weight=1)
        boton_guardar = LtkButtonFill(frame_guardar, self.guardar_informacion, "Guardar Y Salir De Configuracion Gimnasio")
        boton_guardar.grid(row=0, column=0, padx=100, pady=40, sticky="nsew")
        frame_guardar.columnconfigure(0, weight=1)
        frame_guardar.rowconfigure(0, weight=1)


        self.ventana.mainloop()


    def guardar_informacion(self):
        informacion={
            "cantidad_empleados": self.cantidad_empleados.get()
            # Agregar más campos según los datos recolectados
        }
        
        informacion_json=json.dumps(informacion, indent=4)
        config_path=os.path.join(self.ruta_ventana, 'gimnasio.json')

        with open(config_path, 'w') as f:
            f.write(informacion_json)

        messagebox.showinfo("Informacion", "Informacion guardada correctamente")
        self.ventana.destroy()

    def resetear_frame_caracteristicas(self):
        for widget in self.frame_caracteristicas.winfo_children():
            widget.destroy()
    

    def personal(self):

        self.resetear_frame_caracteristicas()
        
        self.cantidad_empleados=IntVar()

        self.etiqueta_titulo_caracteristicas = LtkLabel(self.frame_caracteristicas, texto="Ajustes Del Personal")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)

        self.label_cantidad_empleados = LtkLabel(self.frame_caracteristicas, texto="Cantidad de Empleados:")
        self.label_cantidad_empleados.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_empleados = LtkEntryLine(self.frame_caracteristicas)
        self.cantidad_empleados.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)


        self.etiqueta_horario = LtkLabel(self.frame_caracteristicas, texto="Horario:")
        self.etiqueta_horario.grid(row=4, column=0,padx=(10,10), pady=(5, 10), sticky="w")
        self.entry_horario_inicio = LtkEntryLine(self.frame_caracteristicas, "Hora inicio")
        self.entry_horario_inicio.grid(row=4, column=1, padx=(5,10), pady=(5, 15), sticky="nsew")
        self.entry_horario_cierre = LtkEntryLine(self.frame_caracteristicas, "Hora cierre")
        self.entry_horario_cierre.grid(row=4, column=2, padx=(5,10), pady=(5, 15), sticky="nsew")

    

    def costos(self):
        self.resetear_frame_caracteristicas()

        self.etiqueta_costos = LtkLabel(self.frame_caracteristicas, texto="Ajustes De Costos")
        self.etiqueta_costos.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_costos.grid(row=0, column=0, columnspan=3, pady=(5, 10))

        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)


        self.label_cantidad_empleados = LtkLabel(self.frame_caracteristicas, texto="Costo:")
        self.label_cantidad_empleados.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_empleados = LtkEntryLine(self.frame_caracteristicas)
        self.cantidad_empleados.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.etiqueta_horario = LtkLabel(self.frame_caracteristicas, texto="Horario:")
        self.etiqueta_horario.grid(row=4, column=0,padx=(10,10), pady=(5, 10), sticky="w")

        self.entry_horario_inicio = LtkEntryLine(self.frame_caracteristicas, "Hora inicio")
        self.entry_horario_inicio.grid(row=4, column=1, padx=(5,10), pady=(5, 15), sticky="nsew")
        self.entry_horario_cierre = LtkEntryLine(self.frame_caracteristicas, "Hora cierre")
        self.entry_horario_cierre.grid(row=4, column=2, padx=(5,10), pady=(5, 15), sticky="nsew")


    def horarios(self):
        pass
    def usuarios(self):
        pass
    def maquinas(self):
        pass
    def servicios_generales(self):
        pass
    def baños(self):
        pass
    def vestidores(self):
        pass
    def temporadas(self):
        pass

Gimnasio()
      

