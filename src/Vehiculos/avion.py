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


        
    def calcular_tiempo(self,direccion,nivelTrafico):
        """
        Calcula el tiempo estimado de trayecto para una distancia específica (en km).

        Args:
            distancia (float): Distancia del viaje en kilómetros.

        Returns:
            float | str: Tiempo estimado del trayecto en horas. Devuelve "Error" si los datos no son válidos.
        """
        tiempodetrayecto=self.velocidad / self.distancia
        if self.distancia<=0 or self.velocidad<=0:
            return "Error"
        else:
            print("Tiempo en viaje: "+str(tiempodetrayecto))
            if tiempodetrayecto>20:
                print("No se puede transplante por que el tiempo de trayecto es mayor a 20"+str(tiempodetrayecto))
            return tiempodetrayecto
      

