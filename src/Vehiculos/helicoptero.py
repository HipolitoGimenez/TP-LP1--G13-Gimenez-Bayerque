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
    
        
    def calcular_tiempo(self,nivelTrafico):
        """
        Calcula el tiempo estimado del trayecto en horas basado en la distancia y la velocidad.

        Args:
            distancia (float): Distancia del trayecto en kilómetros.

        Returns:
            float|str: Tiempo estimado en horas si los datos son válidos, o "Error" si distancia o velocidad no son positivas.
        """
        tiempodetrayecto=self.velocidad/self.distancia

        if self.distancia<=0 or self.velocidad<=0:
            print("No se puede realizar el vaje por que distancia y velocidad es menor o igual a 0")
            return 0
        
        else:
            #print("Tiempo en viaje: "+str(tiempodetrayecto))
            if tiempodetrayecto>20:
                print("No se puede transplante por que el tiempo de trayecto es mayor a 20 y es : "+str(tiempodetrayecto))
            return tiempodetrayecto




