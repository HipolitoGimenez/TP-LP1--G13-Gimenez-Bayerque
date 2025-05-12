from vehiculo import vehiculo

class auto(vehiculo):


    def __init__(self, velocidad:int):   
        super().__init__( velocidad)

    def __str__(self):
        return f"auto{self.velocidad}km/h"
    
    def calculo_de_trayecto(self, distancia:float, nivel_de_trafico:float):

        if distancia<=0 or self.velocidad<=0:
            return "Error"
        else:

            return (distancia/self.velocidad) + nivel_de_trafico
      

