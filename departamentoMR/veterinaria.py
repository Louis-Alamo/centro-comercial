from customtkinter import *
from tkinter import messagebox, simpledialog
from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine, LtkButtonTransparentBackground
from componentes_graficos.LtkEntry import LtkEntryLine, LtkEntryFill
from componentes_graficos.LtkLabel import LtkLabel
from tkinter import Checkbutton, StringVar
import tkinter as tk
from tkinter import ttk
import tkinter
import json
import os

class Veterinaria:
    def __init__(self):
        self.lista_personal=[[1, 2, 2]]
        self.lista_sueldos=[[4000, 3000, 3000]]
        self.lista_horarios=[["8:00", "18:00", "11:00", "12:00"]]
        self.lista_usuarios=[[10]]
        self.lista_mascotas=[[10]]
        self.lista_servicios_generales=[[300, 200, 420, 200, 2000]]
        self.lista_inventario=[[100,50,50,50,50]]
        self.lista_temporadas=[[True, 100], [False, 0], [False, 0]]
        self.lista_descuento = [[.10, .20, .05]]
        self.lista_llegada=[(0, "0.0000-0.0000"),...]
        self.lista_medicamento=[(0, "0.0000-0.0000"),...]
        self.lista_mascotas=[(0, "0.0000-0.0000"),...]
        self.lista_accesorios=[(0, "0.0000-0.0000"),...]
        self.lista_tiempo=[(0, "0.0000-0.0000"),...]


        self.ventana=CTk()
        self.ventana.title("Veterinaria")
        self.ventana.geometry("750x800+350+100")
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
        titulo=LtkLabel(frame_titulo, texto="Configuración de la Veterinaria")
        titulo.configure(font=('Poppins', 30, "bold"))
        titulo.grid(row=0, column=0, pady=(1, 1), sticky="nsew")
        frame_titulo.columnconfigure(0, weight=1)
        frame_titulo.rowconfigure(0, weight=1)

        # Frame para las opciones
        frame_opciones=CTkFrame(self.ventana)
        frame_opciones.grid(row=1, column=0, pady=(10, 10))
        self.ventana.columnconfigure(0, weight=2)
        self.ventana.rowconfigure(1, weight=1)

        boton_personal_veterinaria=LtkButtonLine(frame_opciones, self.personal, "Personal De Veterinaria")
        boton_personal_veterinaria.grid(row=0, column=0, padx=(5,5), pady=(5, 5))
        boton_sueldo=LtkButtonLine(frame_opciones, self.sueldos, "Sueldos")
        boton_sueldo.grid(row=1, column=0, padx=(5,5), pady=(5, 5))
        boton_horarios=LtkButtonLine(frame_opciones, self.horarios, "Horarios")
        boton_horarios.grid(row=2, column=0, padx=(5,5), pady=(5, 5))
        boton_usuarios=LtkButtonLine(frame_opciones, self.usuarios, "Usuarios")
        boton_usuarios.grid(row=3, column=0, padx=(5,5), pady=(5, 5))
        boton_mascotas=LtkButtonLine(frame_opciones, self.mascotas, "Mascotas")
        boton_mascotas.grid(row=4, column=0, padx=(5,5), pady=(5, 5))
        boton_servicios_generales=LtkButtonLine(frame_opciones, self.servicios_generales, "Servicios Generales")
        boton_servicios_generales.grid(row=5, column=0, padx=(5,5), pady=(5, 5))
        boton_inventario=LtkButtonLine(frame_opciones, self.inventario, "Inventario")
        boton_inventario.grid(row=6, column=0, padx=(5,5), pady=(5, 5))
        boton_temporadas=LtkButtonLine(frame_opciones, self.temporadas, "Temporadas")
        boton_temporadas.grid(row=7, column=0, padx=(5,5), pady=(5, 5))
        boton_datos_historicos=LtkButtonLine(frame_opciones, self.datos_historicos, "Datos Históricos")
        boton_datos_historicos.grid(row=8, column=0, padx=(5,5), pady=(5, 5))

        # Frame de características
        self.frame_caracteristicas = CTkFrame(self.ventana)
        self.frame_caracteristicas.grid(row=1, column=1, sticky="nsew")
        self.ventana.columnconfigure(1, weight=25)
        self.ventana.rowconfigure(1, weight=2)
        self.frame_caracteristicas.columnconfigure(0, weight=1)

        
        self.sueldos()
        self.horarios()
        self.usuarios()
        self.mascotas()
        self.servicios_generales()
        self.inventario()
        self.temporadas()
        self.personal()

        # Frame para el botón de guardar
        frame_guardar = CTkFrame(self.ventana)
        frame_guardar.grid(row=2, column=0, columnspan=2, sticky="nsew")
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(2, weight=1)
        boton_guardar = LtkButtonFill(frame_guardar, self.guardar_informacion, "Guardar Y Salir De Configuracion Veterinaria")
        boton_guardar.grid(row=0, column=0, padx=100, pady=40, sticky="nsew")
        frame_guardar.columnconfigure(0, weight=1)
        frame_guardar.rowconfigure(0, weight=1)

        self.ventana.mainloop()

    def guardar_informacion(self):
        informacion={
            "cantidad_gerentes": self.lista_personal[0][0],
            "cantidad_veterinarios": self.lista_personal[0][1],
            "cantidad_auxiliares": self.lista_personal[0][2],
            "sueldo_mensual_gerente": self.lista_sueldos[0][0],
            "sueldo_mensual_veterinario": self.lista_sueldos[0][1],
            "sueldo_mensual_auxiliares": self.lista_sueldos[0][2],
            "horario_entrada": self.lista_horarios[0][0],
            "horario_salida": self.lista_horarios[0][1],
            "horario_salida_almuerzo": self.lista_horarios[0][2],
            "horario_entrada_almuerzo": self.lista_horarios[0][3],
            "cantidad_usuarios": self.lista_usuarios[0][0],
            "cantidad_mascotas": self.lista_mascotas[0][0],
            "pago_mensual_luz": self.lista_servicios_generales[0][0],
            "pago_mensual_agua": self.lista_servicios_generales[0][1],
            "pago_mensual_internet": self.lista_servicios_generales[0][2],
            "pago_mensual_spotify": self.lista_servicios_generales[0][3],
            "pago_mensual_renta_local": self.lista_servicios_generales[0][4],
            "paquetes_alimentos": self.lista_inventario[0][0],
            "juguetes": self.lista_inventario[0][1],
            "medicamentos": self.lista_inventario[0][2],
            "vacunas": self.lista_inventario[0][3],
            "accesorios": self.lista_inventario[0][4],
            "temporada_regular": self.lista_temporadas[0][0],
            "temporada_alta": self.lista_temporadas[0][1],
            "temporada_baja": self.lista_temporadas[0][2],
            "descuento_regular": self.lista_descuento[0][0],
            "descuento_alta": self.lista_descuento[0][1],
            "descuento_baja": self.lista_descuento[0][2],
            "lista_llegada": self.lista_llegada,
            "lista_medicamento": self.lista_medicamento,
            "lista_mascotas": self.lista_mascotas,
            "lista_accesorios": self.lista_accesorios,
            "lista_tiempo": self.lista_tiempo

            
        }
        
        informacion_json=json.dumps(informacion, indent=4)
        config_path=os.path.join(self.ruta_ventana, 'veterinaria.json')

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
        self.etiqueta_gerentes = LtkLabel(self.frame_caracteristicas, texto="Cantidad De Gerentes:")
        self.etiqueta_gerentes.grid(row=1, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_gerentes = LtkEntryLine(self.frame_caracteristicas, "1")
        self.cantidad_gerentes.grid(row=1, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_veterinarios = LtkLabel(self.frame_caracteristicas, texto="Cantidad De Veterinarios:")
        self.etiqueta_veterinarios.grid(row=2, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_veterinarios = LtkEntryLine(self.frame_caracteristicas, "2")
        self.cantidad_veterinarios.grid(row=2, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_auxiliares = LtkLabel(self.frame_caracteristicas, texto="Cantidad De Auxiliares:")
        self.etiqueta_auxiliares.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_auxiliares = LtkEntryLine(self.frame_caracteristicas, "2")
        self.cantidad_auxiliares.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        
        boton_guardar = LtkButtonFill(self.frame_caracteristicas,lambda: self.guardar_ajustes(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))

    def guardar_ajustes(self):
        cantidad_gerentes=self.cantidad_gerentes.get()
        cantidad_veterinarios=self.cantidad_veterinarios.get()
        cantidad_auxiliares=self.cantidad_auxiliares.get()

        self.lista_personal.clear()
        self.lista_personal.append([int(cantidad_gerentes),
                                    int(cantidad_veterinarios),
                                    int(cantidad_auxiliares)
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
        self.etiqueta_sueldo_veterinario = LtkLabel(self.frame_caracteristicas, texto="Sueldo Mensual Por Veterinario:")
        self.etiqueta_sueldo_veterinario.grid(row=4, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.sueldo_mensual_veterinario = LtkEntryLine(self.frame_caracteristicas, "3000")
        self.sueldo_mensual_veterinario.grid(row=4, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_sueldo_auxiliares = LtkLabel(self.frame_caracteristicas, texto="Sueldo Mensual Por Auxiliar:")
        self.etiqueta_sueldo_auxiliares.grid(row=5, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.sueldo_mensual_auxiliares = LtkEntryLine(self.frame_caracteristicas, "3000")
        self.sueldo_mensual_auxiliares.grid(row=5, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        boton_guardar = LtkButtonFill(self.frame_caracteristicas,lambda: self.guardar_ajustes1(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))


    def guardar_ajustes1(self):
        sueldo_mensual_gerente=self.sueldo_mensual_gerente.get()
        sueldo_mensual_veterinario=self.sueldo_mensual_veterinario.get()
        sueldo_mensual_auxiliares=self.sueldo_mensual_auxiliares.get()

        self.lista_sueldos.clear()
        self.lista_sueldos.append([int(sueldo_mensual_gerente),
                                    int(sueldo_mensual_veterinario),
                                    int(sueldo_mensual_auxiliares)
                                   ])


    def horarios(self):
        self.resetear_frame_caracteristicas()

        self.etiqueta_titulo_caracteristicas = LtkLabel(self.frame_caracteristicas, texto="Ajustes De Horarios")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)
        self.etiqueta_horario_entrada = LtkLabel(self.frame_caracteristicas, texto="Horario De Entrada:")
        self.etiqueta_horario_entrada.grid(row=1, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.horario_entrada = LtkEntryLine(self.frame_caracteristicas, "8:00")
        self.horario_entrada.grid(row=1, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_horario_salida = LtkLabel(self.frame_caracteristicas, texto="Horario De Salida:")
        self.etiqueta_horario_salida.grid(row=2, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.horario_salida = LtkEntryLine(self.frame_caracteristicas, "18:00")
        self.horario_salida.grid(row=2, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_horario_salida_almuerzo = LtkLabel(self.frame_caracteristicas, texto="Horario De Salida Al Almuerzo:")
        self.etiqueta_horario_salida_almuerzo.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.horario_salida_almuerzo = LtkEntryLine(self.frame_caracteristicas, "11:00")
        self.horario_salida_almuerzo.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_horario_entrada_almuerzo = LtkLabel(self.frame_caracteristicas, texto="Horario De Entrada De Almuerzo:")
        self.etiqueta_horario_entrada_almuerzo.grid(row=4, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.horario_entrada_almuerzo = LtkEntryLine(self.frame_caracteristicas, "12:00")
        self.horario_entrada_almuerzo.grid(row=4, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        boton_guardar = LtkButtonFill(self.frame_caracteristicas,lambda: self.guardar_ajustes2(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))

    def guardar_ajustes2(self):
        horario_entrada=self.horario_entrada.get()
        horario_salida=self.horario_salida.get()
        horario_salida_almuerzo=self.horario_salida_almuerzo.get()
        horario_entrada_almuerzo=self.horario_entrada_almuerzo.get()

        self.lista_horarios.clear()
        self.lista_horarios.append([horario_entrada,
                                    horario_salida,
                                    horario_salida_almuerzo,
                                    horario_entrada_almuerzo
                                   ])


    def usuarios(self):
        self.resetear_frame_caracteristicas()

        self.etiqueta_titulo_caracteristicas = LtkLabel(self.frame_caracteristicas, texto="Ajustes De Horarios")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)
        self.etiqueta_cantidad_usuarios = LtkLabel(self.frame_caracteristicas, texto="Cantidad De Usuarios:")
        self.etiqueta_cantidad_usuarios.grid(row=1, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_usuarios = LtkEntryLine(self.frame_caracteristicas, "10")
        self.cantidad_usuarios.grid(row=1, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
    
    def guardar_ajustes3(self):
        cantidad_usuarios=self.cantidad_usuarios.get()
        self.lista_usuarios.clear()
        self.lista_usuarios.append([int(cantidad_usuarios)])



    def mascotas(self):
        self.resetear_frame_caracteristicas()

        self.etiqueta_titulo_caracteristicas = LtkLabel(self.frame_caracteristicas, texto="Ajustes De Horarios")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)
        self.etiqueta_cantidad_mascotas = LtkLabel(self.frame_caracteristicas, texto="Cantidad De Mascotas:")
        self.etiqueta_cantidad_mascotas.grid(row=1, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.cantidad_mascotas = LtkEntryLine(self.frame_caracteristicas, "10")
        self.cantidad_mascotas.grid(row=1, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

    def guardar_ajustes4(self):
        cantidad_mascotas=self.cantidad_mascotas.get()
        self.lista_mascotas.clear()
        self.lista_mascotas.append([int(cantidad_mascotas)])


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

    def inventario(self):
        self.resetear_frame_caracteristicas()

        self.etiqueta_titulo_caracteristicas=LtkLabel(self.frame_caracteristicas, texto="Ajustes De Servicios Generales")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)

        self.etiquetas_paquetes_alimento=LtkLabel(self.frame_caracteristicas, texto="Paquetes De Alimento:")
        self.etiquetas_paquetes_alimento.grid(row=1, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.paquetes_alimento=LtkEntryLine(self.frame_caracteristicas, "100")
        self.paquetes_alimento.grid(row=1, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_jueguetes=LtkLabel(self.frame_caracteristicas, texto="Jueguetes:")
        self.etiqueta_jueguetes.grid(row=2, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.jueguetes=LtkEntryLine(self.frame_caracteristicas, "50")
        self.jueguetes.grid(row=2, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_medicamentos=LtkLabel(self.frame_caracteristicas, texto="Medicamentos:")
        self.etiqueta_medicamentos.grid(row=3, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.medicamentos=LtkEntryLine(self.frame_caracteristicas, "50")
        self.medicamentos.grid(row=3, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_vacunas=LtkLabel(self.frame_caracteristicas, texto="Vacunas:")
        self.etiqueta_vacunas.grid(row=4, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.vacunas=LtkEntryLine(self.frame_caracteristicas, "50")
        self.vacunas.grid(row=4, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)
        self.etiqueta_accesorios=LtkLabel(self.frame_caracteristicas, texto="Accesorios:")
        self.etiqueta_accesorios.grid(row=5, column=0,padx=(10,10), pady=(5, 2), sticky="w")
        self.accesorios=LtkEntryLine(self.frame_caracteristicas, "50")
        self.accesorios.grid(row=5, column=1, padx=(5,10), pady=(5, 5), sticky="nsew",columnspan=2)

        boton_guardar=LtkButtonFill(self.frame_caracteristicas,lambda: self.guardar_ajustes6(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))

    def guardar_ajustes6(self):
        paquetes_alimento=self.paquetes_alimento.get()
        jueguetes=self.jueguetes.get()
        medicamentos=self.medicamentos.get()
        vacunas=self.vacunas.get()
        accesorios=self.accesorios.get()

        self.lista_inventario.clear()
        self.lista_inventario.append([int(paquetes_alimento), 
                                    int(jueguetes), 
                                    int(medicamentos),
                                    int(vacunas),
                                    int(accesorios)])

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

        boton_guardar = LtkButtonFill(self.frame_caracteristicas, lambda: self.guardar_ajustes7(), "Guardar Ajustes")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))


    def guardar_ajustes7(self):
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
        self.resetear_frame_caracteristicas()
        self.etiqueta_titulo_caracteristicas = LtkLabel(self.frame_caracteristicas, texto="Ajustes De Datos Historicos")
        self.etiqueta_titulo_caracteristicas.configure(font=('Poppins', 14, "bold"))
        self.etiqueta_titulo_caracteristicas.grid(row=0, column=0, columnspan=3, pady=(5, 10))
        self.frame_caracteristicas.columnconfigure(1, weight=1)
        self.frame_caracteristicas.columnconfigure(2, weight=1)

        boton_guardar = LtkButtonFill(self.frame_caracteristicas, lambda: self.pedir_datos(), "Ingresar datos")
        boton_guardar.grid(row=10, column=0, columnspan=3, pady=(5, 10))

    def pedir_datos(self):
        self.resetear_frame_caracteristicas()
        llegada_personas = simpledialog.askinteger("Entrada", "Renglones De Llegada Personas", minvalue=1, parent=self.frame_caracteristicas)
        renglones_medicamento = simpledialog.askinteger("Entrada", "Renglones Para Medicamento", minvalue=1, parent=self.frame_caracteristicas)
        renglones_mascotas = simpledialog.askinteger("Entrada", "Renglones Para Mascotas", minvalue=1, parent=self.frame_caracteristicas)
        renglones_accesorios = simpledialog.askinteger("Entrada", "Renglones Para Accesorios", minvalue=1, parent=self.frame_caracteristicas)
        tiempo_consulta= simpledialog.askinteger("Entrada", "Tiempo De Consulta", minvalue=1, parent=self.frame_caracteristicas)

        current_row = 0
        
        self.check_llegada = StringVar()
        self.checkbutton_llegada = Checkbutton(self.frame_caracteristicas, text="MARCA PARA USAR DATOS HISTORICOS LLEGADA", variable=self.check_llegada, onvalue="Si", offvalue="No")
        self.checkbutton_llegada.deselect()
        self.checkbutton_llegada.grid(row=current_row, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        current_row += 1
        self.entrys_llegada = []
        self.valores_llegada = []
        for i in range(llegada_personas):
            entry_llegada = LtkEntryLine(self.frame_caracteristicas, "5")
            entry_llegada.grid(row=current_row, column=0, padx=(5, 10), pady=(5, 5), sticky="nsew")
            entry = LtkEntryLine(self.frame_caracteristicas, ".15")
            entry.grid(row=current_row, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")
            self.entrys_llegada.append(entry)
            self.valores_llegada.append(entry_llegada)
            current_row += 1
        
        self.check_medicamento = StringVar()
        self.checkbutton_medicamento = Checkbutton(self.frame_caracteristicas, text="MARCA PARA USAR DATOS HISTORICOS MEDICAMENTO", variable=self.check_medicamento, onvalue="Si", offvalue="No")
        self.checkbutton_medicamento.deselect()
        self.checkbutton_medicamento.grid(row=current_row, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        current_row += 1
        self.entrys_medicamento = []
        self.valores_medicamento = []
        for i in range(renglones_medicamento):
            entry_medicamento = LtkEntryLine(self.frame_caracteristicas, "5")
            entry_medicamento.grid(row=current_row, column=0, padx=(5, 10), pady=(5, 5), sticky="nsew")
            entry = LtkEntryLine(self.frame_caracteristicas, "5")
            entry.grid(row=current_row, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")
            self.entrys_medicamento.append(entry)
            self.valores_medicamento.append(entry_medicamento)
            current_row += 1
        
        self.check_mascotas = StringVar()
        self.checkbutton_mascotas = Checkbutton(self.frame_caracteristicas, text="MARCA PARA USAR DATOS HISTORICOS MASCOTAS", variable=self.check_mascotas, onvalue="Si", offvalue="No")
        self.checkbutton_mascotas.deselect()
        self.checkbutton_mascotas.grid(row=current_row, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        current_row += 1
        self.entrys_mascotas = []
        self.valores_mascotas = []
        for i in range(renglones_mascotas):
            entry_mascotas = LtkEntryLine(self.frame_caracteristicas, "5")
            entry_mascotas.grid(row=current_row, column=0, padx=(5, 10), pady=(5, 5), sticky="nsew")
            entry = LtkEntryLine(self.frame_caracteristicas, "5")
            entry.grid(row=current_row, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")
            self.entrys_mascotas.append(entry)
            self.valores_mascotas.append(entry_mascotas)
            current_row += 1

        self.check_accesorios = StringVar()
        self.checkbutton_accesorios = Checkbutton(self.frame_caracteristicas, text="MARCA PARA USAR DATOS HISTORICOS ACCESORIOS", variable=self.check_accesorios, onvalue="Si", offvalue="No")
        self.checkbutton_accesorios.deselect()
        self.checkbutton_accesorios.grid(row=current_row, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        current_row += 1
        self.entrys_accesorios = []
        self.valores_accesorios = []
        for i in range(renglones_accesorios):
            entry_accesorios = LtkEntryLine(self.frame_caracteristicas, "5")
            entry_accesorios.grid(row=current_row, column=0, padx=(5, 10), pady=(5, 5), sticky="nsew")
            entry = LtkEntryLine(self.frame_caracteristicas, "5")
            entry.grid(row=current_row, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")
            self.entrys_accesorios.append(entry)
            self.valores_accesorios.append(entry_accesorios)
            current_row += 1

        self.check_tiempo = StringVar()
        self.checkbutton_tiempo = Checkbutton(self.frame_caracteristicas, text="MARCA PARA USAR DATOS HISTORICOS TIEMPO", variable=self.check_tiempo, onvalue="Si", offvalue="No")
        self.checkbutton_tiempo.deselect()
        self.checkbutton_tiempo.grid(row=current_row, column=0, padx=(10, 10), pady=(5, 2), sticky="w")
        current_row += 1
        self.entrys_tiempo = []
        self.valores_tiempo = []
        for i in range(tiempo_consulta):
            entry_tiempo = LtkEntryLine(self.frame_caracteristicas, "5")
            entry_tiempo.grid(row=current_row, column=0, padx=(5, 10), pady=(5, 5), sticky="nsew")
            entry = LtkEntryLine(self.frame_caracteristicas, "5")
            entry.grid(row=current_row, column=1, padx=(5, 10), pady=(5, 5), sticky="nsew")
            self.entrys_tiempo.append(entry)
            self.valores_tiempo.append(entry_tiempo)
            current_row += 1


        def all_checkbuttons_selected():
            if self.check_llegada.get() == "Si" and self.check_medicamento.get() == "Si" and self.check_mascotas.get() == "Si" and self.check_accesorios.get() == "Si" and self.check_tiempo.get() == "Si":
                return True
            return False
        def guardar_si_todo_seleccionado():
            if all_checkbuttons_selected():
                self.guardar_ajustes8(llegada_personas, renglones_medicamento, renglones_mascotas, renglones_accesorios, tiempo_consulta)
            else:
                messagebox.showerror("Error", "Por favor, selecciona todos los checkbuttons antes de guardar.")
            
        boton_guardar = LtkButtonFill(self.frame_caracteristicas, guardar_si_todo_seleccionado, "Guardar Ajustes Y Ver Tablas")
        boton_guardar.grid(row=current_row, column=0, columnspan=2, pady=(5, 10))

    def guardar_ajustes8(self, llegada_personas, renglones_medicamento, renglones_mascotas, renglones_accesorios, tiempo_consulta):
        rangos_llegada=self.calcular_rangos([float(entry.get()) for entry in self.valores_llegada])
        rangos_medicamento=self.calcular_rangos([float(entry.get()) for entry in self.valores_medicamento])
        rangos_mascotas=self.calcular_rangos([float(entry.get()) for entry in self.valores_mascotas])
        rangos_accesorios=self.calcular_rangos([float(entry.get()) for entry in self.valores_accesorios])
        rangos_tiempo=self.calcular_rangos([float(entry.get()) for entry in self.valores_tiempo])

        self.lista_llegada=[(int(self.valores_llegada[i].get()),rangos_llegada[i][1]) for i in range(llegada_personas)]
        self.lista_medicamento=[(int(self.valores_medicamento[i].get()),rangos_medicamento[i][1]) for i in range(renglones_medicamento)]
        self.lista_mascotas=[(int(self.valores_mascotas[i].get()),rangos_mascotas[i][1]) for i in range(renglones_mascotas)]
        self.lista_accesorios=[(int(self.valores_accesorios[i].get()),rangos_accesorios[i][1]) for i in range(renglones_accesorios)]
        self.lista_tiempo=[(int(self.valores_tiempo[i].get()),rangos_tiempo[i][1]) for i in range(tiempo_consulta)]

        self.tablas_llegada=[(int(self.valores_llegada[i].get()), float(self.entrys_llegada[i].get()), rangos_llegada[i][0], rangos_llegada[i][1]) for i in range(llegada_personas)]
        self.tablas_medicamento=[(int(self.valores_medicamento[i].get()), float(self.entrys_medicamento[i].get()), rangos_medicamento[i][0], rangos_medicamento[i][1]) for i in range(renglones_medicamento)]
        self.tablas_mascotas=[(int(self.valores_mascotas[i].get()), float(self.entrys_mascotas[i].get()), rangos_mascotas[i][0], rangos_mascotas[i][1]) for i in range(renglones_mascotas)]
        self.tablas_accesorios=[(int(self.valores_accesorios[i].get()), float(self.entrys_accesorios[i].get()), rangos_accesorios[i][0], rangos_accesorios[i][1]) for i in range(renglones_accesorios)]
        self.tablas_tiempo=[(int(self.valores_tiempo[i].get()), float(self.entrys_tiempo[i].get()), rangos_tiempo[i][0], rangos_tiempo[i][1]) for i in range(tiempo_consulta)]

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

        self.insertar_tabla(treeview, "Llegada Personas", self.tablas_llegada)
        self.insertar_tabla(treeview, "Medicamento", self.tablas_medicamento)
        self.insertar_tabla(treeview, "Mascotas", self.tablas_mascotas)
        self.insertar_tabla(treeview, "Accesorios", self.tablas_accesorios)
        self.insertar_tabla(treeview, "Tiempo", self.tablas_tiempo)
    
    def insertar_tabla(self, treeview, nombre_tabla, datos_tabla):
        treeview.insert("", tk.END, text=nombre_tabla, values=("", "", ""))
        for valor, probabilidad, prob_acum, rango in datos_tabla:
            treeview.insert("", tk.END, text=str(valor), values=(probabilidad, prob_acum, rango))








Veterinaria()