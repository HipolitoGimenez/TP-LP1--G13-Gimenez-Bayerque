
from datetime import datetime
from typing import List
from viaje import Viaje

class Vehiculo:

    def __init__(self, velocidad:int):
        self.velocidad=velocidad
        self.registro_de_viajes=[]## Lista vacía para cada instancia
        self.distancia=0
        self.nivelTrafico = None
        self.enUso=False
        self.tiempoViaje=0

    def __str__(self):#Muestra la velocidad del vehículo cuando se imprime.

        return f"vehiculo(Velocidad:{self.velocidad}km/h)"
    
    def calcular_tiempo(self):#Calcula el tiempo estimado del viaje usando la velocidad, la distancia y quizás el tráfico.
        pass

    def registrar_viaje(self,direccion, distancia, trafico):#Método para registrar un nuevo viaje. Recibe la dirección del destino, la distancia y el tráfico como parámetros.
        viaje = Viaje(direccion,self.calcular_tiempo(),datetime.now())#Crea una nueva instancia de Viaje, con la dirección, el tiempo calculado y la fecha y hora actual.
        self.registro_de_viajes.append(viaje)#Guarda el viaje en el registro de viajes del vehículo.

    def ocupado(self):#Devuelve un valor booleano que indica si el vehículo está en uso.
        return self.enUso

    def ocupar(self):#Cambia el estado del vehículo a ocupado
        self.enUso = True#para que sirven cada uno si se nombran casi igual
        



