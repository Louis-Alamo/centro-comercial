from componentes_graficos.LtkComboBox import LtkComboBoxLine
from componentes_graficos.LtkEntry import LtkEntryLine
from componentes_graficos.LtkLabel import LtkLabel
from componentes_graficos.LtkButton import LtkButtonFill
from componentes_graficos.LtkCheckBox import LtkCheckBoxFill
import json

from customtkinter import *

class Centro_comercial_configuraciones:

    def __init__(self):

      self.ventana = CTk()
      self.ventana.title("Centro Comercial Configuraciones")
      self.ventana.resizable(False, False)
      self.ventana.configure(fg_color="#FFFFFF")





      self.frame_derecho = CTkFrame(self.ventana)
      self.frame_derecho.grid(row=0, column=1, padx=10, pady=20, sticky="nsew", )

      self.frame_izquierdo = CTkFrame(self.ventana, fg_color="#FFFFFF")
      self.frame_izquierdo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")


      #configuracion de horario

      self.frame_horario = CTkFrame(self.frame_izquierdo)
      self.frame_horario.pack(padx=10, pady=10, fill="x", expand=True)

      self.etiqueta_horario = LtkLabel(self.frame_horario, texto="Horario")
      self.etiqueta_horario.configure(font=("Poppins", 14, "bold"))
      self.etiqueta_horario.grid(row=0, column=0,  padx=10, pady=10, columnspan=3)

      self.etiqeuta_horarip_entrada = LtkLabel(self.frame_horario, texto="Entrada: ")
      self.etiqeuta_horarip_entrada.grid(row=1, column=0, padx=10, pady=10, sticky="w")

      self.campo_horario_entrada = LtkEntryLine(self.frame_horario, placeholder="Formato 00:00")
      self.campo_horario_entrada.grid(row=1, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

      self.etiqeuta_horario_salida = LtkLabel(self.frame_horario, texto="Salida: ")
      self.etiqeuta_horario_salida.grid(row=2, column=0, padx=10, pady=10, sticky="w")

      self.campo_horario_salida = LtkEntryLine(self.frame_horario, placeholder="Formato 00:00")
      self.campo_horario_salida.grid(row=2, column=1, padx=10, pady=10, columnspan=2, sticky="ew")



      #Configuracion capacidades
      self.frame_capacidades = CTkFrame(self.frame_izquierdo)
      self.frame_capacidades.pack(padx=10, pady=10, fill="x", expand=True)

      self.etiqueta_capacidad = LtkLabel(self.frame_capacidades, texto="Capacidades")
      self.etiqueta_capacidad.configure(font=("Poppins", 14, "bold"))
      self.etiqueta_capacidad.grid(row=0, column=0,  padx=10, pady=10, columnspan=2)

      self.etiqeuta_capacidad_general = LtkLabel(self.frame_capacidades, texto="Capacidad General: ")
      self.etiqeuta_capacidad_general.grid(row=1, column=0, padx=10, pady=10, sticky="w")

      self.capacidad_general = LtkEntryLine(self.frame_capacidades, placeholder="Capacidad General")
      self.capacidad_general.grid(row=1, column=1, padx=10, pady=10)

      self.etiqueta_capacidad_areas_descanso = LtkLabel(self.frame_capacidades, texto="Capacidad Areas Descanso: ")
      self.etiqueta_capacidad_areas_descanso.grid(row=2, column=0, padx=10, pady=10, sticky="w")

      self.capacidad_areas_descanso = LtkEntryLine(self.frame_capacidades, placeholder="Capacidad Areas Descanso")
      self.capacidad_areas_descanso.grid(row=2, column=1, padx=10, pady=10, )

      self.etiquetas_capacidad_baños = LtkLabel(self.frame_capacidades, texto="Capacidad Baños: ")
      self.etiquetas_capacidad_baños.grid(row=3, column=0, padx=10, pady=10, sticky="w")

      self.capacidad_baños = LtkEntryLine(self.frame_capacidades, placeholder="Capacidad Baños")
      self.capacidad_baños.grid(row=3, column=1, padx=10, pady=10)



      #Configuraciones adicionales

      self.politica_mascotas_variable = IntVar()

      self.etiqueta_configuraciones_adicionales = LtkLabel(self.frame_derecho, texto="Configuraciones Adicionales")
      self.etiqueta_configuraciones_adicionales.configure(font=("Poppins", 14, "bold"))
      self.etiqueta_configuraciones_adicionales.grid(row=0, column=0,  padx=10, pady=10, columnspan=2)

      self.etiqueta_frecuencias_eventos_especiales = LtkLabel(self.frame_derecho, texto="Frecuencias Eventos Especiales: ")
      self.etiqueta_frecuencias_eventos_especiales.grid(row=1, column=0, padx=10, pady=10, sticky="w")

      self.frecuencias_eventos_especiales = LtkEntryLine(self.frame_derecho, placeholder="Ingresar probabilidad")
      self.frecuencias_eventos_especiales.grid(row=1, column=1, padx=10, pady=10)

      self.etiqueta_nivel_seguridad = LtkLabel(self.frame_derecho, texto="Nivel de Seguridad: ")
      self.etiqueta_nivel_seguridad.grid(row=2, column=0, padx=10, pady=10, sticky="w")

      self.nivel_seguridad = LtkComboBoxLine(self.frame_derecho, ["Bajo", "Medio", "Alto"])
      self.nivel_seguridad.grid(row=2, column=1, padx=10, pady=10)

      self.politica_mascotas = LtkCheckBoxFill(self.frame_derecho, texto="Permitir Mascotas", variable=self.politica_mascotas_variable)
      self.politica_mascotas.grid(row=3, column=0, padx=10, pady=20, columnspan=2)


      self.boton_guardar = LtkButtonFill(self.ventana,lambda: self.guardar_configuracion(), "Guardar configuracion" )
      self.boton_guardar.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

      self.ventana.mainloop()


    def guardar_configuracion(self):
      datos = {
        "horario_apertura": str("08:00" if self.campo_horario_entrada.get_text() == "" else self.campo_horario_entrada.get_text()),
        "horario_cierre": str("20:00" if self.campo_horario_salida.get_text() == "" else self.campo_horario_salida.get_text()),
        "capacidad_maxima_clientes": int(250 if self.capacidad_general.get_text() == "" else self.capacidad_general.get_text()),
        "frecuencia_eventos_especiales": float(0.1 if self.frecuencias_eventos_especiales.get_text() == "" else self.frecuencias_eventos_especiales.get_text()),
        "tipos_eventos_especiales": ["robos", "charlas", "eventos de entretenimiento", "emergencias"],
        "nivel_seguridad": str("Bajo" if self.nivel_seguridad.get() == "" else self.nivel_seguridad.get()),
        "capacidad_areas_comunes": {
          "areas_descanso": int(50 if self.capacidad_areas_descanso.get_text() == "" else self.capacidad_areas_descanso.get_text()),
          "pasillos": "suficiente",
          "baños": int(10 if self.capacidad_baños.get_text() == "" else self.capacidad_baños.get_text())
        },
        "politicas_mascotas": int(self.politica_mascotas_variable.get())
      }

      datos_json = json.dumps(datos, indent=4)

      dir_path = os.path.dirname(os.path.abspath(__file__))
      config_path = os.path.join(dir_path, r'configuraciones\configuracion_dentro_comercial.json')

      # Escribe la cadena JSON en un archivo
      with open(config_path, 'w') as f:
        f.write(datos_json)











