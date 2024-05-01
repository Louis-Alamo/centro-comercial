## Variables de entrada:
1. **Características de la librería:**
   - **Capacidad de la librería:** Número máximo de clientes que pueden estar dentro de la librería simultáneamente.
   - **Cantidad de empleados:** Total de personal que trabaja en la librería.
   - **Categorías de libros:** Lista de categorías o géneros de libros disponibles en la librería (ficción, no ficción, literatura infantil, ciencia ficción, etc.).
   - **Horario de apertura y cierre:** Horario de funcionamiento de la librería.
   - **Rango de precios de libros:** Precios promedio de los libros vendidos en la librería.

2. **Datos históricos:**
   - **Días de eventos literarios:** Días en que se realizan eventos literarios, como presentaciones de libros, charlas con autores, clubes de lectura, etc.
   - **Tendencias de ventas:** Datos sobre las ventas pasadas que pueden ayudar a prever la demanda de ciertos tipos de libros en diferentes momentos del año.
   - **Probabilidad de compra por categoría:** Probabilidad de que los clientes compren libros de una determinada categoría.
   - **Probabilidad de costo**: Probabilidad de que los clientes compren libros de un determinado costo.
   - **Proabbilidad de que una persona se quede a leer en la libreria:** Probabilidad de que una persona que entra a la librería se quede a leer en la librería.
   - **Probabilidad de que una persona compre un libro:** Probabilidad de que una persona que entra a la librería compre un libro.
   - **Probabilidad de que una persona visite la libreria por cierto motivo:** Probabilidad de que una persona que entra a la librería lo haga por cierto motivo.
   
3. **Consideraciones:**
   - **Rotación de inventario:** Frecuencia con la que se actualiza el inventario de libros para mantener una oferta fresca y atractiva para los clientes.

4. **Edificios internos:**
   - **Áreas de exhibición:** Espacios designados para exhibir diferentes categorías de libros, como estanterías, mesas de exhibición, etc.
   - **Área de caja:** Espacio donde se realizan las transacciones de compra de libros.
   - **Espacio para eventos:** Área dedicada para eventos literarios, presentaciones de libros, clubes de lectura, etc.
   - **Zonas de lectura:** Espacios cómodos y tranquilos donde los clientes pueden sentarse y leer los libros antes de comprarlos.

## Entidades del modelo:
- **Clientes:** Personas que visitan la librería con la intención de comprar libros u otros artículos relacionados con la lectura.

## Eventos del modelo:
- **Llegada de un cliente:** Un cliente llega a la librería y se dirige a las diferentes áreas, como las áreas de exhibición de libros o el área de caja.
- **Selección y compra de libros:** Un cliente selecciona libros para comprar y completa la transacción en el área de caja.
- **Participación en eventos literarios:** Un cliente asiste a eventos programados, como presentaciones de libros o clubes de lectura.

## Lógicas de las colas:
- **Disciplina de la cola:** Primero en entrar, primero en salir (FIFO), o por preferencia del cliente (por ejemplo, clientes con membresía prioritaria).
- **Número de servidores:** Número de cajas de pago disponibles para atender a los clientes.
- **Tiempo de servicio:** Tiempo promedio que lleva procesar una transacción de compra en el área de caja.

## Métricas de desempeño:
- **Tiempo promedio de espera en caja:** Tiempo promedio que los clientes esperan para pagar en la caja.
- **Tasa de utilización de caja:** Porcentaje de tiempo que las cajas están ocupadas procesando transacciones.
- **Ingresos por venta de libros:** Ingresos totales generados por la venta de libros.
- **Satisfacción del cliente:** Nivel de satisfacción de los clientes con la experiencia de compra en la librería.
- **Tiempo que una persona tarad en la libreria:** Tiempo que una persona tarda en la librería desde que entra hasta que sale.