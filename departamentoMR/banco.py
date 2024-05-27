from customtkinter import *
from tkinter import messagebox, simpledialog
from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkLabel import LtkLabel
from tkinter import simpledialog, Toplevel, Checkbutton, StringVar, Canvas, Frame, Scrollbar
import tkinter
import tkinter as tk
from tkinter import ttk
import json
import os

class Banco:
    def __init__(self):
        self.lista_personal=[[1, 3, 3, 3, 3]]
        self.lista_sueldos=[[4000, 3000, 3000, 3000, 3000]]
        self.lista_horarios=[["8:00", "17:00"]]
        self.lista_usuarios=[[100]]
        self.lista_servicios_generales=[[300, 200, 420, 2000]]
        self.lista_cajeros_automaticos=[[3]]
        self.lista_temporadas=[[True,100],[False,0],[False,0]]
        self.lista_tipo=[["Oro", "0.0000-0.0000"]]
        self.lista_acude=[["Secretaria", "0.0000-0.0000"]]
        self.lista_llegada=[[3, "0.0000-0.0000"]]
        self.lista_ventanilla=[[3, "0.0000-0.0000"]]
        self.lista_secre=[[3, "0.0000-0.0000"]]
        self.lista_cajero_a=[[3, "0.0000-0.0000"]]
        self.lista_olvido=[[1, "0.0000-0.0000"]]


        self.ventana=CTk()
        self.ventana.title("Banco")
        self.ventana.geometry("900x600+350+100")
        self.ventana.configure(bg="#FFFFFF")
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)
        self.ventana.rowconfigure(1, weight=1)

        self.ruta_ventana=os.path.dirname(os.path.abspath(__file__))
        
        frame_titulo = CTkFrame(self.ventana)
        frame_titulo.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)
        titulo=LtkLabel(frame_titulo, texto="Configuración del Banco")
        titulo.configure(font=('Poppins', 30, "bold"))
        titulo.grid(row=0, column=0, pady=(1, 1), sticky="nsew")
        frame_titulo.columnconfigure(0, weight=1)
        frame_titulo.rowconfigure(0, weight=1)

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
        boton_datos_historicos=LtkButtonLine(frame_opciones, self.datos_historicos, "Datos Históricos")
        boton_datos_historicos.grid(row=7, column=0, padx=(5,5), pady=(5, 5))

        self.frame_caracteristicas = CTkFrame(self.ventana)
        self.frame_caracteristicas.grid(row=1, column=1, sticky="nsew")
        self.ventana.columnconfigure(1, weight=25)
        self.ventana.rowconfigure(1, weight=2)
        self.frame_caracteristicas.columnconfigure(0, weight=1)


        self.sueldos()
        self.horarios()
        self.usuarios()
        self.servicios_generales()
        self.cajeros_automaticos()
        self.temporadas()
        self.datos_historicos()
        self.personal()

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
            "cantidad_ventanillas": self.lista_personal[0][1],
            "cantidad_secretarias": self.lista_personal[0][2],
            "cantidad_guardias_seguridad": self.lista_personal[0][3],
            "cantidad_personal_tecnico": self.lista_personal[0][4],
            "sueldo_gerente": self.lista_sueldos[0][0],
            "sueldo_cajera": self.lista_sueldos[0][1],
            "sueldo_secretaria": self.lista_sueldos[0][2],
            "sueldo_guardia_seguridad": self.lista_sueldos[0][3],
            "sueldo_personal_tecnico": self.lista_sueldos[0][4],
            "horario_entrada": self.lista_horarios[0][0],
            "horario_cierre": self.lista_horarios[0][1],
            "cantidad_usuarios": self.lista_usuarios[0][0],
            "pago_mensual_luz": self.lista_servicios_generales[0][0],	
            "pago_mensual_agua": self.lista_servicios_generales[0][1],
            "pago_mensual_internet": self.lista_servicios_generales[0][2],
            "pago_mensual_renta_local": self.lista_servicios_generales[0][3],
            "cantidad_cajeros_automaticos": self.lista_cajeros_automaticos[0][0],
            "temporada_regular": self.lista_temporadas[0][0],
            "temporada_alta": self.lista_temporadas[0][1],
            "temporada_baja": self.lista_temporadas[0][2],
            "tipo": self.lista_tipo,
            "acude": self.lista_acude,
            "horario_llegada": self.lista_llegada,
            "duracion_ventanilla": self.lista_ventanilla,
            "duracion_secre": self.lista_secre,
            "duracion_cajero_a": self.lista_cajero_a,
            "olvido": self.lista_olvido
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
  

        boton_guardar = LtkButtonFill(self.frame_caracteristicas,lambda: self.guardar_ajustes2(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))

    def guardar_ajustes2(self):
        horario_entrada=self.horario_entrada.get()
        horario_salida=self.horario_salida.get()


        self.lista_horarios.clear()
        self.lista_horarios.append([horario_entrada,
                                   horario_salida
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

    def guardar_ajustes3(self):
        cantidad_usuarios=self.cantidad_usuarios.get()

        self.lista_usuarios.clear()
        self.lista_usuarios.append([int(cantidad_usuarios)])



    def servicios_generales(self):
        self.resetear_frame_caracteristicas()

        self.etiqueta_titulo_caracteristicas=LtkLabel(self.frame_caracteristicas, texto="Ajustes De Servicios Generales")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)
        self.etiqueta_pago_mensual_luz=LtkLabel(self.frame_caracteristicas, texto="Pago Mensual De Luz:")
        self.etiqueta_pago_mensual_luz.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.pago_mensual_luz=LtkEntryLine(self.frame_caracteristicas, "300")
        self.pago_mensual_luz.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_pago_mensual_agua=LtkLabel(self.frame_caracteristicas, texto="Pago Mensual De Agua:")
        self.etiqueta_pago_mensual_agua.grid(row=4, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.pago_mensual_agua=LtkEntryLine(self.frame_caracteristicas, "200")
        self.pago_mensual_agua.grid(row=4, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_pago_mensual_internet=LtkLabel(self.frame_caracteristicas, texto="Pago Mensual De Internet Y Telefono:")
        self.etiqueta_pago_mensual_internet.grid(row=5, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.pago_mensual_internet=LtkEntryLine(self.frame_caracteristicas, "420")
        self.pago_mensual_internet.grid(row=5, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.pago_mensual_renta_local=LtkLabel(self.frame_caracteristicas, texto="Pago Mensual De Renta Del Local:")
        self.pago_mensual_renta_local.grid(row=6, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.pago_mensual_renta_local=LtkEntryLine(self.frame_caracteristicas, "2000")
        self.pago_mensual_renta_local.grid(row=6, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        boton_guardar=LtkButtonFill(self.frame_caracteristicas,lambda: self.guardar_ajustes5(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))
    
    def guardar_ajustes5(self):
        pago_mensual_luz=self.pago_mensual_luz.get()
        pago_mensual_agua=self.pago_mensual_agua.get()
        pago_mensual_internet=self.pago_mensual_internet.get()
        pago_mensual_renta_local=self.pago_mensual_renta_local.get()

        self.lista_servicios_generales.clear()
        self.lista_servicios_generales.append([int(pago_mensual_luz), 
                                    int(pago_mensual_agua), 
                                    int(pago_mensual_internet),
                                    int(pago_mensual_renta_local)])

    def cajeros_automaticos(self):
        self.resetear_frame_caracteristicas()
        self.etiqueta_titulo_caracteristicas=LtkLabel(self.frame_caracteristicas, texto="Ajustes De Cajeros Automaticos")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)

        self.etiqueta_cantidad_cajeros_automaticos=LtkLabel(self.frame_caracteristicas, texto="Cantidad De Cajeros Automaticos:")
        self.etiqueta_cantidad_cajeros_automaticos.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_cajeros_automaticos=LtkEntryLine(self.frame_caracteristicas, "3")
        self.cantidad_cajeros_automaticos.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

    def guardar_ajustes4(self):
        cantidad_cajeros_automaticos=self.cantidad_cajeros_automaticos.get()

        self.lista_cajeros_automaticos.clear()
        self.lista_cajeros_automaticos.append([int(cantidad_cajeros_automaticos)])

    def temporadas(self):
        self.resetear_frame_caracteristicas()
        self.etiqueta_titulo_caracteristicas = LtkLabel(self.frame_caracteristicas, texto="Ajustes De Temporadas")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)

        self.temporada_var = tkinter.IntVar()

        self.temporada_regular = tkinter.Radiobutton(self.frame_caracteristicas, text="Temporada Regular", variable=self.temporada_var, value=1)
        self.temporada_regular.grid(row=3, column=1, padx=(5, 10), pady=(5, 5), sticky="w")

        self.temporada_alta = tkinter.Radiobutton(self.frame_caracteristicas, text="Temporada Alta", variable=self.temporada_var, value=2)
        self.temporada_alta.grid(row=4, column=1, padx=(5, 10), pady=(5, 5), sticky="w")

        self.temporada_baja = tkinter.Radiobutton(self.frame_caracteristicas, text="Temporada Baja", variable=self.temporada_var, value=3)
        self.temporada_baja.grid(row=5, column=1, padx=(5, 10), pady=(5, 5), sticky="w")

        boton_guardar = LtkButtonFill(self.frame_caracteristicas, lambda: self.guardar_ajustes8(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))


    def guardar_ajustes8(self):
        seleccion = self.temporada_var.get()

        if seleccion == 1:
            temporada_regular = [True,80]
            temporada_alta = [False,0]
            temporada_baja = [False,0]
        elif seleccion == 2:
            temporada_regular = [False,0]
            temporada_alta = [True,100]
            temporada_baja = [False,0]
        elif seleccion == 3:
            temporada_regular = [False,0]
            temporada_alta = [False,0]
            temporada_baja = [True,60]

        self.lista_temporadas.clear()
        self.lista_temporadas.append([temporada_regular, temporada_alta, temporada_baja])



    def datos_historicos(self):
        self.resetear_frame_caracteristicas()
        self.etiqueta_titulo_caracteristicas = LtkLabel(self.frame_caracteristicas, texto="Ajustes De Datos Historicos")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)

        boton = LtkButtonFill(self.frame_caracteristicas, lambda: self.pedir_datos(), "Ingresar datos")
        boton.grid(row=10, column=0, columnspan=3, pady=(5, 10))

    def pedir_datos(self):
        self.resetear_frame_caracteristicas()
        tipo_cliente = simpledialog.askinteger("Entrada", "Renglones Para Tipo De Clientes", minvalue=1, parent=self.frame_caracteristicas)
        acude_a = simpledialog.askinteger("Entrada", "Renglones De Acude A", minvalue=1, parent=self.frame_caracteristicas)
        tiempo_llegada = simpledialog.askinteger("Entrada", "Renglones Para Tiempo De Llegada", minvalue=1, parent=self.frame_caracteristicas)
        duracion_ventanilla = simpledialog.askinteger("Entrada", "Renglones Tiempo En ventanilla", minvalue=1, parent=self.frame_caracteristicas)
        duracion_secre = simpledialog.askinteger("Entrada", "Renglones Tiempo En Secretarias", minvalue=1, parent=self.frame_caracteristicas)
        duracion_cajero_a= simpledialog.askinteger("Entrada", "Renglones Tiempo En Cajero Automatico", minvalue=1, parent=self.frame_caracteristicas)
        olvido_tarjeta=simpledialog.askinteger("Entrada", "Renglones Para Olvido De Tarjeta", minvalue=1, parent=self.frame_caracteristicas)

        canvas = Canvas(self.frame_caracteristicas)
        canvas.configure(bg="gray")
        scrollbar = Scrollbar(self.frame_caracteristicas, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas)
        scrollable_frame.configure(bg="gray")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set, width=500)

        canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.frame_caracteristicas.columnconfigure(0, weight=1)
        self.frame_caracteristicas.rowconfigure(0, weight=1)

        current_row = 0
        self.check_tipo = StringVar()
        self.checkbutton_tipo = Checkbutton(scrollable_frame, text="MARCA PARA USAR DATOS HISTORICOS tipo", variable=self.check_tipo, onvalue="Si", offvalue="No")
        self.checkbutton_tipo.deselect()
        self.checkbutton_tipo.grid(row=current_row, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        current_row += 1
        self.entrys_tipo = []
        self.valores_tipo = []
        for i in range(tipo_cliente):
            entry_tipo = LtkEntryLine(scrollable_frame, "Oro")
            entry_tipo.grid(row=current_row, column=0, padx=(5, 10), pady=(5, 5), sticky="nsew")
            entry = LtkEntryLine(scrollable_frame, ".15")
            entry.grid(row=current_row, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")
            self.entrys_tipo.append(entry)
            self.valores_tipo.append(entry_tipo)
            current_row += 1


        self.check_acude=StringVar()
        self.checkbutton_acude=Checkbutton(scrollable_frame, text="MARCA PARA USAR DATOS HISTORICOS acude", variable=self.check_acude, onvalue="Si", offvalue="No")
        self.checkbutton_acude.deselect()
        self.checkbutton_acude.grid(row=current_row, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        current_row += 1
        self.entrys_acude = []
        self.valores_acude = []
        for i in range(acude_a):
            entry_acude = LtkEntryLine(scrollable_frame, "Secretaria")
            entry_acude.grid(row=current_row, column=0, padx=(5, 10), pady=(5, 5), sticky="nsew")
            entry = LtkEntryLine(scrollable_frame, ".15")
            entry.grid(row=current_row, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")
            self.entrys_acude.append(entry)
            self.valores_acude.append(entry_acude)
            current_row += 1


  
        self.check_llegada = StringVar()
        self.checkbutton_llegada = Checkbutton(scrollable_frame, text="MARCA PARA USAR DATOS HISTORICOS LLEGADA", variable=self.check_llegada, onvalue="Si", offvalue="No")
        self.checkbutton_llegada.deselect()
        self.checkbutton_llegada.grid(row=current_row, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        current_row += 1
        self.entrys_llegada = []
        self.valores_llegada = []
        for i in range(tiempo_llegada):
            entry_llegada = LtkEntryLine(scrollable_frame, "3")
            entry_llegada.grid(row=current_row, column=0, padx=(5, 10), pady=(5, 5), sticky="nsew")
            entry = LtkEntryLine(scrollable_frame, ".15")
            entry.grid(row=current_row, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")
            self.entrys_llegada.append(entry)
            self.valores_llegada.append(entry_llegada)
            current_row += 1

        self.check_ventanilla = StringVar()
        self.checkbutton_ventanilla = Checkbutton(scrollable_frame, text="MARCA PARA USAR DATOS HISTORICOS VENTANILLA", variable=self.check_ventanilla, onvalue="Si", offvalue="No")
        self.checkbutton_ventanilla.deselect()
        self.checkbutton_ventanilla.grid(row=current_row, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        current_row += 1
        self.entrys_ventanilla = []
        self.valores_ventanilla = []
        for i in range(duracion_ventanilla):
            entry_ventanilla = LtkEntryLine(scrollable_frame, "3")
            entry_ventanilla.grid(row=current_row, column=0, padx=(5, 10), pady=(5, 5), sticky="nsew")
            entry = LtkEntryLine(scrollable_frame, ".15")
            entry.grid(row=current_row, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")
            self.entrys_ventanilla.append(entry)
            self.valores_ventanilla.append(entry_ventanilla)
            current_row += 1

        self.check_secre = StringVar()
        self.checkbutton_secre = Checkbutton(scrollable_frame, text="MARCA PARA USAR DATOS HISTORICOS SECRE", variable=self.check_secre, onvalue="Si", offvalue="No")
        self.checkbutton_secre.deselect()
        self.checkbutton_secre.grid(row=current_row, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        current_row += 1
        self.entrys_secre = []
        self.valores_secre = []
        for i in range(duracion_secre):
            entry_secre = LtkEntryLine(scrollable_frame, "3")
            entry_secre.grid(row=current_row, column=0, padx=(5, 10), pady=(5, 5), sticky="nsew")
            entry = LtkEntryLine(scrollable_frame, ".15")
            entry.grid(row=current_row, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")
            self.entrys_secre.append(entry)
            self.valores_secre.append(entry_secre)
            current_row += 1

        self.check_cajero_a = StringVar()
        self.checkbutton_cajero_a = Checkbutton(scrollable_frame, text="MARCA PARA USAR DATOS HISTORICOS CAJERO A", variable=self.check_cajero_a, onvalue="Si", offvalue="No")
        self.checkbutton_cajero_a.deselect()
        self.checkbutton_cajero_a.grid(row=current_row, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        current_row += 1
        self.entrys_cajero_a = []
        self.valores_cajero_a = []
        for i in range(duracion_cajero_a):
            entry_cajero_a = LtkEntryLine(scrollable_frame, "3")
            entry_cajero_a.grid(row=current_row, column=0, padx=(5, 10), pady=(5, 5), sticky="nsew")
            entry = LtkEntryLine(scrollable_frame, ".15")
            entry.grid(row=current_row, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")
            self.entrys_cajero_a.append(entry)
            self.valores_cajero_a.append(entry_cajero_a)
            current_row += 1

        self.check_olvido = StringVar()
        self.checkbutton_olvido = Checkbutton(scrollable_frame, text="MARCA PARA USAR DATOS HISTORICOS OLVIDO", variable=self.check_olvido, onvalue="Si", offvalue="No")
        self.checkbutton_olvido.deselect()
        self.checkbutton_olvido.grid(row=current_row, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        current_row += 1
        self.entrys_olvido = []
        self.valores_olvido = []
        for i in range(olvido_tarjeta):
            entry_olvido = LtkEntryLine(scrollable_frame, "3")
            entry_olvido.grid(row=current_row, column=0, padx=(5, 10), pady=(5, 5), sticky="nsew")
            entry = LtkEntryLine(scrollable_frame, ".15")
            entry.grid(row=current_row, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")
            self.entrys_olvido.append(entry)
            self.valores_olvido.append(entry_olvido)
            current_row += 1


        def all_checkbuttons_selected():
            return (self.check_tipo.get() == "Si" and
                    self.check_acude.get() == "Si" and
                    self.check_llegada.get() == "Si" and
                    self.check_ventanilla.get() == "Si" and
                    self.check_secre.get() == "Si" and
                    self.check_cajero_a.get() == "Si" and
                    self.check_olvido.get() == "Si")
        
        def guardar_si_todo_seleccionado():
            if all_checkbuttons_selected():
                self.guardar_ajustes9(tipo_cliente, acude_a, tiempo_llegada, duracion_ventanilla, duracion_secre, duracion_cajero_a, olvido_tarjeta)
            else:
                messagebox.showerror("Error", "Por favor, selecciona todos los checkbuttons antes de guardar.")

        boton_guardar = LtkButtonFill(self.frame_caracteristicas, guardar_si_todo_seleccionado, "Guardar Ajustes Y Ver Tablas")
        boton_guardar.grid(row=current_row, column=0, columnspan=2, pady=(5, 10))


    def guardar_ajustes9(self, tipo_cliente, acude_a, tiempo_llegada, duracion_ventanilla, duracion_secre, duracion_cajero_a, olvido_tarjeta):
        rangos_tipo=self.calcular_rangos([float(entry.get()) for entry in self.entrys_tipo])
        rangos_acude=self.calcular_rangos([float(entry.get()) for entry in self.entrys_acude])
        rangos_llegada=self.calcular_rangos([float(entry.get()) for entry in self.entrys_llegada])
        rangos_ventanilla=self.calcular_rangos([float(entry.get()) for entry in self.entrys_ventanilla])
        rangos_secre=self.calcular_rangos([float(entry.get()) for entry in self.entrys_secre])
        rangos_cajero_a=self.calcular_rangos([float(entry.get()) for entry in self.entrys_cajero_a])
        rangos_olvido=self.calcular_rangos([float(entry.get()) for entry in self.entrys_olvido])

        self.lista_tipo = [(str(self.valores_tipo[i].get()), rangos_tipo[i][1]) for i in range(tipo_cliente)]
        self.lista_acude = [(str(self.valores_acude[i].get()), rangos_acude[i][1]) for i in range(acude_a)]
        self.lista_llegada = [(int(self.valores_llegada[i].get()), rangos_llegada[i][1]) for i in range(tiempo_llegada)]
        self.lista_ventanilla = [(int(self.valores_ventanilla[i].get()), rangos_ventanilla[i][1]) for i in range(duracion_ventanilla)]
        self.lista_secre = [(int(self.valores_secre[i].get()), rangos_secre[i][1]) for i in range(duracion_secre)]
        self.lista_cajero_a = [(int(self.valores_cajero_a[i].get()), rangos_cajero_a[i][1]) for i in range(duracion_cajero_a)]
        self.lista_olvido = [(int(self.valores_olvido[i].get()), rangos_olvido[i][1]) for i in range(olvido_tarjeta)]

        self.tablas_tipo = [(str(self.valores_tipo[i].get()), float(self.entrys_tipo[i].get()), rangos_tipo[i][0], rangos_tipo[i][1]) for i in range(tipo_cliente)]
        self.tablas_acude = [(str(self.valores_acude[i].get()), float(self.entrys_acude[i].get()), rangos_acude[i][0], rangos_acude[i][1]) for i in range(acude_a)]
        self.tablas_llegada = [(int(self.valores_llegada[i].get()), float(self.entrys_llegada[i].get()), rangos_llegada[i][0], rangos_llegada[i][1]) for i in range(tiempo_llegada)]
        self.tablas_ventanilla = [(int(self.valores_ventanilla[i].get()), float(self.entrys_ventanilla[i].get()), rangos_ventanilla[i][0], rangos_ventanilla[i][1]) for i in range(duracion_ventanilla)]
        self.tablas_secre = [(int(self.valores_secre[i].get()), float(self.entrys_secre[i].get()), rangos_secre[i][0], rangos_secre[i][1]) for i in range(duracion_secre)]
        self.tablas_cajero_a = [(int(self.valores_cajero_a[i].get()), float(self.entrys_cajero_a[i].get()), rangos_cajero_a[i][0], rangos_cajero_a[i][1]) for i in range(duracion_cajero_a)]
        self.tablas_olvido = [(int(self.valores_olvido[i].get()), float(self.entrys_olvido[i].get()), rangos_olvido[i][0], rangos_olvido[i][1]) for i in range(olvido_tarjeta)]

        self.imprimir_tablas()

    def calcular_rangos(self, probabilidades):
        probabilidad_acumulada = [sum(probabilidades[:i + 1]) for i in range(len(probabilidades))]
        
        rangos = []
        for i in range(len(probabilidades)):
            rango_inicio = probabilidad_acumulada[i - 1] + 0.0001 if i > 0 else 0.0
            rango_fin = probabilidad_acumulada[i]
            rangos.append((probabilidad_acumulada[i], f"{rango_inicio:.4f}-{rango_fin:.4f}"))
        
        return rangos
    
    def imprimir_tablas(self):
        ventana = tk.Toplevel()
        ventana.title("Tablas")
        ventana.geometry("700x500")
        
        treeview = ttk.Treeview(ventana)
        treeview["columns"] = ("Probabilidad", "Probabilidad Acumulada", "Rango")
        treeview.heading("#0", text="Tabla")
        treeview.heading("Probabilidad", text="Probabilidad")
        treeview.heading("Probabilidad Acumulada", text="Probabilidad Acumulada")
        treeview.heading("Rango", text="Rango")
        treeview.pack(expand=True, fill="both")

        self.insertar_tabla(treeview, "Tipo de Cliente", self.tablas_tipo)
        self.insertar_tabla(treeview, "Acude A", self.tablas_acude)
        self.insertar_tabla(treeview, "Tiempo de Llegada", self.tablas_llegada)
        self.insertar_tabla(treeview, "Duración en ventanilla", self.tablas_ventanilla)
        self.insertar_tabla(treeview, "Duración en Secretarias", self.tablas_secre)
        self.insertar_tabla(treeview, "Duración en Cajero Automático", self.tablas_cajero_a)
        self.insertar_tabla(treeview, "Olvido de Tarjeta", self.tablas_olvido)

    def insertar_tabla(self, treeview, nombre_tabla, datos_tabla):
        treeview.insert("", tk.END, text=nombre_tabla, values=("", "", ""))
        for valor, probabilidad, prob_acum, rango in datos_tabla:
            treeview.insert("", tk.END, text=str(valor), values=(probabilidad, prob_acum, rango))


Banco()