from src.Vehiculos.vehiculo import Vehiculo

class Auto(Vehiculo):

    def __init__(self, velocidad:int):
        """
        Inicializa un Auto con una velocidad dada.

        Args:
            velocidad (int): Velocidad máxima del auto en km/h.

        Returns:
            None
        """
        super().__init__(velocidad)
        self.tipo="auto"

    
    def __str__(self):
        """
        Representa al auto como texto mostrando su velocidad.

        Returns:
            str: Descripción legible del auto.
        """
        return f"Automovil/ambulancia Velocidad: {self.velocidad} km/h ,ocupado: {self.enUso} , tipo: {self.tipo}"
    
    
    def calcular_tiempo(self,nivelTrafico):
        """
        Calcula el tiempo estimado del viaje en horas basado en la distancia y el nivel de tráfico.

        Returns:
            float: Tiempo estimado del viaje en horas. Retorna float('inf') si distancia o velocidad son inválidos.
        """
        print("Velocidad: "+str(self.velocidad))
        print("Distancia 2: "+str(self.distancia))
        print("Nivel de Trafico: "+str(nivelTrafico))

        
        tiempodetrayecto=self.velocidad / (self.distancia + nivelTrafico)
        if self.distancia <= 0 or self.velocidad <= 0:
            return 0
        else:
            print("Tiempo en viaje: "+str(tiempodetrayecto))
        if tiempodetrayecto>20:
            print("No se puede transplante por que el tiempo de trayecto es mayor a 20 y el tiempo de trayecto es:"+str(tiempodetrayecto))
            return 0
        else:
            return tiempodetrayecto
        

        

