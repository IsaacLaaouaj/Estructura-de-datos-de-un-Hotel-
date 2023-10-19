from Hotel import Hotel

def mostrar_menu():
    print("------ Menú del Hotel ------")
    print("1. Añadir nueva habitación")
    print("2. Añadir nuevo cliente")
    print("3. Realizar reserva")
    print("4. Mostrar reservas de un cliente")
    print("5. Cancelar reserva")
    print("6. Mostrar tabla de reservas")
    print("7. Mostrar tabla de clientes")
    print("8. Salir")
    print("-----------------------------")

def ejecutar_menu(hotel):
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            num_habitacion = int(input("Ingrese el número de la nueva habitación: "))
            hotel.nueva_habitacion(num_habitacion)
            print(f"Habitación {num_habitacion} añadida con éxito.\n")

        elif opcion == "2":
            dni = input("Ingrese el DNI del nuevo cliente: ")
            nombre = input("Ingrese el nombre del nuevo cliente: ")
            apellido = input("Ingrese el apellido del nuevo cliente: ")
            hotel.nuevo_cliente(dni, nombre, apellido)
            print("Cliente añadido con éxito.\n")

        elif opcion == "3":
            num_habitacion = int(input("Ingrese el número de la habitación a reservar: "))
            dni_cliente = input("Ingrese el DNI del cliente que reserva: ")
            fecha = input("Ingrese la fecha de la reserva (formato DD-MM-YYYY): ")
            hotel.reservar_habitacion(num_habitacion, dni_cliente, fecha)

        elif opcion == "4":
            dni = input("Ingrese el DNI del cliente: ")
            reservas = hotel.get_reservas_de_cliente(dni)
            if reservas != hotel.CLIENTE_NO_EXISTE:
                print("Reservas del cliente:")
                for reserva in reservas:
                    print(reserva)
            print()

        elif opcion == "5":
            num_reserva = int(input("Ingrese el número de la reserva a cancelar (num_habitacion, dni, fecha): "))
            hotel.cancelar_reserva(num_reserva)
            print("Reserva cancelada con éxito.\n")

        elif opcion == "6":
            print("Tabla de reservas:")
            hotel.hash_reservas.display()
            print()

        elif opcion == "7":
            print("Tabla de clientes:")
            hotel.hash_cliente.display()
            print()

        elif opcion == "8":
            print("¡Gracias por usar nuestro sistema!")
            break

        else:
            print("Opción no válida. Por favor, elija una opción válida.\n")


prueba = Hotel(100)
ejecutar_menu(prueba)
