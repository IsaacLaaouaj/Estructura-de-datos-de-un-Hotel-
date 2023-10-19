# -*- coding: utf-8 -*-

class Habitacion:
    def __init__(self, num_habitacion):
        self.__num_habitacion = num_habitacion
        self.__historico_reservas = {} 

    def get_historico_reservas(self):
        return self.__historico_reservas
        
    def __str__(self) -> str:
        return f"Num. habitación: {self.__num_habitacion}"
    
    def get_id(self):
        return self.__num_habitacion
    
    def esta_reservada(self, fecha) -> bool:
        if self.__historico_reservas[fecha]:
            return True
        return False
    
    def add_reserva(self, reserva):
        self.__historico_reservas[reserva.get_fecha()] = reserva
    

