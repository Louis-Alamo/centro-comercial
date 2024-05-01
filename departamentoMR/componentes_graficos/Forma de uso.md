# Descripcion y forma de uso de los componentes gráficos


## Archivo `LtkButton.py`

### Clase `LtkButtonFill`

#### Descripción
Representa un botón con un fondo lleno.

#### Parámetros del Constructor
- `master`: El widget padre al que pertenece el botón.
- `funcion`: La función que se ejecutará cuando se haga clic en el botón.
- `nombre_boton` (opcional): El texto que se mostrará en el botón.

#### Métodos
- `__init__(self, master, funcion, nombre_boton="LtkButtonFill")`: Inicializa el botón con las configuraciones dadas.
- `disable(self)`: Desactiva el botón y cambia su apariencia a desactivado.
- `enable(self)`: Activa el botón y cambia su apariencia a activado.




### Clase `LtkButtonLine`

#### Descripción
Representa un botón con un borde.

#### Parámetros del Constructor
- `master`: El widget padre al que pertenece el botón.
- `funcion`: La función que se ejecutará cuando se haga clic en el botón.
- `nombre_boton` (opcional): El texto que se mostrará en el botón.

#### Métodos
- `__init__(self, master, funcion, nombre_boton="LtkButtonLine")`: Inicializa el botón con las configuraciones dadas.
- `hover_on(self, event=None)`: Cambia la apariencia del botón cuando el cursor pasa por encima.
- `hover_off(self, event=None)`: Cambia la apariencia del botón cuando el cursor sale de encima.
- `disable(self)`: Desactiva el botón y cambia su apariencia a desactivado.
- `enable(self)`: Activa el botón y cambia su apariencia a activado.

---

## Archivo `LtkCheckBox.py`

### Clase `LtkCheckBoxFill`

#### Descripción
Representa una casilla de verificación con un fondo lleno.

#### Parámetros del Constructor
- `master`: El widget padre al que pertenece la casilla de verificación.
- `texto`: El texto que se mostrará junto a la casilla de verificación.
- `variable`: La variable asociada a la casilla de verificación.

#### Método
- `__init__(self, master, texto, variable)`: Inicializa la casilla de verificación con las configuraciones dadas.

---

## Archivo `LtkComboBox.py`

### Clase `LtkComboBoxFill`

#### Descripción
Representa un ComboBox con un diseño personalizado.

#### Parámetros del Constructor
- `master`: El widget padre al que pertenece el ComboBox.
- `valores`: Una lista de valores que se mostrarán en el ComboBox.

#### Métodos
- `__init__(self, master, valores)`: Inicializa el ComboBox con las configuraciones dadas.
- `disable(self)`: Desactiva el ComboBox y cambia su apariencia a desactivado.
- `enable(self)`: Activa el ComboBox y cambia su apariencia a activado.



### Clase `LtkComboBoxLine`

#### Descripción
Representa un ComboBox con un borde.

#### Parámetros del Constructor
- `master`: El widget padre al que pertenece el ComboBox.
- `valores`: Una lista de valores que se mostrarán en el ComboBox.

#### Métodos
- `__init__(self, master, valores)`: Inicializa el ComboBox con las configuraciones dadas.
- `disable(self)`: Desactiva el ComboBox y cambia su apariencia a desactivado.
- `enable(self)`: Activa el ComboBox y cambia su apariencia a activado.

---

## Archivo `LtkEntry.py`

### Clase `LtkEntryFill`

#### Descripción
Representa un campo de entrada con un fondo lleno.

#### Parámetros del Constructor
- `master`: El widget padre al que pertenece el campo de entrada.
- `placeholder` (opcional): El texto de marcador de posición que se mostrará cuando el campo esté vacío.

#### Método
- `__init__(self, master, placeholder="LtkEntryFill")`: Inicializa el campo de entrada con las configuraciones dadas.



### Clase `LtkEntryLine`

#### Descripción
Representa un campo de entrada con un borde.

#### Parámetros del Constructor
- `master`: El widget padre al que pertenece el campo de entrada.
- `placeholder` (opcional): El texto de marcador de posición que se mostrará cuando el campo esté vacío.

#### Método
- `__init__(self, master, placeholder="LtkEntryLine")`: Inicializa el campo de entrada con las configuraciones dadas.
 

---

## Archivo `LtkTextBox.py`

### Clase `LtkTextboxFill`

#### Descripción
Representa un cuadro de texto con un fondo lleno.

#### Parámetros del Constructor
- `master`: El widget padre al que pertenece el cuadro de texto.

#### Métodos
- `__init__(self, master)`: Inicializa el cuadro de texto con las configuraciones dadas.
- `get_text(self)`: Devuelve el texto actual en el cuadro de texto.
- `insertar_texto(self, texto)`: Inserta el texto dado en el cuadro de texto, reemplazando cualquier texto existente.
- `insertar_texto_final(self, texto)`: Inserta el texto dado al final del texto existente en el cuadro de texto.
- `insertar_lista(self, lista, salto_linea=False)`: Inserta una lista de elementos en el cuadro de texto, opcionalmente separados por saltos de línea.
- `insertar_lista_final(self, lista, salto_linea=False)`: Inserta una lista de elementos al final del texto existente en el cuadro de texto, opcionalmente separados por saltos de línea.
- `limpiar(self)`: Borra todo el texto del cuadro de texto.



## Formas de posicionamiento

### Posicionamiento Absoluto (`place`)

#### Descripción
Permite colocar widgets en una ubicación específica de la ventana o contenedor utilizando coordenadas x e y.

#### Parámetros
- `x`: Coordenada x del widget en relación con el lado izquierdo del contenedor.
- `y`: Coordenada y del widget en relación con la parte superior del contenedor.
- `anchor` (opcional): Especifica cómo se posiciona el widget en relación con el punto (x, y).
- `relx` (opcional): Especifica la posición relativa en el eje x del widget en relación con el tamaño del contenedor.
- `rely` (opcional): Especifica la posición relativa en el eje y del widget en relación con el tamaño del contenedor.
- `relwidth` (opcional): Especifica el ancho relativo del widget en relación con el tamaño del contenedor.
- `relheight` (opcional): Especifica la altura relativa del widget en relación con el tamaño del contenedor.

### Posicionamiento por Rejilla (`grid`)

#### Descripción
Organiza los widgets en una cuadrícula, utilizando filas y columnas.

#### Parámetros
- `row`: Número de fila en la que se colocará el widget.
- `column`: Número de columna en la que se colocará el widget.
- `sticky` (opcional): Determina cómo se expandirá el widget para llenar el espacio asignado.
- `padx` (opcional): Espacio adicional horizontal alrededor del widget.
- `pady` (opcional): Espacio adicional vertical alrededor del widget.
- `ipadx` (opcional): Espacio adicional horizontal dentro del widget.
- `ipady` (opcional): Espacio adicional vertical dentro del widget.

### Posicionamiento por Empaquetado (`pack`)

#### Descripción
Coloca widgets uno al lado del otro o uno debajo del otro, dependiendo de las opciones de empaquetado.

#### Parámetros
- `side` (opcional): Especifica en qué lado del contenedor se colocará el widget ('top', 'bottom', 'left' o 'right').
- `fill` (opcional): Determina cómo el widget se expandirá para llenar el espacio disponible ('x', 'y' o 'both').
- `expand` (opcional): Determina si el widget se expandirá para ocupar todo el espacio disponible.
- `padx` (opcional): Espacio adicional horizontal alrededor del widget.
- `pady` (opcional): Espacio adicional vertical alrededor del widget.

