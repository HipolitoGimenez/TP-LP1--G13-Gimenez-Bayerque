from datetime import datetime
from typing import List

class vehiculo:
    def __init__(self, nombre: str, velocidad: int):
        self.nombre = nombre
        self.velocidad = velocidad
        self.registro_de_viajes = []  # Lista vacía para cada instancia

    def __str__(self):
        return f"{self.nombre} (Velocidad: {self.velocidad} km/h)"
    
    def calcular_tiempo(self, distancia: float, trafico: float):
        if distancia <= 0 or self.velocidad <= 0:
            return "Error"
        else:
            return (distancia / self.velocidad) + trafico

    def registrar_viaje(self, direccion: str, tiempo: float):
        viaje = {
            "direccion": direccion,
            "tiempo": tiempo,
            "fecha": datetime.now()
        }
        self.registro_de_viajes.append(viaje)
