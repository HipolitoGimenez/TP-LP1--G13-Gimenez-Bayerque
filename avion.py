from vehiculo import Vehiculo

class Avion(Vehiculo):
     

    def __init__(self, velocidad:int):   
        super().__init__( velocidad)


    def __str__(self):
        return f"avion( Velocidad: {self.velocidad}km/h)"
    
    def calcular_tiempo(self):
        if self.distancia <= 0 or self.velocidad <= 0:
            return float('inf')
        return self.velocidad / self.distancia
        
    def calculo_de_trayecto(self, distancia:float):

        if distancia<=0 or self.velocidad<=0:
            return "Error"
        else:

            return distancia/self.velocidad
      

