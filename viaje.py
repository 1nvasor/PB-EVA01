class Viaje:


    def __init__(self, id, origen, destino):

        self.id = id
        self.origen = origen
        self.destino = destino
        self.distancia = 0.0
        self.tarifa = 0
        self.estado = "PENDIENTE"

    # IMPLEMENTAR metodo
    def calcularTarifa(self):

        pass

    def iniciar(self):

        if self.estado != "ACEPTADO":
            print("Error: el viaje debe estar aceptado para iniciar.")
            return False

        self.estado = "EN_CURSO"

        return True

    def finalizar(self):

        if self.estado != "EN_CURSO":
            print("Error: el viaje debe estar en curso para finalizar.")
            return False

        self.estado = "FINALIZADO"

        return True

    def obtenerEstado(self):

        print(f"Estado actual del viaje: {self.estado}")