
from datetime import datetime
from typing import List
from viaje import Viaje


class Vehiculo:
    def __init__(self, velocidad: int):
        self.velocidad = velocidad
        self.registro_de_viajes =[]  # Lista vacía para cada instancia
        self.distancia=0
        self.nivelTrafico=None
        self.enUso=False
        self.tiempoViaje=0


    def __str__(self):
        return f"Vehículo (Velocidad: {self.velocidad} km/h)"
    
    def calcular_tiempo(self):
        pass

    def registrar_viaje(self,direccion, distancia, trafico):
        viaje = Viaje(direccion,self.calcular_tiempo(),datetime.now())
        self.registro_de_viajes.append(viaje)

    def ocupado(self):
        return self.enUso

    def ocupar(self):
        self.enUso = True
        
        