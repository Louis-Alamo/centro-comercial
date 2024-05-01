from tkinter import NO, Toplevel
from tkinter.ttk import *

class LtkUserInputTreeView(Treeview):
    """Clase para crear un árbol de vista con entrada de usuario."""

    def __init__(self, master, columnas, filas):
        """Inicializa el árbol de vista.

        Args:
            master: El widget contenedor.
            columnas: Una lista de nombres de columnas.
            filas: Una lista de listas que contiene los valores de las filas.
        """
        super().__init__(master)

        self.columnas = columnas
        self.filas = filas

        self.configurar_columnas()
        self.configurar_filas()

    def configurar_columnas(self):
        """Configura las columnas del árbol de vista."""
        self.column('#0', width=0, stretch=NO)  # Ocultar la columna 0
        self['columns'] = [str(i) for i in range(1, len(self.columnas) + 1)]  # Definir las columnas
        for i, columna in enumerate(self.columnas, start=1):
            self.column(str(i), width=100)
            self.heading(str(i), text=columna)

    def configurar_filas(self):
        """Configura las filas del árbol de vista."""
        for i, fila in enumerate(self.filas):
            self.insert('', 'end', values=fila)


class LtkFileInputTreeView(Treeview):
    """Clase para crear un árbol de vista con entrada de archivo."""

    def __init__(self, master, path):
        """Inicializa el árbol de vista con información de archivo.

        Args:
            master: El widget contenedor.
            path: La ruta al archivo que contiene la información.
        """
        super().__init__(master)
        self.path = path

        self.columnas, self.filas = self.cargar_informacion()
        self.configurar_columnas()
        self.configurar_filas()

        self.bind('<Double-1>', self.on_double_click)  # Vincula el evento de doble clic a la función on_double_click

    def configurar_columnas(self):
        """Configura las columnas del árbol de vista."""
        self.column('#0', width=0, stretch=NO)  # Ocultar la columna 0
        self['columns'] = [str(i) for i in range(1, len(self.columnas) + 1)]  # Definir las columnas
        for i, columna in enumerate(self.columnas, start=1):
            self.column(str(i), width=100)  # Configurar el ancho de la columna
            self.heading(str(i), text=columna)  # Configurar el encabezado de la columna

    def configurar_filas(self):
        """Configura las filas del árbol de vista."""
        for i, fila in enumerate(self.filas):
            self.insert('', 'end', values=fila)  # Insertar la fila en la tabla

    def cargar_informacion(self):
        """Carga la información desde un archivo."""
        with open(self.path, 'r') as f:
            lines = f.readlines()
            columnas = lines[0].strip().split(',')
            filas = [line.strip().split(',') for line in lines[1:]]
        return columnas, filas

    def setPath(self, path):
        """Establece una nueva ruta de archivo."""
        self.path = path
        self.columnas, self.filas = self.cargar_informacion()
        self.configurar_columnas()
        self.configurar_filas()

    def on_double_click(self, event):
        """Maneja el evento de doble clic en una fila."""
        item = self.selection()[0]  # Obtiene el elemento seleccionado
        fila = self.item(item)['values']  # Obtiene los valores de la fila seleccionada
        columna = self.identify_column(event.x)  # Identifica la columna en la que se hizo doble clic

        # Crea una ventana emergente para editar el valor
        edit_window = Toplevel(self)
        edit_window.title("Editar valor")

        # Crea un campo de entrada y lo llena con el valor actual
        entry = Entry(edit_window)
        entry.insert(0, fila[int(columna[1:]) - 1])
        entry.pack()

        # Crea un botón que actualiza el valor cuando se hace clic en él
        button = Button(edit_window, text="Actualizar", command=lambda: self.update_value(item, int(columna[1:]) - 1, entry.get()))
        button.pack()

    def update_value(self, item, columna, valor):
        """Actualiza el valor de una celda."""
        fila = self.item(item)['values']  # Obtiene los valores de la fila seleccionada
        fila[columna] = valor  # Actualiza el valor en la columna especificada
        self.item(item, values=fila)  # Actualiza los valores de la fila en la tabla

    def guardar_informacion(self):
        """Guarda la información en el archivo."""
        with open(self.path, 'w') as f:
            # Escribe los nombres de las columnas en el archivo
            f.write(','.join(self.columnas) + '\n')

            # Recorre todas las filas de la tabla
            for child in self.get_children():
                # Obtiene los valores de la fila
                fila = self.item(child)['values']

                # Escribe los valores de la fila en el archivo
                f.write(','.join(str(valor) for valor in fila) + '\n')


