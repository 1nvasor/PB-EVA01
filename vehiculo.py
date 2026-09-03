class Vehiculo:
    def __init__(self, patente,marca,modelo,anio,capacidad,estado):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.capacidad = capacidad
        self.estado = estado

    def obtenerInformacion(self):
        print(f"Patente: {self.patente}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Anio: {self.anio}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Estado: {self.estado}")


    #Cambiar estado de
    def cambiarEstado(self):

        if self.estado != "NUEVO":
                print("Este auto es Nuevo")
                return False
        
        if self.estado != "CHOCADO":
                 print("Este auto esta chocado")
                 return False
        self.estado = "NUEVO"
        return True
