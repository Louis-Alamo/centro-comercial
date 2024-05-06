## Variables de entrada:
1. **Características de la tienda de electrónica:**
   - **Capacidad de la tienda:** Número máximo de clientes que pueden estar dentro de la tienda simultáneamente.
   - **Cantidad de empleados:** Total de personal que trabaja en la tienda, incluyendo vendedores, técnicos de servicio, personal de atención al cliente, etc.
   - **Categorías de productos:** Lista de categorías de productos electrónicos disponibles en la tienda (televisores, teléfonos inteligentes, computadoras, electrodomésticos, etc.).
   - **Horario de apertura y cierre:** Horario de funcionamiento de la tienda.


2. **Datos históricos:**
   - **Días de ofertas especiales:** Días en que se realizan ofertas especiales o promociones en la tienda.
   - **Tendencias de ventas:** Datos sobre los productos más vendidos y las preferencias de los clientes en diferentes momentos del día o días de la semana.
   - **Tiempo de reparación de productos:** Tiempo promedio que lleva reparar productos en el servicio técnico.
   - **Probabilidad de compra de productos:** Probabilidad de que los clientes compren productos electrónicos en la tienda.
   - **Probabilidad de uso del servicio técnico:** Probabilidad de que los clientes utilicen el servicio técnico para reparar productos.
   - **Rango de precios de productos:** Precios promedio de los productos ofrecidos en la tienda.
   - **Rango de precios de servicios:** Precios promedio de los servicios de reparación y mantenimiento ofrecidos en la tienda.
   
3. **Consideraciones:**
   - **Rotación de inventario:** Frecuencia con la que se actualiza el inventario de productos para ofrecer las últimas novedades y tecnologías.
   - **Espacio de exhibición:** Distribución del espacio de la tienda para optimizar la presentación de productos y la comodidad de los clientes.

4. **Edificios internos:**
   - **Área de exhibición:** Espacio dedicado para exhibir los productos disponibles en la tienda.
   - **Área de servicio técnico:** Espacio donde se realizan las reparaciones y mantenimiento de productos.
   - **Área de caja:** Espacio donde se realizan las transacciones de compra de productos.

## Entidades del modelo:
- **Clientes:** Personas que visitan la tienda con la intención de comprar productos electrónicos o solicitar servicios de reparación.

## Eventos del modelo:
- **Llegada de un cliente:** Un cliente llega a la tienda y se dirige a la exhibición de productos o al área de servicio técnico.
- **Consulta y compra de productos:** Un cliente consulta y compra productos electrónicos en la tienda.
- **Solicitud de reparación:** Un cliente solicita reparación o mantenimiento para un producto.
- **Servicio técnico:** Los técnicos de servicio realizan reparaciones o mantenimiento en los productos solicitados.

## Lógicas de las colas:
- **Disciplina de la cola:** Primero en entrar, primero en salir (FIFO) para la atención al cliente y la reparación de productos.
- **Número de servidores:** Número de vendedores y técnicos de servicio disponibles para atender a los clientes y reparar productos.
- **Tiempo de servicio:** Tiempo promedio que lleva atender a un cliente desde su llegada hasta que se va de la tienda o se completa la reparación.

## Métricas de desempeño:
- **Tiempo promedio de espera:** Tiempo promedio que los clientes esperan desde su llegada hasta que son atendidos o se completa la reparación de su producto.
- **Tasa de ocupación de vendedores:** Porcentaje de tiempo que los vendedores están ocupados atendiendo a los clientes.
- **Tasa de utilización del servicio técnico:** Porcentaje de tiempo que los técnicos de servicio están ocupados reparando productos.
- **Ingresos por ventas:** Ingresos totales generados por la venta de productos.
- **Satisfacción del cliente:** Nivel de satisfacción de los clientes con la experiencia de compra y el servicio técnico recibido en la tienda de electrónica.
