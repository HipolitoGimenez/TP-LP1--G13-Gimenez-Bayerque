from src.Vehiculos.vehiculo import Vehiculo

class Helicoptero(Vehiculo):

    def __init__(self, velocidad:int):  #Constructor del Helicoptero. Llama al constructor de la clase padre (Vehiculo) usando super(), y le pasa la velocidad. 
        super().__init__( velocidad)

    def __str__(self):#Método mágico. Devuelve una representación legible del helicóptero, mostrando su velocidad.
        return f"helicoptero (Velocidad: {self.velocidad}km/h)"
    
        
    def calculo_de_trayecto(self, distancia:float):#Método que calcula el tiempo estimado de trayecto en horas, usando la fórmula tiempo = distancia / velocidad.

        if distancia<=0 or self.velocidad<=0:#Valida que tanto la distancia como la velocidad sean mayores que cero
            return "Error"
        else:#Si los datos son válidos, calcula y devuelve el tiempo del trayecto.

            return distancia/self.velocidad




