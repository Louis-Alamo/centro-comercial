import os
import tabulate
from util.NumerosAleatorios import generar_aleatorio

from departamentoLG.entidades.DatosHistoricos import TablaDatosHistoricos

class TablaInventario:

    def __init__(self, path):


        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.path = os.path.join(dir_path, path)

        self.datos_archivo = self.leer_archivo()

        self.datos, self.titulos = self.clasificar_datos()
        self.calcular_probabilidad_acumulada()



    def leer_archivo(self):
        with open(self.path, 'r') as archivo:
            datos = archivo.readlines()
            return datos

    def clasificar_datos(self):
        titulos = self.datos_archivo[0].split(',')

        datos = []
        for linea in self.datos_archivo[1:]:
            datos.append(linea.strip().split(','))
        return datos, titulos

    def calcular_probabilidad_acumulada(self):
        self.titulos.append("Probabilidad acumulada")

        acumulado = 0.0
        for datos in self.datos:
            acumulado += float(datos[6])  # Convertir a flotante y sumar el último elemento
            datos.append(str(acumulado))  # Agregar el acumulado como una cadena




    def registrar_compra_venta(self, cantidad: int, producto: str):

        for datos in self.datos:
            if datos[0] == producto:
                if int(datos[1]) >= cantidad:
                    datos[1] = str(int(datos[1]) - cantidad)
                    return True

    def registrar_pedido(self, cantidad: int, producto: str):
        for datos in self.datos:
            if datos[0] == producto:
                datos[1] = str(int(datos[1]) + cantidad)
                return True

        return False

    def mostrar_tabla(self):
        print(tabulate.tabulate(self.datos, headers=self.titulos, tablefmt="simple"))



class Ventas:

    def __init__(self):

        self.registro_ventas = []
        self.dinero_total = 0
        self.numero_ventas = 0



    def registrar_venta(self, producto, cantidad, precio):
        self.registro_ventas.append((producto, cantidad, precio))


    def resultados_generales(self):
        for venta in self.registro_ventas:
            self.numero_ventas += 1
            self.dinero_total += venta[1] * venta[2]

    def mostrar_tabla_ventas(self):
        print(tabulate.tabulate(self.registro_ventas, headers=['Producto', 'Cantidad', 'Precio'], tablefmt="simple"))
        print(f"Numero de ventas: {self.numero_ventas}")
        print(f"Dinero total: {self.dinero_total}")


class Pedidos:


    def __init__(self, tabla_tiempo_espera: TablaDatosHistoricos):
        self.registro_pedidos = [] #Registro de pedidos realizados
        self.numero_pedidos = 0 #Numero de pedidos realizados
        self.pedidos_pendientes = 0 #Numero de pedidos que aun no llegan
        self.lista_pedidos_pendientes = [] #Los pedidos que aun no llegan

        self.tabla_tiempo_espera = tabla_tiempo_espera

        self.dinero_total = 0


    def realizar_pedido(self, dia, producto, cantidad, costo_producto):

        self.numero_pedidos += 1
        self.pedidos_pendientes += 1

        tiempo_entrega = self.tabla_tiempo_espera.obtener_valor(generar_aleatorio())

        self.lista_pedidos_pendientes.append((dia, producto, cantidad, tiempo_entrega, dia + tiempo_entrega, costo_producto, cantidad * costo_producto))
        self.registro_pedidos.append((dia, producto, cantidad, tiempo_entrega, dia + tiempo_entrega, costo_producto, cantidad * costo_producto))
        self.dinero_total += cantidad * costo_producto

    def mostrar_pedidos(self):
        print(tabulate.tabulate(self.registro_pedidos, headers=['Dia', 'Producto', 'Cantidad', 'Tiempo de entrega', 'Fecha de entrega', 'Costo por producto', 'Costo total'], tablefmt="simple"))
    def mostrar_resultados(self):
        print(f"Numero de pedidos: {self.numero_pedidos}")
        print(f"Numero de pedidos pendientes: {self.pedidos_pendientes}")
        print(f"Dinero total: {self.dinero_total}")




# tabla = TablaInventario(r'..\jugueteria\datos\probabilidades\Productos')
# tabla.mostrar_tabla()
#
#
# tabla.registrar_compra_venta(10, 'Munecas y figuras de accion')
# tabla.registrar_pedido(1000, 'Munecas y figuras de accion')
# tabla.mostrar_tabla()

# ventas = Ventas()
# ventas.registrar_venta('Munecas y figuras de accion', 10, 100)
# ventas.registrar_venta('Munecas y figuras de accion', 10, 100)
# ventas.registrar_venta('Munecas y figuras de accion', 10, 100)
# ventas.registrar_venta('Munecas y figuras de accion', 10, 100)
#
# ventas.resultados_generales()
# ventas.mostrar_tabla_ventas()