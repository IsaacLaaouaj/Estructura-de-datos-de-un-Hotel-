# Estructura-de-datos-de-un-Hotel-
#Requerimientos del hotel:
Reservar habitación: Debes poder agregar una reserva indicando el nombre del cliente, la fecha y el número de habitación.
Obtener reserva por nombre de cliente: Debes poder verificar si una habitación está disponible en una fecha específica.
Obtener Habitación disponible: Debes poder obtener todas las reservas de un cliente específico.
Cancelar Reserva de una habitación en una fecha determinada : Debes poder cancelar una reserva para una habitación y una fecha específica.
#Estructura:
Una tabla hash donde la clave sea una combinación del número de habitación y la fecha (por ejemplo, "Habitación 101: 20/09/2023") y el valor esté compuesto por el número de habitación, la fecha de reserva y el nombre del cliente.
