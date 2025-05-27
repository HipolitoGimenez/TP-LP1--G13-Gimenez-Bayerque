from datetime import datetime
from typing import List
from auto import Auto
from helicoptero import Helicoptero
from vehiculo import Vehiculo
from cirujano import Cirujano 

class CentroDeSalud:
    def __init__(self, nombre: str, direccion: str, partido: str, provincia: str, telefono: str):#inicializa los datos principales del centro y sus recursos disponibles
        self.nombre = nombre
        self.direccion = direccion
        self.partido = partido
        self.provincia = provincia
        self.telefono = telefono
        self.cirujanos = []  
        self.vehiculos = []  
        self.transplante_realizado = 0 #contador de transplante realizado

    def agregar_vehiculos(self, vehiculo):
        self.vehiculos.append(vehiculo)#añade vehiculo a la lista

    def agregar_cirujano(self, nuevo_cirujano: Cirujano):       
        self.cirujanos.append(nuevo_cirujano)#añade cirujano a la lista
    
    def asignar_cirujano(self, organo_necesario):
      if not self.cirujanos:
        print("No hay cirujanos registrados.")
        return None

      for i in range(len(self.cirujanos)):
        ciru = self.cirujanos[i]  # nombrá explícitamente la variable
        if ciru.disponibilidad and ciru.es_especialista(organo_necesario):#busca cirujano disponible que tenga la especialidad requerida para ese organo
            ciru.ocupado()#marca el cirujano como ocupado
            print(f"Cirujano asignado: {ciru.nombre} para el órgano {organo_necesario}")
            return ciru

        print(f"No se encontró cirujano disponible para el órgano {organo_necesario}")
        return None

    def asignarVehiculo(self, otroCentroSalud, distancia, nivelTrafico):#selecciona el tipo de vehiculo a utilizar en funcion de la distancia geoegrafica entre centros
        if(self._estanEnLaMismaProvinciaYPartido(otroCentroSalud)):
           self.transportarOrgano(otroCentroSalud, self._obtenerVehiculo('Auto'), distancia, nivelTrafico)
        elif (self._estanEnMismaProvincia(otroCentroSalud)):
           self.transportarOrgano(otroCentroSalud, self._obtenerVehiculo('Helicoptero'), distancia, nivelTrafico)
        else:
           self.transportarOrgano(otroCentroSalud, self._obtenerVehiculo('Avion'), distancia, nivelTrafico)

    def _estanEnLaMismaProvinciaYPartido(self, otroCentroSalud):#comparan la ubicacion entre centros
       return self.provincia == otroCentroSalud.provincia and self.partido == otroCentroSalud.partido
    
    def _estanEnMismaProvincia(self, otroCentroSalud):
       return self.provincia == otroCentroSalud.provincia
    
    def transportarOrgano(self, vehiculo, distancia, nivelTrafico):
       vehiculo.distancia = distancia#se gurada en el vehiculi la distancia que debera recorrer, para luego usarla para calcular tiempo de viaje
       vehiculo.nivelTrafico = nivelTrafico# lo mismo que la anterior
       vehiculo.registrar_viaje(self.direccion)#se registra viaje con destino a este centro
    
    def _obtenerVehiculo(self, tipo):
       vehiculoAsignado = None
       for vehiculo in self.vehiculos:
          if tipo == vehiculo.get_class_name() and not vehiculo.ocupado():#se compara el nombre de la clase del vehiculo con un string tipo 'Auto" "avion" "Helicoptero",  es un parametro de entrada que se le pasa a este metodo cuando se llama desde otro lugar de codigo
            vehiculo.ocupar()
            vehiculoAsignado = vehiculo
            break
       return vehiculoAsignado
    
    def asignarCirujano(self):
        for cirujano in self.cirujanos:
           if cirujano.estaDisponible():
              pass

    def realizarAblacion(self, donante, organo):
        organo.fecha_hora_de_ablacion = datetime.now()#se registra el momento que se extrae un organo
        donante.lista_organos.remove(organo)

    def realizarTrasplante(self, vehiculo):
        pass

    def __eq__(self, otroCentroSalud): #METODO MAGICO, se usa para comparar si objetos son iguales con el operador ==, cuando haces if centro1 == centro2 python llama a centro1.__eq__(centro2). Vos le aclaras que significa ser igual si no compararia como objeto dato por dato
        return self.nombre == otroCentroSalud.nombre and self.direccion == otroCentroSalud.direccion #Dos centros de salud son considerados iguales si tienen el mismo nombre y la misma dirección. El resto de los atributos (teléfono, provincia, cirujanos, etc.) no importa para esta comparación.




   
 


        
        




    