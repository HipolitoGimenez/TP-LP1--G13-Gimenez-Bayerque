from src.Vehiculos.vehiculo import Vehiculo

class Avion(Vehiculo):
     

    def __init__(self, velocidad:int):
        """
        Constructor que inicializa un Avión con su velocidad.

        Args:
            velocidad (int): Velocidad del avión en km/h.

        Returns:
            None
        """
        super().__init__( velocidad)
        self.tipo="avion"

    def __str__(self):
        """
        Representación legible del avión con su velocidad.

        Returns:
            str: Descripción del avión.
        """
        return f"avion Velocidad: {self.velocidad}km/h ocupado : {self.enUso} tipo: {self.tipo}"
    

    def calcular_tiempo(self):
        """
        Calcula el tiempo estimado de viaje en horas, usando los atributos `distancia` y `velocidad`.

        Returns:
            float: Tiempo estimado del viaje. Devuelve float('inf') si los valores son inválidos.
        """
        if self.distancia <= 0 or self.velocidad <= 0:
            return float('inf')
        return self.velocidad / self.distancia

        
    def calculo_de_trayecto(self, distancia:float):
        """
        Calcula el tiempo estimado de trayecto para una distancia específica (en km).

        Args:
            distancia (float): Distancia del viaje en kilómetros.

        Returns:
            float | str: Tiempo estimado del trayecto en horas. Devuelve "Error" si los datos no son válidos.
        """
        if distancia<=0 or self.velocidad<=0:
            return "Error"
        else:

            return distancia/self.velocidad
      

