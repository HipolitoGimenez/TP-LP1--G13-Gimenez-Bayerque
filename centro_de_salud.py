from typing import List
from vehiculo import vehiculo,auto, helicoptero, avion
from cirujano import cirujano



class centro_de_salud:



    def __init__(self, nombre: str, direccion: str, partido: str, provincia: str, telefono: str):
        self.nombre = nombre
        self.direccion = direccion
        self.partido = partido
        self.provincia = provincia
        self.telefono = telefono
        self.cirujanos = []  # Lista de cirujanos en el centro
        self.vehiculos = []  # Lista de vehículos disponibles en el centro
        self.transplante_realizado=0#contador de transplantes realizados
      
        
    

    def buscar_transporte(self, provincia, partido):


    
    def buscar_cirujano(self, cir : cirujano):
        




    