import os
import tabulate
import json
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

    def obtener_precio_producto(self, producto: str):
        for datos in self.datos:
            if datos[0] == producto:
                return float(datos[3])
    def obtener_producto(self, numero_aleatorio: float):
        for datos in self.datos:
            if float(datos[7]) >= numero_aleatorio:
                return datos[0]

    def obtener_cantidad_reorden(self, producto: str):
        for datos in self.datos:
            if datos[0] == producto:
                return int(datos[5])
    def obtener_stock_minimo(self, producto: str):
        for datos in self.datos:
            if datos[0] == producto:
                return int(datos[4])
    def obtener_costo_compra(self, producto: str):
        for datos in self.datos:
            if datos[0] == producto:
                return float(datos[2])
    def registrar_compra_venta(self, producto: str,cantidad: int = 1):

        for datos in self.datos:
            if datos[0] == producto:
                if int(datos[1]) >= cantidad:
                    datos[1] = str(int(datos[1]) - cantidad)
                    return True
        return False

    def registrar_pedido(self, cantidad: int, producto: str):
        for datos in self.datos:
            if datos[0] == producto:
                datos[1] = str(int(datos[1]) + cantidad)
                return True

        return False

    def comprobar_stock(self,producto: str,  cantidad: int = 1):
        for datos in self.datos:
            if datos[0] == producto:
                if int(datos[1]) >= cantidad:
                    return True

        return False

    def comprobar_stock_minimo(self, producto):

        for datos in self.datos:
            if datos[0] == producto:
                if int(datos[1]) <= int(datos[4]):
                    return True

        return False

    def mostrar_tabla(self):
        print(tabulate.tabulate(self.datos, headers=self.titulos, tablefmt="simple"))

    def get_nombres_productos(self):
        lista_productos = []
        for datos in self.datos:
            lista_productos.append(datos[0])

        return lista_productos



class Ventas:
    def __init__(self, tabla_inventario: TablaInventario):
        self.contador_dias = 1
        self.registro_ventas = []
        self.dinero_total = 0
        self.numero_ventas = 0
        self.registro_ventas_diaria = []
        self.tabla_inventario = tabla_inventario

        self.registro_total = {
            "dias": {}
        }

    def registrar_venta(self, numero_persona, producto, cantidad=1):
        self.registro_ventas_diaria.append((numero_persona, producto, cantidad, self.tabla_inventario.obtener_precio_producto(producto)))

    def mostrar_tabla_ventas(self):
        print(tabulate.tabulate(self.registro_ventas_diaria, headers=['Numero persona', 'Producto', 'Cantidad', 'Precio'], tablefmt="simple"))
        dinero_total = 0

        for i in range(len(self.registro_ventas_diaria)):
            dinero_total += self.registro_ventas_diaria[i][3]

        print(f"Dinero total: {dinero_total}")
        print(f"Numero de ventas: {len(self.registro_ventas_diaria)}")

    def contar_productos_vendidos(self):
        #print("PRODUCTOS VENDIDOS")

        lista_productos = self.tabla_inventario.get_nombres_productos()
        lista_cantidad_comprados = [0] * len(lista_productos)

        for i in range(len(self.registro_ventas_diaria)):
            producto = self.registro_ventas_diaria[i][1]
            cantidad = self.registro_ventas_diaria[i][2]
            indice = lista_productos.index(producto)
            lista_cantidad_comprados[indice] += cantidad

        productos_cantidad = list(zip(lista_productos, lista_cantidad_comprados))
        #print(tabulate.tabulate(productos_cantidad, headers=['Producto', 'Cantidad'], tablefmt="simple"))

        return productos_cantidad

    def cierre_dia(self):

        dinero_total = 0

        for i in range(len(self.registro_ventas_diaria)):
            dinero_total += self.registro_ventas_diaria[i][3]


        self.dinero_total += dinero_total


        lista_productos_vendidos = self.contar_productos_vendidos()
        self.registro_ventas.append(self.registro_ventas_diaria)

        self.registro_total["dias"][f"Dia {self.contador_dias}"] = {
            "Productos vendidos": lista_productos_vendidos,
            "Dinero total": dinero_total,
            "Numero de ventas": len(self.registro_ventas_diaria)
        }

        # Reiniciamos las variables para el próximo día
        self.numero_ventas = 0
        self.registro_ventas_diaria = []
        self.contador_dias += 1


    def cierre_total(self):
        pass

    def guardar_informacion_json(self, nombre = "Ventas"):
        with open(f'{nombre}.json', 'w') as archivo:
            json.dump(self.registro_total, archivo, indent=4)  # Indentación para legibilidad


class Pedidos:
    def __init__(self, tabla_tiempo_espera: TablaDatosHistoricos):
        self.registro_pedidos = []  # Registro de pedidos realizados
        self.numero_pedidos = 0  # Numero de pedidos realizados
        self.pedidos_pendientes = 0  # Numero de pedidos que aun no llegan
        self.lista_pedidos_pendientes = []  # Los pedidos que aun no llegan
        self.tabla_tiempo_espera = tabla_tiempo_espera

        self.dinero_total = 0

        self.registro_total = {
            "Pedidos": {},
            "Numero de pedidos": self.numero_pedidos,
            "Dinero total": self.dinero_total
        }

    def pedido_por_entregar(self, dia):
        lista_pedidos_entregar = []
        for pedido in self.lista_pedidos_pendientes:
            if pedido[4] == dia:
                lista_pedidos_entregar.append(pedido)
                self.pedidos_pendientes -= 1
                self.lista_pedidos_pendientes.remove(pedido)

        return lista_pedidos_entregar

    def realizar_pedido(self, dia: int, producto, cantidad, costo_producto):
        self.numero_pedidos += 1
        self.pedidos_pendientes += 1

        tiempo_entrega = int(self.tabla_tiempo_espera.obtener_valor(generar_aleatorio()))

        pedido = (dia, producto, cantidad, tiempo_entrega, dia + tiempo_entrega, costo_producto, cantidad * costo_producto)
        self.lista_pedidos_pendientes.append(pedido)
        self.registro_pedidos.append(pedido)
        self.dinero_total += cantidad * costo_producto

        self.registro_total["Pedidos"][f"Pedido {self.numero_pedidos}"] = {
            "Producto": producto,
            "Cantidad": cantidad,
            "Costo por producto": costo_producto,
            "Costo total": cantidad * costo_producto,
            "Dia de pedido": dia,
            "Tiempo de entrega": tiempo_entrega,
            "Fecha de entrega": dia + tiempo_entrega
        }

    def mostrar_pedidos(self):
        print(tabulate.tabulate(self.registro_pedidos, headers=['Dia', 'Producto', 'Cantidad', 'Tiempo de entrega', 'Fecha de entrega', 'Costo por producto', 'Costo total'], tablefmt="simple"))

    def mostrar_pedidos_pendientes(self):
        print(tabulate.tabulate(self.lista_pedidos_pendientes, headers=['Dia', 'Producto', 'Cantidad', 'Tiempo de entrega', 'Fecha de entrega', 'Costo por producto', 'Costo total'], tablefmt="simple"))

    def mostrar_resultados(self):
        print(f"Numero de pedidos: {self.numero_pedidos}")
        print(f"Numero de pedidos pendientes: {self.pedidos_pendientes}")
        print(f"Dinero total: {self.dinero_total}")

    def guardar_datos_json(self, nombre_archivo = "Pedidos"):
        with open(f'{nombre_archivo}.json', 'w') as archivo:
            json.dump(self.registro_total, archivo, indent=4)  # Indentación para legibilidad





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