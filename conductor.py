from persona import Persona


class Conductor(Persona):

    def __init__(self, id, nombre, email, telefono, licencia, vehiculo):

        super().__init__(id, nombre, email, telefono)

        self.licencia = licencia
        self.disponible = True
        self.viajesRealizados = []
        self.vehiculo = vehiculo

    def aceptarViaje(self, viaje):

        if not self.disponible:
            print("Error: el conductor no está disponible.")
            return False

        if viaje.estado != "PENDIENTE":
            print("Error: el viaje no está pendiente.")
            return False

        viaje.estado = "ACEPTADO"
        self.disponible = False

        return True

    def rechazarViaje(self, viaje):

        if viaje.estado != "PENDIENTE":
            print("Error: solo se pueden rechazar viajes pendientes.")
            return False

        viaje.estado = "CANCELADO"

        return True

    #realizar este metodo
    def cambiarDisponibilidad(self):
        if self.disponible == True:
            print("Viaje disponible")
        else:
            print("Viaje no disponible")

        
    def obtenerHistorial(self):

        return self.viajesRealizados