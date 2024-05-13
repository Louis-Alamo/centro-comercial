from customtkinter import *
import tkinter
import tabulate
from tkinter import Checkbutton, Entry, StringVar
from tkinter import messagebox, simpledialog
from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine, LtkButtonTransparentBackground
from componentes_graficos.LtkEntry import LtkEntryLine, LtkEntryFill
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkCheckBox import LtkCheckBoxFill
from componentes_graficos.LtkComboBox import LtkComboBoxLine
from componentes_graficos.LtkTreeView import LtkFileInputTreeView
import json
import tkinter as tk
from tkinter import scrolledtext
import os

class Gimnasio:
    def __init__(self):

        self.lista_personal=[[3, 3, 3, 3, 3]]
        self.lista_sueldos=[[4000, 3000, 2000, 2000, 2000]]
        self.lista_horarios=[["6:00", "22:00", 1, 15, 10, 10]]
        self.lista_usuarios=[[100, 50, 50, 750]]
        self.lista_maquinas=[[50, 20, 30]]
        self.lista_servicios_generales=[[300, 200, 420, 200, 2000]]
        self.lista_baños=[[6, 3, 3]]
        self.lista_vestidores=[[6, 3, 3]]
        self.lista_temporadas=[[0.70,True],[0.15,False],[0.15,False]]
        self.lista_atencion=[["0.05","0.05","0.10","0.15","0.25","0.25","0.15"]]
        self.lista_descompostura=[["0.15","0.20","0.30","0.20","0.15"]]

        self.ventana=CTk()
        self.ventana.title("Gimnasio")
        self.ventana.geometry("750x800+350+100")
        self.ventana.configure(bg="#FFFFFF")
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)
        self.ventana.rowconfigure(1, weight=1)

        self.ruta_ventana=os.path.dirname(os.path.abspath(__file__))
        
        # Frame para el título
        frame_titulo=CTkFrame(self.ventana)
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
        boton_baños=LtkButtonLine(frame_opciones, self.baños, "Baños")
        boton_baños.grid(row=6, column=0, padx=(5,5), pady=(5, 5))
        boton_vestidores=LtkButtonLine(frame_opciones, self.vestidores, "Vestidores")
        boton_vestidores.grid(row=7, column=0, padx=(5,5), pady=(5, 5))
        boton_temporadas=LtkButtonLine(frame_opciones, self.temporadas, "Temporadas")
        boton_temporadas.grid(row=8, column=0, padx=(5,5), pady=(5, 5))
        boton_lista_historicos=LtkButtonLine(frame_opciones, self.datos_historicos, "Datos Historicos")
        boton_lista_historicos.grid(row=9, column=0, padx=(5,5), pady=(5, 5))


        # Frame de características
        self.frame_caracteristicas=CTkFrame(self.ventana)
        self.frame_caracteristicas.grid(row=1, column=1, sticky="nsew")
        self.ventana.columnconfigure(1, weight=25)
        self.ventana.rowconfigure(1, weight=2)
        self.frame_caracteristicas.columnconfigure(0, weight=1)


        self.personal()
        self.sueldos()
        self.horarios()
        self.usuarios()
        self.maquinas()
        self.servicios_generales()
        self.baños()
        self.vestidores()
        self.temporadas()
        self.datos_historicos()
        



        # Frame para el botón de guardar
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
        informacion={
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
            "tiempo_sesion_usuarios": self.lista_horarios[0][2],
            "tiempo_uso_maquina": self.lista_horarios[0][3],
            "tiempo_uso_baño": self.lista_horarios[0][4],
            "tiempo_uso_vestidor": self.lista_horarios[0][5],
            "capacidad_gym": self.lista_usuarios[0][0],
            "cantidad_mujeres": self.lista_usuarios[0][1],
            "cantidad_hombres": self.lista_usuarios[0][2],
            "cobro_mensual_usuario": self.lista_usuarios[0][3],
            "cantidad_maquinas": self.lista_maquinas[0][0],
            "cantidad_maquinas_cardio": self.lista_maquinas[0][1],
            "cantidad_maquinas_musculacion": self.lista_maquinas[0][2],
            "pago_mensual_luz": self.lista_servicios_generales[0][0],
            "pago_mensual_agua": self.lista_servicios_generales[0][1],
            "pago_mensual_internet": self.lista_servicios_generales[0][2],
            "pago_mensual_spotify": self.lista_servicios_generales[0][3],
            "pago_mensual_renta_local": self.lista_servicios_generales[0][4],
            "cantidad_baños": self.lista_baños[0][0],
            "cantidad_baños_mujeres": self.lista_baños[0][1],
            "cantidad_baños_hombres": self.lista_baños[0][2],
            "cantidad_vestidores": self.lista_vestidores[0][0],
            "cantidad_vestidores_mujeres": self.lista_vestidores[0][1],
            "cantidad_vestidores_hombres": self.lista_vestidores[0][2],
            "temporada_regular": self.lista_temporadas[0][0],
            "temporada_alta": self.lista_temporadas[0][1],
            "temporada_baja": self.lista_temporadas[0][2],
            "atencion":[self.lista_atencion[0][0],self.lista_atencion[0][1],self.lista_atencion[0][2],self.lista_atencion[0][3],self.lista_atencion[0][4],self.lista_atencion[0][5],self.lista_atencion[0][6]],
            "descompostura":[self.lista_descompostura[0][0],self.lista_descompostura[0][1],self.lista_descompostura[0][2],self.lista_descompostura[0][3],self.lista_descompostura[0][4]]
            
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
        self.cantidad_gerentes=LtkEntryLine(self.frame_caracteristicas, "3")
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
        self.etiqueta_tiempo_sesion_usuarios=LtkLabel(self.frame_caracteristicas, texto="Tiempo Sesion De Usuarios (Horas):")
        self.etiqueta_tiempo_sesion_usuarios.grid(row=5, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.tiempo_sesion_usuarios=LtkEntryLine(self.frame_caracteristicas, "1")
        self.tiempo_sesion_usuarios.grid(row=5, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_tiempo_uso_maquina=LtkLabel(self.frame_caracteristicas, texto="Tiempo Uso De Maquina (Minutos):")
        self.etiqueta_tiempo_uso_maquina.grid(row=6, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.tiempo_uso_maquina=LtkEntryLine(self.frame_caracteristicas, "15")
        self.tiempo_uso_maquina.grid(row=6, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_tiempo_uso_baño=LtkLabel(self.frame_caracteristicas, texto="Tiempo Uso De Baño (Minutos):")
        self.etiqueta_tiempo_uso_baño.grid(row=6, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.tiempo_uso_bano=LtkEntryLine(self.frame_caracteristicas, "10")
        self.tiempo_uso_bano.grid(row=6, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_tiempo_uso_vestidor=LtkLabel(self.frame_caracteristicas, texto="Tiempo Uso De Vestidor (Minutos):")
        self.etiqueta_tiempo_uso_vestidor.grid(row=7, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.tiempo_uso_vestidor=LtkEntryLine(self.frame_caracteristicas, "10")
        self.tiempo_uso_vestidor.grid(row=7, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        boton_guardar=LtkButtonFill(self.frame_caracteristicas,lambda: self.guardar_ajustes2(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))

    def guardar_ajustes2(self):
        horario_apertura=self.horario_apertura.get()
        horario_cierre=self.horario_cierre.get()
        tiempo_sesion_usuarios=self.tiempo_sesion_usuarios.get()
        tiempo_uso_maquina=self.tiempo_uso_maquina.get()
        tiempo_uso_bano=self.tiempo_uso_bano.get()
        tiempo_uso_vestidor=self.tiempo_uso_vestidor.get()

        self.lista_horarios.clear()
        self.lista_horarios.append([horario_apertura, 
                                    horario_cierre, 
                                    int(tiempo_sesion_usuarios),
                                    int(tiempo_uso_maquina),
                                    int(tiempo_uso_bano),
                                    int(tiempo_uso_vestidor)])


    def usuarios(self):
        self.resetear_frame_caracteristicas()

        self.etiqueta_titulo_caracteristicas=LtkLabel(self.frame_caracteristicas, texto="Ajustes De Usuarios")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)
        self.etiqueta_capacidad_gym=LtkLabel(self.frame_caracteristicas, texto="Capacidad De Usuarios En El Gimnasio:")
        self.etiqueta_capacidad_gym.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.capacidad_gym=LtkEntryLine(self.frame_caracteristicas, "100")
        self.capacidad_gym.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_cantidad_mujeres=LtkLabel(self.frame_caracteristicas, texto="Cantidad De Mujeres:")
        self.etiqueta_cantidad_mujeres.grid(row=4, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_mujeres=LtkEntryLine(self.frame_caracteristicas, "50")
        self.cantidad_mujeres.grid(row=4, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_cantidad_hombres=LtkLabel(self.frame_caracteristicas, texto="Cantidad De Hombres:")
        self.etiqueta_cantidad_hombres.grid(row=5, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_hombres=LtkEntryLine(self.frame_caracteristicas, "50")
        self.cantidad_hombres.grid(row=5, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_cobro_mensual_usuario=LtkLabel(self.frame_caracteristicas, texto="Cobro Mensual Por Usuario:")
        self.etiqueta_cobro_mensual_usuario.grid(row=6, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cobro_mensual_usuario=LtkEntryLine(self.frame_caracteristicas, "750")
        self.cobro_mensual_usuario.grid(row=6, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)



        boton_guardar=LtkButtonFill(self.frame_caracteristicas,lambda: self.guardar_ajustes3(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))


    def guardar_ajustes3(self):
        capacidad_gym=self.capacidad_gym.get()
        cantidad_mujeres=self.cantidad_mujeres.get()
        cantidad_hombres=self.cantidad_hombres.get()
        cobro_mensual_usuario=self.cobro_mensual_usuario.get()

        self.lista_usuarios.clear()
        self.lista_usuarios.append([int(capacidad_gym), 
                                    int(cantidad_mujeres), 
                                    int(cantidad_hombres),
                                    int(cobro_mensual_usuario)])




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
        self.etiqueta_maquinas_cardio=LtkLabel(self.frame_caracteristicas, texto="Cantidad De Maquinas De Cardio:")
        self.etiqueta_maquinas_cardio.grid(row=4, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_maquinas_cardio=LtkEntryLine(self.frame_caracteristicas, "20")
        self.cantidad_maquinas_cardio.grid(row=4, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_maquinas_musculacion=LtkLabel(self.frame_caracteristicas, texto="Cantidad De Maquinas De Musculacion:")
        self.etiqueta_maquinas_musculacion.grid(row=5, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_maquinas_musculacion=LtkEntryLine(self.frame_caracteristicas, "30")
        self.cantidad_maquinas_musculacion.grid(row=5, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        boton_guardar=LtkButtonFill(self.frame_caracteristicas,lambda: self.guardar_ajustes4(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))

    def guardar_ajustes4(self):
        cantidad_maquinas=self.cantidad_maquinas.get()
        cantidad_maquinas_cardio=self.cantidad_maquinas_cardio.get()
        cantidad_maquinas_musculacion=self.cantidad_maquinas_musculacion.get()

        self.lista_maquinas.clear()
        self.lista_maquinas.append([int(cantidad_maquinas), 
                                    int(cantidad_maquinas_cardio), 
                                    int(cantidad_maquinas_musculacion)])




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
        


    def baños(self):
        self.resetear_frame_caracteristicas()

        self.etiqueta_titulo_caracteristicas=LtkLabel(self.frame_caracteristicas, texto="Ajustes De Baños")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)
        self.etiqueta_baños=LtkLabel(self.frame_caracteristicas, texto="Cantidad De Baños:")
        self.etiqueta_baños.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_baños=LtkEntryLine(self.frame_caracteristicas, "6")
        self.cantidad_baños.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_baños_mujeres=LtkLabel(self.frame_caracteristicas, texto="Cantidad De Baños Para Mujeres:")
        self.etiqueta_baños_mujeres.grid(row=4, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_baños_mujeres=LtkEntryLine(self.frame_caracteristicas, "3")
        self.cantidad_baños_mujeres.grid(row=4, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_baños_hombres=LtkLabel(self.frame_caracteristicas, texto="Cantidad De Baños Para Hombres:")
        self.etiqueta_baños_hombres.grid(row=5, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_baños_hombres=LtkEntryLine(self.frame_caracteristicas, "3")
        self.cantidad_baños_hombres.grid(row=5, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        boton_guardar=LtkButtonFill(self.frame_caracteristicas,lambda: self.guardar_ajustes6(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))
    
    def guardar_ajustes6(self):
        cantidad_baños=self.cantidad_baños.get()
        cantidad_baños_mujeres=self.cantidad_baños_mujeres.get()
        cantidad_baños_hombres=self.cantidad_baños_hombres.get()

        self.lista_baños.clear()
        self.lista_baños.append([int(cantidad_baños), 
                                int(cantidad_baños_mujeres), 
                                int(cantidad_baños_hombres)])




    def vestidores(self):
        self.resetear_frame_caracteristicas()
        self.etiqueta_titulo_caracteristicas=LtkLabel(self.frame_caracteristicas, texto="Ajustes De Vestidores")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)
        self.etiqueta_vestidores=LtkLabel(self.frame_caracteristicas, texto="Cantidad De Vestidores:")
        self.etiqueta_vestidores.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_vestidores=LtkEntryLine(self.frame_caracteristicas, "10")
        self.cantidad_vestidores.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_vestidores_mujeres=LtkLabel(self.frame_caracteristicas, texto="Cantidad De Vestidores Para Mujeres:")
        self.etiqueta_vestidores_mujeres.grid(row=4, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_vestidores_mujeres=LtkEntryLine(self.frame_caracteristicas, "5")
        self.cantidad_vestidores_mujeres.grid(row=4, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_vestidores_hombres=LtkLabel(self.frame_caracteristicas, texto="Cantidad De Vestidores Para Hombres:")
        self.etiqueta_vestidores_hombres.grid(row=5, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_vestidores_hombres=LtkEntryLine(self.frame_caracteristicas, "5")
        self.cantidad_vestidores_hombres.grid(row=5, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        boton_guardar=LtkButtonFill(self.frame_caracteristicas,lambda: self.guardar_ajustes7(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))
    
    def guardar_ajustes7(self):
        cantidad_vestidores=self.cantidad_vestidores.get()
        cantidad_vestidores_mujeres=self.cantidad_vestidores_mujeres.get()
        cantidad_vestidores_hombres=self.cantidad_vestidores_hombres.get()

        self.lista_vestidores.clear()
        self.lista_vestidores.append([int(cantidad_vestidores), 
                                    int(cantidad_vestidores_mujeres), 
                                    int(cantidad_vestidores_hombres)])
        



    def temporadas(self):
        self.resetear_frame_caracteristicas()
        self.etiqueta_titulo_caracteristicas=LtkLabel(self.frame_caracteristicas, texto="Ajustes De Temporadas")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)

        self.temporada_var=tkinter.IntVar()

        self.temporada_regular=tkinter.Radiobutton(self.frame_caracteristicas, text="Temporada Regular", variable=self.temporada_var, value=1)
        self.temporada_regular.grid(row=3, column=1, padx=(5, 10), pady=(5, 5), sticky="w")
        self.temporada_alta=tkinter.Radiobutton(self.frame_caracteristicas, text="Temporada Alta", variable=self.temporada_var, value=2)
        self.temporada_alta.grid(row=4, column=1, padx=(5, 10), pady=(5, 5), sticky="w")
        self.temporada_baja=tkinter.Radiobutton(self.frame_caracteristicas, text="Temporada Baja", variable=self.temporada_var, value=3)
        self.temporada_baja.grid(row=5, column=1, padx=(5, 10), pady=(5, 5), sticky="w")



        boton_guardar=LtkButtonFill(self.frame_caracteristicas, lambda: self.guardar_ajustes8(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))


    def guardar_ajustes8(self):
        seleccion=self.temporada_var.get()

        if seleccion == 1:
            temporada_regular=[0.70,True]
            temporada_alta=[0.15,False]
            temporada_baja=[0.15,False]
        elif seleccion == 2:
            temporada_regular=[0.15,False]
            temporada_alta=[0.70,True]
            temporada_baja=[0.15,False]
        elif seleccion == 3:
            temporada_regular=[0.15,False]
            temporada_alta=[0.15,False]
            temporada_baja=[0.70,True]
        else:
            temporada_regular=[0.70,True]
            temporada_alta=[0.15,False]
            temporada_baja=[0.15,False]

        self.lista_temporadas.clear()
        self.lista_temporadas.append([temporada_regular, temporada_alta, temporada_baja])


    def datos_historicos(self):
        self.resetear_frame_caracteristicas()
        self.etiqueta_titulo_caracteristicas=LtkLabel(self.frame_caracteristicas, texto="Ajustes De Datos Historicos")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)

        # Probabilidad de atención
        self.check_atencion=StringVar()
        self.checkbutton_atencion=Checkbutton(self.frame_caracteristicas, text="Ingresar datos históricos para la probabilidad de atención", variable=self.check_atencion, onvalue="Si", offvalue="No")
        self.checkbutton_atencion.deselect()
        self.checkbutton_atencion.grid(row=4, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.minutos1=LtkLabel(self.frame_caracteristicas, texto="Minutos 1:")
        self.minutos1.grid(row=5, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry1=LtkEntryLine(self.frame_caracteristicas, ".05")
        self.entry1.grid(row=5, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.minutos2=LtkLabel(self.frame_caracteristicas, texto="Minutos 2:")
        self.minutos2.grid(row=6, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry2=LtkEntryLine(self.frame_caracteristicas, ".05")
        self.entry2.grid(row=6, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.minutos3=LtkLabel(self.frame_caracteristicas, texto="Minutos 3:")
        self.minutos3.grid(row=7, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry3=LtkEntryLine(self.frame_caracteristicas, ".1")
        self.entry3.grid(row=7, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.minutos4=LtkLabel(self.frame_caracteristicas, texto="Minutos 4:")
        self.minutos4.grid(row=8, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry4=LtkEntryLine(self.frame_caracteristicas, ".15")
        self.entry4.grid(row=8, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.minutos5=LtkLabel(self.frame_caracteristicas, texto="Minutos 5:")
        self.minutos5.grid(row=9, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry5=LtkEntryLine(self.frame_caracteristicas, ".25")
        self.entry5.grid(row=9, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.minutos6=LtkLabel(self.frame_caracteristicas, texto="Minutos 6:")
        self.minutos6.grid(row=10, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry6=LtkEntryLine(self.frame_caracteristicas, ".25")
        self.entry6.grid(row=10, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.minutos7=LtkLabel(self.frame_caracteristicas, texto="Minutos 7:")
        self.minutos7.grid(row=11, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry7=LtkEntryLine(self.frame_caracteristicas, ".15")
        self.entry7.grid(row=11, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)


        # Probabilidad de descompostura de máquinas
        self.check_descompostura=StringVar()
        self.checkbutton_descompostura=Checkbutton(self.frame_caracteristicas, text="Ingresar datos históricos para la probabilidad de descompostura de máquinas", variable=self.check_descompostura, onvalue="Si", offvalue="No")
        self.checkbutton_descompostura.deselect()
        self.checkbutton_descompostura.grid(row=12, column=0, padx=(10,10), pady=(5, 2), sticky="w")

        self.maquina1=LtkLabel(self.frame_caracteristicas, texto="Maquina 1:")
        self.maquina1.grid(row=13, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_m1=LtkEntryLine(self.frame_caracteristicas, ".15")
        self.entry_m1.grid(row=13, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.maquina2=LtkLabel(self.frame_caracteristicas, texto="Maquina 2:")
        self.maquina2.grid(row=14, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_m2=LtkEntryLine(self.frame_caracteristicas, ".20")
        self.entry_m2.grid(row=14, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.maquina3=LtkLabel(self.frame_caracteristicas, texto="Maquina 3:")
        self.maquina3.grid(row=15, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_m3=LtkEntryLine(self.frame_caracteristicas, ".30")
        self.entry_m3.grid(row=15, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.maquina4=LtkLabel(self.frame_caracteristicas, texto="Maquina 4:")
        self.maquina4.grid(row=16, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_m4=LtkEntryLine(self.frame_caracteristicas, ".20")
        self.entry_m4.grid(row=16, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.maquina5=LtkLabel(self.frame_caracteristicas, texto="Maquina 5:")
        self.maquina5.grid(row=17, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.entry_m5=LtkEntryLine(self.frame_caracteristicas, ".15")
        self.entry_m5.grid(row=17, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)



        boton_guardar_y_ver=LtkButtonFill(self.frame_caracteristicas, lambda: self.guardar_ajustes9(), "Guardar Ajustes Y Ver Tablas De Probabilidad")
        boton_guardar_y_ver.grid(row=18, column=0, columnspan=3, pady=(5, 10))


    def guardar_ajustes9(self):
        if self.check_atencion.get() == "Si":
            minutos1 = self.entry1.get()
            minutos2 = self.entry2.get()
            minutos3 = self.entry3.get()
            minutos4 = self.entry4.get()
            minutos5 = self.entry5.get()
            minutos6 = self.entry6.get()
            minutos7 = self.entry7.get()

            self.lista_atencion.clear()
            self.lista_atencion.append([float(minutos1), float(minutos2), float(minutos3), float(minutos4), float(minutos5), float(minutos6), float(minutos7)])

            minutos = [minutos1, minutos2, minutos3, minutos4, minutos5, minutos6, minutos7]
            self.lista_atencion1 = {'minutos': [float(m) for m in minutos]}
        else:
            self.lista_atencion1 = {'minutos': [0.05, 0.05, 0.1, 0.15, 0.25, 0.25, 0.15]}

        self.imprimir_tabla_atencion()

        if self.check_descompostura.get() == "Si":
            maquina1 = self.entry_m1.get()
            maquina2 = self.entry_m2.get()
            maquina3 = self.entry_m3.get()
            maquina4 = self.entry_m4.get()
            maquina5 = self.entry_m5.get()

            self.lista_descompostura.clear()
            self.lista_descompostura.append([float(maquina1), float(maquina2), float(maquina3), float(maquina4), float(maquina5)])

            maquinas = [maquina1, maquina2, maquina3, maquina4, maquina5]
            self.lista_descompostura1 = {'maquinas': [float(m) for m in maquinas]}
        else:
            self.lista_descompostura1 = {'maquinas': [0.15, 0.20, 0.30, 0.20, 0.15]}


        self.imprimir_tabla_descompostura()


    

    def imprimir_tabla_atencion(self):
        ventana1 = CTkToplevel()
        ventana1.title("Tabla de Atención")
        ventana1.geometry("610x300+1100+100")
        ventana1.configure(bg="#FFFFFF")
        area_texto = scrolledtext.ScrolledText(ventana1, width=600, height=300)
        area_texto.pack()
        

        if 'minutos' in self.lista_atencion1:
            minutos = range(1, 8)
            probabilidades = self.lista_atencion1['minutos']
            probabilidad_acumulada = [sum(probabilidades[:i + 1]) for i in range(len(probabilidades))]
            datos_tabla = []
            for i in range(7):
                prob = probabilidades[i] if i < len(probabilidades) else 0.0
                acum = probabilidad_acumulada[i] if i < len(probabilidades) else probabilidad_acumulada[-1]
                rango_inicio = probabilidad_acumulada[i - 1]+0.0001 if i > 0 else 0.0
                rango_fin = acum
                datos_tabla.append([minutos[i], prob, acum, f"{rango_inicio:.4f}-{rango_fin:.4f}"])
            
            titulos_tabla = ["MINUTOS", "PROBABILIDAD", "PROBABILIDAD ACUMULADA", "RANGO"]
            tabla = tabulate.tabulate(datos_tabla, headers=titulos_tabla, tablefmt="grid")
            area_texto.insert(tk.INSERT, tabla)
        else:
            area_texto.insert(tk.INSERT, "No se ingresaron listas para la probabilidad de atención.\n")

        

    def imprimir_tabla_descompostura(self):
        ventana2 = CTkToplevel()
        ventana2.title("Tabla de Descompostura")
        ventana2.geometry("620x240+1100+450")
        ventana2.configure(bg="#FFFFFF")
        area_texto = scrolledtext.ScrolledText(ventana2, width=600, height=300)
        area_texto.pack()
        

        if 'maquinas' in self.lista_descompostura1:
            maquinas = range(1, 6)
            probabilidades = self.lista_descompostura1['maquinas']
            probabilidad_acumulada = [sum(probabilidades[:i + 1]) for i in range(len(probabilidades))]
            datos_tabla = []
            for i in range(5):
                prob = probabilidades[i] if i < len(probabilidades) else 0.0
                acum = probabilidad_acumulada[i] if i < len(probabilidades) else probabilidad_acumulada[-1]
                rango_inicio = probabilidad_acumulada[i - 1]+0.0001 if i > 0 else 0.0
                rango_fin = acum
                datos_tabla.append([maquinas[i], prob, acum, f"{rango_inicio:.4f}-{rango_fin:.4f}"])

            titulos_tabla = ["MAQUINAS", "PROBABILIDAD", "PROBABILIDAD ACUMULADA", "RANGO"]
            tabla = tabulate.tabulate(datos_tabla, headers=titulos_tabla, tablefmt="grid")
            area_texto.insert(tk.INSERT, tabla)
        else:
            area_texto.insert(tk.INSERT, "No se ingresaron listas para la probabilidad de descompostura de máquinas.\n")



Gimnasio()





