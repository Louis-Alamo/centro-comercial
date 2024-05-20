import os
import tabulate


def convertir_datos(path_archivo_datos):
    dir_path = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(dir_path, path_archivo_datos)
    with open(ruta_archivo, 'r') as f:
        datos = [line.strip().split(',') for line in f]

    return datos

def clasificar_datos_comunes(datos):
    titulos = datos[0]
    valores = [float(fila[0]) for fila in datos[1:]]
    probabilidades = [float(fila[1]) for fila in datos[1:]]
    return titulos, valores, probabilidades



    

class TablaDatoshistoricos():

    def __init__(self,ruta_archivo_datos, titulo = None):

        self.titulos, self.valores, self.probabilidades = clasificar_datos_comunes(convertir_datos(ruta_archivo_datos))



        self.probabilidad_acumulada = self.calcular_probabilidad_acumulada()
        self.titulos.append("Probabilidad Acumulada")

        self.titulo_tabla = titulo

        self.datos = [self.valores, self.probabilidades, self.probabilidad_acumulada]

    def calcular_probabilidad_acumulada(self):
        prob_acumulada = []
        acumulado = 0
        for probabilidad in self.probabilidades:
            acumulado += probabilidad
            prob_acumulada.append(acumulado)

        self.titulos.append('Probabilidad Acumulada')
        return prob_acumulada



    def obtener_valor(self, aleatorio):
        for i, probabilidad in enumerate(self.probabilidad_acumulada):
            if aleatorio <= probabilidad:
                return self.valores[i]
        return None

    def mostrar_tabla(self):
        # Preparar los datos para la tabla
        filas = [list(fila) for fila in zip(*self.datos)]
        # Insertar los títulos de las columnas al principio
        filas.insert(0, self.titulos)
        
        # Mostrar la tabla
        print(self.titulo_tabla)
        print(tabulate.tabulate(filas, headers="firstrow", tablefmt="simple"))


    #Metodos get de la clase
    def get_titulos(self):
        return self.titulos

    def get_valores(self):
        return self.valores

    def get_probabilidades(self):
        return self.probabilidades
    






import random

ruta = r'..\\jugueteria\\datos\\lineas de espera\\Tiempo de espera por caja'
tabla = TablaDatoshistoricos(ruta, titulo="Tiempo de espera por caja")
tabla.mostrar_tabla()

#aleatorio = random.random()
#print(f"Valor aleatorio: {aleatorio}")
#valor = tabla.obtener_valor(aleatorio)
#print(f"Valor obtenido: {valor}")

