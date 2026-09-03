class Pago:
    def __init__(self, id, monto, metodo, estado):
        self.id = id
        self.monto = monto
        self.metodo = metodo
        self.estado = estado

    def obtenerMonto(self):
        return self.monto


    #
    def obtenerComprobante(self):
        comprobante = {
            "id_pago": self.id,
            "monto": self.monto,
            "metodo": self.metodo,
            "estado": self.estado
        }
        return comprobante