import os
os.system("cls")
from pasajero import Pasajero
from conductor import Conductor
from vehiculo import Vehiculo
from pago import Pago
from viaje import Viaje


def main():
    pass
    # Crear pasajeros#
    pasajero1 = Pasajero("1","Vicente","vicente@gmail.com",56912345566,"Tarjeta",5)
    pasajero2 = Pasajero("2","Joakin","Joakingelking@gmail.com",56912345678,"Efectivo","3")
    pasajero3 = Pasajero("3","Franko","franko@gmail.com",56988776655,"Tarjeta",2)

    # Crear vehículos#
    vehiculo1 = Vehiculo("rx-tt-67","Susuki","nunuki",2019,4,"Nuevo")
    vehiculo2 = Vehiculo("rt-xg-50","Toyota","toyo",2008,4,"Chocado")

    # Crear conductores#
    conductor1 = Conductor("3","Carlos","carlos@gmail.com",56912344455,"Nueva","Susuki")


    # Actualizar teléfono#
    pasajero1.actualizarTelefono(56935188999)


    # Viaje Solicitado
    viaje1 = pasajero1.solicitarViaje(
         "Plaza de Armas",
         "Universidad"
    )

    viaje2 = pasajero2.solicitarViaje(
        "San joaquin",
        "Universidad catolica"
    )

    viaje3 = pasajero3.solicitarViaje(
        "Universidad finis terrae"
    )

    # Conductor acepta
    conductor1.aceptarViaje()
    
    

    # Definir distancia
    viaje1.distancia = 5.0

    # Calcular tarifa
    viaje1.calcularTarifa()

    # Iniciar viaje
    viaje1.iniciar(pasajero1)
    
    

    # Finalizar viaje
    viaje1.finalizar(pasajero1)



    # Mostrar información
    print("Estado:", viaje1.estado)
    print("Tarifa:", viaje1.tarifa)

    # Generar pago
    pago1 = Pago(
        1,
        viaje1.tarifa,
        pasajero1.metodoPago,
        "PAGADO"
    )

    print("Monto del pago:", pago1.obtenerMonto())

    pago1.generarComprobante()



    # Calificar viaje
    pasajero1.calificarViaje(viaje1)


if __name__ == "__main__":
    main()