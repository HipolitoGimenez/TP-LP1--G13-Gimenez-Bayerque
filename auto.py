from vehiculo import vehiculo

class auto(vehiculo):


    def __init__(self, velocidad, distancia, nivel_de_trafico, registro_de_viajes):   
        super().__init__( velocidad, registro_de_viajes)

        self.velocidad=velocidad
        self.distancia=distancia
        self.nivel_de_trafico=nivel_de_trafico 





    
    def calculo_de_trayecto(self, trayecto, velocidad, distancia, nivel_de_trafico):

        trayecto=velocidad/distancia+nivel_de_trafico