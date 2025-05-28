
from datetime import datetime
from typing import List
from src.Modelos.viaje import Viaje


class Vehiculo:

    def __init__(self, velocidad:int):
        """
        Inicializa un vehículo con su velocidad y atributos para registrar viajes y estado.

        Args:
            velocidad (int): Velocidad máxima del vehículo en km/h.

        Returns:
            None
        """
        self.velocidad=velocidad
        self.registro_de_viajes=[]
        self.distancia=0
        self.nivelTrafico = None
        self.enUso=False
        self.tiempoViaje=0


    def __str__(self):
        """
        Representa el vehículo con su velocidad cuando se imprime.

        Returns:
            str: Descripción del vehículo.
        """
        return f"vehiculo(Velocidad:{self.velocidad}km/h)"
    
    def calcular_tiempo(self):
        """
        Calcula el tiempo estimado del viaje basado en velocidad, distancia y nivel de tráfico.

        Returns:
            float: Tiempo estimado de viaje en horas (o la unidad que se defina).
        """
        pass


    def registrar_viaje(self,direccion, distancia, trafico):
        """
        Registra un nuevo viaje con destino, distancia y nivel de tráfico.

        Args:
            direccion (str): Destino del viaje.
            distancia (float): Distancia en km.
            trafico (str/int): Nivel o estado del tráfico que puede afectar el tiempo.

        Returns:
            None
        """
        viaje = Viaje(direccion,self.calcular_tiempo(),datetime.now())
        self.registro_de_viajes.append(viaje)


    def ocupado(self):
        """
        Indica si el vehículo está actualmente en uso.

        Returns:
            bool: True si está ocupado, False si está disponible.
        """
        return self.enUso


    def ocupar(self):
        """
        Marca el vehículo como ocupado (en uso).

        Returns:
            None
        """
        self.enUso = True
        



