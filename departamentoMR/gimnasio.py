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
        self.ventana.title("Configuracion Gimnasio")
        self.ventana.geometry("800x500+350+100")
        self.ventana.configure(bg="#FFFFFF")

        self.ruta_ventana=os.path.dirname(os.path.abspath(__file__))
        
        # Crear variables para almacenar datos
        self.cantidad_empleados=IntVar()



        #Frame para titulo
        frame_titulo=CTkFrame(self.ventana)
        frame_titulo.pack(fill=BOTH, expand=True)
        titulo=LtkLabel(frame_titulo, "Configuracion Gimnasio")
        titulo.configure(font=("Poppins", 40, "bold"))
        titulo.pack(side=TOP, padx=20, pady=20)


        #Frame prinicial
        frame_prinicial=CTkFrame(self.ventana)
        frame_prinicial.pack(fill=BOTH, expand=True)

        boton_prinicial=LtkButtonLine(frame_prinicial, self.personal, "Personal del GYM")
        boton_prinicial.grid(row=0, column=0, padx=(5,5), pady=(5, 5), sticky="nsew")
        boton_costos=LtkButtonLine(frame_prinicial, self.costos, "Costos")
        boton_costos.grid(row=1, column=0, padx=(5,5), pady=(5, 5), sticky="nsew")
        boton_horarios=LtkButtonLine(frame_prinicial, self.horarios, "Horarios")
        boton_horarios.grid(row=2, column=0, padx=(5,5), pady=(5, 5), sticky="nsew")
        boton_usuarios=LtkButtonLine(frame_prinicial, self.usuarios, "Usuarios")
        boton_usuarios.grid(row=3, column=0, padx=(5,5), pady=(5, 5), sticky="nsew")
        boton_maquinas=LtkButtonLine(frame_prinicial, self.maquinas, "Maquinas")
        boton_maquinas.grid(row=4, column=0, padx=(5,5), pady=(5, 5), sticky="nsew")
        boton_servicios_generales=LtkButtonLine(frame_prinicial, self.servicios_generales, "Servicios Generales")
        boton_servicios_generales.grid(row=5, column=0, padx=(5,5), pady=(5, 5), sticky="nsew")
        boton_baños=LtkButtonLine(frame_prinicial, self.baños, "Baños")
        boton_baños.grid(row=6, column=0, padx=(5,5), pady=(5, 5), sticky="nsew")
        boton_vestidores=LtkButtonLine(frame_prinicial, self.vestidores, "Vestidores")
        boton_vestidores.grid(row=7, column=0, padx=(5,5), pady=(5, 5), sticky="nsew")
        boton_temporadas=LtkButtonLine(frame_prinicial, self.temporadas, "Temporadas")
        boton_temporadas.grid(row=8, column=0, padx=(5,5), pady=(5, 5), sticky="nsew")


        #Frame para guardar
        frame_guardar=CTkFrame(self.ventana)
        frame_guardar.pack(fill=BOTH, expand=True)
        boton_guardar = LtkButtonFill(frame_guardar, self.guardar_informacion, "Guardar Configuracion Banco")
        boton_guardar.pack(side=BOTTOM, padx=20, pady=20)
        
        self.ventana.mainloop()
        
    def resetear_frame_caracteristicas(self):
        for widget in self.frame_caracteristicas.winfo_children():
            widget.destroy()

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

    

    def personal(self):
        cantidad_empleados=simpledialog.askinteger("Cantidad de Empleados", "Ingrese la cantidad de empleados:")
        if cantidad_empleados is not None:
            self.cantidad_empleados.set(cantidad_empleados)

    def costos(self):
        pass
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
      

