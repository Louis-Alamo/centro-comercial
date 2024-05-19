from customtkinter import *
from tkinter import messagebox, simpledialog
from componentes_graficos.LtkButton import LtkButtonFill, LtkButtonLine, LtkButtonTransparentBackground
from componentes_graficos.LtkEntry import LtkEntryLine, LtkEntryFill
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkCheckBox import LtkCheckBoxFill
from componentes_graficos.LtkComboBox import LtkComboBoxLine
from componentes_graficos.LtkTreeView import LtkFileInputTreeView
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
        self.lista_temporadas=[[0.70,True],[0.15,False],[0.15,False]]


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

        self.personal()
        self.sueldos()
        self.horarios()
        self.usuarios()
        self.mascotas()
        self.servicios_generales()
        self.inventario()
        self.temporadas()

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
            "temporada_baja": self.lista_temporadas[0][2]
            
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

    def datos_historicos():
        pass








Veterinaria()