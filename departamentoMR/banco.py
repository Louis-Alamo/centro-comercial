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

class Banco:
    def __init__(self):
        self.lista_personal=[[1, 3, 3, 3, 3]]
        self.lista_sueldos=[[4000, 3000, 3000, 3000, 3000]]
        self.lista_horarios=[["8:00", "17:00", "12:00", "13:00"]]



        self.ventana=CTk()
        self.ventana.title("Banco")
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
        titulo=LtkLabel(frame_titulo, texto="Configuración del Banco")
        titulo.configure(font=('Poppins', 30, "bold"))
        titulo.grid(row=0, column=0, pady=(1, 1), sticky="nsew")
        frame_titulo.columnconfigure(0, weight=1)
        frame_titulo.rowconfigure(0, weight=1)

        # Frame para las opciones
        frame_opciones=CTkFrame(self.ventana)
        frame_opciones.grid(row=1, column=0, pady=(10, 10))
        self.ventana.columnconfigure(0, weight=2)
        self.ventana.rowconfigure(1, weight=1)


        boton_personal_banco=LtkButtonLine(frame_opciones, self.personal, "Personal De Banco")
        boton_personal_banco.grid(row=0, column=0, padx=(5,5), pady=(5, 5))
        boton_sueldo=LtkButtonLine(frame_opciones, self.sueldos, "Sueldos")
        boton_sueldo.grid(row=1, column=0, padx=(5,5), pady=(5, 5))
        boton_horarios=LtkButtonLine(frame_opciones, self.horarios, "Horarios")
        boton_horarios.grid(row=2, column=0, padx=(5,5), pady=(5, 5))
        boton_usuarios=LtkButtonLine(frame_opciones, self.usuarios, "Usuarios")
        boton_usuarios.grid(row=3, column=0, padx=(5,5), pady=(5, 5))
        boton_servicios_generales=LtkButtonLine(frame_opciones, self.servicios_generales, "Servicios Generales")
        boton_servicios_generales.grid(row=4, column=0, padx=(5,5), pady=(5, 5))
        boton_cajeros_automaticos=LtkButtonLine(frame_opciones, self.cajeros_automaticos, "Cajeros Automáticos")
        boton_cajeros_automaticos.grid(row=5, column=0, padx=(5,5), pady=(5, 5))
        boton_temporadas=LtkButtonLine(frame_opciones, self.temporadas, "Temporadas")
        boton_temporadas.grid(row=6, column=0, padx=(5,5), pady=(5, 5))


        # Frame de características
        self.frame_caracteristicas = CTkFrame(self.ventana)
        self.frame_caracteristicas.grid(row=1, column=1, sticky="nsew")
        self.ventana.columnconfigure(1, weight=25)
        self.ventana.rowconfigure(1, weight=2)
        self.frame_caracteristicas.columnconfigure(0, weight=1)


        self.personal()
        self.sueldos()
        self.horarios()


        # Frame para el botón de guardar
        frame_guardar = CTkFrame(self.ventana)
        frame_guardar.grid(row=2, column=0, columnspan=2, sticky="nsew")
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(2, weight=1)
        boton_guardar = LtkButtonFill(frame_guardar, self.guardar_informacion, "Guardar Y Salir De Configuracion Banco")
        boton_guardar.grid(row=0, column=0, padx=100, pady=40, sticky="nsew")
        frame_guardar.columnconfigure(0, weight=1)
        frame_guardar.rowconfigure(0, weight=1)


        self.ventana.mainloop()


    def guardar_informacion(self):
        informacion={
            "cantidad_gerentes": self.lista_personal[0][0],
            "cantidad_cajeras": self.lista_personal[0][1],
            "cantidad_secretarias": self.lista_personal[0][2],
            "cantidad_guardias_seguridad": self.lista_personal[0][3],
            "cantidad_personal_tecnico": self.lista_personal[0][4],
            "sueldo_gerente": self.lista_sueldos[0][0],
            "sueldo_cajera": self.lista_sueldos[0][1],
            "sueldo_secretaria": self.lista_sueldos[0][2],
            "sueldo_guardia_seguridad": self.lista_sueldos[0][3],
            "sueldo_personal_tecnico": self.lista_sueldos[0][4],
            "horario_entrada": self.lista_horarios[0][0],
            "horario_salida": self.lista_horarios[0][1],
            "horario_entrada_almuerzo": self.lista_horarios[0][2],
            "horario_salida_almuerzo": self.lista_horarios[0][3]
        }
        
        informacion_json=json.dumps(informacion, indent=4)
        config_path=os.path.join(self.ruta_ventana, 'banco.json')

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
        self.etiqueta_gerentes = LtkLabel(self.frame_caracteristicas, texto="Cantidad de Gerentes:")
        self.etiqueta_gerentes.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_gerentes = LtkEntryLine(self.frame_caracteristicas, "1")
        self.cantidad_gerentes.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_cajeras = LtkLabel(self.frame_caracteristicas, texto="Cantidad De Cajeras:")
        self.etiqueta_cajeras.grid(row=4, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_cajeras = LtkEntryLine(self.frame_caracteristicas, "3")
        self.cantidad_cajeras.grid(row=4, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_secretarias = LtkLabel(self.frame_caracteristicas, texto="Cantidad de Secretarias:")
        self.etiqueta_secretarias.grid(row=5, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_secretarias = LtkEntryLine(self.frame_caracteristicas, "3")
        self.cantidad_secretarias.grid(row=5, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_guardias_seguridad = LtkLabel(self.frame_caracteristicas, texto="Cantidad Guardias De Seguridad:")
        self.etiqueta_guardias_seguridad.grid(row=6, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_guardias_seguridad = LtkEntryLine(self.frame_caracteristicas, "3")
        self.cantidad_guardias_seguridad.grid(row=6, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_personal_tecnico = LtkLabel(self.frame_caracteristicas, texto="Cantidad De Personal Tecnico Y Limpieza:")
        self.etiqueta_personal_tecnico.grid(row=7, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_personal_tecnico = LtkEntryLine(self.frame_caracteristicas, "3")
        self.cantidad_personal_tecnico.grid(row=7, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)



        
        boton_guardar = LtkButtonFill(self.frame_caracteristicas,lambda: self.guardar_ajustes(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))

    def guardar_ajustes(self):
        cantidad_gerentes=self.cantidad_gerentes.get()
        cantidad_cajeras=self.cantidad_cajeras.get()
        cantidad_secretarias=self.cantidad_secretarias.get()
        cantidad_guardias_seguridad=self.cantidad_guardias_seguridad.get()
        cantidad_personal_tecnico=self.cantidad_personal_tecnico.get()

        self.lista_personal.clear()
        self.lista_personal.append([int(cantidad_gerentes),
                                   int(cantidad_cajeras),
                                   int(cantidad_secretarias),
                                   int(cantidad_guardias_seguridad),
                                   int(cantidad_personal_tecnico)
                                   ])
        


    def sueldos(self):
        self.resetear_frame_caracteristicas()
    
        self.etiqueta_titulo_caracteristicas = LtkLabel(self.frame_caracteristicas, texto="Ajustes Del Sueldo")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)
        self.etiqueta_sueldo_gerente = LtkLabel(self.frame_caracteristicas, texto="Sueldo Mensual Por Gerente:")
        self.etiqueta_sueldo_gerente.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.sueldo_mensual_gerente = LtkEntryLine(self.frame_caracteristicas, "4000")
        self.sueldo_mensual_gerente.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_sueldo_cajera= LtkLabel(self.frame_caracteristicas, texto="Sueldo Mensual Por Cajera:")
        self.etiqueta_sueldo_cajera.grid(row=4, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.sueldo_mensual_cajera = LtkEntryLine(self.frame_caracteristicas, "3000")
        self.sueldo_mensual_cajera.grid(row=4, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_sueldo_secretaria = LtkLabel(self.frame_caracteristicas, texto="Sueldo Mensual Por Secretaria:")
        self.etiqueta_sueldo_secretaria.grid(row=5, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.sueldo_mensual_secretaria = LtkEntryLine(self.frame_caracteristicas, "3000")
        self.sueldo_mensual_secretaria.grid(row=5, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_sueldo_guardia_seguridad = LtkLabel(self.frame_caracteristicas, texto="Sueldo Mensual Por Guardia De Seguridad:")
        self.etiqueta_sueldo_guardia_seguridad.grid(row=6, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.sueldo_mensual_guardia_seguridad = LtkEntryLine(self.frame_caracteristicas, "3000")
        self.sueldo_mensual_guardia_seguridad.grid(row=6, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_sueldo_personal_tecnico = LtkLabel(self.frame_caracteristicas, texto="Sueldo Mensual Por Personal Tecnico:")
        self.etiqueta_sueldo_personal_tecnico.grid(row=7, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.sueldo_mensual_personal_tecnico = LtkEntryLine(self.frame_caracteristicas, "3000")
        self.sueldo_mensual_personal_tecnico.grid(row=7, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        
        boton_guardar = LtkButtonFill(self.frame_caracteristicas,lambda: self.guardar_ajustes1(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))


    def guardar_ajustes1(self):
        sueldo_mensual_gerente=self.sueldo_mensual_gerente.get()
        sueldo_mensual_cajera=self.sueldo_mensual_cajera.get()
        sueldo_mensual_secretaria=self.sueldo_mensual_secretaria.get()
        sueldo_mensual_guardia_seguridad=self.sueldo_mensual_guardia_seguridad.get()
        sueldo_mensual_personal_tecnico=self.sueldo_mensual_personal_tecnico.get()

        self.lista_sueldos.clear()
        self.lista_sueldos.append([int(sueldo_mensual_gerente),
                                   int(sueldo_mensual_cajera),
                                   int(sueldo_mensual_secretaria),
                                   int(sueldo_mensual_guardia_seguridad),
                                   int(sueldo_mensual_personal_tecnico)
                                   ])


    def horarios(self):
        self.resetear_frame_caracteristicas()
    
        self.etiqueta_titulo_caracteristicas = LtkLabel(self.frame_caracteristicas, texto="Ajustes De Horarios")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)
        self.etiqueta_horario_entrada = LtkLabel(self.frame_caracteristicas, texto="Horario De Entrada:")
        self.etiqueta_horario_entrada.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.horario_entrada = LtkEntryLine(self.frame_caracteristicas, "8:00")
        self.horario_entrada.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_horario_salida = LtkLabel(self.frame_caracteristicas, texto="Horario De Salida:")
        self.etiqueta_horario_salida.grid(row=4, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.horario_salida = LtkEntryLine(self.frame_caracteristicas, "17:00")
        self.horario_salida.grid(row=4, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_horario_entrada_almuerzo = LtkLabel(self.frame_caracteristicas, texto="Horario De Entrada Al Almuerzo:")
        self.etiqueta_horario_entrada_almuerzo.grid(row=5, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.horario_entrada_almuerzo = LtkEntryLine(self.frame_caracteristicas, "12:00")
        self.horario_entrada_almuerzo.grid(row=5, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_horario_salida_almuerzo = LtkLabel(self.frame_caracteristicas, texto="Horario De Salida Al Almuerzo:")
        self.etiqueta_horario_salida_almuerzo.grid(row=6, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.horario_salida_almuerzo = LtkEntryLine(self.frame_caracteristicas, "13:00")
        self.horario_salida_almuerzo.grid(row=6, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        boton_guardar = LtkButtonFill(self.frame_caracteristicas,lambda: self.guardar_ajustes2(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))

    def guardar_ajustes2(self):
        horario_entrada=self.horario_entrada.get()
        horario_salida=self.horario_salida.get()
        horario_entrada_almuerzo=self.horario_entrada_almuerzo.get()
        horario_salida_almuerzo=self.horario_salida_almuerzo.get()

        self.lista_horarios.clear()
        self.lista_horarios.append([horario_entrada,
                                   horario_salida,
                                   horario_entrada_almuerzo,
                                   horario_salida_almuerzo
                                   ])



    def usuarios(self):
        self.resetear_frame_caracteristicas()
        self.etiqueta_titulo_caracteristicas = LtkLabel(self.frame_caracteristicas, texto="Ajustes De Horarios")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)

        self.etiqueta_cantidad_usuarios = LtkLabel(self.frame_caracteristicas, texto="Cantidad De Usuarios:")
        self.etiqueta_cantidad_usuarios.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_usuarios = LtkEntryLine(self.frame_caracteristicas, "100")
        self.cantidad_usuarios.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        self.etiqueta


    def servicios_generales(self):
        pass

    def cajeros_automaticos(self):
        pass

    def temporadas(self):
        pass


Banco()