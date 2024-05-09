# Variables de entrada

Las variables de entrada del modelo se clasifican en las siguientes categorías:

## 1. Características del cine:

- **Cantidad de salas:** Número de salas de cine disponibles.
- **Cantidad de empleados:** Número total de empleados que trabajan en el cine.
- **Tipos de películas:** Lista de los tipos de películas que se proyectan en el cine (acción, terror, comedia, drama, infantil, otros).
- **Horario de apertura y cierre:** Horario en que el cine abre y cierra sus puertas.
- **Precio de las entradas:** Precio de las entradas de cine.

## 2. Datos históricos:

- **Días de promociones:** Días en que se realizan promociones especiales en el cine.
- **Probabilidad de compra de alimentos y bebidas:** Probabilidad de que los clientes compren alimentos o bebidas en la dulcería.
- **Probabilidad de uso del baño:** Probabilidad de que los clientes usen el baño durante su visita al cine.
- **Probabilidad de tipo de visita: ** Probabilidad de que los clientes visiten el cine por diferentes motivos (comprar entradas, comprar alimentos y bebidas, usar el baño, otros).
- **Probabilidad de eventos especiales: ** Probabilidad de que ocurran eventos especiales en el cine (estrenos, funciones especiales, etc.).
- **Probabilidad de fallos en el sistema:** Probabilidad de que ocurran fallos en el sistema (problemas técnicos, retrasos en las funciones, etc.).
- **Probabilidad de atracción:** Probabilidad de que los clientes sean atraídos al cine por factores externos (publicidad, eventos en el centro comercial, etc.).
- **Tiempo de espera en la sala:** Tiempo promedio que los clientes esperan para ingresar a una sala de cine.
- **Tiempo de limpieza entre películas:** Tiempo que se tarda en limpiar una sala de cine después de una función.
- **Duración promedio de películas:** Duración promedio de las películas por tipo (acción, terror, comedia, drama, infantil, otros).
- **Tiempo de espera en dulcería:** Tiempo promedio que los clientes esperan para ser atendidos en la dulcería.
- **Tiempo de espera en taquilla:** Tiempo promedio que los clientes esperan para ser atendidos en la taquilla.
- **Tiempo de espera en baño:** Tiempo promedio que los clientes esperan para usar un baño.


## 3. Consideraciones:

- **Operación simultánea de salas:** Máximo número de salas que pueden funcionar simultáneamente.

## 4. Edificios internos:

### a) Salas de cine:

- **Cantidad de salas:** Número de salas de cine disponibles.
- **Capacidad de las salas:** Número máximo de personas que pueden estar en una sala de cine simultáneamente.
- **Cantidad de empleados por sala:** Número de empleados asignados a cada sala de cine.


### b) Dulcería:

- **Cantidad de cajas:** Número de cajas disponibles en la dulcería.
- **Cantidad de empleados por caja:** Número de empleados asignados a cada caja de la dulcería.

### c) Taquillas:

- **Cantidad de taquillas:** Número de taquillas disponibles.
- **Cantidad de empleados por taquilla:** Número de empleados asignados a cada taquilla.

### d) Baño:

- **Cantidad de baños:** Número de baños disponibles.
- **Capacidad máxima por baño:** Número máximo de personas que pueden usar un baño simultáneamente.

# Entidades del modelo

Las entidades del modelo son los elementos que se mueven o procesan dentro del sistema. En este caso, las entidades principales son:

- **Clientes:** Representan a las personas que llegan al cine.
- **Películas:** Representan a las películas que se proyectan en el cine.

# Eventos del modelo

Los eventos del modelo son los acontecimientos que ocurren en el sistema y que modifican el estado de las entidades. Algunos ejemplos de eventos son:

- **Llegada de un cliente:** Un cliente llega al cine y se une a la cola de taquillas.
- **Compra de entrada:** Un cliente compra una entrada y se dirige a la sala de cine correspondiente.
- **Inicio de función:** Una película comienza a proyectarse en una sala de cine.
- **Finalización de función:** Una película termina de proyectarse en una sala de cine.
- **Compra de alimentos y bebidas:** Un cliente compra alimentos o bebidas en la dulcería.
- **Uso del baño:** Un cliente usa el baño.

# Lógicas de las colas

Cada punto de espera (taquillas, dulcería, baños) se representará mediante una cola. Las colas se gestionarán utilizando las siguientes lógicas:

- **Disciplina de la cola:** Primero en entrar, primero en salir (FIFO).
- **Número de servidores:** El número de empleados asignados a cada punto de espera.
- **Tiempo de servicio:** El tiempo promedio que tarda un empleado en atender a un cliente en cada punto de espera.


# Metricas de desempeño

- **Tiempo promedio de espera en taquilla:** Tiempo promedio que los clientes esperan para ser atendidos en la taquilla.
- **Tiempo promedio de espera en dulcería:** Tiempo promedio que los clientes esperan para ser atendidos en la dulcería.
- **Tiempo promedio de espera en baño:** Tiempo promedio que los clientes esperan para usar un baño.
- **Tasa de utilización de taquillas:** Porcentaje de tiempo que las taquillas están ocupadas atendiendo clientes.
- **Tasa de utilización de dulcería:** Porcentaje de tiempo que las cajas de la dulcería están ocupadas atendiendo clientes.
- **Tasa de utilización de baños:** Porcentaje de tiempo que los baños están ocupados.
- **Ingresos por venta de entradas:** Ingresos totales generados por la venta de entradas.
- **Ingresos por venta de alimentos y bebidas:** Ingresos totales generados por la venta de alimentos y bebidas.
- **Satisfacción del cliente:** Nivel de satisfacción de los clientes con el servicio recibido.


Dulceeria:
Demanda de productos.|
Tipo de productos.|
Precios|
Tiempo de servicio|
sueldo de los empleados|
descuento por promocion o dias especiales|
costos de operacion|
Inventario de productos|
costo mantenimineto y limpieza|
Tiempo de espera en la fila|
Rendimiento de los empleados(porcentaje)|
Horarios de funcionamiento


Taquilla:
Demanda de entradas.
Precio de las entradas.
Sueldo de los empleados.
Tiempo de servicio.
Tiempo de espera en la fila.
Rendimiento de los empleados(porcentaje).
Descuentos por promocion o dias especiales.
Costos de operacion.
Costos de mantenimiento y limpieza.
Numero de cajeros


Baños:
Demanda de baños.
Tiempo de espera en la fila.
Capacidad de los baños.
Costos de mantenimiento y limpieza.
Numero de baños.
Tiempo de espera de uso.
