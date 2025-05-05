from vehiculo import vehiculo

class avion(vehiculo):
     

    def __init__(self, velocidad, distancia,  registro_de_viajes):   
        super().__init__( velocidad, registro_de_viajes)

        self.velocidad=velocidad
        self.distancia=distancia

    def __str__(self):
        return f"avion{self.velocidad}km/h"
    
        
    def calculo_de_trayecto(self, distancia):

        if distancia<=0 or self.velocidad<=0:
            return "Error"
        else:

            trayecto=distancia/self.velocidad
      

