from customtkinter import *
from tkinter import messagebox, simpledialog
from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkLabel import LtkLabel
import tkinter
import json
import os

class Banco:
    def __init__(self):
        self.lista_personal=[[1, 3, 3, 3, 3]]
        self.lista_sueldos=[[4000, 3000, 3000, 3000, 3000]]
        self.lista_horarios=[["8:00", "17:00", "12:00", "13:00"]]
        self.lista_usuarios=[[100]]
        self.lista_servicios_generales=[[300, 200, 420, 2000]]
        self.lista_cajeros_automaticos=[[3]]
        self.lista_temporadas=[[True,100],[False,0],[False,0]]
        self.lista_descuento=[[.10,.20,.05]]



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
        boton_datos_historicos=LtkButtonLine(frame_opciones, self.datos_historicos, "Datos Históricos")
        boton_datos_historicos.grid(row=7, column=0, padx=(5,5), pady=(5, 5))



        # Frame de características
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
            "horario_salida_almuerzo": self.lista_horarios[0][3],
            "cantidad_usuarios": self.lista_usuarios[0][0],
            "pago_mensual_luz": self.lista_servicios_generales[0][0],	
            "pago_mensual_agua": self.lista_servicios_generales[0][1],
            "pago_mensual_internet": self.lista_servicios_generales[0][2],
            "pago_mensual_renta_local": self.lista_servicios_generales[0][3],
            "cantidad_cajeros_automaticos": self.lista_cajeros_automaticos[0][0],
            "temporada_regular": self.lista_temporadas[0][0],
            "temporada_alta": self.lista_temporadas[0][1],
            "temporada_baja": self.lista_temporadas[0][2],
            "descuento_regular": self.lista_descuento[0][0],
            "descuento_alta": self.lista_descuento[0][1],
            "descuento_baja": self.lista_descuento[0][2],
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
        self.descuento_regular = LtkEntryLine(self.frame_caracteristicas, ".10")
        self.descuento_regular.grid(row=3, column=2, padx=(5, 10), pady=(5, 5), sticky="w")

        self.temporada_alta = tkinter.Radiobutton(self.frame_caracteristicas, text="Temporada Alta", variable=self.temporada_var, value=2)
        self.temporada_alta.grid(row=4, column=1, padx=(5, 10), pady=(5, 5), sticky="w")
        self.descuento_alta = LtkEntryLine(self.frame_caracteristicas, ".20")
        self.descuento_alta.grid(row=4, column=2, padx=(5, 10), pady=(5, 5), sticky="w")

        self.temporada_baja = tkinter.Radiobutton(self.frame_caracteristicas, text="Temporada Baja", variable=self.temporada_var, value=3)
        self.temporada_baja.grid(row=5, column=1, padx=(5, 10), pady=(5, 5), sticky="w")
        self.descuento_baja = LtkEntryLine(self.frame_caracteristicas, ".05")
        self.descuento_baja.grid(row=5, column=2, padx=(5, 10), pady=(5, 5), sticky="w")

        boton_guardar = LtkButtonFill(self.frame_caracteristicas, lambda: self.guardar_ajustes8(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))


    def guardar_ajustes8(self):
        seleccion = self.temporada_var.get()

        if seleccion == 1:
            descuento_regular = self.descuento_regular.get() or ".10"
            temporada_regular = [True,80]
            temporada_alta = [False,0]
            temporada_baja = [False,0]
        elif seleccion == 2:
            descuento_alta = self.descuento_alta.get() or ".20"
            temporada_regular = [False,0]
            temporada_alta = [True,100]
            temporada_baja = [False,0]
        elif seleccion == 3:
            descuento_baja = self.descuento_baja.get() or ".05"
            temporada_regular = [False,0]
            temporada_alta = [False,0]
            temporada_baja = [True,60]

        self.lista_temporadas.clear()
        self.lista_descuento.clear()

        if seleccion == 1:
            self.lista_descuento.append([float(descuento_regular), 0, 0])
        elif seleccion == 2:
            self.lista_descuento.append([0, float(descuento_alta), 0])
        elif seleccion == 3:
            self.lista_descuento.append([0, 0, float(descuento_baja)])

        self.lista_temporadas.append([temporada_regular, temporada_alta, temporada_baja])



    def datos_historicos(self):
        pass




Banco()