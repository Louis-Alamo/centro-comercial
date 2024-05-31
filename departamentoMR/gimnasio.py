from customtkinter import *
import tkinter
import tabulate
from tkinter import Checkbutton, StringVar
from tkinter import messagebox, simpledialog
from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkLabel import LtkLabel
import tkinter as tk
from tkinter import simpledialog, Toplevel, Checkbutton, StringVar, Canvas, Frame, Scrollbar
import json
from tkinter import *
import tkinter as tk
from tkinter import ttk
import os


class Gimnasio:
    def __init__(self):
        self.lista_personal = [[3, 3, 3, 3, 3]]
        self.lista_sueldos = [[4000, 3000, 2000, 2000, 2000]]
        self.lista_horarios = [["6:00", "22:00"]]
        self.lista_usuarios = [[200,250]]
        self.lista_maquinas = [[50]]
        self.lista_servicios_generales = [[300, 200, 420, 200, 2000]]
        self.lista_temporadas = [[True, 100], [False, 0], [False, 0]]
        self.lista_descuento = [[.10, .20, .05]]
        self.lista_llegada = [(0, "0.0000-0.0000")]
        self.lista_lapso = [(0, "0.0000-0.0000")]
        self.lista_duracion_gym = [(0, "0.0000-0.0000")]
        self.lista_baño = [(0, "0.0000-0.0000")]
        self.lista_sexo=[("Mujer", "0.0000-0.0000")]


        self.ventana=CTk()
        self.ventana.title("Gimnasio")
        self.ventana.geometry("750x800+350+100")
        self.ventana.configure(bg="#FFFFFF")
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)
        self.ventana.rowconfigure(1, weight=1)

        self.ruta_ventana=os.path.dirname(os.path.abspath(__file__))
        
        frame_titulo=CTkFrame(self.ventana)
        frame_titulo.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)
        titulo=LtkLabel(frame_titulo, texto="Configuración del Gimnasio")
        titulo.configure(font=('Poppins', 30, "bold"))
        titulo.grid(row=0, column=0, pady=(1, 1), sticky="nsew")
        frame_titulo.columnconfigure(0, weight=1)
        frame_titulo.rowconfigure(0, weight=1)

        frame_opciones=CTkFrame(self.ventana)
        frame_opciones.grid(row=1, column=0, pady=(10, 10))
        self.ventana.columnconfigure(0, weight=2)
        self.ventana.rowconfigure(1, weight=1)


        boton_personal_gimnasio=LtkButtonLine(frame_opciones, self.personal, "Personal De Gimnasio")
        boton_personal_gimnasio.grid(row=0, column=0, padx=(5,5), pady=(5, 5))
        boton_sueldo=LtkButtonLine(frame_opciones, self.sueldos, "Sueldos")
        boton_sueldo.grid(row=1, column=0, padx=(5,5), pady=(5, 5))
        boton_horarios=LtkButtonLine(frame_opciones, self.horarios, "Horarios")
        boton_horarios.grid(row=2, column=0, padx=(5,5), pady=(5, 5))
        boton_usuarios=LtkButtonLine(frame_opciones, self.usuarios, "Usuarios")
        boton_usuarios.grid(row=3, column=0, padx=(5,5), pady=(5, 5))
        boton_maquinas=LtkButtonLine(frame_opciones, self.maquinas, "Maquinas")
        boton_maquinas.grid(row=4, column=0, padx=(5,5), pady=(5, 5))
        boton_servicios_generales=LtkButtonLine(frame_opciones, self.servicios_generales, "Servicios Generales")
        boton_servicios_generales.grid(row=5, column=0, padx=(5,5), pady=(5, 5))
        boton_lista_historicos=LtkButtonLine(frame_opciones, self.datos_historicos, "Datos Historicos")
        boton_lista_historicos.grid(row=8, column=0, padx=(5,5), pady=(5, 5))
        boton_temporadas=LtkButtonLine(frame_opciones, self.temporadas, "Temporadas")
        boton_temporadas.grid(row=9, column=0, padx=(5,5), pady=(5, 5))
        

        self.frame_caracteristicas=CTkFrame(self.ventana)
        self.frame_caracteristicas.grid(row=1, column=1, sticky="nsew")
        self.ventana.columnconfigure(1, weight=25)
        self.ventana.rowconfigure(1, weight=2)
        self.frame_caracteristicas.columnconfigure(0, weight=1)


        
        self.sueldos()
        self.horarios()
        self.usuarios()
        self.maquinas()
        self.servicios_generales()
        self.temporadas()
        self.datos_historicos()
        self.personal()
        


        frame_guardar=CTkFrame(self.ventana)
        frame_guardar.grid(row=2, column=0, columnspan=2, sticky="nsew")
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(2, weight=1)
        boton_guardar=LtkButtonFill(frame_guardar, self.guardar_informacion, "Guardar Y Salir De Configuracion Gimnasio")
        boton_guardar.grid(row=0, column=0, padx=100, pady=40, sticky="nsew")
        frame_guardar.columnconfigure(0, weight=1)
        frame_guardar.rowconfigure(0, weight=1)


        self.ventana.mainloop()


    def guardar_informacion(self):
        informacion = {
            "cantidad_recepcionistas": self.lista_personal[0][0],
            "cantidad_personal_limpieza": self.lista_personal[0][1],
            "cantidad_gerentes": self.lista_personal[0][2],
            "cantidad_entrenadores": self.lista_personal[0][3],
            "cantidad_personal_tecnico": self.lista_personal[0][4],
            "sueldo_mensual_gerente": self.lista_sueldos[0][0],
            "sueldo_mensual_entrenador": self.lista_sueldos[0][1],
            "sueldo_mensual_recepcionista": self.lista_sueldos[0][2],
            "sueldo_mensual_personal_limpieza": self.lista_sueldos[0][3],
            "sueldo_mensual_personal_tecnico": self.lista_sueldos[0][4],
            "horario_apertura": self.lista_horarios[0][0],
            "horario_cierre": self.lista_horarios[0][1],
            "capacidad_gym": self.lista_usuarios[0][0],
            "cobro_usuario": self.lista_usuarios[0][1],
            "cantidad_maquinas": self.lista_maquinas[0][0],
            "pago_mensual_luz": self.lista_servicios_generales[0][0],
            "pago_mensual_agua": self.lista_servicios_generales[0][1],
            "pago_mensual_internet": self.lista_servicios_generales[0][2],
            "pago_mensual_spotify": self.lista_servicios_generales[0][3],
            "pago_mensual_renta_local": self.lista_servicios_generales[0][4],
            "temporada_regular": self.lista_temporadas[0][0],
            "temporada_alta": self.lista_temporadas[0][1],
            "temporada_baja": self.lista_temporadas[0][2],
            "descuento_regular": self.lista_descuento[0][0],
            "descuento_alta": self.lista_descuento[0][1],
            "descuento_baja": self.lista_descuento[0][2],
            "llegada_usuarios": self.lista_llegada,
            "lapso_usuarios": self.lista_lapso,
            "duracion_gym": self.lista_duracion_gym,
            "duracion_baño": self.lista_baño,
            "lista_sexo": self.lista_sexo

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
    
        self.etiqueta_titulo_caracteristicas=LtkLabel(self.frame_caracteristicas, texto="Ajustes Del Personal")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)
        self.etiqueta_recepcion=LtkLabel(self.frame_caracteristicas, texto="Cantidad De Recepcionistas:")
        self.etiqueta_recepcion.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_recepcionistas=LtkEntryLine(self.frame_caracteristicas, "3")
        self.cantidad_recepcionistas.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_personal_limpieza=LtkLabel(self.frame_caracteristicas, texto="Cantidad Personal De limpieza:")
        self.etiqueta_personal_limpieza.grid(row=4, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_personal_limpieza=LtkEntryLine(self.frame_caracteristicas, "3")
        self.cantidad_personal_limpieza.grid(row=4, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_gerentes=LtkLabel(self.frame_caracteristicas, texto="Cantidad De Gerentes:")
        self.etiqueta_gerentes.grid(row=5, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_gerentes=LtkEntryLine(self.frame_caracteristicas, "1")
        self.cantidad_gerentes.grid(row=5, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_entrenadores=LtkLabel(self.frame_caracteristicas, texto="Cantidad De Entrenadores:")
        self.etiqueta_entrenadores.grid(row=6, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_entrenadores=LtkEntryLine(self.frame_caracteristicas, "3")
        self.cantidad_entrenadores.grid(row=6, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_personal_tecnico=LtkLabel(self.frame_caracteristicas, texto="Cantidad De Personal Tecnico Y Limpieza:")
        self.etiqueta_personal_tecnico.grid(row=7, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_personal_tecnico=LtkEntryLine(self.frame_caracteristicas, "3")
        self.cantidad_personal_tecnico.grid(row=7, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        boton_guardar=LtkButtonFill(self.frame_caracteristicas,lambda: self.guardar_ajustes(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))

    def guardar_ajustes(self):
        cantidad_recepcionistas=self.cantidad_recepcionistas.get()
        cantidad_personal_limpieza=self.cantidad_personal_limpieza.get()
        cantidad_gerentes=self.cantidad_gerentes.get()
        cantidad_entrenadores=self.cantidad_entrenadores.get()
        cantidad_personal_tecnico=self.cantidad_personal_tecnico.get()

        self.lista_personal.clear()
        self.lista_personal.append([int(cantidad_recepcionistas), 
                                    int(cantidad_personal_limpieza), 
                                    int(cantidad_gerentes), 
                                    int(cantidad_entrenadores), 
                                    int(cantidad_personal_tecnico)])
        


    def sueldos(self):
        self.resetear_frame_caracteristicas()
    
        self.etiqueta_titulo_caracteristicas=LtkLabel(self.frame_caracteristicas, texto="Ajustes Del Sueldo")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)
        self.etiqueta_sueldo_gerente=LtkLabel(self.frame_caracteristicas, texto="Sueldo Mensual Por Gerente:")
        self.etiqueta_sueldo_gerente.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.sueldo_mensual_gerente=LtkEntryLine(self.frame_caracteristicas, "4000")
        self.sueldo_mensual_gerente.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_sueldo_entrenador=LtkLabel(self.frame_caracteristicas, texto="Sueldo Mensual Por Entrenador:")
        self.etiqueta_sueldo_entrenador.grid(row=4, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.sueldo_mensual_entrenador=LtkEntryLine(self.frame_caracteristicas, "3000")
        self.sueldo_mensual_entrenador.grid(row=4, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.sueldo_mensual_recepcionista=LtkLabel(self.frame_caracteristicas, texto="Sueldo Mensual Por Recepcionista:")
        self.sueldo_mensual_recepcionista.grid(row=5, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.sueldo_mensual_recepcionista=LtkEntryLine(self.frame_caracteristicas, "2000")
        self.sueldo_mensual_recepcionista.grid(row=5, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.sueldo_mensual_personal_limpieza=LtkLabel(self.frame_caracteristicas, texto="Sueldo Mensual Por Personal De Limpieza:")
        self.sueldo_mensual_personal_limpieza.grid(row=6, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.sueldo_mensual_personal_limpieza=LtkEntryLine(self.frame_caracteristicas, "2000")
        self.sueldo_mensual_personal_limpieza.grid(row=6, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.sueldo_mensual_personal_tecnico=LtkLabel(self.frame_caracteristicas, texto="Sueldo Mensual Por Personal Tecnico:")
        self.sueldo_mensual_personal_tecnico.grid(row=7, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.sueldo_mensual_personal_tecnico=LtkEntryLine(self.frame_caracteristicas, "2000")
        self.sueldo_mensual_personal_tecnico.grid(row=7, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        
        boton_guardar=LtkButtonFill(self.frame_caracteristicas,lambda: self.guardar_ajustes1(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))


    def guardar_ajustes1(self):
        sueldo_mensual_gerente=self.sueldo_mensual_gerente.get()
        sueldo_mensual_entrenador=self.sueldo_mensual_entrenador.get()
        sueldo_mensual_recepcionista=self.sueldo_mensual_recepcionista.get()
        sueldo_mensual_personal_limpieza=self.sueldo_mensual_personal_limpieza.get()
        sueldo_mensual_personal_tecnico=self.sueldo_mensual_personal_tecnico.get()

        self.lista_sueldos.clear()
        self.lista_sueldos.append([int(sueldo_mensual_gerente), 
                                    int(sueldo_mensual_entrenador), 
                                    int(sueldo_mensual_recepcionista), 
                                    int(sueldo_mensual_personal_limpieza), 
                                    int(sueldo_mensual_personal_tecnico)])


    def horarios(self):
        self.resetear_frame_caracteristicas()

        self.etiqueta_titulo_caracteristicas=LtkLabel(self.frame_caracteristicas, texto="Ajustes De Horarios")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)
        self.etiqueta_horario_apertura=LtkLabel(self.frame_caracteristicas, texto="Horario De Apertura:") 
        self.etiqueta_horario_apertura.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.horario_apertura=LtkEntryLine(self.frame_caracteristicas, "6:00")
        self.horario_apertura.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_horario_cierre=LtkLabel(self.frame_caracteristicas, texto="Horario De Cierre:")
        self.etiqueta_horario_cierre.grid(row=4, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.horario_cierre=LtkEntryLine(self.frame_caracteristicas, "22:00")
        self.horario_cierre.grid(row=4, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        boton_guardar=LtkButtonFill(self.frame_caracteristicas,lambda: self.guardar_ajustes2(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))

    def guardar_ajustes2(self):
        horario_apertura=self.horario_apertura.get()
        horario_cierre=self.horario_cierre.get()

        self.lista_horarios.clear()
        self.lista_horarios.append([horario_apertura, 
                                    horario_cierre])


    def usuarios(self):
        self.resetear_frame_caracteristicas()

        self.etiqueta_titulo_caracteristicas=LtkLabel(self.frame_caracteristicas, texto="Ajustes De Usuarios")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)
        self.etiqueta_capacidad_gym=LtkLabel(self.frame_caracteristicas, texto="Capacidad De Usuarios En El Gimnasio:")
        self.etiqueta_capacidad_gym.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.capacidad_gym=LtkEntryLine(self.frame_caracteristicas, "200")
        self.capacidad_gym.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_cobro_usuario=LtkLabel(self.frame_caracteristicas, texto="Cobro Por Usuario:")
        self.etiqueta_cobro_usuario.grid(row=6, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cobro_usuario=LtkEntryLine(self.frame_caracteristicas, "250")
        self.cobro_usuario.grid(row=6, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)



        boton_guardar=LtkButtonFill(self.frame_caracteristicas,lambda: self.guardar_ajustes3(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))


    def guardar_ajustes3(self):
        capacidad_gym=self.capacidad_gym.get()
        cobro_usuario=self.cobro_usuario.get()

        self.lista_usuarios.clear()
        self.lista_usuarios.append([int(capacidad_gym), 
                                    int(cobro_usuario)])




    def maquinas(self):
        self.resetear_frame_caracteristicas()

        self.etiqueta_titulo_caracteristicas=LtkLabel(self.frame_caracteristicas, texto="Ajustes De Maquinas")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)
        self.etiqueta_maquinas=LtkLabel(self.frame_caracteristicas, texto="Cantidad De Maquinas:")
        self.etiqueta_maquinas.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_maquinas=LtkEntryLine(self.frame_caracteristicas, "50")
        self.cantidad_maquinas.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        boton_guardar=LtkButtonFill(self.frame_caracteristicas,lambda: self.guardar_ajustes4(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))

    def guardar_ajustes4(self):
        cantidad_maquinas=self.cantidad_maquinas.get()

        self.lista_maquinas.clear()
        self.lista_maquinas.append([int(cantidad_maquinas)])




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
        self.etiqueta_pago_mensual_spotify=LtkLabel(self.frame_caracteristicas, texto="Pago Mensual De Spotify:")
        self.etiqueta_pago_mensual_spotify.grid(row=6, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.pago_mensual_spotify=LtkEntryLine(self.frame_caracteristicas, "200")
        self.pago_mensual_spotify.grid(row=6, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.pago_mensual_renta_local=LtkLabel(self.frame_caracteristicas, texto="Pago Mensual De Renta Del Local:")
        self.pago_mensual_renta_local.grid(row=7, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.pago_mensual_renta_local=LtkEntryLine(self.frame_caracteristicas, "2000")
        self.pago_mensual_renta_local.grid(row=7, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        boton_guardar=LtkButtonFill(self.frame_caracteristicas,lambda: self.guardar_ajustes5(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))
    
    def guardar_ajustes5(self):
        pago_mensual_luz=self.pago_mensual_luz.get()
        pago_mensual_agua=self.pago_mensual_agua.get()
        pago_mensual_internet=self.pago_mensual_internet.get()
        pago_mensual_spotify=self.pago_mensual_spotify.get()
        pago_mensual_renta_local=self.pago_mensual_renta_local.get()

        self.lista_servicios_generales.clear()
        self.lista_servicios_generales.append([int(pago_mensual_luz), 
                                    int(pago_mensual_agua), 
                                    int(pago_mensual_internet),
                                    int(pago_mensual_spotify),
                                    int(pago_mensual_renta_local)])
        

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
        llegada_personas = simpledialog.askinteger("Entrada", "Renglones De Llegada Personas", minvalue=1, parent=self.frame_caracteristicas)
        lapso_llegada = simpledialog.askinteger("Entrada", "Renglones Lapso De Llegada", minvalue=1, parent=self.frame_caracteristicas)
        duracion_gym = simpledialog.askinteger("Entrada", "Renglones Duracion En GYM", minvalue=1, parent=self.frame_caracteristicas)
        tiempo_baño = simpledialog.askinteger("Entrada", "Renglones Tiempo En Baño", minvalue=1, parent=self.frame_caracteristicas)
        cantidad_genero = simpledialog.askinteger("Entrada", "Cantidad de géneros a ingresar", minvalue=1, parent=self.frame_caracteristicas)


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
        self.check_llegada = StringVar()
        self.checkbutton_llegada = Checkbutton(scrollable_frame, text="MARCA PARA USAR DATOS HISTORICOS LLEGADA", variable=self.check_llegada, onvalue="Si", offvalue="No")
        self.checkbutton_llegada.deselect()
        self.checkbutton_llegada.grid(row=current_row, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        current_row += 1

        self.entrys_llegada = []
        self.valores_llegada = []
        for i in range(llegada_personas):
            entry_llegada = LtkEntryLine(scrollable_frame, "5")
            entry_llegada.grid(row=current_row, column=0, padx=(5, 10), pady=(5, 5), sticky="nsew")
            entry = LtkEntryLine(scrollable_frame, ".15")
            entry.grid(row=current_row, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")
            self.entrys_llegada.append(entry)
            self.valores_llegada.append(entry_llegada)
            current_row += 1

        self.check_lapso = StringVar()
        self.checkbutton_lapso = Checkbutton(scrollable_frame, text="MARCA PARA USAR DATOS HISTORICOS LAPSO LLEGADA", variable=self.check_lapso, onvalue="Si", offvalue="No")
        self.checkbutton_lapso.deselect()
        self.checkbutton_lapso.grid(row=current_row, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        current_row += 1

        self.entrys_lapso = []
        self.valores_lapso = []
        for i in range(lapso_llegada):
            entry_lapso = LtkEntryLine(scrollable_frame, "5")
            entry_lapso.grid(row=current_row, column=0, padx=(5, 10), pady=(5, 5), sticky="nsew")
            entry = LtkEntryLine(scrollable_frame, ".15")
            entry.grid(row=current_row, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")
            self.entrys_lapso.append(entry)
            self.valores_lapso.append(entry_lapso)
            current_row += 1

        self.check_duracion_gym = StringVar()
        self.checkbutton_duracion_gym = Checkbutton(scrollable_frame, text="MARCA PARA USAR DATOS HISTORICOS DURACION EN GYM", variable=self.check_duracion_gym, onvalue="Si", offvalue="No")
        self.checkbutton_duracion_gym.deselect()
        self.checkbutton_duracion_gym.grid(row=current_row, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        current_row += 1

        self.entrys_duracion_gym = []
        self.valores_duracion_gym = []
        for i in range(duracion_gym):
            entry_duracion_gym = LtkEntryLine(scrollable_frame, "5")
            entry_duracion_gym.grid(row=current_row, column=0, padx=(5, 10), pady=(5, 5), sticky="nsew")
            entry = LtkEntryLine(scrollable_frame, ".15")
            entry.grid(row=current_row, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")
            self.entrys_duracion_gym.append(entry)
            self.valores_duracion_gym.append(entry_duracion_gym)
            current_row += 1

        self.check_baño = StringVar()
        self.checkbutton_baño = Checkbutton(scrollable_frame, text="MARCA PARA USAR DATOS HISTORICOS TIEMPO EN BAÑO", variable=self.check_baño, onvalue="Si", offvalue="No")
        self.checkbutton_baño.deselect()
        self.checkbutton_baño.grid(row=current_row, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        current_row += 1

        self.entrys_baño = []
        self.valores_baño = []
        for i in range(tiempo_baño):
            entry_baño = LtkEntryLine(scrollable_frame, "5")
            entry_baño.grid(row=current_row, column=0, padx=(5, 10), pady=(5, 5), sticky="nsew")
            entry = LtkEntryLine(scrollable_frame, ".15")
            entry.grid(row=current_row, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")
            self.entrys_baño.append(entry)
            self.valores_baño.append(entry_baño)
            current_row += 1

        self.check_sexo = StringVar()
        self.checkbutton_sexo = Checkbutton(scrollable_frame, text="MARCA PARA USAR DATOS HISTORICOS SEXO", variable=self.check_sexo, onvalue="Si", offvalue="No")
        self.checkbutton_sexo.deselect()
        self.checkbutton_sexo.grid(row=current_row, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        current_row += 1
        self.entrys_sexo = []
        self.valores_sexo = []
        for i in range(cantidad_genero):
            entry_sexo = LtkEntryLine(scrollable_frame, "Mujer")
            entry_sexo.grid(row=current_row, column=0, padx=(5, 10), pady=(5, 5), sticky="nsew")
            entry = LtkEntryLine(scrollable_frame, ".15")
            entry.grid(row=current_row, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")
            self.entrys_sexo.append(entry)
            self.valores_sexo.append(entry_sexo)
            current_row += 1

        def all_checkbuttons_selected():
            return (self.check_llegada.get() == "Si" and
                    self.check_lapso.get() == "Si" and
                    self.check_duracion_gym.get() == "Si" and
                    self.check_baño.get() == "Si" and
                    self.check_sexo.get() == "Si")

        def guardar_si_todo_seleccionado():
            if all_checkbuttons_selected():
                self.guardar_ajustes9(llegada_personas, lapso_llegada, duracion_gym, tiempo_baño, cantidad_genero)
            else:
                messagebox.showerror("Error", "Por favor, selecciona todos los checkbuttons antes de guardar.")

        boton_guardar = LtkButtonFill(self.frame_caracteristicas, guardar_si_todo_seleccionado, "Guardar Ajustes Y Ver Tablas")
        boton_guardar.grid(row=current_row, column=0, columnspan=2, pady=(5, 10))


    def guardar_ajustes9(self, llegada_personas, lapso_llegada, duracion_gym, tiempo_baño, cantidad_genero):
        rangos_llegada = self.calcular_rangos([float(entry.get()) for entry in self.entrys_llegada])
        rangos_lapso = self.calcular_rangos([float(entry.get()) for entry in self.entrys_lapso])
        rangos_duracion_gym = self.calcular_rangos([float(entry.get()) for entry in self.entrys_duracion_gym])
        rangos_baño = self.calcular_rangos([float(entry.get()) for entry in self.entrys_baño])
        rangos_sexo = self.calcular_rangos([float(entry.get()) for entry in self.entrys_sexo])
        
        self.lista_llegada = [(int(self.valores_llegada[i].get()), rangos_llegada[i][1]) for i in range(llegada_personas)]
        self.lista_lapso = [(int(self.valores_lapso[i].get()), rangos_lapso[i][1]) for i in range(lapso_llegada)]
        self.lista_duracion_gym = [(int(self.valores_duracion_gym[i].get()), rangos_duracion_gym[i][1]) for i in range(duracion_gym)]
        self.lista_baño = [(int(self.valores_baño[i].get()), rangos_baño[i][1]) for i in range(tiempo_baño)]
        self.lista_sexo = [(str(self.valores_sexo[i].get()), rangos_sexo[i][1]) for i in range(cantidad_genero)]

        self.tablas_llegada = [(int(self.valores_llegada[i].get()), float(self.entrys_llegada[i].get()), rangos_llegada[i][0], rangos_llegada[i][1]) for i in range(llegada_personas)]
        self.tablas_lapso = [(int(self.valores_lapso[i].get()), float(self.entrys_lapso[i].get()), rangos_lapso[i][0], rangos_lapso[i][1]) for i in range(lapso_llegada)]
        self.tablas_duracion_gym = [(int(self.valores_duracion_gym[i].get()), float(self.entrys_duracion_gym[i].get()), rangos_duracion_gym[i][0], rangos_duracion_gym[i][1]) for i in range(duracion_gym)]
        self.tablas_baño = [(int(self.valores_baño[i].get()), float(self.entrys_baño[i].get()), rangos_baño[i][0], rangos_baño[i][1]) for i in range(tiempo_baño)]
        self.tablas_sexo = [(str(self.valores_sexo[i].get()), float(self.entrys_sexo[i].get()), rangos_sexo[i][0], rangos_sexo[i][1]) for i in range(cantidad_genero)]

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

        self.insertar_tabla(treeview, "Tabla Llegada Personas", self.tablas_llegada)
        self.insertar_tabla(treeview, "Tabla Lapso Llegada", self.tablas_lapso)
        self.insertar_tabla(treeview, "Tabla Duración GYM", self.tablas_duracion_gym)
        self.insertar_tabla(treeview, "Tabla Tiempo Baño", self.tablas_baño)
        self.insertar_tabla(treeview, "Tabla Sexo", self.tablas_sexo)

    def insertar_tabla(self, treeview, nombre_tabla, datos_tabla):
        treeview.insert("", tk.END, text=nombre_tabla, values=("", "", ""))
        for valor, probabilidad, prob_acum, rango in datos_tabla:
            treeview.insert("", tk.END, text=str(valor), values=(probabilidad, prob_acum, rango))



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

