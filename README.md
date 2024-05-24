# centro-comercial
Programa en interfaz grafica que simulara un centro comercial y simulara como se comporta en diferentes situaciones del año


### Librerias necesarias

- customtkinter
- tkinter
- Pillow
- tabulate
- numpy
- scipy


## Consideraciones del codigo o de los programas

- La entidad principal de simulacion manejara los datos de los siguiente manera:
  - Manejara los dias como valores enteros es decir 250 cae en un septiembre (lo pueden considerar en su codigo para los dias de afluencia o de atraccion de clientes).
  - Los dias seran las cantidades de simulaciones.
  - IMPORTANTE: La logica debe estar separada de la interfaz es decir, interfaz aparte, pueden considerar guardar los resultados de la simulacion en un archivo y luego en la interfaz extraerlos de ese archivo, esto con la finalidad de realizar simulaciones simultaneas y no aparescan las ventanas inecesarias y que solo se abra la ventana de resultados cuando se pulse un boton.
  - En el constructor de su logica de negocio recibiran la cantidad de dias y de personas a recibir(como valores enteros).
  - La probabilidad de atraccion de clientes deberan guardarla en un archivo o si ya tienen uno existente decirme cual es y como obtenerlo (que el valor sea en decimal). Esto con la finalidad de sacar probabilidad acumulada y rangos para asignar la cantidad de clientes a cada departamento.
  - Existen funciones en la carpeta util talvez ya tenga algo que necesiten como aleatorios.

  

