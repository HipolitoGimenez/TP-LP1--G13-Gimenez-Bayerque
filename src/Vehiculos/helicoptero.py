from src.Vehiculos.vehiculo import Vehiculo

class Helicoptero(Vehiculo):

    def __init__(self, velocidad:int): 
        """
        Inicializa un helicóptero con una velocidad específica.

        Args:
            velocidad (int): Velocidad máxima del helicóptero en km/h.

        Returns:
            None
        """ 
        super().__init__( velocidad)
        self.tipo="helicoptero"

    def __str__(self):
        """
        Representa al helicóptero como texto mostrando su velocidad.

        Returns:
            str: Descripción legible del helicóptero.
        """
        return f"helicoptero Velocidad: {self.velocidad}km/h ocupado: {self.enUso} tipo: {self.tipo}"
    
        
    def calculo_de_trayecto(self, distancia:float):
        """
        Calcula el tiempo estimado del trayecto en horas basado en la distancia y la velocidad.

        Args:
            distancia (float): Distancia del trayecto en kilómetros.

        Returns:
            float|str: Tiempo estimado en horas si los datos son válidos, o "Error" si distancia o velocidad no son positivas.
        """
        if distancia<=0 or self.velocidad<=0:
            return "Error"
        else:
            return distancia/self.velocidad




