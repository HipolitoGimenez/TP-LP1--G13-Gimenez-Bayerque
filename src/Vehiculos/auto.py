from src.Vehiculos.vehiculo import Vehiculo

class Auto(Vehiculo):

    def __init__(self, velocidad):#Inicializa un Auto con una velocidad dada, usando el constructor de la clase base Vehiculo.

        super().__init__(velocidad)
    
    def __str__(self):

        return f"Vehículo Terrestre (Velocidad: {self.velocidad} km/h)"

    def calcular_tiempo(self):#Devuelve el tiempo en horas, suponiendo que distancia está en km y velocidad en km/h.

        if self.distancia <= 0 or self.velocidad <= 0:

            return float('inf')

        return self.velocidad / (self.distancia + self.nivelTrafico)
