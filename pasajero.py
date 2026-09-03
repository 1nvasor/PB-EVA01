from persona import Persona
from viaje import Viaje


class Pasajero(Persona):

    def __init__(self, id, nombre, email, telefono, metodoPago, calificacionPromedio=0.0):

        super().__init__(id, nombre, email, telefono)

        self.metodoPago = metodoPago
        self.calificacionPromedio = calificacionPromedio

    def solicitarViaje(self, origen, destino):

        if origen == destino:
            print("Error: el origen y el destino no pueden ser iguales.")
            return None

        viaje = Viaje(origen, destino)

        return viaje

    def cancelarViaje(self, viaje):

        if viaje.estado == "PENDIENTE" or viaje.estado == "ACEPTADO":
            viaje.estado = "CANCELADO"
            return True

        print("Error: el viaje no puede ser cancelado.")
        return False

    #IMPLEMENTAR METODO
    def calificarViaje(self, viaje, puntuacion):

        pass

