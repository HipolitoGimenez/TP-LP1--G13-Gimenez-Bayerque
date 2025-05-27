from datetime import datetime
from typing import List
from auto import Auto
from helicoptero import Helicoptero
from vehiculo import Vehiculo
from cirujano import Cirujano 

class CentroDeSalud:
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

    def agregar_cirujano(self, nuevo_cirujano: Cirujano):       
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

    def asignarVehiculo(self, otroCentroSalud, distancia, nivelTrafico):
        if(self._estanEnLaMismaProvinciaYPartido(otroCentroSalud)):
           self.transportarOrgano(otroCentroSalud, self._obtenerVehiculo('Auto'), distancia, nivelTrafico)
        elif (self._estanEnMismaProvincia(otroCentroSalud)):
           self.transportarOrgano(otroCentroSalud, self._obtenerVehiculo('Helicoptero'), distancia, nivelTrafico)
        else:
           self.transportarOrgano(otroCentroSalud, self._obtenerVehiculo('Avion'), distancia, nivelTrafico)

    def _estanEnLaMismaProvinciaYPartido(self, otroCentroSalud):
       return self.provincia == otroCentroSalud.provincia and self.partido == otroCentroSalud.partido
    
    def _estanEnMismaProvincia(self, otroCentroSalud):
       return self.provincia == otroCentroSalud.provincia
    
    def transportarOrgano(self, vehiculo, distancia, nivelTrafico):
       vehiculo.distancia = distancia
       vehiculo.nivelTrafico = nivelTrafico
       vehiculo.registrar_viaje(self.direccion)
    
    def _obtenerVehiculo(self, tipo):
       vehiculoAsignado = None
       for vehiculo in self.vehiculos:
          if tipo == vehiculo.get_class_name() and not vehiculo.ocupado():
            vehiculo.ocupar()
            vehiculoAsignado = vehiculo
            break
       return vehiculoAsignado
    
    def asignarCirujano(self):
        for cirujano in self.cirujanos:
           if cirujano.estaDisponible():
              pass

    def realizarAblacion(self, donante, organo):
        organo.fecha_hora_de_ablacion = datetime.now()
        donante.lista_organos.remove(organo)

    def realizarTrasplante(self, vehiculo):
        pass

    def __eq__(self, otroCentroSalud): 
        return self.nombre == otroCentroSalud.nombre and self.direccion == otroCentroSalud.direccion


   
 


        
        




    