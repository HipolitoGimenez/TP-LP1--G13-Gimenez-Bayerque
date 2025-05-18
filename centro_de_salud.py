from typing import List
from cirujano import cirujano 
from helicoptero import helicoptero
from avion import avion

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
        ciru = self.cirujanos[i]  
        if ciru.disponibilidad and ciru.es_especialista(organo_necesario):
            ciru.ocupado()
            print(f"Cirujano asignado: {ciru.nombre} para el órgano {organo_necesario}")
            return ciru

        print(f"No se encontró cirujano disponible para el órgano {organo_necesario}")
        return None
    
    def obtener_vehiculo_para(self, destino_partido, destino_provincia):
        if self.partido == destino_partido and self.provincia == destino_provincia:
            terrestres = [v for v in self.vehiculos if not isinstance(v, (helicoptero, avion))]
            if terrestres:
                return max(terrestres, key=lambda v: v.velocidad)
        elif self.provincia == destino_provincia:
            for v in self.vehiculos:
                if isinstance(v, helicoptero):
                    return v
        else:
            for v in self.vehiculos:
                if isinstance(v, avion):
                    return v
        return None
    
 
    
    



        
        




    