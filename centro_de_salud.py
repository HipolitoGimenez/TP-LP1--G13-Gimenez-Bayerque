from typing import List
from vehiculo import vehiculo
from auto import auto
from helicoptero import helicoptero
from avion import avion
from cirujano import cirujano
from organo import organo


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
      
    
    def agregar_vehiculos(self, vehiculo:vehiculo):

        self.vehiculos.append(vehiculo)

    def agregar_cirujano(self, cirujano:cirujano):
                
        self.cirujanos.append(cirujano)


    def buscar_cirujano(self, organo_requerido, ):

        for cirujano in self.cirujanos:

            if organo_requerido in 



    

'''
    def asignar_transporte(self, provincia:str, partido:str, distancia:float, trafico, direccion):

        vehiculo=None

        if self.provincia==provincia:
            if self.partido==partido:
                max_vel=-1
                for v in self.vehiculos:
                    if v.velocidad>max_vel:
                        vehiculo=v
                        max_vel=v.velocidad
            else:
                for v in self.vehiculos:
                    if isinstance(v, helicoptero):
                        vehiculo=v
                        break
        else:
            for v in self.vehiculos:
                if isinstance(v, avion):
                    vehiculo=v
                    break
        
        if vehiculo is None:
            print("No se encontro vehiculo adecuado")
            return None
        
        tiempo=vehiculo.calcular_tiempo(distancia, trafico)
        vehiculo.registrar_viaje(direccion, tiempo)
        print(f"Vehiculo asignado: {vehiculo} con un tiempo estimado de {tiempo} horas")
        return vehiculo
   '''
 


        
        




    