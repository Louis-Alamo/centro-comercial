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
        self.lista_personal=[[3, 3, 3, 3, 3]]
        self.lista_sueldos=[[4000, 3000]]
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
        boton_sueldo=LtkButtonLine(frame_opciones, self.sueldo, "Sueldo")
        boton_sueldo.grid(row=1, column=0, padx=(5,5), pady=(5, 5))
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


        self.personal()
        self.sueldo()


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
            "cantidad_recepcionistas": self.lista_personal[0][0],
            "cantidad_personal_limpieza": self.lista_personal[0][1],	
            "cantidad_gerentes": self.lista_personal[0][2],
            "cantidad_entrenadores": self.lista_personal[0][3],
            "cantidad_personal_tecnico": self.lista_personal[0][4],
            "sueldo_mensual_gerente": self.lista_sueldos[0][0],
            "sueldo_mensual_entrenador": self.lista_sueldos[0][1]
        }
        
        informacion_json=json.dumps(informacion, indent=4)
        config_path=os.path.join(self.ruta_ventana, 'gimnasio.json')

        with open(config_path, 'w') as f:
            f.write(informacion_json)

        messagebox.showinfo("Informacion", "Informacion guardada correctamente")
        self.ventana.destroy()

    def resetear_frame_caracteristicas(self):
        for widget in self.frame_caracteristicas.winfo_children():
            widget.grid_remove()
    
    def personal(self):
        self.resetear_frame_caracteristicas()
    
        self.etiqueta_titulo_caracteristicas = LtkLabel(self.frame_caracteristicas, texto="Ajustes Del Personal")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)

        self.etiqueta_recepcion = LtkLabel(self.frame_caracteristicas, texto="Cantidad de Recepcionistas:")
        self.etiqueta_recepcion.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_recepcionistas = LtkEntryLine(self.frame_caracteristicas, "3")
        self.cantidad_recepcionistas.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.etiqueta_personal_limpieza = LtkLabel(self.frame_caracteristicas, texto="Cantidad Personal De limpieza:")
        self.etiqueta_personal_limpieza.grid(row=4, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_personal_limpieza = LtkEntryLine(self.frame_caracteristicas, "3")
        self.cantidad_personal_limpieza.grid(row=4, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.etiqueta_gerentes = LtkLabel(self.frame_caracteristicas, texto="Cantidad de Gerentes:")
        self.etiqueta_gerentes.grid(row=5, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_gerentes = LtkEntryLine(self.frame_caracteristicas, "3")
        self.cantidad_gerentes.grid(row=5, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        
        self.etiqueta_entrenadores = LtkLabel(self.frame_caracteristicas, texto="Cantidad de Entrenadores:")
        self.etiqueta_entrenadores.grid(row=6, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_entrenadores = LtkEntryLine(self.frame_caracteristicas, "3")
        self.cantidad_entrenadores.grid(row=6, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.etiqueta_personal_tecnico = LtkLabel(self.frame_caracteristicas, texto="Cantidad Personal de Tecnico:")
        self.etiqueta_personal_tecnico.grid(row=7, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_personal_tecnico = LtkEntryLine(self.frame_caracteristicas, "3")
        self.cantidad_personal_tecnico.grid(row=7, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)



        
        boton_guardar = LtkButtonFill(self.frame_caracteristicas,lambda: self.guardar_ajustes(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))

    def guardar_ajustes(self):
        cantidad_recepcionistas = self.cantidad_recepcionistas.get()
        cantidad_personal_limpieza = self.cantidad_personal_limpieza.get()
        cantidad_gerentes = self.cantidad_gerentes.get()
        cantidad_entrenadores = self.cantidad_entrenadores.get()
        cantidad_personal_tecnico = self.cantidad_personal_tecnico.get()

        self.lista_personal.clear()
        self.lista_personal.append([int(cantidad_recepcionistas), 
                                    int(cantidad_personal_limpieza), 
                                    int(cantidad_gerentes), 
                                    int(cantidad_entrenadores), 
                                    int(cantidad_personal_tecnico)])
        


    def sueldo(self):
        self.resetear_frame_caracteristicas()
    
        self.etiqueta_titulo_caracteristicas = LtkLabel(self.frame_caracteristicas, texto="Ajustes Del Sueldo")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)

        self.etiqueta_sueldo_gerente = LtkLabel(self.frame_caracteristicas, texto="Sueldo Mensual Para El Gerente:")
        self.etiqueta_sueldo_gerente.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.sueldo_mensual_gerente = LtkEntryLine(self.frame_caracteristicas, "4000")
        self.sueldo_mensual_gerente.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.etiqueta_sueldo_entrenador = LtkLabel(self.frame_caracteristicas, texto="Sueldo Mensual Por Entrenador:")
        self.etiqueta_sueldo_entrenador.grid(row=4, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.sueldo_mensual_entrenador = LtkEntryLine(self.frame_caracteristicas, "3000")
        self.sueldo_mensual_entrenador.grid(row=4, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        
        boton_guardar = LtkButtonFill(self.frame_caracteristicas,lambda: self.guardar_ajustes1(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))


    def guardar_ajustes1(self):
        sueldo_mensual_gerente=self.sueldo_mensual_gerente.get()
        sueldo_mensual_entrenador=self.sueldo_mensual_entrenador.get()

        self.lista_sueldos.clear()
        self.lista_sueldos.append([int(sueldo_mensual_gerente),
                                    int(sueldo_mensual_entrenador)
                                   ])



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
      

