from vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, velocidad):
        super().__init__(velocidad)
    
    def __str__(self):
        return f"Vehículo Terrestre (Velocidad: {self.velocidad} km/h)"

    def calcular_tiempo(self):
        if self.distancia <= 0 or self.velocidad <= 0:

            return float('inf')

        return self.velocidad / (self.distancia + self.nivelTrafico)
