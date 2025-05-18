from typing import List
from vehiculo import vehiculo
from cirujano import cirujano 

class centro_de_salud:
    def __init__(self, nombre: str, direccion: str, partido: str, provincia: str, telefono: str):
        self.nombre = nombre
        self.direccion = direccion
        self.partido = partido
        self.provincia = provincia
        self.telefono = telefono
        self.cirujanos = []  
        self.vehiculos = []  
        self.transplante_realizado = 0

    def agregar_vehiculos(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def agregar_cirujano(self, nuevo_cirujano: cirujano):       
        self.cirujanos.append(nuevo_cirujano)
    
    def asignar_cirujano(self, organo_necesario):
      if not self.cirujanos:
        print("No hay cirujanos registrados.")
        return None

      for i in range(len(self.cirujanos)):
        ciru = self.cirujanos[i]  # nombrá explícitamente la variable
        if ciru.disponibilidad and ciru.es_especialista(organo_necesario):
            ciru.ocupado()
            print(f"Cirujano asignado: {ciru.nombre} para el órgano {organo_necesario}")
            return ciru

        print(f"No se encontró cirujano disponible para el órgano {organo_necesario}")
        return None



"""
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
        return vehiculo"""
   
 


        
        




    