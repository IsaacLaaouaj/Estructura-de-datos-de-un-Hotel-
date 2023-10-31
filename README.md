# Estructura de datos de un Hotel (Actividad de Algoritmos y Estructuras de Datos)
Tabla de hash para la estrucutura de datos de un hotel. Empecé configurando los siguientes procesos:

1. **Reservar una habitación**: Permití agregar una reserva indicando el nombre del cliente, la fecha y el número de habitación.
2. **Verificación de disponibilidad**: Introduje una función para verificar si una habitación estaba disponible en una fecha concreta.
3. **Recuperar reservas por cliente**: Habilité la función para obtener todas las reservas asociadas a un cliente específico.
4. **Cancelar Reserva**: Se me ocurrió una solución para cancelar una reserva basándome en la habitación y la fecha concreta.

Para estructurar la información, decidí:

- Crear una tabla hash donde la combinación del número de habitación y la fecha sirviera de clave. Por ejemplo, "Habitación 101: 20/09/2023", y el valor asociado a esta clave contendría el número de habitación, la fecha de reserva y el nombre del cliente.
- Implementar una segunda tabla hash que utilizara el nombre del cliente como clave, y el valor sería una lista de todas sus reservas.

Para probar el sistema, añadí datos de muestra: 5 habitaciones diferentes, 3 fechas distintas para las reservas y 3 clientes, cada uno con al menos una reserva.


