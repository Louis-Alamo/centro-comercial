## Variables de entrada:
1. **Características del restaurante:**
   - **Capacidad del restaurante:** Número máximo de clientes que pueden estar dentro del restaurante simultáneamente.
   - **Cantidad de empleados:** Total de personal que trabaja en el restaurante, incluyendo cocineros, camareros, personal de limpieza, etc.
   - **Tipo de cocina:** Tipo de cocina que ofrece el restaurante (italiana, mexicana, asiática, etc.).
   - **Horario de apertura y cierre:** Horario de funcionamiento del restaurante.
   - **Precio promedio de los platos:** Rango de precios de los platos ofrecidos en el restaurante.
   - **Cantidad de mesas:** Número total de mesas disponibles en el restaurante.
   - **Capacidad de las mesas:** Número máximo de personas que pueden sentarse en cada mesa.
   - **Capacidad de empleados en la cocina:** Número máximo de cocineros que pueden trabajar simultáneamente en la cocina.
   - **Capacidad de empleados en el salón:** Número máximo de camareros que pueden atender a los clientes en el salón.
   - **Capacidad de empleados en el bar:** Número máximo de bartenders que pueden atender a los clientes en el bar.
   - **Capacidad de empleados en caja:** Número máximo de cajeros que pueden atender a los clientes en la caja.
   - 
2. **Datos históricos:**
   - **Días de mayor afluencia:** Días de la semana o eventos especiales en los que el restaurante experimenta una mayor afluencia de clientes.
   - **Tiempo de preparación de platos:** Tiempo promedio que lleva preparar cada tipo de plato en la cocina.
   - **Tendencias de pedido:** Datos sobre los platos más populares y las preferencias de los clientes en diferentes momentos del día o días de la semana.

3. **Consideraciones:**
   - **Rotación de mesas:** Velocidad con la que las mesas se desocupan y se pueden asignar a nuevos clientes.

4. **Edificios internos:**
   - **Área de cocina:** Espacio dedicado para la preparación de alimentos.
   - **Salón:** Espacio donde se ubican las mesas y sillas para los clientes.
   - **Área de bar:** Espacio para preparar y servir bebidas alcohólicas y no alcohólicas.
   - **Caja:** Espacio para realizar el pago de la cuenta y recibir el cambio.
   - 
## Entidades del modelo:
- **Clientes:** Personas que visitan el restaurante con la intención de comer.

## Eventos del modelo:
- **Llegada de un cliente:** Un cliente llega al restaurante y se le asigna una mesa disponible.
- **Pedido de comida:** Un cliente realiza un pedido de comida al camarero.
- **Preparación de platos:**: Los cocineros preparan los platos pedidos en la cocina.
- **Servicio de comida:** Los camareros llevan los platos preparados a las mesas de los clientes.
- **Pago de la cuenta:** Los clientes realizan el pago de su comida en la caja o al camarero.

## Lógicas de las colas:
- **Disciplina de la cola:** Primero en entrar, primero en salir (FIFO) para la asignación de mesas y preparación de platos.
- **Número de servidores:** Número de camareros y cocineros disponibles para atender a los clientes y preparar los platos.
- **Tiempo de servicio:** Tiempo promedio que lleva atender a un cliente desde su llegada hasta que se va del restaurante.

## Métricas de desempeño:
- **Tiempo promedio de espera:** Tiempo promedio que los clientes esperan desde su llegada hasta que son atendidos y reciben su comida.
- **Tasa de ocupación de mesas:** Porcentaje de tiempo que las mesas del restaurante están ocupadas por clientes.
- **Ingresos por ventas:** Ingresos totales generados por la venta de alimentos y bebidas.
- **Satisfacción del cliente:** Nivel de satisfacción de los clientes con la experiencia gastronómica y el servicio recibido en el restaurante.
