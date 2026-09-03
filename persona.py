class Persona:

    def __init__(self, id, nombre, email, telefono):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def iniciarSesion(self):
        return True

    #Actualizamos el numero de la persona
    def actualizarTelefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono
        print("Telefono actualizado")

    def obtenerNombre(self):
        return self.nombre