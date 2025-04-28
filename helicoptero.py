from vehiculo import vehiculo

class helicoptero(vehiculo):

    def __init__(self, velocidad, distancia,  registro_de_viajes):   
        super().__init__( velocidad, registro_de_viajes)

        self.velocidad=velocidad
        self.distancia=distancia

    def calculo_de_trayecto(self, trayecto, velocidad, distancia, nivel_de_trafico):

        trayecto=velocidad/distancia+nivel_de_trafico
      



