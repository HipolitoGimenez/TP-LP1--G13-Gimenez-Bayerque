from src.Vehiculos.vehiculo import Vehiculo

class Auto(Vehiculo):

    def __init__(self, velocidad):
        """
        Inicializa un Auto con una velocidad dada.

        Args:
            velocidad (int): Velocidad máxima del auto en km/h.

        Returns:
            None
        """
        super().__init__(velocidad)
    

    def __str__(self):
        """
        Representa al auto como texto mostrando su velocidad.

        Returns:
            str: Descripción legible del auto.
        """
        return f"Vehículo Terrestre (Velocidad: {self.velocidad} km/h)"


    def calcular_tiempo(self):
        """
        Calcula el tiempo estimado del viaje en horas basado en la distancia y el nivel de tráfico.

        Returns:
            float: Tiempo estimado del viaje en horas. Retorna float('inf') si distancia o velocidad son inválidos.
        """
        if self.distancia <= 0 or self.velocidad <= 0:

            return float('inf')

        return self.velocidad / (self.distancia + self.nivelTrafico)
