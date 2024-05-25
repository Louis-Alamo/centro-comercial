import os
import tabulate

import os


def convertir_datos(path_archivo_datos):
    """
    Convierte los datos de un archivo CSV en una lista de listas.

    Parámetros:
    -----------
    path_archivo_datos : str
        Ruta relativa del archivo que contiene los datos.

    Retorna:
    --------
    list
        Lista de listas que contiene los datos leídos del archivo.
    """
    dir_path = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(dir_path, path_archivo_datos)
    with open(ruta_archivo, 'r') as f:
        datos = [line.strip().split(',') for line in f]

    return datos


def clasificar_datos_comunes(datos):
    """
    Clasifica los datos en títulos, valores y probabilidades.

    Parámetros:
    -----------
    datos : list
        Lista de listas que contiene los datos leídos del archivo.

    Retorna:
    --------
    tuple
        Una tupla que contiene:
        - titulos (list): Lista de títulos de las columnas.
        - valores (list): Lista de valores de los datos.
        - probabilidades (list): Lista de probabilidades asociadas a los valores de los datos.
    """
    titulos = datos[0]
    valores = [str(fila[0]) for fila in datos[1:]]
    probabilidades = [str(fila[1]) for fila in datos[1:]]
    return titulos, valores, probabilidades


class TablaDatosHistoricos():
    """
    Clase para manejar y operar sobre una tabla de datos históricos con probabilidades asociadas.

    Atributos:
    ----------
    titulos : list
        Lista de títulos de las columnas de la tabla.
    valores : list
        Lista de valores de los datos.
    probabilidades : list
        Lista de probabilidades asociadas a los valores de los datos.
    probabilidad_acumulada : list
        Lista de probabilidades acumuladas calculadas a partir de las probabilidades.
    titulo_tabla : str
        Título de la tabla (opcional).
    datos : list
        Lista que agrupa valores, probabilidades y probabilidades acumuladas.
    """

    def __init__(self, ruta_archivo_datos, titulo=None):
        """
        Inicializa la clase TablaDatosHistoricos.

        Parámetros:
        -----------
        ruta_archivo_datos : str
            Ruta al archivo que contiene los datos históricos.
        titulo : str, opcional
            Título de la tabla (por defecto es None).
        """
        self.titulos, self.valores, self.probabilidades = clasificar_datos_comunes(convertir_datos(ruta_archivo_datos))
        self.probabilidad_acumulada = self.calcular_probabilidad_acumulada()
        self.titulos.append("Probabilidad Acumulada")
        self.titulo_tabla = titulo
        self.datos = [self.valores, self.probabilidades, self.probabilidad_acumulada]

    def calcular_probabilidad_acumulada(self):
        """
        Calcula la probabilidad acumulada a partir de las probabilidades individuales.

        Retorna:
        --------
        list
            Lista de probabilidades acumuladas.
        """
        prob_acumulada = []
        acumulado = 0
        for probabilidad in self.probabilidades:
            acumulado += float(probabilidad)
            prob_acumulada.append(acumulado)
        return prob_acumulada

    def obtener_valor(self, aleatorio):
        """
        Obtiene el valor correspondiente a un número aleatorio dado según la probabilidad acumulada.

        Parámetros:
        -----------
        aleatorio : float
            Número aleatorio para el cual se desea encontrar el valor correspondiente.

        Retorna:
        --------
        any
            Valor correspondiente al número aleatorio proporcionado o None si no se encuentra.
        """
        for i, probabilidad in enumerate(self.probabilidad_acumulada):
            if aleatorio <= probabilidad:
                return self.valores[i]
        return None

    def mostrar_tabla(self):
        """
        Muestra la tabla de datos con sus títulos, valores, probabilidades y probabilidades acumuladas.
        """
        # Preparar los datos para la tabla
        filas = [list(fila) for fila in zip(*self.datos)]
        # Insertar los títulos de las columnas al principio
        filas.insert(0, self.titulos)

        # Mostrar la tabla
        print(self.titulo_tabla)
        print(tabulate.tabulate(filas, headers="firstrow", tablefmt="simple"))

    # Métodos get de la clase
    def get_titulos(self):
        """
        Obtiene los títulos de las columnas de la tabla.

        Retorna:
        --------
        list
            Lista de títulos de las columnas.
        """
        return self.titulos

    def get_valores(self):
        """
        Obtiene los valores de los datos de la tabla.

        Retorna:
        --------
        list
            Lista de valores de los datos.
        """
        return self.valores

    def get_probabilidades(self):
        """
        Obtiene las probabilidades asociadas a los valores de los datos.

        Retorna:
        --------
        list
            Lista de probabilidades.
        """
        return self.probabilidades





#import random

#ruta = r'..\\jugueteria\\datos\\lineas de espera\\Tiempo de realizacion servicio'
#tabla = TablaDatoshistoricos(ruta, titulo="Tiempo de realizacion servicio")
#tabla.mostrar_tabla()

#aleatorio = random.random()
#print(f"Valor aleatorio: {aleatorio}")
#valor = tabla.obtener_valor(aleatorio)
#print(f"Valor obtenido: {valor}")

