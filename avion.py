from vehiculo import Vehiculo

class Avion(Vehiculo):
     

    def __init__(self, velocidad:int):#Constructor que inicializa un Avion con su velocidad, usando el constructor de la clase base Vehiculo.
        super().__init__( velocidad)


    def __str__(self):
        return f"avion( Velocidad: {self.velocidad}km/h)"
    
    def calcular_tiempo(self):#Devuelve el tiempo en horas, suponiendo que distancia está en km y velocidad en km/h.
        if self.distancia <= 0 or self.velocidad <= 0:
            return float('inf')
        return self.velocidad / self.distancia

        
    def calculo_de_trayecto(self, distancia:float):#Este método calcula el tiempo de trayecto para una distancia dada como argumento, devolviendo también el tiempo en horas.

        if distancia<=0 or self.velocidad<=0:
            return "Error"
        else:

            return distancia/self.velocidad
      

