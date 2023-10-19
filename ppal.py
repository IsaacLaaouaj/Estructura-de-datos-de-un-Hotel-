from Hotel import Hotel


hotel = Hotel(100)

hotel.nuevo_cliente('10h','Juan','Rodriguez')


hotel.insertar_hash_reserva(60,'03-11-2023','Juan')
print(hotel.buscar_hash_reserva(99,'03-11-2023'))

hotel.reservar_habitacion(99,'10h','03-11-2023')
hotel.reservar_habitacion(99,'10h','04-11-2023')
hotel.insertar_hash_cliente('Juan')
print(hotel.buscar_hash_cliente('Juan'))

